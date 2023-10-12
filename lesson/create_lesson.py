from pathlib import Path

import requests
from requests import Response

from settings import BASE_URL
from sigcad_requests.constants.FrontendConstants import FrontendConstants
from sigcad_requests.constants.UrlConstants import UrlConstants

url = f"{BASE_URL}/{UrlConstants.CREATE_LESSON_ENDPOINT}"


def create_lesson(token: str, lesson_name: str, description: str, video_url: str, questions: list[str] = None, answers: list[str] = None, generator_path: Path = None, html_path: Path = None) -> Response:
    if not (questions and answers) and not generator_path:
        raise ValueError("Either question-answer pairs or generator must be provided")
    html = html_path.open() if html_path else None
    generator = generator_path.open() if generator_path else None
    data = {
        FrontendConstants.USER_TOKEN: token,
        FrontendConstants.LESSON_NAME: lesson_name,
        FrontendConstants.DESCRIPTION: description,
        FrontendConstants.VIDEO: video_url,
    }
    if questions and answers:
        data[FrontendConstants.QUESTIONS] = questions
        data[FrontendConstants.ANSWERS] = answers
    files = {}
    if html or generator:
        files = {
            FrontendConstants.GENERATOR: (
                generator_path.name,
                generator,
            ) if generator_path else None,
            FrontendConstants.HTML: (
                html_path.name,
                html,
            ) if html_path else None,
        }
    response = requests.post(
        url,
        data,
        files=files
    )
    if html:
        html.close()
    if generator:
        generator.close()
    return response

