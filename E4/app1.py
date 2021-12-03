from seaborn.palettes import color_palette
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
sns.set_style("darkgrid")
st.title("Visualizador de defunciones por regiones, Chile (2010 - 2021)")
df = pd.read_csv("https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto32/Defunciones.csv")
region_seleccionada = st.radio("Seleccione una región:", df.Region.unique())
filtroregion=df[(df.Region==region_seleccionada)]
año_seleccionado = st.slider('Seleccione un año:',value=2010,min_value = 2010, max_value = 2021, step = 1)
st.write("Año seleccionado:", año_seleccionado)
if año_seleccionado==2010:
    if region_seleccionada=='Antofagasta':
        colporaño = (df.iloc[0:8,4:369])
    elif region_seleccionada=='Arica y Parinacota':
        colporaño = (df.iloc[8:12,4:369])
    elif region_seleccionada=='Atacama':
        colporaño = (df.iloc[12:21,4:369])
    elif region_seleccionada=='Aysén del General Carlos Ibáñez del Campo':
        colporaño = (df.iloc[21:31,4:369])
    elif region_seleccionada=='Biobío':
        colporaño = (df.iloc[31:64,4:369])
    elif region_seleccionada=='Coquimbo':
        colporaño = (df.iloc[64:79,4:369])
    elif region_seleccionada=='La Araucanía':
        colporaño = (df.iloc[79:111,4:369])
    elif region_seleccionada=='La Araucanía':
        colporaño = (df.iloc[79:111,4:369])
    elif region_seleccionada=="Libertador General Bernardo O'Higgins":
        colporaño = (df.iloc[111:143,4:369])
    elif region_seleccionada=='Los Lagos':
        colporaño = (df.iloc[143:173,4:369])
    elif region_seleccionada=='Los Ríos':
        colporaño = (df.iloc[173:185,4:369])
    elif region_seleccionada=='Magallanes y de la Antártica Chilena':
        colporaño = (df.iloc[185:190,4:369])
    elif region_seleccionada=='Maule':
        colporaño = (df.iloc[190:220,4:369])
    elif region_seleccionada=='Metropolitana de Santiago':
        colporaño = (df.iloc[220:272,4:369])
    elif region_seleccionada=='Tarapacá':
        colporaño = (df.iloc[272:279,4:369])
    elif region_seleccionada=='Valparaíso':
        colporaño = (df.iloc[279:316,4:369])
    elif region_seleccionada=='Ñuble':
        colporaño = (df.iloc[316:336,4:369])
elif año_seleccionado==2011:
    if region_seleccionada=='Antofagasta':
        colporaño = (df.iloc[0:8,369:734])
    elif region_seleccionada=='Arica y Parinacota':
        colporaño = (df.iloc[8:12,369:734])
    elif region_seleccionada=='Atacama':
        colporaño = (df.iloc[12:21,369:734])
    elif region_seleccionada=='Aysén del General Carlos Ibáñez del Campo':
        colporaño = (df.iloc[21:31,369:734])
    elif region_seleccionada=='Biobío':
        colporaño = (df.iloc[31:64,369:734])
    elif region_seleccionada=='Coquimbo':
        colporaño = (df.iloc[64:79,369:734])
    elif region_seleccionada=='La Araucanía':
        colporaño = (df.iloc[79:111,369:734])
    elif region_seleccionada=='La Araucanía':
        colporaño = (df.iloc[79:111,369:734])
    elif region_seleccionada=="Libertador General Bernardo O'Higgins":
        colporaño = (df.iloc[111:143,369:734])
    elif region_seleccionada=='Los Lagos':
        colporaño = (df.iloc[143:173,369:734])
    elif region_seleccionada=='Los Ríos':
        colporaño = (df.iloc[173:185,369:734])
    elif region_seleccionada=='Magallanes y de la Antártica Chilena':
        colporaño = (df.iloc[185:190,369:734])
    elif region_seleccionada=='Maule':
        colporaño = (df.iloc[190:220,369:734])
    elif region_seleccionada=='Metropolitana de Santiago':
        colporaño = (df.iloc[220:272,369:734])
    elif region_seleccionada=='Tarapacá':
        colporaño = (df.iloc[272:279,369:734])
    elif region_seleccionada=='Valparaíso':
        colporaño = (df.iloc[279:316,369:734])
    elif region_seleccionada=='Ñuble':
        colporaño = (df.iloc[316:336,369:734])
