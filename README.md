# 🧠 Quora Clone – Django Q&A Web App

A Quora-inspired Question and Answer web application built with Django.  
Users can register, log in, post questions, answer others' questions, and like answers.

---

## ✨ Features

- ✅ User Registration & Login
- ✅ Post Questions
- ✅ View Questions from Other Users
- ✅ Answer Questions
- ✅ Like Answers
- ✅ Logout

---

## 🚀 Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, Bootstrap 5
- **Database:** SQLite (default Django DB)
- **Authentication:** Django's built-in auth system

---

## 🛠️ Getting Started


1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/quora-clone.git
cd quora-clone
```

2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Set up the database
```bash
python manage.py migrate
```

5. Create a superuser
```bash
python manage.py createsuperuser
```

6.  Run the Development Server
```bash
python manage.py runserver
```
