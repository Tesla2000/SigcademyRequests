import requests
from requests import Response

from settings import BASE_URL
from constants.FrontendConstants import FrontendConstants
from constants.UrlConstants import UrlConstants

url = f"{BASE_URL}/{UrlConstants.GET_USER_ENDPOINT}"


def get_user(token: str, student_id: str) -> Response:
    return requests.get(
        url,
        {
            FrontendConstants.USER_TOKEN: token,
            FrontendConstants.USER: student_id,
        },
    )