elif año_seleccionado==2012:
    if region_seleccionada=='Antofagasta':
        colporaño = (df.iloc[0:8,734:1100])
    elif region_seleccionada=='Arica y Parinacota':
        colporaño = (df.iloc[8:12,734:1100])
    elif region_seleccionada=='Atacama':
        colporaño = (df.iloc[12:21,734:1100])
    elif region_seleccionada=='Aysén del General Carlos Ibáñez del Campo':
        colporaño = (df.iloc[21:31,734:1100])
    elif region_seleccionada=='Biobío':
        colporaño = (df.iloc[31:64,734:1100])
    elif region_seleccionada=='Coquimbo':
        colporaño = (df.iloc[64:79,734:1100])
    elif region_seleccionada=='La Araucanía':
        colporaño = (df.iloc[79:111,734:1100])
    elif region_seleccionada=='La Araucanía':
        colporaño = (df.iloc[79:111,734:1100])
    elif region_seleccionada=="Libertador General Bernardo O'Higgins":
        colporaño = (df.iloc[111:143,734:1100])
    elif region_seleccionada=='Los Lagos':
        colporaño = (df.iloc[143:173,734:1100])
    elif region_seleccionada=='Los Ríos':
        colporaño = (df.iloc[173:185,734:1100])
    elif region_seleccionada=='Magallanes y de la Antártica Chilena':
        colporaño = (df.iloc[185:190,734:1100])
    elif region_seleccionada=='Maule':
        colporaño = (df.iloc[190:220,734:1100])
    elif region_seleccionada=='Metropolitana de Santiago':
        colporaño = (df.iloc[220:272,734:1100])
    elif region_seleccionada=='Tarapacá':
        colporaño = (df.iloc[272:279,734:1100])
    elif region_seleccionada=='Valparaíso':
        colporaño = (df.iloc[279:316,734:1100])
    elif region_seleccionada=='Ñuble':
        colporaño = (df.iloc[316:336,734:1100])
elif año_seleccionado==2013:
    if region_seleccionada=='Antofagasta':
        colporaño = (df.iloc[0:8,1100:1465])
    elif region_seleccionada=='Arica y Parinacota':
        colporaño = (df.iloc[8:12,1100:1465])
    elif region_seleccionada=='Atacama':
        colporaño = (df.iloc[12:21,1100:1465])
    elif region_seleccionada=='Aysén del General Carlos Ibáñez del Campo':
        colporaño = (df.iloc[21:31,1100:1465])
    elif region_seleccionada=='Biobío':
        colporaño = (df.iloc[31:64,1100:1465])
    elif region_seleccionada=='Coquimbo':
        colporaño = (df.iloc[64:79,1100:1465])
    elif region_seleccionada=='La Araucanía':
        colporaño = (df.iloc[79:111,1100:1465])
    elif region_seleccionada=='La Araucanía':
        colporaño = (df.iloc[79:111,1100:1465])
    elif region_seleccionada=="Libertador General Bernardo O'Higgins":
        colporaño = (df.iloc[111:143,1100:1465])
    elif region_seleccionada=='Los Lagos':
        colporaño = (df.iloc[143:173,1100:1465])
    elif region_seleccionada=='Los Ríos':
        colporaño = (df.iloc[173:185,1100:1465])
    elif region_seleccionada=='Magallanes y de la Antártica Chilena':
        colporaño = (df.iloc[185:190,1100:1465])
    elif region_seleccionada=='Maule':
        colporaño = (df.iloc[190:220,1100:1465])
    elif region_seleccionada=='Metropolitana de Santiago':
        colporaño = (df.iloc[220:272,1100:1465])
    elif region_seleccionada=='Tarapacá':
        colporaño = (df.iloc[272:279,1100:1465])
    elif region_seleccionada=='Valparaíso':
        colporaño = (df.iloc[279:316,1100:1465])
    elif region_seleccionada=='Ñuble':
        colporaño = (df.iloc[316:336,1100:1465])
