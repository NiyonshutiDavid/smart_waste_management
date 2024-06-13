# Smart Waste Management System

## Project Setup

1. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

2. **Set up the database:**
    ```sh
    flask db init
    flask db migrate
    flask db upgrade
    ```

3. **Run the application:**
    ```sh
    flask run
    ```

## Features

- User Registration and Login
- Waste Collection Schedule
- Recycling Tracker
- Waste Collection Services Management
- Admin Dashboard

## Testing

Run tests using:
```sh
python -m unittest discover -s tests
