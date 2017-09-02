import os
import urllib

from bs4 import BeautifulSoup


def get_html(url_link):
    url = urllib.urlopen(url_link)
    return url.read()


def write_adhyays(lis, directory):
    base_name = "adhyay"
    no = 1
    for li in lis:
        if not os.path.isfile(directory + "/" + base_name + str(no)):
            f = open(directory + "/" + base_name + str(no) + ".txt", 'w+')
        no = no + 1
        html = get_html("https://mr.wikisource.org" + li.a['href'])
        soup = BeautifulSoup(html)
        ps = soup.find_all('p')
        for p in ps:
            lines = p.text
            lines = lines.replace('<poem>', ' ')
            lines = lines.replace('<br>', ' ')
            f.write(lines.encode('utf-8') + "\n")


def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def get_adhyay_links():
    directory = "./datasets/dnyaneshwari"
    if not os.path.exists(directory):
        os.makedirs(directory)
    url = "https://mr.wikisource.org/wiki/%E0%A4%9C%E0%A5%8D%E0%A4%9E%E0%A4%BE%E0%A4%A8%E0%A5%87%E0%A4%B6%E0%A5%8D%E0%A4%B5%E0%A4%B0%E0%A5%80"
    html = get_html(url)
    soup = BeautifulSoup(html)
    ol = soup.find('ol')
    lis = ol.find_all('li')
    create_directory(directory)
    write_adhyays(lis, directory)


if __name__ == "__main__":
    get_adhyay_links()
