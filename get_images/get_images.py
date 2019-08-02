import os
import urllib.request as ulib
from bs4 import BeautifulSoup as Soup
import json
import requests as req
import re
from google_images_download import google_images_download



url_a = 'https://www.google.com/search?ei=1m7NWePfFYaGmQG51q7IBg&hl=en&q={}'
url_b = '\&tbm=isch&ved=0ahUKEwjjovnD7sjWAhUGQyYKHTmrC2kQuT0I7gEoAQ&start={}'
url_c = '\&yv=2&vet=10ahUKEwjjovnD7sjWAhUGQyYKHTmrC2kQuT0I7gEoAQ.1m7NWePfFYaGmQG51q7IBg'
url_d = '\.i&ijn=1'
url_base = ''.join((url_a, url_b, url_c))

headers = {'User-Agent': 'Chrome/ 75.0.3770.142 Safari/537.36'}


def get_links(search_name):
    response = google_images_download.googleimagesdownload()  # class instantiation
    arguments = {"keywords": search_name, "limit": 2, "print_urls": True}
    paths = response.download(arguments)
    for i, fullpath in enumerate(paths[0][search_name]):
        dir_name = os.path.dirname(fullpath)
        os.rename(fullpath, os.path.join(dir_name,'{:06}.png'.format(i)))

    return paths


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
    #save_images(links, search_name)