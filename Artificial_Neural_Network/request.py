import requests
import json
def sendHttp(arg):
    url='http://88.8.71.112:3367/send'
    headers = {'content-type': 'application/json'}
    return requests.post(url, data=json.dumps(arg), headers=headers)
