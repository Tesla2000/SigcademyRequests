from datetime import datetime

import requests
from requests import Response

from settings import BASE_URL
from constants.FrontendConstants import FrontendConstants
from constants.UrlConstants import UrlConstants

url = f"{BASE_URL}/{UrlConstants.REMOVE_SCHOOL_RESTRICTION_TERM_ENDPOINT}"


def remove_school_term_restriction(
    token: str,
    school_id: str,
    lesson_id: str,
    dt: datetime,
    duration: int,
    weekly_repetition: bool,
) -> Response:
    date = dt.date().strftime("%d-%m-%y")
    time = dt.time().strftime("%H:%M")
    data = {
        FrontendConstants.USER_TOKEN: token,
        FrontendConstants.SCHOOL_NAME: school_id,
        FrontendConstants.LESSON_NAME: lesson_id,
        FrontendConstants.DATE: date,
        FrontendConstants.TIME: time,
        FrontendConstants.DURATION: duration,
        FrontendConstants.WEEKLY_REPETITION: weekly_repetition,
    }
    return requests.post(
        url,
        data,
    )
