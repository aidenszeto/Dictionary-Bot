import urllib.request, urllib.parse, urllib.error
import json

def check(current, calls):
    url = 'http://worldclockapi.com/api/json/est/now'
    doc = urllib.request.urlopen(url)
    data = doc.read().decode()
    try:
        js = json.loads(data)
    except:
        js = None
    if js['dayOfTheWeek'] != current:
        calls = 0

def current():
    url = 'http://worldclockapi.com/api/json/est/now'
    doc = urllib.request.urlopen(url)
    data = doc.read().decode()
    try:
        js = json.loads(data)
    except:
        js = None
    return js['dayOfTheWeek']
