from abc import ABCMeta
from dataclasses import dataclass


class Reqeust(ABCMeta):
    pass


@dataclass
class SearchBanRecordRequest(Reqeust):
    user_name: str
