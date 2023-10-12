import requests
from requests import Response

from settings import BASE_URL
from sigcad_requests.constants.FrontendConstants import FrontendConstants
from sigcad_requests.constants.UrlConstants import UrlConstants

url = f"{BASE_URL}/{UrlConstants.GET_TRAINING_MATERIAL_ENDPOINT}"


def get_training_material(token: str, training_material_id: str) -> Response:
    return requests.get(
        url,
        {
            FrontendConstants.USER_TOKEN: token,
            FrontendConstants.TRAINING_MATERIAL_ID: training_material_id,
        },
    )
