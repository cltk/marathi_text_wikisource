import urllib
import urllib.request
import re
import os
import string
import regex
from bs4 import BeautifulSoup


def get_html(url_link):
    with urllib.request.urlopen(url_link) as url:
        return url.read()


def get_adhyay_links():
    directory = "./datasets/dnyaneshwari"
    if not os.path.exists(directory):
        os.makedirs(directory)
    url = "https://mr.wikisource.org/wiki/%E0%A4%9C%E0%A5%8D%E0%A4%9E%E0%A4%BE%E0%A4%A8%E0%A5%87%E0%A4%B6%E0%A5%8D%E0%A4%B5%E0%A4%B0%E0%A5%80"
    html = get_html(url)
    soup = BeautifulSoup(html)
    h_tag = soup.find('li')
    print h_tag

if __name__ == "__main__":
    get_adhyay_links()
