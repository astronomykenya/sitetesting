#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  4 14:30:08 2025

@author: lekshmigopal
"""

import streamlit as st
import subprocess
from PIL import Image as IMG
from streamlit_image_coordinates import streamlit_image_coordinates
from PIL import ImageOps
import pyglet
import streamlit as st
import subprocess
from PIL import Image as IMG
from streamlit_image_coordinates import streamlit_image_coordinates
from PIL import ImageOps
import pyglet
import base64
import streamlit as st
from st_clickable_images import clickable_images

st.header("Optical Telescope site testing in Kenya",divider='blue')


campussky=IMG.open("skycampus.jpg")
st.image(campussky)
st.caption("Classroom against outer Milky Way at Turkana Basin Institute, Ileret campus, Turkana, Northern Kenya. Photo by Dr. Kenneth Duncan")
st.markdown("Kenya’s access to the equatorial sky is a great asset for astronomy in the country. The atmospheric conditions of the north are indicative of a globally-competitive site for the placement of a research-grade optical telescope. The pursuit of establishing this site is a collaboration between institutions from the UK and Kenya, working to collect weather data from 3 test locations: Mt. Nyiro, Mt. Mara, and Mt. Kenya.")
st.subheader("DSIT Tactical fund")
st.write("A significant part of this project has been funded by the British High Commission's Department of Science, Technology and Innovation (DSIT) Tactical Fund. This funding has covered the Mt. Nyiro field trip (and installation), the Site testing Workshop, the development of the Data Visualisation Toolkit, and the adaptation of the WRF Met model to the Kenyan context.") 
logos1=IMG.open("logoswide3.png")
st.image(logos1)
logos2=IMG.open("logoswide4.png")
st.image(logos2)

tab1,tab2,tab3,tab4,tab5 = st.tabs(["Weather stations", "Student Field Trip" , "WRF model","Workshop Resources","Data"])

with tab1:     
    campbell=IMG.open("campbell.png")
    col1, col2 = st.columns(2)

    with col1:
        st.image(campbell)
        st.caption('Weather station at Mt. Kenya with surrounding electric fence')

    with col2:
        st.write("We use Campbell Scientific Weather stations to collect atmospheric data for the 3 sites. The systems are equipped with 2 sensors: Climavue50 and SL515 Apogee Pyranometer. The Climavue sensor measures all main meteorological parameters, and the apogee sensor records solar groundwave radiation. The instrument also has a raingauge and a lightning detector. The sensors make recordings that are collected by the CR350 data loggers which store and transmit the data. The data loggers are configured to transmit to the public server hosted at Turkana Basin Institute using the safaricom network. Stations are collecting data every 10 minutes and up to 3 months of data can be stored on the internal hard disk. The size of data collected is small ~ 10KB per hour. Each station has been secured based on the needs of its locality - i.e. what the highest risk of interference in the region is.")

with tab2:
    st.write("The weather station at Mt.Nyiro was installed as part of a field trip by a team of students, researchers, technical staff, and community liaisons.") 

    nyiromap=IMG.open("nyiromap.jpg")
    st.image(nyiromap)
    st.write("Mt. Nyiro (Ol dono Ng'iro) lies towards the south-east of Lake Turkana in northern Kenya. It is located in Samburu county and is in the territory of the samburu community. The samburu are traditionally pastorolists and this continues to be the major economic activity in the mountain and surrounding regions. Camels, goats and cows graze up to the very top of the mountain. Water scarcity is a big problem facing the community, with only a small stream originating in the mountain top. The area is semi-arid, though the mountain hosts diverse vegetation and is up to **10** degrees cooler at the top. The highest peak at Mt Nyiro has an altitude of 2848m." )
    st.subheader("Community engagement")
    st.write("A major part of the expedition was engagement with the community. Our expedition set off from the eastern side of the mountain where the Loongerin village is. Jacob Lekupe, a native of the village, was brought on as the community liasion for the project. He advised on the protocols for engaging the elders of the community, the resources needed to climb the mountain, arranged porters for carrying equipment up the mountain, and accompanied the team during the expedition.")
    st.write("Upon arrival, the team joined a community meeting with the elders in which we described our goals and intentions, and asked for permission to climb the mountain and to leave our instrument at the peak. The elders - through their chief- set out their expectations of us, and shared their blessings. ")
        # tab21,tab22,tab23,tab24,tab25,tab26,tab27,tab28,tab29,tab210,tab211,tab212,tab213,tab214,tab215,tab216,tab217,tab218,tab219,tab220,tab221,tab222,tab223,tab224,tab225,tab226,tab227= st.tabs(["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27"])
        #tab21,tab22,tab23,tab24,tab25,tab26,tab27,tab28 = st.tabs(["1","2","3","4","5","6","7","8"])
    tab21,tab22,tab23= st.tabs(["1","2","3"])
    st.subheader("Trek and installation")
    st.write(" The climb took between 7-11 hours, with equipment going up from 2 days before the day of the main hike. Almost 4 trips were made by porters to get all equipment up to the peak, including solar panels, the station's mast, and food and tents for the team. Camp was set up for 3 nights and installation was done within 2 days. Students took measurements of weather data on hand held devices as a test of current conditions. Once the mast was secured and the data logger attached with sensors, the solar panels were set up. This completed the installation and the team descended the following day.")
    with tab21:
        nyiro1=IMG.open("nyiro1.jpg")
        st.image(nyiro1)
        st.caption("From the summit of Mt. Nyiro")
    with tab22:
        nyiro1=IMG.open("nyiro2.jpg")
        st.image(nyiro1)    
        st.caption("Loongerin village")
    with tab23:
        nyiro1=IMG.open("nyiro3.jpg")
        st.image(nyiro1)
        st.caption("AirTurkana flight arriving with the team at Sedar airstrip,Samburu.")
        
with tab3:
    st.subheader("WRF Model")     
    st.write("The Weather Research and Forecast (WRF) model is an advanced mesoscale atmospheric model that can be run in 'nested' mode at very high resolution for limited areas of Earth. In this instance, we are using it to produce real-time weather forecasts, relevant for astronomers, nested at resolutions of 25km (whole of Kenya), 5km (county scale) and 1km (individual mountain peaks e.g. Ol Donyo Nyiro, Ol Donyo Mara, Mt Kenya) in order to elucidate atmospheric conditions forecast over the forthcoming 24-48hrs.")
    
with tab4:
    st.subheader("Slides from talks")
    
      
with tab5:
    st.subheader("Data")
    st.write('The data is visualized in a chart that shows hourly averages of the chosen parameters. The parameters are:')
    st.write('1. Temperature (K)')
    st.write('2. Relative Humidity (%)')
    st.write('3. Downward longwave radiation flux at the ground (W/m^2, downward is positive)')
    st.write('4. Total column-integrated water vapor and cloud variables (For EPCC model only)')
    st.write('5. Air Pressure (Pa)')
    st.write('6. Wind Speed (Knots)')
    st.write('7. Wind direction')
    st.write('Data from previous midnight to current time are taken from the weather station and predictive data is shown using the WRF met model forecast for an additional 24 hours ')
    
    st.subheader("Geographical Information System (GIS) Toolkit: Viewing the Data")
    st.write("Data from each station is available to view. Click on the relevant station to retrieve data (can take up to a minute to load).")
 
    images = []
    for file in ["wx1n.png", "wx2m.png","wx3k.png","wx4e.png"]:
        with open(file, "rb") as image:
            encoded = base64.b64encode(image.read()).decode()
            images.append(f"data:image/jpeg;base64,{encoded}")

    clicked = clickable_images(
        images,
        titles=[f"Image #{str(i)}" for i in range(len(images))],
        div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
        img_style={"margin": "0px", "height": "250px", "width":"250"},
    )

    if clicked ==0:
        with st.spinner("Please wait"):
            st.write("Mt Nyiro Data vis will appear here")

            # def start_capture():
            #     subprocess.run(["python", "arrowsmag.py"])
                
            # start_capture()
    if clicked ==1:
        with st.spinner("Please wait"):
            st.write("Mt.Mara data vis will appear here")

            # def start_capture():
            #     subprocess.run(["python", "arrowsmag.py"])
                
            # start_capture()
                            

    if clicked ==2:
        with st.spinner("Please wait"):

            def start_capture():
                subprocess.run(["python", "arrowsmag.py"])
                
            start_capture()
