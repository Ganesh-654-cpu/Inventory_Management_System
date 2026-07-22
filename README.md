# 📦 Inventory Management System

A web-based Inventory Management System developed using **Django** that helps businesses efficiently manage products, categories, suppliers, purchases, sales, and stock levels.

---

## 🚀 Features

- 🔐 User Authentication (Login & Logout)
- 📊 Dashboard with Inventory Summary
- 📦 Product Management (Add, Update, Delete)
- 🗂️ Category Management
- 🏢 Supplier Management
- 👥 Customer Management
- 🛒 Purchase Management
- 💰 Sales Management
- 📈 Stock Management
- 🔍 Search & Filter Products
- 📋 Reports Module
- 🖼️ Product Image Upload
- 📱 Responsive UI

---

## 🛠️ Tech Stack

### Backend
- Python 3.x
- Django 5.x

### Frontend
- HTML5
- CSS3
- Bootstrap 5
- JavaScript

### Database
- SQLite (Development)
- PostgreSQL/MySQL (Production)

### Tools
- Git
- GitHub
- Visual Studio Code

---

## 📂 Project Structure

```
inventory_management/
│
├── inventory_management/
│
├── accounts/
├── dashboard/
├── categories/
├── products/
├── suppliers/
├── customers/
├── purchases/
├── sales/
├── reports/
│
├── media/
├── static/
├── templates/
│
├── manage.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/inventory-management-system.git
```

Go to Project Folder

```bash
cd inventory-management-system
```

Create Virtual Environment

```bash
python -m venv .venv
```

Activate Virtual Environment

### Windows

```bash
.venv\Scripts\activate
```

### Linux / Mac

```bash
source .venv/bin/activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

Create Superuser

```bash
python manage.py createsuperuser
```

Run Server

```bash
python manage.py runserver
```

Open Browser

```
http://127.0.0.1:8000/
```

Admin Panel

```
http://127.0.0.1:8000/admin/
```

---

## 📸 Screenshots

Add screenshots here after completing the project.

Example:

- Login Page
- Dashboard
- Product List
- Add Product
- Sales Module
- Reports

---

## 📊 Modules

### Dashboard
- Total Products
- Low Stock Products
- Sales Summary
- Purchase Summary

### Categories
- Add Category
- Update Category
- Delete Category

### Products
- Product CRUD
- Product Image
- Barcode
- Stock Quantity

### Suppliers
- Supplier Information
- Contact Details

### Customers
- Customer Records

### Purchases
- Purchase Entry
- Stock Update

### Sales
- Sales Invoice
- Stock Deduction

### Reports
- Sales Report
- Purchase Report
- Stock Report

---

## 🔒 Authentication

- User Login
- Logout
- Django Admin
- Session Management

---

## 📦 Future Enhancements

- Barcode Scanner
- QR Code Generator
- Email Notifications
- GST Billing
- Invoice PDF Download
- Export Excel & PDF
- REST API
- Role-Based Access Control
- Multi-Warehouse Support
- Docker Deployment

---

## 🤝 Contributing

1. Fork the repository
2. Create a new branch

```bash
git checkout -b feature-name
```

3. Commit changes

```bash
git commit -m "Add new feature"
```

4. Push to GitHub

```bash
git push origin feature-name
```

5. Create a Pull Request

---

## 👨‍💻 Author

**Ganesh Mahajan**

- Python Full Stack Developer
- Pune, Maharashtra
- GitHub: https://github.com/Ganesh-654-cpu
- LinkedIn: https://www.linkedin.com/in/ganeshmahajan654

If you found this project helpful, please give it a ⭐ on GitHub.

Happy Coding! 🚀
