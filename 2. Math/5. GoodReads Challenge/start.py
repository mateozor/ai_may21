#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 12:30:13 2021

@author: mateo
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd
#import numpy as np

for n in range(0, 30, 10):
    try:
        restaurants = requests.get('https://www.yelp.de/search?cflt=restaurants&find_loc=Berlin&start=', n)
        bars = requests.get('https://www.yelp.de/search?cflt=bars&find_loc=Berlin&start=', n)
        soup1 = BeautifulSoup(restaurants.text, 'html.parser')
        df = pd.DataFrame(soup1)
        soup2 = BeautifulSoup(bars.text, 'html.parser')
        df = pd.DataFrame(soup2)
    except:
        break




soup1 = BeautifulSoup(restaurants.text, 'html.parser')
soup2 = BeautifulSoup(bars.text, 'html.parser')
print(df)               
                
