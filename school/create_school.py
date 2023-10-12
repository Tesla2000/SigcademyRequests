import requests
from requests import Response

from settings import BASE_URL
from sigcad_requests.constants.UrlConstants import UrlConstants

url = f"{BASE_URL}/{UrlConstants.CREATE_SCHOOL_ENDPOINT}"


def create_school(token: str, school_name: str) -> Response:
    return requests.post(url, {"token": token, "school_name": school_name})
