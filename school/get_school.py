import requests
from requests import Response

from settings import BASE_URL
from sigcad_requests.constants.UrlConstants import UrlConstants

url = f"{BASE_URL}/{UrlConstants.GET_SCHOOL_ENDPOINT}"


def get_school(token: str, school_name: str) -> Response:
    return requests.get(url, {"token": token, "school_name": school_name})
