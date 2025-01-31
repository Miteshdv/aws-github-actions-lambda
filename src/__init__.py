# src/__init__.py

import logging

# Initialize a logger for the package
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

# Import the primary Lambda function handler
from .handler import lambda_handler

# Define what should be accessible when the package is imported
__all__ = ['lambda_handler']
