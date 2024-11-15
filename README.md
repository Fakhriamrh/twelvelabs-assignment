# Twelve Labs Assignment

This project contains a suite of automated tests for API endpoints related to index management. The tests cover the following operations:

- **Create Index**
- **List Indexes**
- **Get Index by ID**
- **Delete Index**

The tests use **pytest** for execution, **Allure** for enhanced reporting, and **requests** to make API calls to the endpoints.

## Assumptions
- Authentication is required for all API requests, and an API key will be provided in the configuration.
- The API responses will be in JSON format.
- The API's behavior is consistent with the following:
    - **Create Index**: Returns a success message with a unique _id for the created index.
    - **List Indexes**: Returns a list of all existing indexes
    - **Get Index by ID**: Returns details of a specific index when provided with a valid _id.
    - **Delete Index**: Deletes an index and returns a confirmation of deletion.

## Features
- Integration with **Allure** for test reporting
- Use of **pytest** for test execution

## Requirements

To run the tests, you'll need the following dependencies:

- Python 3.x
- pytest
- allure-pytest
- requests

To install the dependencies, you can use `pip`:

```bash
pip install -r requirements.txt
```

## Requirements File (requirements.txt):
```bash
pytest==7.4.0
allure-pytest==2.10.0
requests==2.28.0
```

## Project Structure
The project is organized as follows:

```bash 
.
├── tests
│   ├── indexes
│   │   ├── test_create_index.py      # Test for creating an index
│   │   ├── test_list_index.py        # Test for listing indexes
│   │   ├── test_get_index_by_id.py   # Test for getting an index by ID
│   │   ├── test_delete_index.py      # Test for deleting an index
├── utils
│   ├── api_client.py                 # Utility for making API calls
├── tests_data
│   ├── tests_data.py                 # Contains sample data used in tests
├── config.py                         # Configuration for the project
├── conftest.py                       # Pytest configuration and fixtures
├── requirements.txt                  # Python dependencies
└── README.md                         # Project documentation
```

## Setup
### Clone the repository:

```bash
git clone https://github.com/Fakhriamrh/twelvelabs-assignment.git
cd twelvelabs-assignment
```

### Install the required dependencies:
```bash
pip install -r requirements.txt
```

### Configure the API URL and authentication in the config.py file:

Before running the tests, configure the API URL and authentication details in the **config.py** file:
1. Set the base URL of the API.
2. Provide the API key for authentication.

Example of **config.py** :
```bash
BASE_URL = "https://api.example.com/"
API_KEY = "your-api-key"
```

## Running Tests
### Run All Tests  :
```bash
pytest
```

### Run Tests with Allure Reporting:
To generate Allure results:
```bash
pytest --alluredir=allure-results
```
This will execute the tests and store the Allure results in the **allure-resulsts** directory

### Run a Specific Test File:
```bash
pytest tests/index/create_index.test.py
```

## Generating Allure Reports :
Once the tests have been executed and results are stored in the **allure-results** directory, you can generate an interactive Allure report:
1. Install Allure if not already installed:

MacOS (using Homebrew):
```bash
brew install allure
```
2. Serve the Allure report:

After executing the tests and generating results, you can view the Allure report:
```bash
allure serve allure-results
```
This will open a browser displaying the detailed report with the test execution results.

--------------------

