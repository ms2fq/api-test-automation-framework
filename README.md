# api-test-automation-framework
Repository containing a production-grade API testing framework using Python, PyTest, and Docker for automated validation of RESTful services, with CI/CD integration using GitHub Actions.

## Project Overview
This framework showcases professional API testing approaches:
- **Clean Architecture**: Base client and resource specific clients created for maintainability
- **Comprehensive Test Coverage**: Validate CRUD operations with positive and negative scenarios (e.g., edge cases and error scenarios)
- **Containerization**: Docker support for consistent execution environments
- **CI/CD Ready**: GitHub Actions integration for automated testing

Built as a portfolio project demonstrating skills directly applicable to SDET, DevOps, and test infrastructure roles.

## Technologies Used
- **Python 3.13**: Language
- **PyTest**: Testing framework
- **Requests**: HTTP library for API interactions
- **Docker**: Used for containerization
- **GitHub Actions**: CI/CD automation
- **JSONPlaceholder API**: Free REST API for testing

## Project Structure
```
api-test-automation-framework/
├── config/
│   ├── __init__.py
│   └── config.py              # Configuration management
├── tests/
│   ├── __init__.py
│   ├── conftest.py            # PyTest configuration
│   ├── test_users.py          # User API tests
│   ├── test_posts.py          # Post API tests
│   └── test_todos.py          # Todo API tests
├── utils/
│   ├── __init__.py
│   ├── api_client.py          # Base HTTP client
│   ├── users_client.py        # Users resource client
│   ├── posts_client.py        # Posts resource client
│   └── todos_client.py        # Todos resource client
├── Dockerfile                  # Container definition
├── docker-compose.yml          # Multi-container orchestration
├── requirements.txt            # Python dependencies
├── pytest.ini                  # PyTest configuration
└── README.md
```
