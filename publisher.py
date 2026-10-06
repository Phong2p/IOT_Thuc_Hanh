import paho.mqtt.client as mqtt
import time

# Cấu hình MQTT Broker
broker = "broker.hivemq.com"
port = 1883
topic = "iot/thuchanh1/test"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Đã kết nối tới MQTT Broker!")
    else:
        print(f"Kết nối thất bại, mã lỗi {rc}")

# Khởi tạo client
client = mqtt.Client()
client.on_connect = on_connect

# Kết nối tới broker
client.connect(broker, port)
client.loop_start()

try:
    while True:
        msg = "Hello MQTT từ Python Publisher!"
        result = client.publish(topic, msg)
        status = result[0]
        if status == 0:
            print(f"Đã gửi: `{msg}` tới topic `{topic}`")
        else:
            print(f"Gửi tin nhắn thất bại tới topic {topic}")
        time.sleep(5) # Gửi tin nhắn mỗi 5 giây
except KeyboardInterrupt:
    print("Dừng publisher.")
finally:
    client.loop_stop()
    client.disconnect()
