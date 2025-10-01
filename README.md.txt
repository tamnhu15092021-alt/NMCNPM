# Selenium Login Test

## 📌 Yêu cầu
- Python 3.x
- Selenium
- ChromeDriver (cùng version với Chrome đang dùng)

## ▶️ Cách chạy
1. Chạy server:
   ```bash
   python -m http.server 8000
## Kết quả chạy test
- Test 1: Login thành công ✅
- Test 2: Sai password -> hiển thị lỗi ✅
- Test 3: Bỏ trống input -> cảnh báo yêu cầu nhập ✅
- Test 4: Link Forgot password hoạt động ✅
- Test 5: Link SIGN UP hoạt động ✅
- Test 6: Hiển thị đủ 3 nút social login (Facebook, Twitter, Google) ✅
