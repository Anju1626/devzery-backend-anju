# devzery-backend-anju

Here's a README file for setting up and starting a Flask project:

# Flask Project Setup Guide

This guide will help you set up and run the Flask backend for the Test Case Management application.

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Setup

1. Clone the repository (if you haven't already):
   ```
   git clone <repository-url>
   cd <project-directory>
   ```

2. Create a virtual environment:
   ```
   python3 -m venv venv
   ```

3. Activate the virtual environment:
   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```
   - On Windows:
     ```
     venv\Scripts\activate
     ```

4. Install required packages:
   ```
   pip install flask flask-cors psycopg2-binary
   ```

## Configuration

1. Create a `.env` file in the project root directory:
   ```
   touch .env
   ```

2. Add the following environment variables to the `.env` file:
   ```
   FLASK_APP=app.py
   FLASK_ENV=development
   DB_NAME=devzery_database
   DB_USER=tester
   DB_PASSWORD=test_password
   DB_HOST=localhost
   DB_PORT=5432
   ```
   Replace `test_password` with the actual password you set for your PostgreSQL user.

## Running the Application

1. Ensure your PostgreSQL database is running and properly set up (refer to the PostgreSQL setup guide).

2. With your virtual environment activated, start the Flask application:
   ```
   flask run
   ```

3. The application should now be running on `http://127.0.0.1:3001/`

## API Endpoints

- GET `/api/testcases`: Retrieve all test cases
- PUT `/api/testcases/<case_id>`: Update a specific test case
- GET `/api/testcases/search?query=<search_term>`: Search for test cases

## Development

- To enable debug mode, set `FLASK_ENV=development` in your `.env` file or export it as an environment variable.
- The application will automatically reload when you make changes to the code.

## Troubleshooting

- If you encounter a "ModuleNotFoundError", ensure you've activated the virtual environment and installed all required packages.
- For database connection issues, verify your PostgreSQL setup and connection details in the `.env` file.

## Additional Commands

- To deactivate the virtual environment:
  ```
  deactivate
  ```

- To install additional packages:
  ```
  pip install package-name
  ```

- To generate a `requirements.txt` file:
  ```
  pip freeze > requirements.txt
  ```

## Security Notes

- Never commit your `.env` file or any file containing sensitive information like database credentials to version control.
- For production deployment, ensure to set `FLASK_ENV=production` and use a production-ready WSGI server like Gunicorn.

For more detailed information, refer to the [Flask documentation](https://flask.palletsprojects.com/).


This README provides a comprehensive guide for setting up and running your Flask project. It covers:

1. Setting up a virtual environment
2. Installing dependencies
3. Configuring environment variables
4. Running the application
5. Basic API endpoint information
6. Troubleshooting tips
7. Additional useful commands
8. Security considerations

You may want to customize this further based on any specific requirements or additional setup steps for your particular project.


Here's a README file for setting up PostgreSQL for your project:

# PostgreSQL Setup Guide

This guide will help you set up PostgreSQL for the Test Case Management application.

## Prerequisites

- macOS operating system
- Homebrew package manager

## Installation

1. Install PostgreSQL using Homebrew:
   ```
   brew install postgresql
   ```

2. Start the PostgreSQL service:
   ```
   brew services start postgresql
   ```

3. Verify that PostgreSQL is running:
   ```
   brew services list
   ```
   You should see postgresql with the status "started".

## Database Setup

1. Connect to PostgreSQL:
   ```sql
   psql postgres
   ```

2. Create a new database:
   ```sql
   CREATE DATABASE devzery_database;
   ```

4. Connect to the new database:
   ```sql
   \c devzery_database
   ```

3. Create a new user role:
   ```sql
   CREATE USER tester WITH PASSWORD 'test_password';
   ```

4. Grant privileges to the new user:
   ```sql
   GRANT ALL PRIVILEGES ON DATABASE devzery_database TO tester;
   ```

4. Connect to the new database:
   ```sql
   \c devzery_database
   ```
5. Grant privileges on the public schema to the new user
   ```sql
   GRANT ALL ON SCHEMA public TO tester;
   ```

5. Create the 'testcases' table:
   ```sql
   CREATE TABLE testcases (
       id SERIAL PRIMARY KEY,
       name VARCHAR(255) NOT NULL,
       estimate_time VARCHAR(50),
       module VARCHAR(100),
       priority VARCHAR(50),
       status VARCHAR(50)
   );
   ```

6. Insert sample data:
   ```sql
   INSERT INTO testcases (name, estimate_time, module, priority, status)
   VALUES 
       ('Test Case 1', '5 Minutes', 'Onboarding', 'Low', 'Select'),
       ('Test Case 2', '5 Minutes', 'User Log In', 'Medium', 'Select'),
       ('Test Case 3', '5 Minutes', 'Password', 'High', 'Select');
   ```

7. Exit psql:
   ```
   \q
   ```

## Configuration

Update the database connection parameters in your Flask application:

```python
DB_NAME = "devzery_database"
DB_USER = "tester"
DB_PASSWORD = "test_password"  # The password you set in step 4
DB_HOST = "localhost"
DB_PORT = "5432"
```

## Useful Commands

- Stop PostgreSQL: `brew services stop postgresql`
- Restart PostgreSQL: `brew services restart postgresql`
- Check PostgreSQL version: `postgres --version`

## Troubleshooting

If you encounter any issues:
1. Ensure PostgreSQL is running: `brew services list`
2. Check PostgreSQL logs: `brew services log postgresql`
3. Verify database connection parameters in your application

For more detailed information, refer to the [PostgreSQL documentation](https://www.postgresql.org/docs/).
```

This README provides a step-by-step guide for setting up PostgreSQL on macOS, creating the necessary database and table, and includes some useful commands and troubleshooting tips. You may want to customize it further based on your specific project requirements or add any additional setup steps that might be necessary for your application.
