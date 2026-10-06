# pyrefly: ignore [missing-import]
from datetime import datetime
import paho.mqtt.client as mqtt

BROKER = "test.mosquitto.org"
PORT = 1883
TOPIC = "iot/lab/message"

def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        print("Ket noi broker thanh cong!")
        print("Dang lang nghe topic:", TOPIC)
        client.subscribe(TOPIC)
    else:
        print("Ket noi that bai:", reason_code)

def on_message(client, userdata, msg):
    print("\nNhan duoc message:")
    print("Topic:", msg.topic)
    print("Payload:", msg.payload.decode("utf-8"))
    print("Time:", datetime.now().strftime("%H:%M:%S"))

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message

print("Dang ket noi toi broker...")
client.connect(BROKER, PORT, 60)

try:
    client.loop_forever()
except KeyboardInterrupt:
    print("\nKet thuc Subscriber")
finally:
    client.disconnect()
