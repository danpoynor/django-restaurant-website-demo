# Django Restaurant Website Demo

This demo app provides a basic website for a fictitious restaurant allowing customers to view the menu, learn more about the restaurant, and make a reservation.

The app is built using [Django](https://www.djangoproject.com/) web framework using Python, SQLite, HTML, and CSS.

## Screenshots

## Features

The application includes the following features:

- **Home Page**: The landing page of the website.
- **About Page**: Provides information about the restaurant.
- **Booking Page**: Allows customers to make a booking.
- **Menu Page**: Displays the restaurant's menu.
- **Menu Item Page**: Provides details about a specific menu item.

## Views

The application includes the following views:

- `home`: Renders the home page.
- `about`: Renders the about page.
- `book`: Renders the booking page and handles the booking form submission.
- `menu`: Renders the menu page.
- `display_menu_item`: Renders a specific menu item page.

## Forms

The application includes a basic `BookingForm` in forms.py that allows customers to make a booking. Fields are based on the `Booking` model created in models.py.

## Installation and Setup

Follow these steps to get the project set up on your local machine:

1. Clone the repository:

```sh
git clone <repository-url>
```

2. Navigate to the project directory:

```sh
cd <project-directory>
```

3. Create a virtual environment and activate it:

```sh
python3 -m venv env
source env/bin/activate
```

4. Install the required packages:

```sh
pip install -r requirements.txt
```

5. Run the migrations:

```sh
python manage.py migrate
```

6. Create a superuser for the Django admin interface:

```sh
python manage.py createsuperuser
```

Follow the prompts to set a username, email, and password for the superuser.

7. Start the development server:

```sh
python manage.py runserver
```

The application will be available at `http://localhost:8000`.

## Admin Area

The Django admin area is used to manage menu items for the restaurant. You can add, edit, and delete menu items through the admin interface.

To access the admin area:

1. Start the development server:

```sh
python manage.py runserver
```

2. Open a web browser and navigate to `http://localhost:8000/admin`.

3. Log in with your admin credentials. If you haven't created an admin user yet, you can do so using the following command:

```sh
python manage.py createsuperuser
```

Once logged in, you can manage menu items by clicking on "Menus" under the "RESTAURANT" section.

## Tests

The application includes 21 tests for the models, views, and forms and cover a range of scenarios, including checking that the correct templates are used, the correct context data is passed to the templates, and the forms behave as expected.

### Running Tests

To run these tests, use the following command:

```sh
python manage.py test
```

This will run all the tests and provide a summary of the results.
