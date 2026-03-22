# 🍽️ Recipe Hub – Django CRUD Application

## 📌 Overview

Recipe Hub is a web-based application built using Django that allows users to create, read, update, and delete (CRUD) recipes. This project was developed as a learning initiative to understand backend development concepts, database handling, and full-stack integration using Django.

The platform enables users to manage recipes efficiently while demonstrating best practices in Django architecture, templating, and database operations.

---

## 🎯 Purpose of the Project

This project was built with the goal of:

- Learning Django framework fundamentals
- Understanding CRUD operations in real-world scenarios
- Implementing backend logic with database interaction
- Building dynamic web pages using Django templates
- Practicing clean and modular project architecture

---



## 🚀 Features

-  Add new recipes with title, description, and image
-  View all recipes in a structured format
-  Update existing recipes
-  Delete recipes
- Search recipes by name
-  Clean UI using HTML, CSS (Bootstrap optional)
-  Django Admin panel integration

---



## 🛠️ Tech Stack

| Technology        | Usage                          |
|------------------|--------------------------------|
| Django           | Backend framework              |
| Python           | Programming language           |
| SQLite           | Database (default Django DB)   |
| HTML/CSS         | Frontend                       |
| Bootstrap        | UI Styling (optional)          |

---

## 📂 Project Structure

```bash
project_root/
│
├── manage.py
├── db.sqlite3
├── README.md
│
├── core/                      # Project configuration
│   ├── __pycache__/
│   ├── core/
│   └── settings.py
│
├── vege/                      # Main Django project
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── admin.py
│
├── recipe/                    # Django app (CRUD logic)
│   ├── __pycache__/
│   ├── migrations/
│   ├── templates/
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── recipes.html
│   │   ├── recipe_detail.html
│   │   └── update_recipe.html
│   │
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── templates/                 # Global templates
│   └── base.html
│
└── public/
    └── media/                 # Uploaded files (images hidden)
```

> Note: The `media/` folder stores uploaded recipe images and is not expanded here for clarity.



---

## 🧠 Architecture Diagram

### 🔹 ASCII Representation
      +---------------------+
      |      User           |
      +----------+----------+
                 |
                 v
      +---------------------+
      |    Django Views     |
      +----------+----------+
                 |
      +----------+----------+
      |     Django Models   |
      +----------+----------+
                 |
      +---------------------+
      |     SQLite DB       |
      +---------------------+

                 ^
                 |
      +----------+----------+
      |   Templates (HTML)  |
      +---------------------+


---

### 🔹 Mermaid Diagram (Optional)

```mermaid
graph TD
    A[User] --> B[Django Views]
    B --> C[Django Models]
    C --> D[SQLite Database]
    B --> E[Templates (HTML)]
    E --> A
    
⚙️ Installation & Setup

1️⃣ Clone the repository
git clone https://github.com/your-username/recipe-hub.git
cd recipe-hub


2️⃣ Create virtual environment
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

3️⃣ Install dependencies
pip install -r requirements.txt


4️⃣ Apply migrations
python manage.py makemigrations
python manage.py migrate

5️⃣ Run server
python manage.py runserver` 

🌐 Usage

Open browser and go to:

http://127.0.0.1:8000/