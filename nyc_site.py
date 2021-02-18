#!/usr/bin/env python
# coding: utf-8

# In[1]:

import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image

image1 = Image.open('images/nyc1.jfif')
image2 = Image.open('images/nyc2.jfif')
image3 = Image.open('images/nyc3.jfif')
image4 = Image.open('images/nyc4.png')
image5 = Image.open('images/nyc5.png')
image6 = Image.open('images/nyc6.png')
image7 = Image.open('images/nyc7.png')
graph = Image.open('images/nycgraph1.png')
fc_sat_1 = Image.open('images/fc_sat_1975.jfif')
fc_sat_2 = Image.open('images/fc_sat_1988.jfif')
fc_sat_3 = Image.open('images/fc_sat_1999.jfif')
fc_sat_4 = Image.open('images/fc_sat_2010.jfif')
fc_sat_5 = Image.open('images/fc_sat_2015.jfif')
fc_sat_6 = Image.open('images/fc_sat_2020.jfif')

city_dict = {
  'Full_City':{
    'Satellite':{1975:fc_sat_1,1988:fc_sat_2,1999:fc_sat_3,2010:fc_sat_4,2015:fc_sat_5,2020:fc_sat_6},
    'NDVI':[1975,1988,1999,2010,2015,2020],
    'Water':[1975,1988,1999,2010,2015,2020],
    'Buildings':[1975,1988,1999,2010,2015,2020],
    'Greenery':[1975,1988,1999,2010,2015,2020],
    'Full':[1975,1988,1999,2010,2015,2020]},
    'Brooklyn':{
      'Satellite':[1975,1988,1999,2010,2015,2020],
      'NDVI':[1975,1988,1999,2010,2015,2020],
      'Water':[1975,1988,1999,2010,2015,2020],
      'Buildings':[1975,1988,1999,2010,2015,2020],
      'Greenery':[1975,1988,1999,2010,2015,2020],
      'Full':[1975,1988,1999,2010,2015,2020]},
      'Queens':{
        'Satellite':[1975,1988,1999,2010,2015,2020],
        'NDVI':[1975,1988,1999,2010,2015,2020],
        'Water':[1975,1988,1999,2010,2015,2020],
        'Buildings':[1975,1988,1999,2010,2015,2020],
        'Greenery':[1975,1988,1999,2010,2015,2020],
        'Full':[1975,1988,1999,2010,2015,2020]},
        'Manhattan':{
          'Satellite':[1975,1988,1999,2010,2015,2020],
          'NDVI':[1975,1988,1999,2010,2015,2020],
          'Water':[1975,1988,1999,2010,2015,2020],
          'Buildings':[1975,1988,1999,2010,2015,2020],
          'Greenery':[1975,1988,1999,2010,2015,2020],
          'Full':[1975,1988,1999,2010,2015,2020]},
          'The_Bronx':{
            'Satellite':[1975,1988,1999,2010,2015,2020],
            'NDVI':[1975,1988,1999,2010,2015,2020],
            'Water':[1975,1988,1999,2010,2015,2020],
            'Buildings':[1975,1988,1999,2010,2015,2020],
            'Greenery':[1975,1988,1999,2010,2015,2020],
            'Full':[1975,1988,1999,2010,2015,2020]}
        }
full_city_dict = {'Satellite': image1,'NDVI Filter': image2,'City Boundary Cutout': image3,
              'Water': image5, 'Concrete': image6, 'Greenery': image7, 'Final': image4}

City = {0: image1,'NDVI Filter': image2,'City Boundary Cutout': image3,
              'Water': image5, 'Concrete': image6, 'Greenery': image7, 'Final': image4}

Brooklyn = [1,2,3]

st.title('New York City Landcover Analysis')
side = st.sidebar.selectbox(
    'Select a Location',
    ('-----', 'Full City','Brookyln', 'Queens', 'Manhattan', 'The Bronx', 'Staten Island')
)
side2 = st.sidebar.selectbox(
  'Select a View',
  ('-----', 'Satellite','NDVI filter','Water','Buildings','Greenery','Full')
  
)
def home_page(x,y):
  if x == '-----' or y == '-----':
    st.write('Select a location and view using the left sidebar to see how to landcover has changed over time')
  if x == 'Full City':
    x = 'Full_City'
  z = st.select_slider('Year',options= [1975, 1988, 1999, 2010, 2015, 2020])
  st.image(city_dict[x][y][z])
  
home_page(side,side2,)
                             



hmm = '''def show_image(choice):
    if choice in full_city_dict.keys():
        st.image(full_city_dict[choice])
        st.subheader(choice)
        if choice == 'Water':
            st.write('Water Cover Percentage: 36.3%')
        if choice == 'Greenery':
            st.write('Greenery Cover Percentage: 15.1%')
        if choice == 'Concrete':
            st.write('Concrete and Building Cover Percentage: 48.6%')
        if choice == 'Final':
            st.image(graph)
show_image(view)
'''
def view_select(choice):
    if choice in selection.keys():
        global images
        images = selection.get(choice)
        
def show_image(choice):
    st.image(choice[view])
    st.subheader(choice.keys())
    if choice == 'Water':
      st.write('Water Cover Percentage: 36.3%')
    if choice == 'Greenery':
      st.write('Greenery Cover Percentage: 15.1%')
    if choice == 'Concrete':
      st.write('Concrete and Building Cover Percentage: 48.6%')
    if choice == 'Final':
      st.image(graph)
            
#view_select(side)
#show_image(images)


