# FastAPI Login App 🚀

![FastAPI](https://img.shields.io/badge/FastAPI-0.110.0-blue?style=flat-square&logo=fastapi)  
API autentikasi menggunakan **FastAPI** dan **PostgreSQL**, mendukung **JWT Authentication** dan **Token Blacklist**.

## 📌 Fitur
✅ **Register & Login Pengguna**  
✅ **Autentikasi JWT (Access & Refresh Token)**  
✅ **Blacklist Token untuk Logout**  
✅ **Swagger UI dan Redoc otomatis**  

## 🚀 Instalasi

### 1. Clone Repo
```bash
git clone https://github.com/bebeksalju/login_app.git
cd login_app
```

### 2. Buat Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Buat File .env
Buat file `.env` di root proyek dan tambahkan konfigurasi berikut:
```bash
DATABASE_URL=postgresql://user:password@localhost:5432/db_name
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### 5. Jalankan Server
```bash
uvicorn main:app --reload
```
Server akan berjalan di [http://127.0.0.1:8000](http://127.0.0.1:8000)

## 📖 Dokumentasi API
FastAPI menyediakan dokumentasi otomatis:
- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- Redoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## 📌 Endpoint API
```bash
POST   /auth/register      # Registrasi pengguna baru
POST   /auth/login         # Login dan mendapatkan JWT Token
POST   /auth/refresh       # Mendapatkan Access Token baru dari Refresh Token
POST   /auth/logout        # Logout dan blacklist token
GET    /users/profile      # Mendapatkan info user
```

## 🌟 Kontribusi
Pull request sangat diterima! Pastikan untuk mengikuti standar coding yang baik.
