# STQM-Assessment3

Assessment 3 for Software Testing and Quality Management course - Automated browser testing implementation for online retail platform.

This repository contains automated Selenium tests for the e-commerce website: https://ecommerce-playground.lambdatest.io/

## Prerequisites
- Python 3.12.8 or higher
- Chrome browser (latest version)
- Git

## Quick Start

### 1. Clone the Repository
```bash
git clone <repository-url>
cd STQM-Assessment3
```

### 2. Create Virtual Environment
```bash
python -m venv venv
```

### 3. Activate Virtual Environment
- **macOS/Linux:**
  ```bash
  source venv/bin/activate
  ```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Run Tests
```bash
# Run all tests
pytest tests/ -v

# Run specific test
pytest tests/test_user_login.py -v

# Run with HTML report
pytest tests/ --html=test_results/report.html --self-contained-html
```

## Test Cases

This repository includes three comprehensive test cases:

1. **Test Case T001**: User Registration/Login Functionality
2. **Test Case T002**: Product Search and Filter Functionality
3. **Test Case T003**: Shopping Cart Functionality

Each test case includes:
- Detailed test steps
- Source code

## Project Structure
```
STQM-Assessment3/
├── tests/                  # Test files
│    ├── test_user_login.py
│    ├── test_product_search.py
│    └── test_shopping_cart.py
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## Notes
- Tests use Chrome browser by default
- WebDriver is managed automatically via webdriver-manager
