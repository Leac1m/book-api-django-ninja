# Book API Project using Django Ninja

This project is a RESTful API built with Django Ninja, designed to manage a collection of books and their reviews. It serves as a learning project for understanding the Django Ninja framework and its capabilities.

## Features

- **Book Management**: Create, read, update, and delete books.
- **Review System**: Users can add reviews to books.
- **Authentication**: JWT-based authentication for secure access.
- **Pagination**: Efficiently handle large datasets with pagination.

## Getting Started

Follow these instructions to set up and run the project on your local machine.

### Prerequisites

- Python 3.x
- Git

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Leac1m/book-api-django-ninja.git
   cd book-api-django-ninja
   ```

2. **Create a virtual environment**:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database**:
   ```bash
   python3 manage.py makemigrations
   python3 manage.py migrate
   ```

5. **Run the server**:
   ```bash
   python3 manage.py runserver
   ```

### Usage

- Access the API at `http://localhost:8000/api/`.
- Use an API client like Postman to interact with the endpoints.

### Project Structure

- **accounts**: Handles user authentication and management.
- **books**: Manages book-related operations.
- **reviews**: Manages review-related operations.

### Configuration

- **Database**: Configured to use SQLite by default. You can change this in `django_project/settings.py` (lines 83-88).
- **Authentication**: JWT authentication is set up in `books/auth.py` (lines 1-10).

### Testing

Run the tests using:
```bash
python3 manage.py test
```

### Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

### License

This project is licensed under the MIT License.

### Contact

For any questions or issues, please open an issue on the GitHub repository.
