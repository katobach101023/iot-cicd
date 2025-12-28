from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    # Đây là nội dung hiển thị khi bạn truy cập vào server
    return "Chào mừng bạn đến với IoT API Server - Phien ban 2.0"

@app.route('/status')
def status():
    # Giả lập một API kiểm tra trạng thái thiết bị
    return jsonify({"device": "Cảm biến nhiệt độ", "status": "Hoạt động"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)