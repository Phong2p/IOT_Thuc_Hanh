# pyrefly: ignore [missing-import]
import json
import paho.mqtt.client as mqtt

BROKER = "test.mosquitto.org"
PORT = 1883
TOPIC = "iot/lab/sensor01/data"

def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        print("Ket noi broker thanh cong!")
        print("Dang lang nghe topic:", TOPIC)
        client.subscribe(TOPIC)
    else:
        print("Ket noi that bai:", reason_code)

def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode("utf-8"))

    print("\nDevice:", data["device_id"])
    print("Temperature:", data["temperature"], "C")
    print("Humidity:", data["humidity"], "%")

    if data["temperature"] > 35:
        print("CANH BAO: Nhiet do cao")

    if data["humidity"] < 40:
        print("CANH BAO: Do am thap")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message

print("Dang ket noi toi broker...")
client.connect(BROKER, PORT, 60)

try:
    client.loop_forever()

except KeyboardInterrupt:
    print("\nKet thuc Monitoring Subscriber")

finally:
    client.disconnect()
