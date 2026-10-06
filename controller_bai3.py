import json
import threading

import paho.mqtt.client as mqtt

BROKER = "test.mosquitto.org"
PORT = 1883
COMMAND_TOPIC = "iot/lab/light01/cmd"
STATUS_TOPIC = "iot/lab/light01/status"
RESPONSE_TIMEOUT = 5
SUBSCRIBE_TIMEOUT = 10

subscription_complete = threading.Event()
subscription_failed = threading.Event()
response_received = threading.Event()
response_lock = threading.Lock()
latest_status = None


def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        print("Ket noi broker thanh cong!")
        result, _ = client.subscribe(STATUS_TOPIC)
        if result != mqtt.MQTT_ERR_SUCCESS:
            print("Dang ky topic trang thai that bai:", result)
            subscription_failed.set()
            subscription_complete.set()
    else:
        print("Ket noi that bai:", reason_code)
        subscription_failed.set()
        subscription_complete.set()


def on_subscribe(client, userdata, mid, reason_code_list, properties):
    if any(reason_code.is_failure for reason_code in reason_code_list):
        print("Broker tu choi dang ky topic trang thai.")
        subscription_failed.set()
        subscription_complete.set()
        return

    print("Dang lang nghe topic:", STATUS_TOPIC)
    subscription_complete.set()


def on_message(client, userdata, msg):
    global latest_status

    try:
        payload = msg.payload.decode("utf-8")
        data = json.loads(payload)
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        print("Khong doc duoc trang thai JSON:", error)
        return

    if (
        not isinstance(data, dict)
        or data.get("device_id") != "light01"
        or data.get("status") not in ("ON", "OFF")
    ):
        print("Trang thai nhan duoc khong hop le:", payload)
        return

    with response_lock:
        latest_status = payload
    print("\nTrang thai nhan duoc:")
    print(payload)
    response_received.set()


client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_subscribe = on_subscribe
client.on_message = on_message

print("Dang ket noi toi broker...")
client.connect(BROKER, PORT, 60)
client.loop_start()

try:
    if not subscription_complete.wait(SUBSCRIBE_TIMEOUT):
        if subscription_failed.is_set():
            raise RuntimeError("Khong the dang ky topic trang thai.")
        raise TimeoutError("Het thoi gian cho dang ky topic trang thai.")
    if subscription_failed.is_set():
        raise RuntimeError("Khong the dang ky topic trang thai.")

    while True:
        try:
            command = input("Nhap lenh (ON/OFF, EXIT de thoat): ").strip().upper()
        except EOFError:
            print("\nKet thuc Controller App")
            break

        if command == "EXIT":
            print("Ket thuc Controller App")
            break

        if command not in ("ON", "OFF"):
            print("Lenh khong hop le. Vui long nhap ON, OFF hoac EXIT.")
            continue

        response_received.clear()
        with response_lock:
            latest_status = None

        result = client.publish(COMMAND_TOPIC, command)
        if result.rc != mqtt.MQTT_ERR_SUCCESS:
            print("Gui lenh that bai:", result.rc)
            continue

        print(f"Da gui lenh {command} toi light01")
        if not response_received.wait(RESPONSE_TIMEOUT):
            print("Khong nhan duoc phan hoi trang thai trong thoi gian cho.")
            continue

        with response_lock:
            status_payload = latest_status
        if status_payload is None:
            print("Da nhan tin nhan nhung khong co trang thai hop le.")
except KeyboardInterrupt:
    print("\nKet thuc Controller App")
finally:
    client.loop_stop()
    client.disconnect()
