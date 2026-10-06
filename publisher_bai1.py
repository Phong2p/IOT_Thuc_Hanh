# pyrefly: ignore [missing-import]
import time
import paho.mqtt.client as mqtt

BROKER = "test.mosquitto.org"
PORT = 1883
TOPIC = "iot/lab/message"

HO_TEN = "[NHẬP HỌ TÊN CỦA BẠN]"
MA_SV = "[NHẬP MÃ SV]"
LOI_CHAO = "Xin chao tu client Python MQTT"

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
        payload = f"{LOI_CHAO} - {MA_SV} - {HO_TEN}"
        client.publish(TOPIC, payload)

        print("Da gui message:")
        print("Topic:", TOPIC)
        print("Payload:", payload)
        print()

        time.sleep(5)

except KeyboardInterrupt:
    print("\nKet thuc Publisher")

finally:
    client.loop_stop()
    client.disconnect()
