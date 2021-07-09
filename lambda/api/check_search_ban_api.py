from _typeshed import Self
from lambda.request import SearchBanRecordRequest
from lambda.response import LambdaApiResponse, SearchBanRecordResponse
from twitter_api import TwitterAPI


def lambda_handler(event, _context):
    request = SearchBanRecordRequest(event['pathParameters']['user-name'])

    api = TwitterAPI()
    
    tweet_count, retweet_count = api.get_24h_tweet_user(request.user_name)
    body = SearchBanRecordResponse(request.user_name,
                                   exist_user(api, request.user_name),
                                   is_search_ban(api, request.user_name),
                                   tweet_count, retweet_count)

    return LambdaApiResponse(statusCode=200, headers=Self._get_cors_header(),
                             body=body)


def is_search_ban(api: TwitterAPI, user_name: str) -> bool:
    res = api.from_user_tweet(user_name)
    if res:
        return False
    
    return True


def exist_user(api: TwitterAPI, user_name: str) -> bool:
    if api.get_user(user_name):
        return True
    return False
