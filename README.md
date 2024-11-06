------------------------------------------------------------------------------------------------------------------------------------

# File Sharing System

## Overview

The **File Sharing System** is a Django-based web application that allows users to upload, share, and manage files securely. It provides essential features such as user authentication, file management, and secure file sharing. The system ensures that users can easily store files and share them with others via unique, time-limited links.

## Features

- **User Authentication**: Users can sign up, log in, and log out securely.
- **File Upload**: Users can upload files of different types (e.g., documents, images, videos).
- **File Management**: Users can manage their uploaded files (view, delete, etc.).
- **File Sharing**: Users can generate unique, shareable links to allow others to download files.
- **Secure Download Links**: Links are time-limited for added security.
- **File Preview**: Users can preview certain file types (images, PDFs, etc.).
- **Admin Panel**: Django's built-in admin panel for managing users and files.

## Technologies Used

- **Backend**: Django (Python Web Framework)
- **Frontend**: HTML, CSS, JavaScript (Basic UI)
- **Database**: SQLite (default for development)
- **Authentication**: Django’s built-in user authentication system

## Installation Guide

### Prerequisites

Before setting up the project, ensure the following are installed on your system:

- Python 3.x (preferably 3.8 or above)
- pip (Python package installer)
- Git

### Clone the Repository

Start by cloning the repository to your local machine:

```bash
git clone https://github.com/sakib078/File-sharing-system.git
cd File-sharing-system
```

### Set Up Virtual Environment (Recommended)

Creating a virtual environment ensures that dependencies for the project are isolated:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Install Dependencies

Once the virtual environment is activated, install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

### Set Up Database

The project uses SQLite for local development. Set up the database with the following command:

```bash
python manage.py migrate
```

### Create a Superuser

Create a superuser account to access the Django admin panel:

```bash
python manage.py createsuperuser
```

Follow the prompts to set up the admin credentials.

### Run the Development Server

Finally, run the development server:

```bash
python manage.py runserver
```

You can now access the project in your browser at:  
`http://127.0.0.1:8000/`

## Usage

1. **Sign Up / Login**: Users can sign up for an account and log in using their credentials.
2. **Upload Files**: Once logged in, users can upload files via the dashboard.
3. **Manage Files**: Users can manage uploaded files (view, delete, etc.).
4. **Share Files**: Users can generate a unique, shareable download link for their files.
5. **Download Files**: Anyone with the link can download the file within the specified time limit.
6. **File Preview**: Supported file types (e.g., images, PDFs) can be previewed directly on the website.

## Testing

To run tests for the project, execute the following command:

```bash
python manage.py test
```

This will run the tests defined in the `tests.py` file and output the results to the terminal.

## Contributing

Contributions are welcome! If you'd like to contribute to the project, follow these steps:

1. Fork the repository.
2. Create a branch for your feature or bug fix.
3. Implement your changes.
4. Write tests if necessary.
5. Submit a pull request to the main repository.

Make sure to create an issue if you plan to add a feature or fix a bug. This will help in managing tasks and ensuring that everyone is on the same page.

## License

This project is licensed under the **MIT License**. See the `LICENSE` file for more details.

---
