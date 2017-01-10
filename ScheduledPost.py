import schedule
import time
import urllib
import requests
import json
from bs4 import BeautifulSoup

def job():
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


schedule.every().day.at("13:30").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
