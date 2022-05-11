#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 09:03:54 2020

@author: Alastair
"""
#import libraries
import pandas as pd
import geocoder
from os import path

#set directory
DATA_DIR = '/Users/Alastair/Desktop/python/geo/'

#read .csv of UK towns and their population from a source like the ons
df = pd.read_csv(path.join(DATA_DIR, 'geo_uk_pop.csv'))

#check df looks ok
df.head()

#add 'United Kingdon' to the town so that other areas around the world aren't searched for
df['town'] = df['town'] + ', United Kingdom'

#create functions using geocoder to search for the latitude and logitude values for the towns
def geocode_lat(town):
    
    g = geocoder.google(town, key='AIzaSyAXUeaPIQzaEk7EG9uJ-_R8qcLhbEC4tVk')
    
    return g.latlng[0]

def geocode_lng(town):
    
    g = geocoder.google(town, key='AIzaSyAXUeaPIQzaEk7EG9uJ-_R8qcLhbEC4tVk')
    
    return g.latlng[1]

#use functions on all the towns to create new columns
df['lat'] = df['town'].apply(geocode_lat)

df['lng'] = df['town'].apply(geocode_lng)

#check df looks ok again
df.head()

#save as csv 
df.to_csv(path.join(DATA_DIR, 'geo_uk_pop_latlng.csv'))

