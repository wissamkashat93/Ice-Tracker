# Ice Tracker

Ice Tracker is a Django-based web application designed to track and manage various cryptocurrency metrics. The application includes features such as tracking price changes, historical data, and analytical tools to provide insights into the cryptocurrency market.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Prerequisites

- Python 3.6+
- Django 3.0+
- PostgreSQL (or any preferred database)
- Virtualenv (recommended)

### Steps

1. **Clone the repository:**

    ```bash
    git clone https://github.com/wissamkashat93/Ice-Tracker.git
    cd Ice-Tracker
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the database:**

    - Create a PostgreSQL database.
    - Update the `DATABASES` setting in `settings.py` with your database configuration.

5. **Run migrations:**

    ```bash
    python manage.py migrate
    ```

6. **Create a superuser:**

    ```bash
    python manage.py createsuperuser
    ```

7. **Start the development server:**

    ```bash
    python manage.py runserver
    ```

8. **Access the application:**

    Open your web browser and navigate to `http://127.0.0.1:8000`.

## Usage

### Admin Interface

The admin interface can be accessed at `http://127.0.0.1:8000/admin`. Use the superuser credentials created earlier to log in.

### User Interface

Users can interact with the application through the main interface. Features include tracking cryptocurrency metrics, viewing historical data, and using analytical tools.

## Project Structure

The project structure is as follows:

```
Ice-Tracker/
├── Ice-Tracker/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── app/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py
└── requirements.txt
```

### Key Files

- `admin.py`: Configuration for the Django admin interface.
- `apps.py`: Application configuration.
- `forms.py`: Forms used in the application.
- `models.py`: Data models for the application.
- `tests.py`: Unit tests for the application.
- `urls.py`: URL routing configuration.
- `views.py`: View functions/classes for handling requests and rendering responses.

## Features

- Track cryptocurrency price changes and historical data.
- Analytical tools to provide insights into the market.
- User-friendly admin interface for managing data.
- Secure authentication and user management.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss your ideas.

### Steps to Contribute

1. Fork the repository.
2. Create a new branch: `git checkout -b my-feature-branch`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin my-feature-branch`
5. Submit a pull request.
