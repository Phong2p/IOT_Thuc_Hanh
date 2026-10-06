# Bài thực hành MQTT - Buổi 1

Dự án gồm ba bài thực hành về giao thức MQTT bằng Python: gửi/nhận thông điệp, mô phỏng cảm biến và điều khiển đèn thông minh.

## Yêu cầu môi trường

- Python 3.x
- MQTT broker có thể truy cập qua TCP
- Thư viện `paho-mqtt`

Cài thư viện:

```bash
pip install paho-mqtt
```

## Cấu hình MQTT broker

Các chương trình hiện sử dụng broker công cộng `test.mosquitto.org`, cổng TCP không mã hóa `1883`. Broker và topic được khai báo ở đầu mỗi file Python bằng các biến `BROKER`, `PORT` và các biến topic tương ứng (`TOPIC`, `COMMAND_TOPIC`, `STATUS_TOPIC`). Nếu dùng broker khác, cập nhật các giá trị đó trong các chương trình liên quan để publisher và subscriber kết nối cùng broker và dùng cùng topic.

Broker công cộng phù hợp cho thực hành, không đảm bảo tính riêng tư hay tính sẵn sàng. Không gửi dữ liệu nhạy cảm; nếu broker không truy cập được, kiểm tra kết nối Internet/tường lửa hoặc cấu hình broker khác.

## Bài 1: Gửi và nhận thông điệp cơ bản

Trước khi chạy, mở `publisher_bai1.py` và thay giá trị `HO_TEN` và `MA_SV` bằng thông tin của người nộp.

Mở hai cửa sổ terminal tại thư mục dự án:

```bash
python subscriber_bai1.py
```

```bash
python publisher_bai1.py
```

Publisher gửi lên topic `iot/lab/message` mỗi 5 giây. Subscriber in topic, nội dung và thời điểm nhận. Nhấn Ctrl+C để dừng mỗi chương trình.

## Bài 2: Mô phỏng cảm biến nhiệt độ và độ ẩm

Mở hai cửa sổ terminal. Khởi động chương trình theo dõi trước:

```bash
python monitor_subscriber_bai2.py
```

```bash
python sensor_publisher_bai2.py
```

Sensor Publisher gửi JSON lên `iot/lab/sensor01/data` mỗi 3 giây. Monitoring Subscriber hiển thị thiết bị, nhiệt độ, độ ẩm và cảnh báo khi nhiệt độ > 35°C hoặc độ ẩm < 40%. Nhấn Ctrl+C để dừng mỗi chương trình.

## Bài 3: Điều khiển đèn thông minh

Mở hai cửa sổ terminal. Khởi động thiết bị trước để thiết bị sẵn sàng nhận lệnh:

```bash
python device_bai3.py
```

```bash
python controller_bai3.py
```

Controller subscribe topic trạng thái `iot/lab/light01/status` rồi mới nhận lệnh từ bàn phím. Nhập `ON` hoặc `OFF` để gửi lệnh lên `iot/lab/light01/cmd` và chờ phản hồi trạng thái. Nhập `EXIT` hoặc nhấn Ctrl+C để thoát controller; nhấn Ctrl+C để dừng thiết bị.

Thiết bị khởi tạo trạng thái là `OFF`. Với lệnh hợp lệ, thiết bị cập nhật trạng thái và publish JSON, ví dụ:

```json
{"device_id": "light01", "status": "ON"}
```

Lệnh khác `ON`, `OFF` hoặc `EXIT` sẽ không được gửi.

## Kết quả mong đợi

- **Bài 1:** Subscriber nhận payload gồm lời chào, mã sinh viên và họ tên.
- **Bài 2:** Monitoring Subscriber hiển thị dữ liệu JSON cảm biến và cảnh báo đúng các ngưỡng.
- **Bài 3:** Sau khi nhập `ON` hoặc `OFF`, controller nhận trạng thái JSON tương ứng từ thiết bị.

Bài 3 đã được kiểm thử end-to-end với broker công khai `broker.emqx.io` bằng topic riêng cho lượt thử. Broker mặc định trong mã vẫn là `test.mosquitto.org`; kết quả kiểm thử không đảm bảo broker công cộng luôn sẵn sàng.

Các kết quả Bài 1 và Bài 2 ở trên mô tả hành vi mong đợi khi broker hoạt động và các chương trình tương ứng đang chạy.

## Danh sách chương trình

| Bài | Chương trình gửi/thiết bị | Chương trình nhận/điều khiển |
|---|---|---|
| 1 | `publisher_bai1.py` | `subscriber_bai1.py` |
| 2 | `sensor_publisher_bai2.py` | `monitor_subscriber_bai2.py` |
| 3 | `device_bai3.py` | `controller_bai3.py` |
