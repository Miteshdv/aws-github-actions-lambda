import json
from src.handler import lambda_handler

def test_lambda_handler():
    # Test event
    event = {
        'body': json.dumps({'test': 'data'})
    }
    
    # Test context
    class Context:
        function_name = "test-function"
    
    response = lambda_handler(event, Context())
    assert response['statusCode'] == 200