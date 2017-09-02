import os
import urllib

from bs4 import BeautifulSoup


def get_html(url_link):
    url = urllib.urlopen(url_link)
    return url.read()


def write_haripath(lis, directory):
    no = 0
    names = ['by_dnyandev_maharaj','by_namdev_maharaj','by_eknath_maharaj','by_tukaram_maharaj','by_nivritti_maharaj']
    for li in lis:
        f = open(directory + "/" + names[no] + ".txt", 'w+')
        no = no + 1
        html = get_html("https://mr.wikisource.org" + li.a['href'])
        soup = BeautifulSoup(html)
        ps = soup.find_all('p')
        for p in ps:
            lines = p.text
            lines = lines.replace('{{{notes}}}', ' ')
            lines = lines.replace('<poem>', ' ')
            lines = lines.replace('<br>', ' ')
            lines = lines.replace('{', '')
            lines = lines.replace('}', '')
            f.write(lines.encode('utf-8') + "\n")


def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def get_haripath_links():
    directory = "./datasets/haripath"
    url = "https://mr.wikisource.org/wiki/%E0%A4%B9%E0%A4%B0%E0%A4%BF%E0%A4%AA%E0%A4%BE%E0%A4%A0"
    html = get_html(url)
    soup = BeautifulSoup(html)
    ul = soup.find('ul')
    lis = ul.find_all('li')
    create_directory(directory)
    write_haripath(lis, directory)


if __name__ == "__main__":
    get_haripath_links()
