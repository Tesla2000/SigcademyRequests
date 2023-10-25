import requests
from requests import Response

from settings import BASE_URL
from constants.FrontendConstants import FrontendConstants
from constants.UrlConstants import UrlConstants

url = f"{BASE_URL}/{UrlConstants.SCORE_TRAINING_MATERIAL_ENDPOINT}"


def score_training_material(
    token: str, training_material_id: str, comment: str, score: int
) -> Response:
    return requests.post(
        url,
        {
            FrontendConstants.SCORE: score,
            FrontendConstants.COMMENT: comment,
            FrontendConstants.TRAINING_MATERIAL_ID: training_material_id,
            FrontendConstants.USER_TOKEN: token,
        },
    )
