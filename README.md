![FixItNow Banner](banner.png)

# FixItNow - Professional Home Service Providing Platform

[![Deployment](https://img.shields.io/badge/Deployed-Vercel-black?style=flat-square&logo=vercel)](https://vercel.com)
[![Django](https://img.shields.io/badge/Framework-Django-092E20?style=flat-square&logo=django)](https://www.djangoproject.com/)
[![SQLite](https://img.shields.io/badge/Database-PostgreSQL/SQLite-336791?style=flat-square&logo=postgresql)](https://www.postgresql.org/)
[![Razorpay](https://img.shields.io/badge/Payments-Razorpay-020425?style=flat-square&logo=razorpay)](https://razorpay.com/)

**FixItNow** is a modern, full-stack home service marketplace designed to bridge the gap between homeowners and skilled service professionals. Whether it's plumbing, electrical work, cleaning, or general repairs, FixItNow provides a seamless platform for booking reliable services with integrated secure payments.

---

## 🚀 Key Features

- **Dual Authentication**: Dedicated portals for both Customers and Service Professionals.
- **Service Categories**: Browse categorized services like Cleaning, Plumbing, Electrical, etc.
- **Booking Management**: Real-time booking system with status tracking (Pending, Confirmed, Completed).
- **Secure Payments**: Integrated with **Razorpay** for safe and seamless transactions.
- **Reviews & Ratings**: Transparent feedback system to ensure high-quality service.
- **Admin Dashboard**: Comprehensive control panel to manage users, services, cities, and orders.
- **Dynamic Search**: Filter services by city and category to find exactly what you need.

---

## 🛠️ Tech Stack

- **Backend**: Python, Django (Web Framework)
- **Frontend**: HTML5, CSS3 (Vanilla), JavaScript
- **Database**: PostgreSQL (Production/Vercel), SQLite (Local Development)
- **Payment Gateway**: Razorpay API
- **Static File Handling**: WhiteNoise
- **Deployment**: Vercel

---

## 📥 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/vishnucax/fixitnow-home-service-providing-platform.git
cd fixitnow-home-service-providing-platform
```

### 2. Create Virtual Environment
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/macOS
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser (Admin)
```bash
python manage.py createsuperuser
```

### 6. Run Server
```bash
python manage.py runserver
```
Visit `http://127.0.0.1:8000` to see the app in action!

---

## ☁️ Deployment on Vercel

This project is pre-configured for deployment on Vercel.

1. **Push your changes** to your GitHub repository.
2. **Import the project** in the [Vercel Dashboard](https://vercel.com).
3. **Environment Variables**: Set the following variables in Vercel:
   - `SECRET_KEY`: Your Django secret key.
   - `RAZOR_KEY_ID`: Your Razorpay Test/Live ID.
   - `RAZOR_KEY_SECRET`: Your Razorpay Test/Live Secret.
   - `EMAIL_HOST_USER`: Your Gmail address.
   - `EMAIL_HOST_PASSWORD`: Your Gmail App Password.
4. **Database**: Link a **Vercel Postgres** database to the project.

---

## 🔒 Security Recommendations

- **Environment Variables**: Always move sensitive keys (Razorpay, SMTP, Secret Key) to environment variables in production.
- **Debug Mode**: Ensure `DEBUG = False` in `settings.py` for live deployments.

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Developed with ❤️ for the BCA Final Year Project.
