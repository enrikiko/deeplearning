import requests
import json
import time

def save(info):
    file=str(time.time())
    file='tmp/'+file
    with open(file, "a") as f:
        f.write(info+"\n")

def sendHttp(arg):
    url='http://88.8.71.112:3367/send'
    headers = {'content-type': 'application/json'}
    return requests.post(url, data=json.dumps(arg), headers=headers)