elif año_seleccionado==2014:
    if region_seleccionada=='Antofagasta':
        colporaño = (df.iloc[0:8,1465:1830])
    elif region_seleccionada=='Arica y Parinacota':
        colporaño = (df.iloc[8:12,1465:1830])
    elif region_seleccionada=='Atacama':
        colporaño = (df.iloc[12:21,1465:1830])
    elif region_seleccionada=='Aysén del General Carlos Ibáñez del Campo':
        colporaño = (df.iloc[21:31,1465:1830])
    elif region_seleccionada=='Biobío':
        colporaño = (df.iloc[31:64,1465:1830])
    elif region_seleccionada=='Coquimbo':
        colporaño = (df.iloc[64:79,1465:1830])
    elif region_seleccionada=='La Araucanía':
        colporaño = (df.iloc[79:111,1465:1830])
    elif region_seleccionada=='La Araucanía':
        colporaño = (df.iloc[79:111,1465:1830])
    elif region_seleccionada=="Libertador General Bernardo O'Higgins":
        colporaño = (df.iloc[111:143,1465:1830])
    elif region_seleccionada=='Los Lagos':
        colporaño = (df.iloc[143:173,1465:1830])
    elif region_seleccionada=='Los Ríos':
        colporaño = (df.iloc[173:185,1465:1830])
    elif region_seleccionada=='Magallanes y de la Antártica Chilena':
        colporaño = (df.iloc[185:190,1465:1830])
    elif region_seleccionada=='Maule':
        colporaño = (df.iloc[190:220,1465:1830])
    elif region_seleccionada=='Metropolitana de Santiago':
        colporaño = (df.iloc[220:272,1465:1830])
    elif region_seleccionada=='Tarapacá':
        colporaño = (df.iloc[272:279,1465:1830])
    elif region_seleccionada=='Valparaíso':
        colporaño = (df.iloc[279:316,1465:1830])
    elif region_seleccionada=='Ñuble':
        colporaño = (df.iloc[316:336,1465:1830])
elif año_seleccionado==2015:
    if region_seleccionada=='Antofagasta':
        colporaño = (df.iloc[0:8,1830:2195])
    elif region_seleccionada=='Arica y Parinacota':
        colporaño = (df.iloc[8:12,1830:2195])
    elif region_seleccionada=='Atacama':
        colporaño = (df.iloc[12:21,1830:2195])
    elif region_seleccionada=='Aysén del General Carlos Ibáñez del Campo':
        colporaño = (df.iloc[21:31,1830:2195])
    elif region_seleccionada=='Biobío':
        colporaño = (df.iloc[31:64,1830:2195])
    elif region_seleccionada=='Coquimbo':
        colporaño = (df.iloc[64:79,1830:2195])
    elif region_seleccionada=='La Araucanía':
        colporaño = (df.iloc[79:111,1830:2195])
    elif region_seleccionada=='La Araucanía':
        colporaño = (df.iloc[79:111,1830:2195])
    elif region_seleccionada=="Libertador General Bernardo O'Higgins":
        colporaño = (df.iloc[111:143,1830:2195])
    elif region_seleccionada=='Los Lagos':
        colporaño = (df.iloc[143:173,1830:2195])
    elif region_seleccionada=='Los Ríos':
        colporaño = (df.iloc[173:185,1830:2195])
    elif region_seleccionada=='Magallanes y de la Antártica Chilena':
        colporaño = (df.iloc[185:190,1830:2195])
    elif region_seleccionada=='Maule':
        colporaño = (df.iloc[190:220,1830:2195])
    elif region_seleccionada=='Metropolitana de Santiago':
        colporaño = (df.iloc[220:272,1830:2195])
    elif region_seleccionada=='Tarapacá':
        colporaño = (df.iloc[272:279,1830:2195])
    elif region_seleccionada=='Valparaíso':
        colporaño = (df.iloc[279:316,1830:2195])
    elif region_seleccionada=='Ñuble':
        colporaño = (df.iloc[316:336,1830:2195])
