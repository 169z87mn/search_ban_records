import json
from twitter_api import TwitterAPI

api = TwitterAPI()

def lambda_handler(event, context):
    user_name = event['pathParameters']['user-name']

    response = {
        'statusCode': 200,
        'body': None,
    }

    body = {
        'user_name': user_name,
        'exist': 'true',
        'search_ban': is_search_ban(user_name),
        'tweet_count': None,
        'retweet_count': None,
    }

    tweet_count = api.get_24h_tweet_user(user_name)

    if tweet_count[0] == 0:
        body['exist'] = 'false'
        response['statusCode'] = 400
        response['body'] = json.dumps(body)
        return response

    body['tweet_count'] = tweet_count[0]
    body['retweet_count'] = tweet_count[1]
    response['body'] = json.dumps(body)

    return response


def is_search_ban(user_name: str) -> bool:
    res = api.from_user_tweet(user_name)
    if res:
        return False
    
    return True