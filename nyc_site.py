#!/usr/bin/env python
# coding: utf-8

# In[1]:

import pandas as pd
from datetime import datetime
import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image
import arcgis
import sys
from arcgis.gis import GIS
from arcgis.raster.functions import apply, clip, remap, colormap
from arcgis.geometry import lengths, areas_and_lengths, project
from arcgis.geometry import Point, Polyline, Polygon, Geometry
from arcgis.geocoding import geocode
from arcgis.features import FeatureLayer
gis = GIS()
image1 = Image.open('images/nyc1.jfif')
image2 = Image.open('images/nyc2.jfif')
image3 = Image.open('images/nyc3.jfif')
image4 = Image.open('images/nyc4.png')
image5 = Image.open('images/nyc5.png')
image6 = Image.open('images/nyc6.png')
image7 = Image.open('images/nyc7.png')
graph = Image.open('images/nycgraph1.png')

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

# boroughs

landsat_item = gis.content.search('title:Multispectral Landsat', 'Imagery Layer', outside_org=True)[0]
landsat = landsat_item.layers[0]
area = geocode("New York City", out_sr=landsat.properties.spatialReference)[0]
landsat.extent = area['extent']
selected = landsat.filter_by(where="(Category = 1) AND (cloudcover <=0.05)",
                            time=[datetime(2020, 4, 1), datetime(2020, 6, 30)],
                             geometry=arcgis.geometry.filters.intersects(area['extent']))

df = selected.query(out_fields="AcquisitionDate, GroupName, CloudCover, DayOfYear", 
                    order_by_fields="AcquisitionDate").sdf
df['AcquisitionDate'] = pd.to_datetime(df['AcquisitionDate'], unit='ms')
nyc_image = landsat.filter_by('OBJECTID=3372200')
apply(nyc_image, 'Natural Color with DRA')
nyc_colorized = apply(nyc_image, 'NDVI Raw')

boroughs = FeatureLayer('https://gisservices.its.ny.gov/arcgis/rest/services/NYS_Civil_Boundaries/FeatureServer/2')
nh_df = pd.DataFrame.spatial.from_layer(boroughs)
#Brooklyn
bk_df = nh_df.loc[nh_df['NAME'] == 'Kings']
#Staten Island
si_df = nh_df.loc[nh_df['NAME'] == 'Richmond']
#Manhattan
m_df = nh_df.loc[nh_df['NAME'] == 'New York']
#The Bronx
tb_df = nh_df.loc[nh_df['NAME'] == 'Bronx']
#Queens
q_df = nh_df.loc[nh_df['NAME'] == 'Queens']
def all_together(df, name):

    def land_clip(df):
        global shape
        global poly
        global masked
        poly = df.iloc[0].SHAPE
        shape = clip(nyc_colorized,poly)
        shape.extent = area['extent']
        masked = colormap(remap(shape,
                        input_ranges=[-1,0,     # water
                                     -0.1, 0.4, # Concrete
                                     0.4, 1],   # Vegetation, Trees      
                        output_values=[1, 2, 3]),
                        colormap=[[1, 1, 255, 248], [2, 144, 148, 148], [3,14,247,22]], astype='u8')
    land_clip(df)
    def landcover_hist(shape,masked):
        global hist
        xpix = (shape.extent['xmax'] - shape.extent['xmin']) / 800
        ypix = (shape.extent['ymax'] - shape.extent['ymin']) / 400

        full_res = masked.compute_histograms(shape.extent,
                                   pixel_size={'x':xpix, 'y': ypix})
        total_pix = 0
        hist = full_res['histograms'][0]['counts'][0:]
        for i in hist[1:]:
            total_pix += i
    landcover_hist(shape,masked)
    
    def pie_chart(hist, name):
        colors=['#01FFF8','#909494','#0EF716']
        labels=['Water', 'Concrete', 'Green Cover']
        sizes = hist[1:]
        plt.pie(sizes,autopct='%1.1f%%',colors=colors,shadow=True)
        plt.title('Landcover of '+ str(name))
        plt.legend(labels,loc = 'right',bbox_to_anchor=(1.45, 0.75), ncol=1)
        plt.show()
    pie_chart(hist, name)
    return masked

all_together(bk_df,'Brooklyn')
