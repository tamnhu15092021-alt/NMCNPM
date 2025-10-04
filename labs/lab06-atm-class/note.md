# Lab 06 – Thiết kế chi tiết lớp & kiến trúc ATM

## 1. Class Diagram
- File: `class-atm.puml`, `class-atm.png`
- Nội dung: mô tả các lớp trong hệ thống ATM gồm ATM, Card, Account, Transaction.
- Quan hệ:
  - ATM sử dụng Card và Transaction
  - Card liên kết với Account
  - Account liên kết với Transaction

## 2. Package Diagram
- File: `package-diagram.puml`, `package-diagram.png`
- Nội dung: mô tả kiến trúc hệ thống ATM ở mức package.
- Các package chính:
  - **UI**: giao diện người dùng
  - **Controller**: xử lý logic chính
  - **BankService**: dịch vụ ngân hàng (quản lý tài khoản, giao dịch)
  - **Hardware**: phần cứng ATM (card reader, cash dispenser)

## 3. Danh sách file nộp
- `class-atm.puml`
- `class-atm.png`
- `package-diagram.puml`
- `package-diagram.png`
- `notes.md`
