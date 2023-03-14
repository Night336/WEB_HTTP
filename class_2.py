import sys

from geo_api import get_toponim, get_ll_by_toponym, get_span_by_toponym
from map_api import get_map_image

# python class_2.py Москва, ул. Ак. Королева, 12
toponym_to_find = " ".join(sys.argv[1:])
toponym = get_toponim(toponym_to_find)
ll = get_ll_by_toponym(toponym)
span = get_span_by_toponym(toponym)

image = get_map_image(ll=ll, spn=span, pt=ll)
image.show()
