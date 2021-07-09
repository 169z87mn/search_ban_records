from dataclasses import dataclass


class Reqeust():
    pass


@dataclass
class SearchBanRecordRequest(Reqeust):
    user_name: str
