import json
import requests

def grab_variant(link):
    link = link + ".json"
    response = json.loads(requests.get(link).text)
    vars_length = (len(response['product']['variants']))

    return response