elif año_seleccionado==2016:
    if region_seleccionada=='Antofagasta':
        colporaño = (df.iloc[0:8,2195:2560])
    elif region_seleccionada=='Arica y Parinacota':
        colporaño = (df.iloc[8:12,2195:2560])
    elif region_seleccionada=='Atacama':
        colporaño = (df.iloc[12:21,2195:2560])
    elif region_seleccionada=='Aysén del General Carlos Ibáñez del Campo':
        colporaño = (df.iloc[21:31,2195:2560])
    elif region_seleccionada=='Biobío':
        colporaño = (df.iloc[31:64,2195:2560])
    elif region_seleccionada=='Coquimbo':
        colporaño = (df.iloc[64:79,2195:2560])
    elif region_seleccionada=='La Araucanía':
        colporaño = (df.iloc[79:111,2195:2560])
    elif region_seleccionada=='La Araucanía':
        colporaño = (df.iloc[79:111,2195:2560])
    elif region_seleccionada=="Libertador General Bernardo O'Higgins":
        colporaño = (df.iloc[111:143,2195:2560])
    elif region_seleccionada=='Los Lagos':
        colporaño = (df.iloc[143:173,2195:2560])
    elif region_seleccionada=='Los Ríos':
        colporaño = (df.iloc[173:185,2195:2560])
    elif region_seleccionada=='Magallanes y de la Antártica Chilena':
        colporaño = (df.iloc[185:190,2195:2560])
    elif region_seleccionada=='Maule':
        colporaño = (df.iloc[190:220,2195:2560])
    elif region_seleccionada=='Metropolitana de Santiago':
        colporaño = (df.iloc[220:272,2195:2560])
    elif region_seleccionada=='Tarapacá':
        colporaño = (df.iloc[272:279,2195:2560])
    elif region_seleccionada=='Valparaíso':
        colporaño = (df.iloc[279:316,2195:2560])
    elif region_seleccionada=='Ñuble':
        colporaño = (df.iloc[316:336,2195:2560])
elif año_seleccionado==2017:
    if region_seleccionada=='Antofagasta':
        colporaño = (df.iloc[0:8,2560:2925])
    elif region_seleccionada=='Arica y Parinacota':
        colporaño = (df.iloc[8:12,2560:2925])
    elif region_seleccionada=='Atacama':
        colporaño = (df.iloc[12:21,2560:2925])
    elif region_seleccionada=='Aysén del General Carlos Ibáñez del Campo':
        colporaño = (df.iloc[21:31,2560:2925])
    elif region_seleccionada=='Biobío':
        colporaño = (df.iloc[31:64,2560:2925])
    elif region_seleccionada=='Coquimbo':
        colporaño = (df.iloc[64:79,2560:2925])
    elif region_seleccionada=='La Araucanía':
        colporaño = (df.iloc[79:111,2560:2925])
    elif region_seleccionada=='La Araucanía':
        colporaño = (df.iloc[79:111,2560:2925])
    elif region_seleccionada=="Libertador General Bernardo O'Higgins":
        colporaño = (df.iloc[111:143,2560:2925])
    elif region_seleccionada=='Los Lagos':
        colporaño = (df.iloc[143:173,2560:2925])
    elif region_seleccionada=='Los Ríos':
        colporaño = (df.iloc[173:185,2560:2925])
    elif region_seleccionada=='Magallanes y de la Antártica Chilena':
        colporaño = (df.iloc[185:190,2560:2925])
    elif region_seleccionada=='Maule':
        colporaño = (df.iloc[190:220,2560:2925])
    elif region_seleccionada=='Metropolitana de Santiago':
        colporaño = (df.iloc[220:272,2560:2925])
    elif region_seleccionada=='Tarapacá':
        colporaño = (df.iloc[272:279,2560:2925])
    elif region_seleccionada=='Valparaíso':
        colporaño = (df.iloc[279:316,2560:2925])
    elif region_seleccionada=='Ñuble':
        colporaño = (df.iloc[316:336,2560:2925])
