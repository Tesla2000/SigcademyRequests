import requests
from requests import Response

from settings import BASE_URL
from constants.UrlConstants import UrlConstants

url = f"{BASE_URL}/{UrlConstants.CREATE_STUDENT_TOKEN_ENDPOINT}"


def create_student_invitation(token: str, class_name: str) -> Response:
    return requests.post(
        url,
        {
            "token": token,
            "class_name": class_name,
        },
    )
