import urllib.parse
import urllib.request
import io
import zipfile 
import numpy as np
import pandas as pd
from urllib import *
import csv

def save_france(date):
    year = date[0:4]
    month = date[4:6]
    day = date[6:8]
    folder = 'C:\\Users\Wattgo\Desktop\Xinqiao\\rte_challenge'
    folder = '/home/xinqiao/Desktop/xinqiao/test'
    datesave = year +'_' +month + '_' + day +'_France'
    output = 'eco2mix_' + datesave + '.csv'
    output = folder +'/'+output
    print(output)
    url = 'https://eco2mix.rte-france.com/curves/eco2mixDl?date='+ day +'/' + month +'/' + year


    u = urllib.request.urlopen(url)
    s = io.BytesIO(u.read())
    z = zipfile.ZipFile(s)
    l = z.namelist()
    f = z.open(l[0])
    df = pd.read_csv(f,sep='\t',encoding='cp1252')
    df.to_csv(output, encoding = 'UTF8',sep = ';',header = False)


datebase = '201705'
for i in range(1,18):
    i = str(i)
    if len(i)==1:
        i= '0'+i
    print(i)
    date =datebase + i
    save_france(date)
