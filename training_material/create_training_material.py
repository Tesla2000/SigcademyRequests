from itertools import zip_longest
from pathlib import Path
from typing import Optional

import requests
from requests import Response

from settings import BASE_URL
from sigcad_requests.constants.FrontendConstants import FrontendConstants
from sigcad_requests.constants.UrlConstants import UrlConstants

url = f"{BASE_URL}/{UrlConstants.CREATE_TRAINING_MATERIAL_ENDPOINT}"


def create_training_material(token: str, lesson_id: str, training_material_name: str, feedback_urls: list[Optional[str]], step_times: list[int], question_sets: list[list[str]] = None, answer_sets: list[list[str]] = None, generator_paths: list[Path] = None, html_paths: list[Path] = None) -> Response:
    data = {
        FrontendConstants.LESSON_NAME: lesson_id,
        FrontendConstants.TRAINING_MATERIAL_NAME: training_material_name,
        FrontendConstants.EXPECTED_STEP_TIMES: step_times,
        FrontendConstants.VIDEOS: feedback_urls,
        FrontendConstants.USER_TOKEN: token,
    }
    for part, (questions, answers, generator_path) in enumerate(zip_longest(question_sets, answer_sets, generator_paths)):
        if not (questions and answers) and not generator_path:
            raise ValueError("Either question-answer pairs or generator must be provided")
        data[f"{FrontendConstants.QUESTIONS}_{part}"] = questions
        data[f"{FrontendConstants.ANSWERS}_{part}"] = answers
    files = dict((FrontendConstants.HTML_FILE.format(index), (html_path.name, html_path.open())) for index, html_path in enumerate(
        html_paths) if html_path)
    files = {**files, **dict((FrontendConstants.PY_FILE.format(index), (generator_path.name, generator_path.open())) for index, generator_path in enumerate(
        generator_paths) if generator_path)}
    response = requests.post(
        url,
        data,
        files=files,
    )
    tuple(file[1].close() for file in files)
    return response
