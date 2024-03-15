
<h1 align="center">
  <br>
  <br>
  Django Simple admin dashboard and Signup/SignIn page
  <br>
</h1>

<h4 align="center">A secure Django project with user authentication, admin panel (can create ,edit ,search or delete user) and also a signUp and signIn page with basic constraints.</h4>


<p align="center"><img src="https://maxmautner.com/public/images/django.gif" width="200" height="100" /></p>

## Key Features

* User authentication with login and signup functionality.
* Signup page with restriction on creating already exsisted username or email.ii
* Robust admin panel accessible only to authorized admin.
* Secure session handling to prevent unauthorized access.
* CRUD (Create, Read, Update, Delete) operations for admin in the admin panel.

## How To Use

If only need login,signup & admin Page:
You can add this to your website by simply adding the web app called support_app inside the NDBlog folder 

else:
simply download the whole project .If needed you can also download the venv.

**OR GO FOR:**
Installation

1) Prerequisites:
* Python (https://www.python.org/downloads/)
* pip (package installer for Python)

2) Clone the repository:
git clone https://your-repository-url.git
cd your-project-name

3) Create a virtual environment (recommended):
python -m venv venv
source venv/bin/activate

4) Install dependencies:
pip install -r requirements.txt

5) Migrate database schema:
python manage.py migrate

6) Create a superuser:
python manage.py createsuperuser


> **USAGE**

* Start the development server:
	Bash
	python manage.py runserver
		This will typically run the server on http://127.0.0.1:8000/ by default.

Access the login page:
	Visit http://127.0.0.1:8000/login/ in your web browser.

Log in or sign up:
	If you already have an account, enter your credentials and log in.
	If you are a new user, click on the "Sign Up" link and create a new account.

Access the admin panel (authorized users only):
	The admin panel URL will be generated dynamically based on your settings (e.g., http://127.0.0.1:8000/admin/).
	Only authorized users (superuser or users with appropriate permissions) can access the admin panel.

CRUD operations in the admin panel:
	Manage data using the provided forms in the admin interface.

***Security Considerations***

Session Management: 	This project employs secure session handling to prevent unauthorized access after login.<br>

CSRF Protection: 	Django's built-in CSRF protection is enabled to mitigate cross-site request forgery attacks.<br>

Password Hashing: 	User passwords are securely hashed using Django's password hashing mechanism.<br>

Regular Updates: 	Keep your project's dependencies (Django, Python) up-to-date to benefit from security fixes.<br>

<br>
<br>
***Contributing***

We welcome contributions to this project! Feel free to create pull requests with improvements or bug fixes.


