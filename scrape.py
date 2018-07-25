from lxml import etree
import urllib2
import os  
import numpy as np  
import pandas as pd  
import matplotlib.pyplot as plt 
from re import sub
from decimal import Decimal
import time


def chop(s):
    return str(s)[2:-2]

rowslist = []
urltimes = []
htmltimes = []
totaltimes = []
idnum = 1
for i in range(1,1691):
    print('Search Page ' + str(i))
    start = time.time()
    baseurl = 'https://pitchfork.com/reviews/albums/?page='
    url = baseurl + str(i)
    try: 
    	doc = urllib2.urlopen( url )
    except:
    	print('Bad Page')
    	continue
    middle = time.time()
    urltimes.append(middle - start)
    root = etree.HTML(doc.read())
    tree = etree.ElementTree(root)
    for j in range(1,12):

        albumlink =  chop(tree.xpath('//*[@id="reviews"]/div[2]/div/div[1]/div[1]/div/div/div[' + str(j) + ']/a/@href'))
        title = chop(tree.xpath('//*[@id="reviews"]/div[2]/div/div[1]/div[1]/div/div/div['+ str(j) + ']/a/div[2]/ul/li/text()'))
        artist = chop(tree.xpath('//*[@id="reviews"]/div[2]/div/div[1]/div[1]/div/div/div['+ str(j) + ']/a/div[2]/h2/text()'))

        #locorg = (tree.xpath('//*[@id="lpf-tabs2-a"]/article[' + str(j) + ']/div/div/div/a/div[2]/div/div[2]/h6[1]/span[1]/text()'))
        #print locorg

        DataList = {'Title': title, 'Artist': artist, 'Link': albumlink, 'id': idnum}
        idnum += 1
        rowslist.append(DataList)


df = pd.DataFrame(rowslist)
df.set_index('id')
df.to_csv('pf.csv')