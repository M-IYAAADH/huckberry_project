
HUCKBERRY – E-COMMERCE WEB APPLICATION
======================================

Huckberry is a Django-based e-commerce website built for selling sunglasses. It includes core features like product listings, filtering, user login/signup, cart management, checkout, and a full admin dashboard.

FEATURES
--------
• Browse and filter products
• User registration and login system
• Add items to cart
• Update or remove cart items
• Checkout and order confirmation
• Admin panel for managing users, products, and orders
• Mobile-friendly (responsive design)

TECHNOLOGIES USED
-----------------
• Backend: Python 3.12, Django 5.2
• Frontend: HTML5, CSS3, Bootstrap
• Database: SQLite3
• Other: Pillow (image support)

SETUP INSTRUCTIONS
------------------
1. Clone or extract the project
   > git clone <repo-url> OR unzip the folder

2. Navigate into the project folder
   > cd webdev

3. Create and activate a virtual environment
   > python -m venv env
   > env\Scripts\activate (Windows) OR source env/bin/activate (Mac/Linux)

4. Install dependencies
   > pip install -r requirements.txt

5. Run migrations
   > python manage.py makemigrations
   > python manage.py migrate

6. Create a superuser (admin)
   > python manage.py createsuperuser

7. Start the development server
   > python manage.py runserver

8. Access the site
   > Website: http://127.0.0.1:8000
   > Admin:   http://127.0.0.1:8000/admin

DEFAULT LOGIN CREDENTIALS
--------------------------
Admin:
• Username: user
• Password: user123

Test User:
• Username: tester
• Password: Pass@123

FOLDER STRUCTURE
----------------
webdev/
├── huckberry_project/
├── store/
├── static/
├── templates/
├── media/
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.txt

LESP CONSIDERATIONS
-------------------
• Legal: Privacy policy added; no sensitive payment data stored.
• Ethical: No dark patterns, honest data handling.
• Social: Clean, responsive, accessible design.
• Professional: Clean codebase, follows Django best practices.

AUTHOR INFO
-----------
• Name: Mohamed Iyaadh Ahmed
• Student ID: S2401276
• Program: BSc (Hons) Computer Science (UWE)
• College: Villa College
• Batch: September 2024
