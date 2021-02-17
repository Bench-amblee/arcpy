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

full_city_dict = {'Satellite': image1,'NDVI Filter': image2,'City Boundary Cutout': image3,
              'Water': image5, 'Concrete': image6, 'Greenery': image7, 'Final': image4}

City = {0: image1,'NDVI Filter': image2,'City Boundary Cutout': image3,
              'Water': image5, 'Concrete': image6, 'Greenery': image7, 'Final': image4}
Brooklyn = {0:bimage1,'Map':bimage2,'Masked':bimage3}
Queens = {'Chart':qimage1,'Map':qimage2,'Masked':qimage3}
Manhattan = {'Chart':mimage1,'Map':mimage2,'Masked':mimage3}
Staten = {'Chart':simage1,'Map':simage2,'Masked':simage3}
Bronx = {'Chart':timage1,'Map':timage2,'Masked':timage3}
selection = {'Full City': City, 'Brooklyn': Brooklyn, 'Queens': Queens, 'Manhattan': Manhattan, 'The Bronx': Bronx, 'Staten Island': Staten}

# Front End

st.title('New York City Landcover Analysis')
side = st.sidebar.selectbox(
    'Select a Location',
    ('-----', 'Full City','Brookyln', 'Queens', 'Manhattan', 'The Bronx', 'Staten Island')
)
side2 = st.sidebar.selectbox(
  'Select a View',
  ('-----', 'Satellite','NDVI filter','Water','Buildings','Greenery','Full')
  
)
def home_page():
  if side == '-----' and side2 == '-----':
    st.write('Select a location and view using the left sidebar to see how to landcover has changed over time')
  
                             
view = st.select_slider('Year',options= [1975, 1988, 1999, 2010, 2015, 2020])


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
        
view_select()
        
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


