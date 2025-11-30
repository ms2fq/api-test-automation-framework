# api-test-automation-framework
![Tests](https://github.com/ms2fq/api-test-automation-framework/workflows/API%20Tests/badge.svg)
![Python](https://img.shields.io/badge/python-3.13+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
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

### Local Execution
```bash
# Clone repository
git clone https://github.com/ms2fq/api-test-automation-framework.git
cd api-test-automation-framework

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run all tests
python -m pytest -v

# Run specific test file
python -m pytest tests/test_users.py -v

# Run with HTML report
python -m pytest --html=reports/report.html --self-contained-html
```

### Docker Execution
```bash
# Build Docker image
docker build -t api-test-framework .

# Run tests in container
docker run api-test-framework

# Using docker-compose
docker-compose up
```

## Architecture
The framework implements a layered architecture for scalability and maintainability:

**Base Layer: APIClient**
- Provides core HTTP operations (GET, POST, PUT, PATCH, DELETE)
- Handles session management, timeouts, and error handling
- Implements request/response logging
- Shared foundation for all resource clients

**Resource Layer: Specialized Clients**
- `UsersClient` - User CRUD operations and related queries
- `PostsClient` - Post management and comment retrieval
- `TodosClient` - Todo operations with completion tracking

Each resource client:
- Inherits from base `APIClient`
- Encapsulates all operations for one API resource
- Provides clean, semantic method names

## Test Coverage
**Functional Tests**
- CRUD operations for all resources (Create, Read, Update, Delete)
- Positive test cases with valid data
- Negative test cases with invalid inputs
- Boundary value testing

**Edge Cases**
- Invalid IDs (zero, negative, non-existent)
- Empty strings and missing fields
- Malformed data

**Integration Tests**
- Resource relationships (user posts, post comments, user todos)
- Multi-step workflows

## Docker Integration
- Based on Python 3.13 slim image
- Optimized layer caching
- Minimal image size
- Self-contained execution environment

## CI/CD Integration
GitHub Actions workflow automatically:
- Builds Docker container on every push
- Runs complete test suite
- Generates test reports
- Validates code quality

See `.github/workflows/test.yml` for configuration.

## Skills Demonstrated

This project showcases capabilities relevant to:
- **SDET Roles**: Framework design, API testing, automation
- **DevOps Roles**: Containerization, CI/CD, infrastructure as code
- **QA Engineering**: Test strategy, coverage, quality assurance
- **Platform Engineering**: Tool building, developer productivity

## Contact

**Michael Santucci**
- LinkedIn: [santuccim](https://www.linkedin.com/in/santuccim/)

---

**Note**: This is a portfolio project built to demonstrate test automation and infrastructure skills. The architecture and patterns mirror production frameworks I've developed professionally, adapted for a public API to enable code sharing while respecting proprietary work restrictions.
