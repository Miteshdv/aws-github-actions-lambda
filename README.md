# aws-github-actions-lambda

This repository contains a Lambda function that is built and deployed using GitHub Actions.


## Files

- **.github/workflows/build.yml**: GitHub Actions workflow for building and deploying the Lambda function.
- **Dockerfile**: Dockerfile for building the Lambda function image.
- **requirements.txt**: List of Python dependencies.
- **src/**: Directory containing the Lambda function source code.
  - **handler.py**: Main Lambda function handler.
- **tests/**: Directory containing unit tests.
  - **test_handler.py**: Unit tests for the Lambda function.

## Setup

1. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

2. **Run tests**:
    ```sh
    pytest tests/ --cov=src
    ```

## Deployment

The deployment is handled by GitHub Actions. On every push to the `main` branch or when a release is created, the workflow defined in [build.yml](http://_vscodecontentref_/8) will be triggered. This workflow will:

1. Set up Python.
2. Install dependencies.
3. Run tests.
4. Configure AWS credentials.
5. Build and push the Docker image to Amazon ECR.

## Lambda Function

The Lambda function is defined in [handler.py](http://_vscodecontentref_/9) with the main handler function [lambda_handler](http://_vscodecontentref_/10).

```python
def lambda_handler(event, context):
    # Function implementation