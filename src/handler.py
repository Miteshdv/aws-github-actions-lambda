import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event,context):
    try:
        logger.info('Event: %s', event)
        
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({
                'message': 'THIS IS FROM LAMBDA'
            })
        }
    except Exception as e:
        logger.error('Error: %s', str(e))
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({
                'error': str(e)
            })
        }