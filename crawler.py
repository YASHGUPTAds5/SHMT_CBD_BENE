import requests
from bs4 import BeautifulSoup
import pandas as pd
import urllib.request

urls = ['https://lordjones.com/',
        'https://www.charlottesweb.com/',
        'https://www.thecbdistillery.com/',
        'https://medterracbd.com/',
        'https://www.diamondcbd.com/',
        'https://www.pluscbdoil.com/',
        'https://bluebirdbotanicals.com/',
        'https://www.elixinol.com/',
        'https://www.lazarusnaturals.com/',
        'https://cbdfx.com/',
        'https://greenroads.com/',
        ]

def rec(url, j=0):
    if j>15:
        return "<h1ml></html>"
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    req = urllib.request.Request(url, headers=headers)
    j += 1
    try:
        html = urllib.request.urlopen(req).read()
    except:
        html = rec(url, j)
    return html
def crawl():
    i = 0
    df = {"URL": [],
        "Description": [],
        "Keywords": []
            }
    for url in urls:
        html = rec(url, 0)
        soup = BeautifulSoup(html, 'html5lib')
        i+=1

        try:
            description = soup.find("meta", attrs={'name': "description"})['content']
        except TypeError:
            description = ""
        try:
            keywords = soup.find("meta", attrs={'name': "keywords"})['content']
        except TypeError:
            keywords = ""
        df['URL'].append(url)
        df['Description'].append(description)
        df['Keywords'].append(keywords.lower().replace("medterra", ""))

    df = pd.DataFrame(df)
    df.to_csv("metadata.csv")
if __name__ == "__main__":
    crawl()