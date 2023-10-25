import requests
from requests import Response

from settings import BASE_URL
from constants.FrontendConstants import FrontendConstants
from constants.UrlConstants import UrlConstants

url = f"{BASE_URL}/{UrlConstants.CREATE_SCHOOL_RESTRICTION_ENDPOINT}"


def create_school_restriction(token: str, school_id: str, lesson_name: str) -> Response:
    data = {
        FrontendConstants.USER_TOKEN: token,
        FrontendConstants.SCHOOL_NAME: school_id,
        FrontendConstants.LESSON_NAME: lesson_name,
    }
    return requests.post(
        url,
        data,
    )
