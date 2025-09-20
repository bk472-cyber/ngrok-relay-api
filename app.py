from flask import Flask, request, jsonify

app = Flask(__name__)

# === Cấu hình bảo mật ===
SECRET_TOKEN = "123456"  # Trùng với token từ Máy A

# === Biến lưu URL mới nhất ===
latest_data = {}

# === Endpoint nhận URL từ máy A ===
@app.route("/update", methods=["POST"])
def update_url():
    auth = request.headers.get("Authorization", "")
    if auth != f"Bearer {SECRET_TOKEN}":
        return jsonify({"error": "Unauthorized"}), 401

    data = request.get_json()
    if not data or "url" not in data:
        return jsonify({"error": "Missing URL"}), 400

    latest_data["url"] = data["url"]
    latest_data["machine"] = data.get("machine", "unknown")
    return jsonify({"message": "URL updated successfully"}), 200

# === Endpoint cho máy B lấy URL mới nhất ===
@app.route("/latest", methods=["GET"])
def get_latest():
    if "url" not in latest_data:
        return jsonify({"error": "No data yet"}), 404
    return jsonify(latest_data), 200

# === Kiểm tra server đang chạy ===
@app.route("/", methods=["GET"])
def index():
    return "Relay API is running.", 200
