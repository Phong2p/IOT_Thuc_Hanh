import paho.mqtt.client as mqtt

# Cấu hình MQTT Broker
broker = "broker.hivemq.com"
port = 1883
topic = "iot/thuchanh1/test"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Đã kết nối tới MQTT Broker!")
        # Đăng ký nhận tin nhắn từ topic
        client.subscribe(topic)
        print(f"Đang lắng nghe trên topic: {topic}")
    else:
        print(f"Kết nối thất bại, mã lỗi {rc}")

def on_message(client, userdata, msg):
    print(f"Nhận được: `{msg.payload.decode()}` từ topic `{msg.topic}`")

# Khởi tạo client
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Kết nối tới broker
client.connect(broker, port)

# Bắt đầu vòng lặp để duy trì kết nối và lắng nghe tin nhắn
try:
    client.loop_forever()
except KeyboardInterrupt:
    print("Dừng subscriber.")
finally:
    client.disconnect()
