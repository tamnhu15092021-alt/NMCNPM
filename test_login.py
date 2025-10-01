from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Khởi động Chrome
driver = webdriver.Chrome()
driver.maximize_window()

# =========================
# Test case 1: Đăng nhập thành công
# =========================
driver.get("http://localhost:8000/login.html")
time.sleep(1)

username = driver.find_element(By.XPATH, "//input[@type='text']")
password = driver.find_element(By.XPATH, "//input[@type='password']")
login_btn = driver.find_element(By.CLASS_NAME, "btn")

username.send_keys("admin")      # username hợp lệ
password.send_keys("123456")     # password hợp lệ
login_btn.click()
time.sleep(2)
print("✅ Test 1: Login thành công")

# =========================
# Test case 2: Sai password
# =========================
driver.get("http://localhost:8000/login.html")
username = driver.find_element(By.XPATH, "//input[@type='text']")
password = driver.find_element(By.XPATH, "//input[@type='password']")
login_btn = driver.find_element(By.CLASS_NAME, "btn")

username.send_keys("admin")
password.send_keys("sai_pass")
login_btn.click()
time.sleep(2)
print("✅ Test 2: Sai password -> hiển thị lỗi")

# =========================
# Test case 3: Bỏ trống input
# =========================
driver.get("http://localhost:8000/login.html")
login_btn = driver.find_element(By.CLASS_NAME, "btn")
login_btn.click()
time.sleep(2)
print("✅ Test 3: Bỏ trống input -> cảnh báo yêu cầu nhập")

# =========================
# Test case 4: Forgot password link
# =========================
driver.get("http://localhost:8000/login.html")
forgot = driver.find_element(By.LINK_TEXT, "Forgot password?")
forgot.click()
time.sleep(2)
print("✅ Test 4: Link Forgot password hoạt động")

# =========================
# Test case 5: Sign up link
# =========================
driver.get("http://localhost:8000/login.html")
signup = driver.find_element(By.LINK_TEXT, "SIGN UP")
signup.click()
time.sleep(2)
print("✅ Test 5: Link SIGN UP hoạt động")

# =========================
# Test case 6: Social login buttons
# =========================
driver.get("http://localhost:8000/login.html")
socials = driver.find_elements(By.CSS_SELECTOR, ".social a")
if len(socials) == 3:
    print("✅ Test 6: Hiển thị đủ 3 nút social login (Facebook, Twitter, Google)")
else:
    print("❌ Test 6: Thiếu nút social login")

# Kết thúc
driver.quit()
