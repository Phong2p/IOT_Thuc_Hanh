# Bài thực hành MQTT cơ bản với Python

Đây là bài thực hành Bài 1: Ứng dụng gửi và nhận thông điệp MQTT cơ bản.
Dự án bao gồm 2 chương trình Python để minh họa cơ chế publisher/subscriber.

## Yêu cầu môi trường
- Python 3.x
- Thư viện `paho-mqtt`

### Cài đặt thư viện
Chạy lệnh sau để cài đặt thư viện cần thiết:
```bash
pip install paho-mqtt
```

## Cấu hình MQTT Broker
Trong bài này, chúng ta sử dụng một Public MQTT Broker để test:
- **Broker**: `broker.hivemq.com`
- **Port**: `1883`
- **Topic**: `iot/thuchanh1/test` (Có thể thay đổi trong code nếu muốn)

## Hướng dẫn chạy code

1. **Chạy Subscriber (Người nhận)**:
   Mở một terminal và chạy lệnh sau để bắt đầu lắng nghe tin nhắn:
   ```bash
   python subscriber.py
   ```

2. **Chạy Publisher (Người gửi)**:
   Mở một terminal thứ hai và chạy lệnh sau để bắt đầu gửi tin nhắn định kỳ (mỗi 5 giây):
   ```bash
   python publisher.py
   ```

3. **Quan sát kết quả**:
   Bạn sẽ thấy terminal chạy `publisher.py` in ra log mỗi khi gửi tin nhắn thành công, và terminal chạy `subscriber.py` sẽ in ra nội dung tin nhắn ngay khi nhận được.
