# Bài thực hành MQTT - Buổi 1

Dự án này chứa mã nguồn cho 2 bài thực hành về giao thức MQTT, được cập nhật theo source code mẫu của môn học.

## Yêu cầu môi trường
- Python 3.x
- Thư viện `paho-mqtt` (Bản mới)
- Cài đặt thư viện: `pip install paho-mqtt`

## BÀI 1: Gửi và nhận thông điệp cơ bản
Gửi một chuỗi ký tự chứa thông tin cá nhân.
- File gửi: `publisher_bai1.py`
- File nhận: `subscriber_bai1.py`

*Lưu ý: Mở file `publisher_bai1.py` và sửa biến `HO_TEN` và `MA_SV` (dòng 9, 10) thành thông tin thật của bạn trước khi chạy để đúng format nộp bài nhé!*

## BÀI 2: Mô phỏng Sensor IoT (Gửi nhận định dạng JSON)
Gửi dữ liệu nhiệt độ, độ ẩm giả lập. Subscriber sẽ parse JSON và cảnh báo nếu nhiệt độ > 35 độ hoặc độ ẩm < 40%.
- File mô phỏng cảm biến (gửi): `sensor_publisher_bai2.py`
- File theo dõi (nhận & cảnh báo): `monitor_subscriber_bai2.py`
