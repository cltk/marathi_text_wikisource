import os
import urllib.request

from bs4 import BeautifulSoup


def get_html(url_link):
    url = urllib.request.urlopen(url_link)
    return url.read()


def write_dashak(lis, directory):
    base_name = "dashak"
    no = 1
    for li in lis:
        if not os.path.isfile(directory + "/" + base_name + str(no)):
            f = open(directory + "/" + base_name + str(no) + ".txt", 'wb+')
        no = no + 1
        html = get_html("https://mr.wikisource.org" + li.a['href'])
        soup = BeautifulSoup(html)
        ps = soup.find_all('p')
        for p in ps:
            lines = p.text
            lines = lines.replace('<poem>', ' ')
            lines = lines.replace('<br>', ' ')
            f.write(lines.encode('utf-8') + "\n".encode('utf-8'))


def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def get_adhyay_links():
    directory = "./datasets/dasbodh"
    if not os.path.exists(directory):
        os.makedirs(directory)
    url = "https://mr.wikisource.org/wiki/%E0%A4%A6%E0%A4%BE%E0%A4%B8%E0%A4%AC%E0%A5%8B%E0%A4%A7"
    html = get_html(url)
    soup = BeautifulSoup(html, "lxml")
    ol = soup.find('ol')
    lis = ol.find_all('li')
    create_directory(directory)
    write_dashak(lis, directory)


if __name__ == "__main__":
    get_adhyay_links()
