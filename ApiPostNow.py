import datetime
import urllib
import requests
import json
from bs4 import BeautifulSoup

now = datetime.datetime.now()
year = now.year
month = now.month
day = now.day

req = requests.get("https://api.nasa.gov/planetary/apod?api_key=XrHiFbpljJFM1OpzTfebJqXLCCrOTTWzm09iKTL3&hd=true")
con = req.content

soup = BeautifulSoup(con, "html.parser")
print(str(soup))
data = json.loads(str(soup))
try:
    cr = data['copyright']
    hd = data['hdurl']

except KeyError:
    cr = 'null'
    hd = 'null'
pass
date = data['date']
exp = data['explanation']
mt = data['media_type']
sv = data['service_version']
t = data['title']
url = data['url']

urlcode = {'date': date, 'copyright': cr, 'hdurl': hd, 'title': t, 'url': url, 'explanation': exp}
load = urllib.parse.urlencode(urlcode)

url = "https://infinite-skies.herokuapp.com/"

payload = load
headers = {
    'content-type': "application/x-www-form-urlencoded",
    'cache-control': "no-cache"
}

response = requests.request("POST", url, data=payload, headers=headers)
print(response.status_code)
