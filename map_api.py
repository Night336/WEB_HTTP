from io import BytesIO

import requests
from PIL import Image

API_SERVER = "http://static-maps.yandex.ru/1.x/"


def get_map_image(*args, **kwargs):
    params = {
        "l": "map"}
    for key in kwargs:
        params[key] = kwargs[key]

    response = requests.get(API_SERVER, params=params)

    return Image.open(BytesIO(response.content))