elif año_seleccionado==2018:
    if region_seleccionada=='Antofagasta':
        colporaño = (df.iloc[0:8,2925:3290])
    elif region_seleccionada=='Arica y Parinacota':
        colporaño = (df.iloc[8:12,2925:3290])
    elif region_seleccionada=='Atacama':
        colporaño = (df.iloc[12:21,2925:3290])
    elif region_seleccionada=='Aysén del General Carlos Ibáñez del Campo':
        colporaño = (df.iloc[21:31,2925:3290])
    elif region_seleccionada=='Biobío':
        colporaño = (df.iloc[31:64,2925:3290])
    elif region_seleccionada=='Coquimbo':
        colporaño = (df.iloc[64:79,2925:3290])
    elif region_seleccionada=='La Araucanía':
        colporaño = (df.iloc[79:111,2925:3290])
    elif region_seleccionada=='La Araucanía':
        colporaño = (df.iloc[79:111,2925:3290])
    elif region_seleccionada=="Libertador General Bernardo O'Higgins":
        colporaño = (df.iloc[111:143,2925:3290])
    elif region_seleccionada=='Los Lagos':
        colporaño = (df.iloc[143:173,2925:3290])
    elif region_seleccionada=='Los Ríos':
        colporaño = (df.iloc[173:185,2925:3290])
    elif region_seleccionada=='Magallanes y de la Antártica Chilena':
        colporaño = (df.iloc[185:190,2925:3290])
    elif region_seleccionada=='Maule':
        colporaño = (df.iloc[190:220,2925:3290])
    elif region_seleccionada=='Metropolitana de Santiago':
        colporaño = (df.iloc[220:272,2925:3290])
    elif region_seleccionada=='Tarapacá':
        colporaño = (df.iloc[272:279,2925:3290])
    elif region_seleccionada=='Valparaíso':
        colporaño = (df.iloc[279:316,2925:3290])
    elif region_seleccionada=='Ñuble':
        colporaño = (df.iloc[316:336,2925:3290])
elif año_seleccionado==2019:
    if region_seleccionada=='Antofagasta':
        colporaño = (df.iloc[0:8,3290:3655])
    elif region_seleccionada=='Arica y Parinacota':
        colporaño = (df.iloc[8:12,3290:3655])
    elif region_seleccionada=='Atacama':
        colporaño = (df.iloc[12:21,3290:3655])
    elif region_seleccionada=='Aysén del General Carlos Ibáñez del Campo':
        colporaño = (df.iloc[21:31,3290:3655])
    elif region_seleccionada=='Biobío':
        colporaño = (df.iloc[31:64,3290:3655])
    elif region_seleccionada=='Coquimbo':
        colporaño = (df.iloc[64:79,3290:3655])
    elif region_seleccionada=='La Araucanía':
        colporaño = (df.iloc[79:111,3290:3655])
    elif region_seleccionada=='La Araucanía':
        colporaño = (df.iloc[79:111,3290:3655])
    elif region_seleccionada=="Libertador General Bernardo O'Higgins":
        colporaño = (df.iloc[111:143,3290:3655])
    elif region_seleccionada=='Los Lagos':
        colporaño = (df.iloc[143:173,3290:3655])
    elif region_seleccionada=='Los Ríos':
        colporaño = (df.iloc[173:185,3290:3655])
    elif region_seleccionada=='Magallanes y de la Antártica Chilena':
        colporaño = (df.iloc[185:190,3290:3655])
    elif region_seleccionada=='Maule':
        colporaño = (df.iloc[190:220,3290:3655])
    elif region_seleccionada=='Metropolitana de Santiago':
        colporaño = (df.iloc[220:272,3290:3655])
    elif region_seleccionada=='Tarapacá':
        colporaño = (df.iloc[272:279,3290:3655])
    elif region_seleccionada=='Valparaíso':
        colporaño = (df.iloc[279:316,3290:3655])
    elif region_seleccionada=='Ñuble':
        colporaño = (df.iloc[316:336,3290:3655])
