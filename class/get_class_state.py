import requests
from requests import Response

from settings import BASE_URL
from sigcad_requests.constants.UrlConstants import UrlConstants

url = f"{BASE_URL}/{UrlConstants.GET_CLASS_STATE_ENDPOINT}"


def get_class(token: str, class_id: str) -> Response:
    return requests.get(url, {
        "token": token,
        "class_id": class_id,
    })
