import requests
import warnings


def execute(text):

    _HEADER = {'content-type': 'application/x-www-form-urlencoded'}
    _URL = 'https://qbin.io/'

    params = {
        'Q': text,
        'E': 0,
        'S': 'none',
        'R': 0
    }

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        response = requests.post(_URL, data=params, headers=_HEADER, verify=False)

    if response.status_code == requests.codes.ok:
        return response.url

