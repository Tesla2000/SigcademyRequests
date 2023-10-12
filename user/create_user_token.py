import requests
from requests import Response

from settings import BASE_URL
from sigcad_requests.constants.FrontendConstants import FrontendConstants
from sigcad_requests.constants.UrlConstants import UrlConstants

url = f"{BASE_URL}/{UrlConstants.TOKEN_CREATION_ENDPOINT}"


def create_user_token(email: str, password: str) -> Response:
    return requests.post(
        url,
        {
            FrontendConstants.EMAIL: email,
            FrontendConstants.PASSWORD: password,
        },
    )
