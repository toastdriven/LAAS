import json
import pylev
from itty import get, Response, run_itty


__author__ = 'Daniel Lindsley'
__version__ = (1, 0, 0)
__license__ = 'New BSD'


@get('/')
def lev(request):
    original_word = request.GET.get('original_word', '')
    new_word = request.GET.get('new_word', '')

    if len(original_word) == 0 or len(new_word) == 0:
        data = {
            'status': 'error',
            'message': "You must supply both 'original_word' & 'new_word' as GET params.",
            'description': """It's Levenshtein-As-A-Service. You know, for the lulz.

            Please direct all VC monies to Daniel Lindsley.""",
            'version': '1.0.0',
        }
    else:
        data = {
            'status': 'success',
            'distance': pylev.levenschtein(original_word, new_word),
            'version': '1.0.0',
        }

    return Response(json.dumps(data), content_type='application/json')


run_itty()
