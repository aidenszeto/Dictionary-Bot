import urllib.request, urllib.parse, urllib.error
import json

# Resets calls to 0 if worldclockapi indicates new day
def check(current, calls):
    # Connect with worldclockapi
    url = 'http://worldclockapi.com/api/json/est/now'
    doc = urllib.request.urlopen(url)
    data = doc.read().decode()
    # Create JSON object with api data
    try:
        js = json.loads(data)
    except:
        js = None
    # Reset calls to 0 if dayOfTheWeek does not match previous dayOfTheWeek
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
