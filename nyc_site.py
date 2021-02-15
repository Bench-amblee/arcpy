#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
from PIL import Image
image1 = Image.open('nyc1.jfif')
image2 = Image.open('nyc2.jfif')
image3 = Image.open('nyc3.jfif')
image4 = Image.open('nyc4.png')
image5 = Image.open('nyc5.png')
image6 = Image.open('nyc6.png')
image7 = Image.open('nyc7.png')
graph = Image.open('nycgraph1.png')

image_dict = {'Satellite': image1,'NDVI Filter': image2,'City Boundary Cutout': image3,
              'Water': image5, 'Concrete': image6, 'Greenery': image7, 'Final': image4}

# In[7]:


st.title('New York City Landcover Analysis')
view = st.select_slider('Select a  view of the city',
                         options=['Satellite', 'NDVI Filter', 'City Boundary Cutout',
                                  'Water', 'Concrete', 'Greenery', 'Final'])

def show_image(choice):
    if choice in image_dict.keys():
        st.image(image_dict[choice])
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

