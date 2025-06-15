# NC Cinema Star Wars

NC Cinema is a full-stack Django web application that allows users to browse movies, view screening times, and book tickets online. It supports user registration, login/logout, and includes role-based access through Django’s built-in admin panel. This project was developed to demonstrate competency across several full-stack development learning outcomes.
![main](https://github.com/jaredakigbesote/cinema-p4/blob/main/static/assets/images/media/NCmain.PNG)

## Features

- Home page displaying currently showing movies with images

![home](https://github.com/jaredakigbesote/cinema-p4/blob/main/static/assets/images/media/ncfilmbox.PNG)

- Individual movie detail pages with description, release info, and screening times

![details](https://github.com/jaredakigbesote/cinema-p4/blob/main/static/assets/images/media/details.PNG)

- User authentication (sign up, log in, log out)

![usersign](https://github.com/jaredakigbesote/cinema-p4/blob/main/static/assets/images/media/singup.PNG)
![userlog](https://github.com/jaredakigbesote/cinema-p4/blob/main/static/assets/images/media/login.PNG)

- Logged-in users can book available screenings

![notloogedin](https://github.com/jaredakigbesote/cinema-p4/blob/main/static/assets/images/media/notlog.PNG)
![loggedin](https://github.com/jaredakigbesote/cinema-p4/blob/main/static/assets/images/media/loggedin.PNG)

- Admin panel to manage movies, screenings, and bookings

![admin](https://github.com/jaredakigbesote/cinema-p4/blob/main/static/assets/images/media/admin.PNG)

- footer with authentication-based links

![footer](https://github.com/jaredakigbesote/cinema-p4/blob/main/static/assets/images/media/footer.PNG)

- Flash messages for user feedback (e.g. successful booking)

- Fully styled with a responsive CSS layout

## Design
- The design of NC Cinema focuses on creating an intuitive and visually appealing user experience that aligns with a modern movie-going theme. Key design decisions include:

__Layout and Structure__
- Home Page (Movie List): A clean grid layout displays currently showing movies with titles and posters. Each movie links to a detailed view.

- Movie Detail Page: Provides a dedicated space for movie information with a larger poster, synopsis, duration, release date, and a clearly separated booking section.

- Authentication Pages (Login & Signup): Styled simply and consistently, with centered forms and clear call-to-actions.

- Footer Navigation: Persistent at the bottom of the screen, allowing users to easily log in, sign up, or log out from any page.

__Styling and Aesthetics__
- Background: The site uses a full-page cinema-themed background to immerse users in a moviegoing experience.

- Color Scheme: A dark overlay with golden and light blue highlights was chosen to reflect a cinematic, luxurious vibe.

- Typography: Clean and readable fonts were used, with consistent sizing for headings, body text, and buttons.

__User Experience (UX)__
- Responsive Elements: The layout adapts to screen size and keeps key features (like booking buttons) accessible.

- Feedback: A popup message confirms successful bookings for better interaction.

- Error Handling: User-friendly error messages for login, signup, and form submissions.

- The overall design ensures that the site is easy to navigate, visually consistent, and enhances the user’s experience from browsing movies to booking seats.


## User Experience Flow

__Landing Page__:

- Users see a list of movies with posters and titles.

- They can click on any movie to view more details.

__Detail Page__:

- Users see the selected movie’s info, upcoming screenings, and can book tickets if logged in.

- If not logged in, the site prompts them to log in before booking.

__Authentication__:

- Users can create an account or log in.

- Once authenticated, users can make a booking and view success messages.

__Admin Access__:

- Admins can add/edit/delete movies, screenings, and users through Django’s admin interface.

## Technologies Used

- Python 3.12

- Django 5.2.3

- HTML/CSS 

- SQLite3 (development DB)

- Git & GitHub

- Gitpod

- cloudinary

## Key Issues & Fixes

__Issue__

- Static files (CSS) not loading

__Solution__

- Corrected static path and used {% load static %} with proper STATICFILES_DIRS

__Issue__

- Images not showing per movie

__Solution__

- Added ImageField to Movie model and ensured Pillow was installed

__Issue__

- Booking without being logged in

__Solution__

- Added logic to restrict booking views to authenticated users

__Issue__

- Logout error (HTTP 405)

__Solution__

- Changed logout to use POST method via form

__Issue__

- Database changes not showing

__Solution__

- Fixed with makemigrations and migrate

__Issue__

- Signup reverse URL error

__Solution__

- Corrected name='signup' in urls.py and ensured view was connected

__Issue__

- Broken footer layout

__Solution__

- Used flexbox and fixed alignment to maintain visual structure

## Future Features

- Add user booking history view

- Allow movie ratings and comments

- Add pagination to movie list

- Integrate Stripe for online payments

## Agile Methodologies

- Used Trello and GitHub Issues for tracking features, bugs, and progress

- Project evolved iteratively with priority-based tasks

## Data Modeling

- Models: Movie, Screening, Booking

- Used relational foreign keys and appropriate field types (e.g. DateTimeField, ImageField)

## Authentication & Authorization

- Implemented login, logout, signup

- Used Django’s @login_required decorator for view protection

- Admin role via Django’s admin panel

## Object-Oriented Programming

- Created models as Python classes

- Views use class-based and function-based structure with OOP principles

## Testing

- Navigation and page links tested across all main pages.

- Registration, login/logout, and user authentication flows verified.

- Admin panel access and content management functions confirmed.

- Image uploads tested via Django Admin and verified on Cloudinary.

- Booking restrictions for authenticated users tested successfully.

- Media and static files served correctly on Heroku deployment.

## Code Validation

- Python code validated with flake8 to ensure PEP8 compliance.(https://www.codewof.co.nz/style/python3/)

- HTML validated using W3C Markup Validator.(https://validator.w3.org/nu/?doc=https%3A%2F%2Fnc-cinema-0b8ae11a4fc2.herokuapp.com%2F)

- CSS validated with W3C CSS Validator.(https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fnc-cinema-0b8ae11a4fc2.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)

## Deployment

- GitHub used for version control

-  Create Heroku App

- Log in to Heroku Dashboard.

- Click New → Create new app, and give it a unique name (nc-cinema).

- Choose your region 

- Connect to GitHub Repository

- In your app dashboard, go to the Deploy tab.

-  Choose GitHub as the deployment method.

- Connect your GitHub account and search for your repository.

- Click Connect.

-  Set Buildpacks

- Set Config Vars

- Add Required Files(requirements.txt, Procfile)

- Push to Heroku

- Run Migrations & Create Superuser

- Launch the App

## Source Control

- Frequent commits with clear messages

- Used branching where appropriate (e.g. feature/signup-form)

## How to Run Locally

- Clone the repo:

- git clone https://github.com/yourusername/cinema-p4.git
cd cinema-p4

- Create virtual environment and activate it:

- python -m venv env
source env/bin/activate

- Install dependencies:

- pip install -r requirements.txt

- pip install pillow

- cd /workspace/cinema-p4/cinema_site

- Run migrations and start server:

- python manage.py migrate
- python manage.py runserver

- Visit http://127.0.0.1:8000/

## Credits

Heroku for project deployment

Cloudinary

Developed by [jared akigbesote]