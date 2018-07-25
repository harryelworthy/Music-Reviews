from lxml import etree
from urllib import request
import os  
import numpy as np  
import pandas as pd  
import matplotlib.pyplot as plt 
from re import sub
from decimal import Decimal
import time

hdr = {'User-Agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.4; en-US; rv:1.9.2.2) Gecko/20100316 Firefox/3.6.2',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

def toMSquared(s):
    if s[-1:] == 'm':
        return int(s[:-2].replace(",",""))
    if s[-1:]=='d':
        return float(s[:-8].replace(",",""))*10000
    return 0

rowslist = []
urltimes = []
htmltimes = []
totaltimes = []
idnum = 1
for i in range(1,11):
    print('Search Page ' + str(i))
    start = time.time()
    baseurl = 'https://www.active.com/cycling?page='
    url = baseurl + str(i)
    req = request.Request(url, headers=hdr)
    try: 
    	doc = request.urlopen( req )
    except:
    	print('Bad Page')
    	continue
    middle = time.time()
    urltimes.append(middle - start)
    root = etree.HTML(doc.read())
    tree = etree.ElementTree(root)
    for j in range(1,11):

        title =  tree.xpath('//*[@id="lpf-tabs2-a"]/article[' + str(j) + ']/div/div/div/a/div[2]/div/h5/text()')


        DataList = {'Title': title, 'id' = idnum}
        idnum += 1
        rowslist.append(DataList)


df = pd.DataFrame(rowslist)
df.set_index('id')
df.to_csv('cyc.csv')