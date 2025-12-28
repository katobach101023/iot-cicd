# Bước 1: Lấy môi trường Python có sẵn
FROM python:3.9-slim

# Bước 2: Đặt thư mục làm việc trong máy ảo
WORKDIR /app

# Bước 3: Copy file code của bạn vào máy ảo
COPY app.py .

# Bước 4: Cài đặt thư viện cần thiết trong máy ảo
RUN pip install flask

# Bước 5: Ra lệnh cho máy ảo chạy file app.py khi khởi động
CMD ["python", "app.py"]