# Quick Polls - Django Based Polling Application

## Overview

CRUD is a Django Based Simple Python Project allow user to understand the concept of Django & Ajax. Built with the Django framework and styled with Bootstrap & Implemented with Ajax, this application offers features such as user authentication, dynamic user creation with ajax, user updatation & More.

## Features

- **User Authentication**: Users can register, log in, and manage their accounts.
- **Login Required Middleware**: Ensure that certain views are accessible only to authenticated users.
- **Django Forms**: Utilize Django’s form handling to create and manage polls and user input.
- **Bootstrap UI**: A responsive and modern UI using Bootstrap for a better user experience.
- **Dynamic User Creation**: Create Users directly from home page without reloading application.

## Tech Stack

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)
![HTML](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E)
![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/mohit-trootech/Django-Crud
   cd Django-Crud
   ```

2. **Create and Activate a Virtual Environment**

   ```bash
   python -m venv env
   source env/bin/activate 
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**

   ```bash
   python manage.py migrate
   ```

5. **Create a Superuser (for admin access)**

   ```bash
   python manage.py createsuperuser
   ```

6. **Load sample data**

   ```bash
   python manage.py loaddata data.json
   ```

7. **Run the Development Server**

   ```bash
   python manage.py runserver
   ```

8. **Access the Application**

   Open your browser and navigate to `http://127.0.0.1:8000/`.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For any questions or issues, please contact:

- **GitHub**: [Github](https://github.com/mohit-trootech)
