import requests
from requests import Response

from settings import BASE_URL
from sigcad_requests.constants.FrontendConstants import FrontendConstants
from sigcad_requests.constants.UrlConstants import UrlConstants

url = f"{BASE_URL}/{UrlConstants.REMOVE_SCHOOL_RESTRICTION_ENDPOINT}"


def remove_school_restriction(token: str, school_id: str, lesson_id: str) -> Response:
    data = {
        FrontendConstants.USER_TOKEN: token,
        FrontendConstants.SCHOOL_NAME: school_id,
        FrontendConstants.LESSON_NAME: lesson_id,
    }
    return requests.post(
        url,
        data,
    )
