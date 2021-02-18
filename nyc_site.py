#!/usr/bin/env python
# coding: utf-8

# In[1]:

import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image
import time

fc_sat_1 = Image.open('images/fc_sat_1975.jfif')
fc_sat_2 = Image.open('images/fc_sat_1988.jfif')
fc_sat_3 = Image.open('images/fc_sat_1999.jfif')
fc_sat_4 = Image.open('images/fc_sat_2010.jfif')
fc_sat_5 = Image.open('images/fc_sat_2015.jfif')
fc_sat_6 = Image.open('images/fc_sat_2020.jfif')
b_sat_1 = Image.open('images/b_sat_1975.jfif')
b_sat_2 = Image.open('images/b_sat_1988.jfif')
b_sat_3 = Image.open('images/b_sat_1999.jfif')
b_sat_4 = Image.open('images/b_sat_2010.jfif')
b_sat_5 = Image.open('images/b_sat_2015.jfif')
b_sat_6 = Image.open('images/b_sat_2020.jfif')
q_sat_1 = Image.open('images/q_sat_1975.jfif')
q_sat_2 = Image.open('images/q_sat_1988.jfif')
q_sat_3 = Image.open('images/q_sat_1999.jfif')
q_sat_4 = Image.open('images/q_sat_2010.jfif')
q_sat_5 = Image.open('images/q_sat_2015.jfif')
q_sat_6 = Image.open('images/q_sat_2020.jfif')
m_sat_1 = Image.open('images/m_sat_1975.jfif')
m_sat_2 = Image.open('images/m_sat_1988.jfif')
m_sat_3 = Image.open('images/m_sat_1999.jfif')
m_sat_4 = Image.open('images/m_sat_2010.jfif')
m_sat_5 = Image.open('images/m_sat_2015.jfif')
m_sat_6 = Image.open('images/m_sat_2020.jfif')
tb_sat_1 = Image.open('images/tb_sat_1975.jfif')
tb_sat_2 = Image.open('images/tb_sat_1988.jfif')
tb_sat_3 = Image.open('images/tb_sat_1999.jfif')
tb_sat_4 = Image.open('images/tb_sat_2010.jfif')
tb_sat_5 = Image.open('images/tb_sat_2015.jfif')
tb_sat_6 = Image.open('images/tb_sat_2020.jfif')
si_sat_1 = Image.open('images/si_sat_1975.jfif')
si_sat_2 = Image.open('images/si_sat_1988.jfif')
si_sat_3 = Image.open('images/si_sat_1999.jfif')
si_sat_4 = Image.open('images/si_sat_2010.jfif')
si_sat_5 = Image.open('images/si_sat_2015.jfif')
si_sat_6 = Image.open('images/si_sat_2020.jfif')


city_dict = {
  'Full_City':{
    'Satellite':{1975:fc_sat_1,1988:fc_sat_2,1999:fc_sat_3,2010:fc_sat_4,2015:fc_sat_5,2020:fc_sat_6},
    'NDVI':[1975,1988,1999,2010,2015,2020],
    'Water':[1975,1988,1999,2010,2015,2020],
    'Buildings':[1975,1988,1999,2010,2015,2020],
    'Greenery':[1975,1988,1999,2010,2015,2020],
    'Full':[1975,1988,1999,2010,2015,2020]},
    'Brooklyn':{
      'Satellite':{1975:b_sat_1,1988:b_sat_2,1999:b_sat_3,2010:b_sat_4,2015:b_sat_5,2020:b_sat_6},
      'NDVI':[1975,1988,1999,2010,2015,2020],
      'Water':[1975,1988,1999,2010,2015,2020],
      'Buildings':[1975,1988,1999,2010,2015,2020],
      'Greenery':[1975,1988,1999,2010,2015,2020],
      'Full':[1975,1988,1999,2010,2015,2020]},
      'Queens':{
        'Satellite':{1975:q_sat_1,1988:q_sat_2,1999:q_sat_3,2010:q_sat_4,2015:q_sat_5,2020:q_sat_6},
        'NDVI':[1975,1988,1999,2010,2015,2020],
        'Water':[1975,1988,1999,2010,2015,2020],
        'Buildings':[1975,1988,1999,2010,2015,2020],
        'Greenery':[1975,1988,1999,2010,2015,2020],
        'Full':[1975,1988,1999,2010,2015,2020]},
        'Manhattan':{
          'Satellite':{1975:m_sat_1,1988:m_sat_2,1999:m_sat_3,2010:m_sat_4,2015:m_sat_5,2020:m_sat_6},
          'NDVI':[1975,1988,1999,2010,2015,2020],
          'Water':[1975,1988,1999,2010,2015,2020],
          'Buildings':[1975,1988,1999,2010,2015,2020],
          'Greenery':[1975,1988,1999,2010,2015,2020],
          'Full':[1975,1988,1999,2010,2015,2020]},
          'The_Bronx':{
            'Satellite':{1975:tb_sat_1,1988:tb_sat_2,1999:tb_sat_3,2010:tb_sat_4,2015:tb_sat_5,2020:tb_sat_6},
            'NDVI':[1975,1988,1999,2010,2015,2020],
            'Water':[1975,1988,1999,2010,2015,2020],
            'Buildings':[1975,1988,1999,2010,2015,2020],
            'Greenery':[1975,1988,1999,2010,2015,2020],
            'Full':[1975,1988,1999,2010,2015,2020]},
  'Staten_Island':{
    'Satellite':{1975:si_sat_1,1988:si_sat_2,1999:si_sat_3,2010:si_sat_4,2015:si_sat_5,2020:si_sat_6},
    'NDVI':[1975,1988,1999,2010,2015,2020],
    'Water':[1975,1988,1999,2010,2015,2020],
    'Buildings':[1975,1988,1999,2010,2015,2020],
    'Greenery':[1975,1988,1999,2010,2015,2020],
    'Full':[1975,1988,1999,2010,2015,2020]}
        }

st.title('New York City Landcover Analysis')
side = st.sidebar.selectbox(
    'Select a Location',
    ('-----', 'Full City','Brooklyn', 'Queens', 'Manhattan', 'The Bronx', 'Staten Island')
)
side2 = st.sidebar.selectbox(
  'Select a View',
  ('-----', 'Satellite','NDVI filter','Water','Buildings','Greenery','Full')
  
)
def home_page(x,y):
  if x == 'Full City':
    x = 'Full_City'
  if x == 'The Bronx':
    x = 'The_Bronx'
  if x == 'Staten Island':
    x = 'Staten_Island'
  z = st.select_slider('Year',options= [1975, 1988, 1999, 2010, 2015, 2020])
  #st.image(city_dict[x][y][z],width=1500)
  col1, col2 = st.beta_columns(2)
  original = Image.open(image)
  col1.header("Original")
  col1.image(city_dict[x][y][z],width=1500)
  col2.header("")
  st.write(str(x)+ ' in ' +str(z))
                             
home_page(side,side2)
