import requests
from requests import Response

from settings import BASE_URL
from constants.FrontendConstants import FrontendConstants
from constants.UrlConstants import UrlConstants

url = f"{BASE_URL}/{UrlConstants.GET_LESSON_ENDPOINT}"


def get_lesson(token: str, lesson_id: str) -> Response:
    return requests.get(
        url,
        {
            FrontendConstants.USER_TOKEN: token,
            FrontendConstants.LESSON_NAME: lesson_id,
        },
    )
