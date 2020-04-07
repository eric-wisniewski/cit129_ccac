# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 19:35:56 2020

@author: wisni
"""

'''
Eric Darsow of CCAC's Online Scrapping Demo for DAT-129

Ebay Scraping

Question: What is the avg cost of a computer on ebay
 
Before scraping a page, check:
    1) Are the URLs encoded in a sensible way that we can use
    the urllib to grap the HTML page easily?
    2) Are the elemts on the page we want to scrape enclosed
    in HTML tags with distinctive classes names or tag names?
    

'''

import urllib
from bs4 import BeautifulSoup

def getSearchURL(term):
    '''
    gets query against ebay.com given a search term
    '''
    url = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313.TR12.TRC2.A0.H0.Xcomputer.TRS0&_nkw=%s&_sacat=0" % (str(term))
    return url

def getPageText(url):
    '''
    given a url, fetches the raw HTML from the interwebs
    '''
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        return response.read()

def main():
    term = 'computer'
    url = getSearchURL(term)
    pageText = getPageText(url)
    #print(pageText)
    
    soup = BeautifulSoup(pageText, 'html.parser')

    computerdivprice = soup.find_all('div', 's-item__detail s-item__detail--primary')
    
    #print(computerdivprice)
    title = []
    
    counter = 0
    for comp in computerdivprice:
        counter += 1
        try:
            title.append(comp.find('span', {'class' : 's-item__price'}).string)
        except NameError:
            pass
        try:
            title.append(comp.find('span', {'class' : 's-item__price'}).string)
        except AttributeError:
            pass
    print(title)
          
main()
    
