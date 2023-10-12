import requests
from requests import Response

from settings import BASE_URL
from sigcad_requests.constants.FrontendConstants import FrontendConstants
from sigcad_requests.constants.UrlConstants import UrlConstants

url = f"{BASE_URL}/{UrlConstants.CREATE_CLASS_RESTRICTION_ENDPOINT}"


def create_class_restriction(token: str, class_id: str, lesson_name: str) -> Response:
    data = {
        FrontendConstants.USER_TOKEN: token,
        FrontendConstants.CLASS_NAME: class_id,
        FrontendConstants.LESSON_NAME: lesson_name,
    }
    return requests.post(
        url,
        data,
    )
