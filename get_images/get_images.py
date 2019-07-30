import os
import urllib.request as ulib
from bs4 import BeautifulSoup as Soup
import json
import requests as req
import re


url_a = 'https://www.google.com/search?ei=1m7NWePfFYaGmQG51q7IBg&hl=en&q={}'
url_b = '\&tbm=isch&ved=0ahUKEwjjovnD7sjWAhUGQyYKHTmrC2kQuT0I7gEoAQ&start={}'
url_c = '\&yv=2&vet=10ahUKEwjjovnD7sjWAhUGQyYKHTmrC2kQuT0I7gEoAQ.1m7NWePfFYaGmQG51q7IBg'
url_d = '\.i&ijn=1'
url_base = ''.join((url_a, url_b, url_c))

headers = {'User-Agent': 'Chrome/ 75.0.3770.142 Safari/537.36'}


def get_links(search_name):
    search_name = search_name.replace(' ', '+')
    url = url_base.format(search_name, 0)
    response = req.get(url)
    soup = Soup(response.text, 'html.parser')
    images = soup.find_all('img')
    links = [image['src'] for image in images]
    return links


def save_images(links, search_name):
    directory = os.path.join('images',search_name.replace(' ', '_'))
    if not os.path.isdir(directory):
        os.mkdir(directory)

    cpt = 0
    for i, link in enumerate(links):
        cpt += 1
        savepath = os.path.join(directory, '{:06}.png'.format(cpt))
        ulib.urlretrieve(link, savepath)


if __name__ == '__main__':
    search_name = 'fidget kid spinner toys'
    links = get_links(search_name)
    save_images(links, search_name)