elif año_seleccionado==2020:
    if region_seleccionada=='Antofagasta':
        colporaño = (df.iloc[0:8,3655:4020])
    elif region_seleccionada=='Arica y Parinacota':
        colporaño = (df.iloc[8:12,3655:4020])
    elif region_seleccionada=='Atacama':
        colporaño = (df.iloc[12:21,3655:4020])
    elif region_seleccionada=='Aysén del General Carlos Ibáñez del Campo':
        colporaño = (df.iloc[21:31,3655:4020])
    elif region_seleccionada=='Biobío':
        colporaño = (df.iloc[31:64,3655:4020])
    elif region_seleccionada=='Coquimbo':
        colporaño = (df.iloc[64:79,3655:4020])
    elif region_seleccionada=='La Araucanía':
        colporaño = (df.iloc[79:111,3655:4020])
    elif region_seleccionada=='La Araucanía':
        colporaño = (df.iloc[79:111,3655:4020])
    elif region_seleccionada=="Libertador General Bernardo O'Higgins":
        colporaño = (df.iloc[111:143,3655:4020])
    elif region_seleccionada=='Los Lagos':
        colporaño = (df.iloc[143:173,3655:4020])
    elif region_seleccionada=='Los Ríos':
        colporaño = (df.iloc[173:185,3655:4020])
    elif region_seleccionada=='Magallanes y de la Antártica Chilena':
        colporaño = (df.iloc[185:190,3655:4020])
    elif region_seleccionada=='Maule':
        colporaño = (df.iloc[190:220,3655:4020])
    elif region_seleccionada=='Metropolitana de Santiago':
        colporaño = (df.iloc[220:272,3655:4020])
    elif region_seleccionada=='Tarapacá':
        colporaño = (df.iloc[272:279,3655:4020])
    elif region_seleccionada=='Valparaíso':
        colporaño = (df.iloc[279:316,3655:4020])
    elif region_seleccionada=='Ñuble':
        colporaño = (df.iloc[316:336,3655:4020])
elif año_seleccionado==2021:
    if region_seleccionada=='Antofagasta':
        colporaño = (df.iloc[0:8,4020:4385])
    elif region_seleccionada=='Arica y Parinacota':
        colporaño = (df.iloc[8:12,4020:4385])
    elif region_seleccionada=='Atacama':
        colporaño = (df.iloc[12:21,4020:4385])
    elif region_seleccionada=='Aysén del General Carlos Ibáñez del Campo':
        colporaño = (df.iloc[21:31,4020:4385])
    elif region_seleccionada=='Biobío':
        colporaño = (df.iloc[31:64,4020:4385])
    elif region_seleccionada=='Coquimbo':
        colporaño = (df.iloc[64:79,4020:4385])
    elif region_seleccionada=='La Araucanía':
        colporaño = (df.iloc[79:111,4020:4385])
    elif region_seleccionada=='La Araucanía':
        colporaño = (df.iloc[79:111,4020:4385])
    elif region_seleccionada=="Libertador General Bernardo O'Higgins":
        colporaño = (df.iloc[111:143,4020:4385])
    elif region_seleccionada=='Los Lagos':
        colporaño = (df.iloc[143:173,4020:4385])
    elif region_seleccionada=='Los Ríos':
        colporaño = (df.iloc[173:185,4020:4385])
    elif region_seleccionada=='Magallanes y de la Antártica Chilena':
        colporaño = (df.iloc[185:190,4020:4385])
    elif region_seleccionada=='Maule':
        colporaño = (df.iloc[190:220,4020:4385])
    elif region_seleccionada=='Metropolitana de Santiago':
        colporaño = (df.iloc[220:272,4020:4385])
    elif region_seleccionada=='Tarapacá':
        colporaño = (df.iloc[272:279,4020:4385])
    elif region_seleccionada=='Valparaíso':
        colporaño = (df.iloc[279:316,4020:4385])
    elif region_seleccionada=='Ñuble':
        colporaño = (df.iloc[316:336,4020:4385])
st.table(colporaño)
fig,ax = plt.subplots()
to_plot = colporaño.iloc[:,0:-1]
ax.plot(to_plot.T)
ax.set_title(region_seleccionada)
ax.set_ylabel("Defunciones")
ax.set_xlabel("Fecha")
xs = np.arange(0,colporaño.shape[1]-2,30)
plt.xticks(xs,rotation=90)
st.pyplot(fig)