import json
from twitter_api import TwitterAPI

api = TwitterAPI()

def lambda_handler(event, context):
    user_name = event['pathParameters']['user-name']

    response = {
        'statusCode': 200,
        'headers': {
            "Access-Control-Allow-Headers" : "Content-Type",
            "Access-Control-Allow-Origin": "http://searchbanrecords.s3-website-ap-northeast-1.amazonaws.com",
            "Access-Control-Allow-Methods": "GET,OPTIONS",
            "Access-Control-Allow-Credentials": True
        },
        'body': None,
    }

    body = {
        'user_name': user_name,
        'exist': exist_user(user_name),
        'search_ban': is_search_ban(user_name),
        'tweet_count': None,
        'retweet_count': None,
    }

    tweet_count = api.get_24h_tweet_user(user_name)

    body['tweet_count'] = tweet_count[0]
    body['retweet_count'] = tweet_count[1]


    response['body'] = json.dumps(body)

    return response


def is_search_ban(user_name: str) -> bool:
    res = api.from_user_tweet(user_name)
    if res:
        return False
    
    return True


def exist_user(user_name: str) -> bool:
    if api.get_user(user_name):
        return True
    return False