# The purpose of this code is to automatically grab the weather status in Calgary, AB Canada
# https://weather.gc.ca/

import bs4, requests

def getCalgaryWeather(weatherURL):
    res = requests.get(weatherURL)
    res.raise_for_status()
    
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#wb-auto-4 > div.col-sm-10.text-center > div > div:nth-child(2) > dl > dd:nth-child(2)')
    return elems[0].text.strip()

weather = getCalgaryWeather('https://weather.gc.ca/city/pages/ab-52_metric_e.html')
print('The weather today is ' + weather)

