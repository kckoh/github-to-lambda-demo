import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import lambda_function
import json

# def test_lambda_handler_success():
#         event = {}
#         context = {}
#         expected_response = {"statusCode": 200, "body": '["repo1","repo2"]'}
#         response = lambda_function.lambda_handler(event, context)
#         unittest.TestCase.assertEqual(response, expected_response)

def test_lambda_handler_success():
    event = {}
    context = {}
    expected_response =  {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
    response = lambda_function.lambda_handler(event, context)
    assert response == expected_response
    