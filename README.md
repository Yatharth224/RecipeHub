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
project_root/
│
├── manage.py
├── db.sqlite3
├── README.md
│
├── core/                      # Project configuration
│   ├── __pycache__/
│   ├── core/
│   ├── settings.py
│
├── vege/                      # Main Django project
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── admin.py
│
├── recipe/                    # Django app (CRUD logic)
│   ├── __pycache__/
│   ├── migrations/
│   ├── templates/
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── recipes.html
│   │   ├── recipe_detail.html
│   │   ├── update_recipe.html
│   │
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│
├── templates/                 # Global templates
│   ├── base.html
│
├── public/
│   ├── media/                 # Uploaded files (images not shown)
