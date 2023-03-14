import requests

from geo_api import get_toponim, get_ll_by_toponym, get_span_by_toponym
from map_api import get_map_image
import geopy.distance


# python search.py Москва, ул. Ак. Королева, 12
toponym_to_find = input()
toponym = get_toponim(toponym_to_find)

address_ll = get_ll_by_toponym(toponym)
gsb = get_span_by_toponym(toponym)

search_api_server = "https://search-maps.yandex.ru/v1/"
api_key = "dda3ddba-c9ea-4ead-9010-f43fbc15c6e3"

search_params = {
    "apikey": api_key,
    "text": "аптека",
    "lang": "ru_RU",
    "ll": address_ll,
    "type": "biz"
}

response = requests.get(search_api_server, params=search_params)
if not response:
    # ...
    pass
# Преобразуем ответ в json-объект
json_response = response.json()
points = []
print(response.url)
for organization in json_response["features"][:10]:
    org_address = organization["properties"]["CompanyMetaData"]["address"]
    time_work = organization["properties"]["CompanyMetaData"]["Hours"]["text"]
    if "круглосуточно" in time_work.lower():
        a = "pmgns"
    elif len(time_work) > 5:
        a = "pmdbs"
    else:
        a = "pmgrs"
    # Получаем координаты ответа.
    point = organization["geometry"]["coordinates"]
    org_point = "{0},{1},{2}".format(point[0], point[1], a)
    points.append(org_point)
img = get_map_image(pt="~".join(points))
img.show()
