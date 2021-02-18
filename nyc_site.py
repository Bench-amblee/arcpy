#!/usr/bin/env python
# coding: utf-8

# In[1]:

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import time
import matplotlib as mpl
mpl.rcParams['font.size'] = 3.0
# Satellite
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
#NDVI
fc_ndvi_1 = Image.open('images/fc_ndvi_1975.png')
fc_ndvi_2 = Image.open('images/fc_ndvi_1988.png')
fc_ndvi_3 = Image.open('images/fc_ndvi_1999.png')
fc_ndvi_4 = Image.open('images/fc_ndvi_2010.png')
fc_ndvi_5 = Image.open('images/fc_ndvi_2015.png')
fc_ndvi_6 = Image.open('images/fc_ndvi_2020.png')
b_ndvi_1 = Image.open('images/b_ndvi_1975.png')
b_ndvi_2 = Image.open('images/b_ndvi_1988.png')
b_ndvi_3 = Image.open('images/b_ndvi_1999.png')
b_ndvi_4 = Image.open('images/b_ndvi_2010.png')
b_ndvi_5 = Image.open('images/b_ndvi_2015.png')
b_ndvi_6 = Image.open('images/b_ndvi_2020.png')
q_ndvi_1 = Image.open('images/q_ndvi_1975.png')
q_ndvi_2 = Image.open('images/q_ndvi_1988.png')
q_ndvi_3 = Image.open('images/q_ndvi_1999.png')
q_ndvi_4 = Image.open('images/q_ndvi_2010.png')
q_ndvi_5 = Image.open('images/q_ndvi_2015.png')
q_ndvi_6 = Image.open('images/q_ndvi_2020.png')
m_ndvi_1 = Image.open('images/m_ndvi_1975.png')
m_ndvi_2 = Image.open('images/m_ndvi_1988.png')
m_ndvi_3 = Image.open('images/m_ndvi_1999.png')
m_ndvi_4 = Image.open('images/m_ndvi_2010.png')
m_ndvi_5 = Image.open('images/m_ndvi_2015.png')
m_ndvi_6 = Image.open('images/m_ndvi_2020.png')
tb_ndvi_1 = Image.open('images/tb_ndvi_1975.png')
tb_ndvi_2 = Image.open('images/tb_ndvi_1988.png')
tb_ndvi_3 = Image.open('images/tb_ndvi_1999.png')
tb_ndvi_4 = Image.open('images/tb_ndvi_2010.png')
tb_ndvi_5 = Image.open('images/tb_ndvi_2015.png')
tb_ndvi_6 = Image.open('images/tb_ndvi_2020.png')
si_ndvi_1 = Image.open('images/si_ndvi_1975.png')
si_ndvi_2 = Image.open('images/si_ndvi_1988.png')
si_ndvi_3 = Image.open('images/si_ndvi_1999.png')
si_ndvi_4 = Image.open('images/si_ndvi_2010.png')
si_ndvi_5 = Image.open('images/si_ndvi_2015.png')
si_ndvi_6 = Image.open('images/si_ndvi_2020.png')
#data 
Hists = pd.ExcelFile('data/nyc_site_hist_values.xlsx')

