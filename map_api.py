from io import BytesIO

import requests
from PIL import Image

API_SERVER = "http://static-maps.yandex.ru/1.x/"


def get_map_image(ll, span):
    map_params = {
        "ll": ll,
        "spn": span,
        "l": "map",
        "pt": ll
    }

    response = requests.get(API_SERVER, params=map_params)

    return Image.open(BytesIO(response.content))
