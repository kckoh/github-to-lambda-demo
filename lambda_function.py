import json
def lambda_handler(event, context):
    print('Done x1.2')
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
    