city_dict = {
  'Full_City':{
    'Satellite':{1975:fc_sat_1,1988:fc_sat_2,1999:fc_sat_3,2010:fc_sat_4,2015:fc_sat_5,2020:fc_sat_6},
    'NDVI_Filter':{1975:fc_ndvi_1,1988:fc_ndvi_2,1999:fc_ndvi_3,2010:fc_ndvi_4,2015:fc_ndvi_5,2020:fc_ndvi_6}},
    'Brooklyn':{
      'Satellite':{1975:b_sat_1,1988:b_sat_2,1999:b_sat_3,2010:b_sat_4,2015:b_sat_5,2020:b_sat_6},
      'NDVI_Filter':{1975:b_ndvi_1,1988:b_ndvi_2,1999:b_ndvi_3,2010:b_ndvi_4,2015:b_ndvi_5,2020:b_ndvi_6}},
      'Queens':{
        'Satellite':{1975:q_sat_1,1988:q_sat_2,1999:q_sat_3,2010:q_sat_4,2015:q_sat_5,2020:q_sat_6},
        'NDVI_Filter':{1975:q_ndvi_1,1988:q_ndvi_2,1999:q_ndvi_3,2010:q_ndvi_4,2015:q_ndvi_5,2020:q_ndvi_6}},
        'Manhattan':{
          'Satellite':{1975:m_sat_1,1988:m_sat_2,1999:m_sat_3,2010:m_sat_4,2015:m_sat_5,2020:m_sat_6},
          'NDVI_Filter':{1975:m_ndvi_1,1988:m_ndvi_2,1999:m_ndvi_3,2010:m_ndvi_4,2015:m_ndvi_5,2020:m_ndvi_6}},
          'The_Bronx':{
            'Satellite':{1975:tb_sat_1,1988:tb_sat_2,1999:tb_sat_3,2010:tb_sat_4,2015:tb_sat_5,2020:tb_sat_6},
            'NDVI_Filter':{1975:tb_ndvi_1,1988:tb_ndvi_2,1999:tb_ndvi_3,2010:tb_ndvi_4,2015:tb_ndvi_5,2020:tb_ndvi_6}},
  'Staten_Island':{
    'Satellite':{1975:si_sat_1,1988:si_sat_2,1999:si_sat_3,2010:si_sat_4,2015:si_sat_5,2020:si_sat_6},
    'NDVI_Filter':{1975:si_ndvi_1,1988:si_ndvi_2,1999:si_ndvi_3,2010:si_ndvi_4,2015:si_ndvi_5,2020:si_ndvi_6}}
        }
st. set_page_config(layout="wide")
st.title('New York City Landcover Analysis')
side = st.sidebar.selectbox(
    'Select a Location',
    ('-----', 'Full City','Brooklyn', 'Queens', 'Manhattan', 'The Bronx', 'Staten Island')
)
side2 = st.sidebar.selectbox(
  'Select a View',
  ('-----', 'Satellite','NDVI Filter')
  
)
def home_page(x,y):
  if x == '-----' or y == '-----':
    st.write('pick an option using the left sidebar')
  if x == 'Full City' or x == 'The Bronx' or x == 'Staten Island':
    global x_
    x_ = x.replace(" ","_")
  else:
    x_ = x
  if y == 'NDVI Filter':
    global y_
    y_ = y.replace(" ","_")
  else:
    y_ = y
  #satellite
  if y == 'Satellite':
    z = st.select_slider('Year',options= [1975,1988, 1999, 2010, 2015, 2020])
    st.image(city_dict[x_][y_][z],width=1400)
    st.write(str(x)+ ' in ' +str(z))
  #ndvi graphs
  if y == 'NDVI Filter':
    col1, col2 = st.beta_columns(2)
    labels = 'Water','Buildings','Greenery'
    colors=['#01FFF8','#909494','#0EF716']
    with col1:
      z = st.select_slider('Year',options= [1975, 1988, 1999, 2010, 2015, 2020],key='compare1')
      st.image(city_dict[x_][y_][z])
      st.write(str(x)+ ' in ' +str(z))
      df = pd.read_excel(Hists, x_)
      fig1, ax1 = plt.subplots()
      #ax1.pie(df[z],labels=labels,colors=colors,autopct='%1.1f%%')
      ax1.pie(df[z],colors=colors)
      fig1 = plt.gcf()
      fig1.set_size_inches(1.2,1.2)
      st.pyplot(fig1)
    with col2:
      a = st.select_slider('Year',options= [1975, 1988, 1999, 2010, 2015, 2020],key='compare2')
      st.image(city_dict[x_][y_][a])
      st.write(str(x)+ ' in ' +str(a))
      df = pd.read_excel(Hists, x_)
      fig2, ax1 = plt.subplots()
      #ax1.pie(df[a],labels=labels,colors=colors,autopct='%1.1f%%')
      ax1.pie(df[a],colors=colors)
      fig2 = plt.gcf()
      fig2.set_size_inches(1.2,1.2)
      st.pyplot(fig2)
  #col1, col2, col3 = st.beta_columns(3)
  #original = Image.open('images/white.jpg')
  #col1.image(city_dict[x][y][z],width=1200)
  #col2.image(original)
  #col3.image(original)
                             
home_page(side,side2)
