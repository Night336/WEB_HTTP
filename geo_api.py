import requests


APIKEY = "40d1649f-0493-4b70-98ba-98533de7710b"
API_SERVER = "http://geocode-maps.yandex.ru/1.x/"


def get_toponim(toponym_to_find):
    geocoder_params = {
        "apikey": APIKEY,
        "geocode": toponym_to_find,
        "format": "json"}
    response = requests.get(API_SERVER, params=geocoder_params)
    if not response:
        # обработка ошибочной ситуации
        pass
    json_response = response.json()
    toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    return toponym


def get_pos_by_toponym(toponym):
    return toponym["Point"]["pos"]


def get_ll_by_toponym(toponym):
    toponym_coodrinates = get_pos_by_toponym(toponym)
    toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")
    ll = ",".join([toponym_longitude, toponym_lattitude])
    return ll


def get_span_by_toponym(toponym):
    evelope = toponym["boundedBy"]["Envelope"]

    l, b = evelope["lowerCorner"].split(" ")
    r, t = evelope["upperCorner"].split(" ")

    dx = abs(float(l) - float(r)) / 2.0
    dy = abs(float(t) - float(b)) / 2.0

    span = f'{dx},{dy}'
    return span
