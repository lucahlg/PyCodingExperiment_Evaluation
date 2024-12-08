# Smart Fridge Application

## Project Overview

The Smart Fridge Application is designed to help users manage their fridge inventory efficiently. The application consists of a frontend built with React and a backend built with Flask and Flask-RestX. The backend communicates with a MySQL database to store user and inventory data.

## Tech Stack

- **Frontend:** React, React Router, Axios, Bootstrap
- **Backend:** Flask, Flask-RestX, Flask-CORS, Flask-Login, MySQL Connector, Python Dotenv
- **Database:** MySQL

## Directory Structure

```
smart-fridge-app/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── routes/
│   │   │   └── main.py
│   │   ├── models/
│   │   └── services/
│   ├── .env
│   ├── .gitignore
│   ├── app.py
│   ├── requirements.txt
├── db/
│   └── schema.sql
├── docs/
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   └── Home.js
│   │   ├── services/
│   │   ├── styles/
│   │   ├── App.js
│   │   ├── index.js
│   ├── .gitignore
│   ├── package.json
│   ├── package-lock.json
├── .gitignore
├── README.md
```

## Setup Instructions

### Prerequisites

- Node.js and npm
- Python 3 and pip
- MySQL

### Frontend Setup

1. Navigate to the `frontend/` directory:
    ```bash
    cd frontend
    ```

2. Install the dependencies:
    ```bash
    npm install
    ```

3. Start the React application:
    ```bash
    npm start
    ```

### Backend Setup

1. Navigate to the `backend/` directory:
    ```bash
    cd backend
    ```

2. Create a virtual environment:
    ```bash
    python3 -m venv venv
    ```

3. Activate the virtual environment:
    ```bash
    source venv/bin/activate
    ```

4. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Set up the MySQL database:
    - Create a database named `smart_fridge`.
    - Run the `schema.sql` script to create the necessary tables:
        ```bash
        mysql -u root -p smart_fridge < ../db/schema.sql
        ```

6. Start the Flask application:
    ```bash
    python app.py
    ```

### Environment Variables

- The backend uses environment variables to store sensitive information. Create a `.env` file in the `backend/` directory with the following content:
    ```
    DB_HOST=localhost
    DB_USER=root
    DB_PASSWORD=password
    DB_NAME=smart_fridge
    ```

## Contributing

If you would like to contribute to the project, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.
