import requests
from requests import Response

from settings import BASE_URL
from constants.UrlConstants import UrlConstants

url = f"{BASE_URL}/{UrlConstants.CREATE_CLASS_ENDPOINT}"


def create_class(token: str, class_name: str, school_name: str) -> Response:
    return requests.post(
        url, {"token": token, "class_name": class_name, "school_name": school_name}
    )
