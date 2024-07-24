# devzery-backend-anju
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
   CREATE DATABASE testcase_management;
   ```

4. Connect to the new database:
   ```sql
   \c testcase_management
   ```

3. Create a new user role:
   ```sql
   CREATE USER testcase_user WITH PASSWORD 'your_secure_password';
   ```

4. Grant privileges to the new user:
   ```sql
   GRANT ALL PRIVILEGES ON DATABASE testcase_management TO testcase_user;
   ```

4. Connect to the new database:
   ```sql
   \c testcase_management
   ```
5. Grant privileges on the public schema to the new user
   ```sql
   GRANT ALL ON SCHEMA public TO testcase_user;
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
DB_NAME = "testcase_management"
DB_USER = "testcase_user"
DB_PASSWORD = "your_secure_password"  # The password you set in step 4
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
