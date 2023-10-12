from requests import Response

import requests

from settings import BASE_URL
from sigcad_requests.constants.UrlConstants import UrlConstants

url = f"{BASE_URL}/{UrlConstants.DELETE_CLASS_API}"


def create_class(token: str, class_name: str) -> Response:
    return requests.post(url, {
        "token": token,
        "class_name": class_name,
    })
