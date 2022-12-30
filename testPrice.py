# The purpose of this code is to automatically grab the weather status in Calgary, AB Canada
# https://weather.gc.ca/

import bs4, requests

def getCalgaryWeather(weatherURL):
    res = requests.get(weatherURL)
    res.raise_for_status()
    
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#ProductPrice-171446861852 > span')
    return elems[0].text.strip()

weather = getCalgaryWeather('https://eightouncecoffee.ca/collections/electric-grinders/products/baratza-encore-coffee-grinder')
print('The weather today is ' + weather)

