# Gas Utility Service Website

## Overview

The Gas Utility Service website is a Django-based web application designed to streamline gas utility service management. Users can submit service requests, track their status, and manage their account information. Customer support representatives can also manage and resolve service requests efficiently.

## Features

- User-friendly registration and authentication system.
- Submission of service requests with the option to provide details and attach files.
- Real-time tracking of service requests, including submission and resolution timestamps.
- Responsive and intuitive interface for both users and administrators.

## Technologies Used

- **Backend**: Django
- **Frontend**: HTML, CSS, JavaScript
- **Database**: PostgreSQL
- **Deployment**: Gunicorn, Nginx, Render
- **Version Control**: Git

## Live Demo

Visit the live site: [Gas Utility Service Website](https://gas-utility-website-1.onrender.com)

---

## Installation

### Prerequisites

Before setting up the project, ensure you have:

- Python 3.x installed
- `pip` package manager
- PostgreSQL (if using a production-ready database)

### Steps to Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/gas-utility-website.git
   cd gas-utility-website
   ```

2. **Create a Virtual Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Database**
   - Create a PostgreSQL database:
     ```sql
     CREATE DATABASE gas_utility_db;
     CREATE USER your_user WITH PASSWORD 'your_password';
     ALTER ROLE your_user SET client_encoding TO 'utf8';
     ALTER ROLE your_user SET default_transaction_isolation TO 'read committed';
     ALTER ROLE your_user SET timezone TO 'UTC';
     GRANT ALL PRIVILEGES ON DATABASE gas_utility_db TO your_user;
     ```

   - Update `DATABASES` in `settings.py` to match the new database credentials.

5. **Run Database Migrations**
   ```bash
   python manage.py migrate
   ```

6. **Collect Static Files**
   ```bash
   python manage.py collectstatic
   ```

7. **Run the Development Server**
   ```bash
   python manage.py runserver
   ```

   Visit `http://127.0.0.1:8000` in your browser.

---

## Deployment

The website is deployed on Render. Follow these steps to deploy:

1. **Create a Web Service on Render**:
   - Link it to your GitHub repository.

2. **Set Environment Variables**:
   - Add variables like `DATABASE_URL`, `SECRET_KEY`, etc., in Render's settings.

3. **Configure Commands**:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn gas_utility.wsgi:application`

4. **Static Files**:
   Ensure `STATIC_ROOT` is correctly configured in `settings.py` for deployment.

Your site will be live at the URL provided by Render.

---

## Contributing

Contributions are welcome! Feel free to submit a pull request to enhance the project or fix issues.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

