from datetime import datetime

import requests
from requests import Response

from settings import BASE_URL
from sigcad_requests.constants.FrontendConstants import FrontendConstants
from sigcad_requests.constants.UrlConstants import UrlConstants

url = f"{BASE_URL}/{UrlConstants.GET_LESSON_RESULTS_ENDPOINT}"


def get_lesson_progress(
    token: str,
    class_ids: list[str],
    student_ids: list[str],
    lesson_ids: list[str],
    start_date: datetime,
    end_date: datetime,
) -> Response:
    return requests.get(
        url,
        {
            FrontendConstants.USER_TOKEN: token,
            FrontendConstants.CLASSES: class_ids,
            FrontendConstants.STUDENTS: student_ids,
            FrontendConstants.LESSONS: lesson_ids,
            FrontendConstants.START_DATE: start_date.strftime("%d-%m-%y"),
            FrontendConstants.END_DATE: end_date.strftime("%d-%m-%y"),
            FrontendConstants.DT_FORMAT: "%d-%m-%y",
        },
    )
