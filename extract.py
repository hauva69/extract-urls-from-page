#!/usr/local/bin/python3

from bs4 import BeautifulSoup

import sys
import urllib.request

def printelementattributepair(soup, elem, attr):
    for link in soup.find_all(elem):
        print(link.get(attr))

def main():
    html = urllib.request.urlopen(sys.argv[1]).read()
    soup = BeautifulSoup(html, 'html.parser')
    printelementattributepair(soup, 'a', 'href')
    printelementattributepair(soup, 'img', 'src')

if __name__ == '__main__':
    main()
