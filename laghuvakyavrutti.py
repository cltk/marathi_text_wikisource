import os
import urllib.request

from bs4 import BeautifulSoup


def get_html(url_link):
    url = urllib.request.urlopen(url_link)
    return url.read()


def write_ovya(lis, directory):
    base_name = "ovya"
    start = 1
    end = 100
    for li in lis:
        if not os.path.isfile(directory + "/" + base_name + str(start) + "to" + str(end)):
            f = open(directory + "/" + base_name + str(start) + "to" + str(end) + ".txt", 'wb+')
        start = start + 100
        end = end + 100
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


def get_ovya_links():
    directory = "./datasets/laghuvakyavrutti"
    if not os.path.exists(directory):
        os.makedirs(directory)
    url = "https://mr.wikisource.org/wiki/%E0%A4%B8%E0%A4%BE%E0%A4%B0%E0%A5%8D%E0%A4%A5_%E0%A4%B2%E0%A4%98%E0%A5%81%E0%A4%B5%E0%A4%BE%E0%A4%95%E0%A5%8D%E0%A4%AF%E0%A4%B5%E0%A5%83%E0%A4%A4%E0%A5%8D%E0%A4%A4%E0%A5%80"
    html = get_html(url)
    soup = BeautifulSoup(html, "lxml")
    ol = soup.find('ol')
    lis = ol.find_all('li')
    create_directory(directory)
    write_ovya(lis, directory)


if __name__ == "__main__":
    get_ovya_links()
