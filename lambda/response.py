from dataclasses import dataclass
from typing import Any, Dict


class Response():
    pass


@dataclass
class LambdaApiResponse(Response):
    statusCode: int
    headers: Dict[str, Any]
    body: str

    @classmethod
    def _get_cors_header(cls, stage: str):
        origin = "http://localhost:8080" if stage == 'dev' else "http://searchbanrecords.s3-website-ap-northeast-1.amazonaws.com"
        return {
            "Access-Control-Allow-Headers" : "Content-Type",
            "Access-Control-Allow-Origin": origin,
            "Access-Control-Allow-Methods": "GET,OPTIONS",
            "Access-Control-Allow-Credentials": True
        }


@dataclass
class SearchBanRecordResponse(Response):
    user_name: str
    exist: bool
    search_ban: bool
    tweet_count: int
    retweet_count: int
