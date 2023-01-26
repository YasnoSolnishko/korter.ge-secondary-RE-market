# import libraries
import pandas as pd
from bs4 import BeautifulSoup
import requests
import re
import json
import math
from pathlib import Path
from datetime import datetime


def parse_page_to_dict(link):
    """
    The function parses webpage with ads and returns the dictionary with the data
    for each webpage
    """

    # Request to website and download HTML contents
    webpage = requests.get(link)

    soup = BeautifulSoup(webpage.content, "html.parser")
    body_text = str(soup.body()[0])

    # search for the position where the dictionary begins and ends
    # span gives the initial and final position of the searched string, gives as a list, positions of the initial and final element
    # span()[0] - access the position of the initial element
    # span()[1] - access the position of the final element

    start_symbol = re.search(r'window.INITIAL_STATE = ', body_text).span()[1]
    end_symbol = re.search(r'window.lang', body_text).span()[0] - 12

    # обрезка, чтобы получить в body_text текст только словаря
    body_text = body_text[start_symbol:end_symbol]

    # преобразуем результат в json
    res = json.loads(body_text)

    # extracting only the necessary information from json and adding it to the dictionary

    return res['apartmentListingStore']['apartments']


date_now = str(datetime.now().isoformat(timespec='seconds'))
date_now = date_now.replace(':', '_')
print('parsing started on {}'.format(date_now))

# requesting the webpage for defining the number of pages for parsing

# Request to website and download HTML contents
# https://korter.ge/en/apartments-for-sale-in-tbilisi#9.71/41.7227/44.8103/0/60
url = 'https://korter.ge/en/apartments-for-sale-in-tbilisi#9.71/41.7227/44.8103/0/60'
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")
body_text = str(soup.body()[0])

# define a page number for parsing

# search for the position where the dictionary begins and ends
# span gives the initial and final position of the searched string, gives as a list, positions of the initial and final element
# span()[0] - access the position of the initial element
# span()[1] - access the position of the final element

start_symbol = re.search(r'window.INITIAL_STATE = ', body_text).span()[1]
end_symbol = re.search(r'window.lang', body_text).span()[0] - 12

# cropping to get only the dictionary text in body_text
body_text = body_text[start_symbol:end_symbol]

# converting result to json
res = json.loads(body_text)

# get the number of ads in category apartments-for-sale-in-tbilisi

apartments_count = res['navigationStore']['geoObjects'][0]['links']['apartments']['count']

# getting number of pages that need to be scanned, the site by default shows 20 ads per page

if apartments_count % 20 == 0:
    page_count = int(apartments_count / 20)
else:
    page_count = int(math.floor(apartments_count / 20) + 1)

# creating the initial dictionary

data = res['apartmentListingStore']['apartments']

# traversing through pages and further populating the database

for i in range(2, page_count + 1):
    # make a link with a page number
    url = 'https://korter.ge/en/apartments-for-sale-in-tbilisi?page={}#9.71/41.7227/44.8103/0/60'.format(i)
    df = parse_page_to_dict(url)
    for item in df:
        data.append(item)

# converting dictionary to DataFrame
# adding link and price per square meter
data = pd.DataFrame(data)
data['link'] = data.link.apply(lambda x: 'https://korter.ge' + str(x))
data['price_m_sq'] = data.price / data.area

date_now = str(datetime.now().isoformat(timespec='seconds'))
date_now = date_now.replace(':', '_')

# creating a filename
filename = '/home/ubuntu/Documents/korter_data/' + date_now + '.csv'  # linux

filepath = Path(filename)
data.to_csv(filepath)

print('parsing completed on {}'.format(date_now))
