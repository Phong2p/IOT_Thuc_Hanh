import json

import paho.mqtt.client as mqtt

BROKER = "test.mosquitto.org"
PORT = 1883
COMMAND_TOPIC = "iot/lab/light01/cmd"
STATUS_TOPIC = "iot/lab/light01/status"

light_status = "OFF"


def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        print("Ket noi broker thanh cong!")
        print("Dang lang nghe topic:", COMMAND_TOPIC)
        client.subscribe(COMMAND_TOPIC)
    else:
        print("Ket noi that bai:", reason_code)


def on_message(client, userdata, msg):
    global light_status

    command = msg.payload.decode("utf-8").strip().upper()
    if command not in ("ON", "OFF"):
        print("Lenh khong hop le:", command)
        return

    light_status = command
    payload = json.dumps({
        "device_id": "light01",
        "status": light_status,
    })
    result = client.publish(STATUS_TOPIC, payload)
    if result.rc == mqtt.MQTT_ERR_SUCCESS:
        print("Da cap nhat trang thai:", payload)
    else:
        print("Gui trang thai that bai:", result.rc)


client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message

print("Dang ket noi toi broker...")
client.connect(BROKER, PORT, 60)

try:
    client.loop_forever()
except KeyboardInterrupt:
    print("\nKet thuc Smart Light Device")
finally:
    client.disconnect()
