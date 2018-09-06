import requests
import warnings

def create(text):
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    params = {
        'Q': text,
        'E': 0,
        'S': 'none',
        'R': 0
    }

    url = 'https://qbin.io/'

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        response = requests.post(url, data=params, headers=headers, verify=False)

    if response.status_code == requests.codes.ok:
        # Everything went fine, print paste URL and Session cookie
        return response.url
