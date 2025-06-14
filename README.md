!Overview

NC Cinema is a full-stack Django web application that allows users to browse movies, view screening times, and book tickets online. It supports user registration, login/logout, and includes role-based access through Django’s built-in admin panel. This project was developed to demonstrate competency across several full-stack development learning outcomes.

!Features

Home page displaying currently showing movies with images

Individual movie detail pages with description, release info, and screening times

User authentication (sign up, log in, log out)

Logged-in users can book available screenings

Admin panel to manage movies, screenings, and bookings

Dynamic navbar/footer with authentication-based links

Flash messages for user feedback (e.g. successful booking)

Fully styled with a responsive CSS layout

!User Experience Flow

Landing Page:

Users see a list of movies with posters and titles.

They can click on any movie to view more details.

Detail Page:

Users see the selected movie’s info, upcoming screenings, and can book tickets if logged in.

If not logged in, the site prompts them to log in before booking.

Authentication:

Users can create an account or log in.

Once authenticated, users can make a booking and view success messages.

Admin Access:

Admins can add/edit/delete movies, screenings, and users through Django’s admin interface.

Technologies Used

Python 3.12

Django 5.2.3

HTML/CSS 

SQLite3 (development DB)

Git & GitHub

Gitpod (

  Key Issues & Fixes

Issue

Solution

Static files (CSS) not loading

Corrected static path and used {% load static %} with proper STATICFILES_DIRS

Images not showing per movie

Added ImageField to Movie model and ensured Pillow was installed

Booking without being logged in

Added logic to restrict booking views to authenticated users

Logout error (HTTP 405)

Changed logout to use POST method via form

Database changes not showing

Fixed with makemigrations and migrate

Signup reverse URL error

Corrected name='signup' in urls.py and ensured view was connected

Broken footer layout

Used flexbox and fixed alignment to maintain visual structure

future Improvements

Add user booking history view

Allow movie ratings and comments

Add pagination to movie list

Integrate Stripe for online payments (optional)



 Learning Outcomes

LO1: Agile Methodologies

Used Trello and GitHub Issues for tracking features, bugs, and progress

Project evolved iteratively with priority-based tasks

LO2: Data Modeling

Models: Movie, Screening, Booking

Used relational foreign keys and appropriate field types (e.g. DateTimeField, ImageField)

LO3: Authentication & Authorization

Implemented login, logout, signup

Used Django’s @login_required decorator for view protection

Admin role via Django’s admin panel

LO4: Object-Oriented Programming

Created models as Python classes

Views use class-based and function-based structure with OOP principles

LO5: Testing (to be completed)


LO6: Deployment

Project hosted in Gitpod with persistent DB

GitHub used for version control

LO7: Source Control

Frequent commits with clear messages

Used branching where appropriate (e.g. feature/signup-form)

How to Run Locally

Clone the repo:

git clone https://github.com/yourusername/cinema-p4.git
cd cinema-p4

Create virtual environment and activate it:

python -m venv env
source env/bin/activate

Install dependencies:

pip install -r requirements.txt

Run migrations and start server:

python manage.py migrate
python manage.py runserver

Visit http://127.0.0.1:8000/

Credits

Developed by [jared akigbesote]