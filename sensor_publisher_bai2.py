# pyrefly: ignore [missing-import]
import json
import random
import time
import paho.mqtt.client as mqtt

BROKER = "test.mosquitto.org"
PORT = 1883
TOPIC = "iot/lab/sensor01/data"

def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        print("Ket noi broker thanh cong!")
    else:
        print("Ket noi that bai:", reason_code)

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect

print("Dang ket noi toi broker...")
client.connect(BROKER, PORT, 60)
client.loop_start()

try:
    while True:
        data = {
            "device_id": "sensor01",
            "temperature": round(random.uniform(20, 40), 1),
            "humidity": round(random.uniform(30, 80), 1)
        }

        payload = json.dumps(data)
        client.publish(TOPIC, payload)

        print("Da gui:", payload)

        time.sleep(3)

except KeyboardInterrupt:
    print("\nKet thuc Sensor Publisher")

finally:
    client.loop_stop()
    client.disconnect()
