import os
import urllib.request

from bs4 import BeautifulSoup


def get_html(url_link):
    url = urllib.request.urlopen(url_link)
    return url.read()


def write_gatha(uls, directory):
    base_name = "gatha"
    start = 0
    end = 300
    for ul in uls:
        if start == 0:
            start = 1
            continue
        if not os.path.isfile(directory + "/" + base_name + str(start) + "to" + str(end)):
            f = open(directory + "/" + base_name + str(start) + "to" + str(end) + ".txt", 'wb+')
        start = start + 300
        end = end + 300
        html = get_html("https://mr.wikisource.org" + ul.li.a['href'])
        soup = BeautifulSoup(html)
        ps = soup.find_all('p')
        pres = soup.find_all('pre')
        pre_num = 1
        pre_size = pres.__len__()
        for p in ps:
            lines = p.text
            lines = lines.replace('<poem>', ' ')
            lines = lines.replace('<br>', ' ')
            f.write(lines.encode('utf-8') + "\n".encode('utf-8'))
            if pres.__len__() == 0 or pre_size <= pre_num:
                continue
            lines = pres[pre_num].text
            lines = lines.replace('<poem>', ' ')
            lines = lines.replace('<br>', ' ')
            f.write(lines.encode('utf-8') + "\n".encode('utf-8'))
            pre_num = pre_num + 1

def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def get_gatha_links():
    directory = "./datasets/tukaramgatha"
    if not os.path.exists(directory):
        os.makedirs(directory)
    url = "https://mr.wikisource.org/wiki/%E0%A4%A4%E0%A5%81%E0%A4%95%E0%A4%BE%E0%A4%B0%E0%A4%BE%E0%A4%AE_%E0%A4%97%E0%A4%BE%E0%A4%A5%E0%A4%BE"
    html = get_html(url)
    soup = BeautifulSoup(html, "lxml")
    divs = soup.find_all('div')
    div = divs[2]
    uls = div.find_all('ul')
    create_directory(directory)
    write_gatha(uls, directory)


if __name__ == "__main__":
    get_gatha_links()
