# Lab 07 – Phát triển Module Rút tiền (Withdraw)

## 🎯 Mục tiêu
- Viết module mô phỏng chức năng **Withdraw** trong ATM.
- Kết nối MySQL, xử lý giao dịch, kiểm tra số dư, log transaction.

## 📂 Thư mục
`/labs/lab07-withdraw-module/`

## 🛠 Công cụ
- Python 3
- MySQL + mysql-connector-python

## ⚙️ Cách chạy
1. Tạo database và bảng:
   ```sql
   CREATE DATABASE atm_demo;
   USE atm_demo;

   CREATE TABLE accounts (
       account_id INT AUTO_INCREMENT PRIMARY KEY,
       balance DECIMAL(10,2) NOT NULL
   );

   CREATE TABLE cards (
       card_no VARCHAR(20) PRIMARY KEY,
       account_id INT,
       pin_hash VARCHAR(64),
       FOREIGN KEY (account_id) REFERENCES accounts(account_id)
   );

   CREATE TABLE transactions (
       tx_id INT AUTO_INCREMENT PRIMARY KEY,
       account_id INT,
       card_no VARCHAR(20),
       atm_id INT,
       tx_type VARCHAR(20),
       amount DECIMAL(10,2),
       balance_after DECIMAL(10,2),
       created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
   );
