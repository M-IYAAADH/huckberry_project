# Project Structure

```text
huckberry_project/
├── huckberry_project/              # Django project config package
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── __pycache__/                # Compiled Python files
│       └── ...
│
├── store/                          # Main Django app
│   ├── migrations/                 # Database migrations
│   │   ├── __init__.py
│   │   └── ...                     # 0001_initial.py, etc.
│   │
│   ├── templates/
│   │   ├── base.html
│   │   └── store/
│   │       ├── home.html
│   │       ├── products.html
│   │       ├── product_detail.html
│   │       ├── view_cart.html
│   │       ├── checkout.html
│   │       ├── checkout_success.html
│   │       ├── signup.html
│   │       ├── login.html
│   │       ├── contact.html
│   │       ├── contact_success.html
│   │       ├── about.html
│   │       └── privacy.html
│   │
│   ├── __pycache__/                # Compiled Python files
│   │   └── ...
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   ├── forms.py                    # (if present)
│   └── tests.py                    # (if present)
│
├── static/                         # Static assets
│   ├── css/
│   │   └── ...                     # Stylesheets
│   ├── js/
│   │   └── ...                     # JavaScript files
│   └── images/
│       └── ...                     # Static images, icons, logos
│
├── media/                          # Uploaded / media files
│   └── product_images/
│       └── ...                     # Product image files
│
├── db.sqlite3                      # SQLite database file
├── db.json                         # Fixture / exported data (if used)
├── manage.py                       # Django management script
├── requirements.txt                # Python dependencies
└── README.md                       # Project overview
