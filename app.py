from flask import Flask, request, jsonify

app = Flask(__name__)
stored_url = None

# Token bí mật để xác thực giữa máy A và máy B
SECRET_TOKEN = "123456"

@app.route("/", methods=["GET"])
def index():
    return "Ngrok Relay API is running.", 200

@app.route("/update", methods=["POST"])
def update_url():
    auth = request.headers.get("Authorization")
    if auth != f"Bearer {SECRET_TOKEN}":
        return jsonify({"error": "Unauthorized"}), 401

    data = request.get_json()
    if not data or "url" not in data:
        return jsonify({"error": "Missing URL in body"}), 400

    global stored_url
    stored_url = data["url"]
    print(f"[Relay] Received new URL: {stored_url}")
    return jsonify({"message": "URL updated"}), 200

@app.route("/latest", methods=["GET"])
def get_latest():
    if stored_url:
        return jsonify({"url": stored_url}), 200
    else:
        return jsonify({"message": "No URL stored yet"}), 404

if __name__ == "__main__":
    # chạy API trên port 5001
    app.run(host="0.0.0.0", port=5001)
