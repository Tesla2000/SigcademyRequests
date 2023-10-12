import requests
from requests import Response

from settings import BASE_URL
from sigcad_requests.constants.FrontendConstants import FrontendConstants
from sigcad_requests.constants.UrlConstants import UrlConstants

url = f"{BASE_URL}/{UrlConstants.DELETE_LESSON_API}"


def delete_lesson(token: str, lesson_id: str) -> Response:
    return requests.post(
        url,
        {
            FrontendConstants.USER_TOKEN: token,
            FrontendConstants.LESSON_NAME: lesson_id,
        },
    )
