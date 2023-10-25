import requests
from requests import Response

from settings import BASE_URL
from constants.FrontendConstants import FrontendConstants
from constants.UrlConstants import UrlConstants

url = f"{BASE_URL}/{UrlConstants.DOWNGRADE_USER_ENDPOINT}"


def downgrade_user(token: str, email: str) -> Response:
    return requests.post(
        url,
        {
            FrontendConstants.EMAIL: email,
            FrontendConstants.USER_TOKEN: token,
        },
    )
