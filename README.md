# Ngrok Relay API

Một API relay để máy A gửi URL ngrok và máy B lấy URL mới nhất.

## Endpoints

- `POST /update`: cập nhật URL mới  
  - Header `Authorization: Bearer <TOKEN>`  
  - Body JSON: `{"url": "https://..."}`

- `GET /latest`: lấy URL mới nhất đã được cập nhật

## Cấu hình

- Thay `SECRET_TOKEN` trong `app.py` thành token bí mật của bạn  
- Deploy app này lên Render.com hoặc bất kỳ server nào có thể public internet  
- Máy A gửi đến `https://<yourdomain>/update`, Máy B lấy từ `https://<yourdomain>/latest`
