import json
from dataclasses import asdict
from request import SearchBanRecordRequest
from response import LambdaApiResponse, SearchBanRecordResponse
from twitter_api import TwitterAPI


def lambda_handler(event, _context):
    request = SearchBanRecordRequest(user_name=event['pathParameters']['user-name'])

    api = TwitterAPI()
    
    tweet_count, retweet_count = api.get_24h_tweet_user(request.user_name)
    body = SearchBanRecordResponse(user_name=request.user_name,
                                   exist=exist_user(api, request.user_name),
                                   search_ban=is_search_ban(api, request.user_name),
                                   tweet_count=tweet_count,
                                   retweet_count=retweet_count)

    return asdict(LambdaApiResponse(statusCode=200,
                                    headers=LambdaApiResponse._get_cors_header(event['headers']['origin']),
                                    body=json.dumps(asdict(body))))


def is_search_ban(api: TwitterAPI, user_name: str) -> bool:
    res = api.from_user_tweet(user_name)
    if res:
        return False
    
    return True


def exist_user(api: TwitterAPI, user_name: str) -> bool:
    if api.get_user(user_name):
        return True
    return False
