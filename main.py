# importing dependencies
import pandas as pd
import streamlit as st
from PIL import Image
import csv
import math

# title for web app
st.write("""
# Efficient 911 Assists
""")
st.write('WEC 2021 | Stella Lee, Alexandria Lin, Isabel Higgon, Mahira Moftah')

# image for web app
image = Image.open('one.jpg')
st.image(image, use_column_width = True)

# co-ordinates of fire stations and hospitals
firestation1lat = 40.0137071
firestation1long = -75.3961213
firestation2lat = 40.0251013
firestation2long = -75.4490013
hospital1lat =  40.0514920
hospital1long = -75.3965480
hospital2lat = 40.0329254
hospital2long = -75.2750179

totalTimeF1=0
totalTimeF2=0
totalTimeH1=0
totalTimeH2=0

# import csv
series1 = pd.read_csv('WEC.csv')
with open('WEC.csv') as csvDataFile:
    data = list(csv.reader(csvDataFile))
    csvReader = csv.reader(csvDataFile)

option = st.sidebar.selectbox('Emergencies', ('All', 'EMS', 'Fire', 'Traffic'))

if option == 'All':
    # printing data
        for x in range(0, 135):
            if data[x][4] == 'EMS:':
                st.text(" * ")
                st.text("Time call was placed: " + str(data[x][6]))
                st.text("Type of emergency: " + str(data[x][5]))
                st.text("District: " + str(data[x][7]))
                distanceE1 = math.sqrt( ((hospital1lat-float(data[x][0]))**2)+((hospital1long-float(data[x][1]))**2) )*111
                distanceE2= math.sqrt( ((hospital2lat-float(data[x][0]))**2)+((hospital2long-float(data[x][1]))**2) )*111
                if distanceE1 > distanceE2:
                    st.text("Distance to Hospital (Hospital 1): "+ str(distanceE1)+ " km")
                    time = 7+4+2*distanceE1
                    st.text("Time to complete (in mins): " + str(time)+"\n\n")
                    totalTimeH1 = totalTimeH1 + time
                else:
                    st.text("Distance to Hospital (Hospital 2): "+ str(distanceE2) + " km")
                    time = 7+4+2*distanceE2
                    st.text("Time to complete (in mins): " + str(time)+"\n\n")
                    totalTimeH2 = totalTimeH2 + time

            elif data[x][4] == 'Fire:':
                st.text(" * ")
                st.text("Time call was placed: " + str(data[x][6]))
                st.text("Type of emergency: " + str(data[x][5]))
                st.text("District: " + str(data[x][7]))
                distanceF1 = math.sqrt( ((firestation1lat-float(data[x][0]))**2)+((firestation1long-float(data[x][1]))**2) )*111
                distanceF2= math.sqrt( ((firestation2lat-float(data[x][0]))**2)+((firestation2long-float(data[x][1]))**2) )*111
                if distanceF1 > distanceF2:
                    st.text("Distance to Fire Station (Fire Station 1): "+ str(distanceF1)+ " km")
                    time = 10+30+2*distanceF1/0.833
                    st.text("Time to complete (in mins): " + str(time)+"\n\n")
                    totalTimeF1 = totalTimeF1 + time
                else:
                    st.text("Distance to Fire Station (Fire Station 2): "+ str(distanceF2)+ " km")
                    time = 10+30+2*distanceF2/0.833
                    st.text("Time to complete (in mins): " + str(time)+"\n\n")
                    totalTimeF2 = totalTimeF2 + time

            elif data[x][4] == 'Traffic:':
                st.text(" * ")
                st.text("Time call was placed: " + str(data[x][6]))
                st.text("Type of emergency: " + str(data[x][5]))
                st.text("District: " + str(data[x][7]))
                distanceT1 = math.sqrt( ((hospital1lat-float(data[x][0]))**2)+((hospital1long-float(data[x][1]))**2) )*111
                distanceT2= math.sqrt( ((hospital2lat-float(data[x][0]))**2)+((hospital2long-float(data[x][1]))**2) )*111
                if distanceT1 > distanceT2:
                    st.text("Distance to Hospital (Hospital 1): "+ str(distanceT1)+ " km")
                    time = 7+4+2*distanceT1
                    st.text("Time to complete (in mins): " + str(time)+"\n\n")
                    totalTimeH1 = totalTimeH1 + time
                else:
                    st.text("Distance to Hospital (Hospital 2): "+ str(distanceT2)+ " km")
                    time = 7+4+2*distanceT2
                    st.text("Time to complete (in mins): " + str(time)+"\n\n")
                    totalTimeH2 = totalTimeH2 + time
                    
        if st.sidebar.button('Press to see total time spent for each location'):
            st.sidebar.write("Total time from start (Hospital 1): " + str(totalTimeH1) + " mins")
            st.sidebar.write("Total time from start (Hospital 2): " + str(totalTimeH2) + " mins")
            st.sidebar.write("Total time from start (Fire Station 1): " + str(totalTimeF1) + " mins")
            st.sidebar.write("Total time from start (Fire Station 2): " + str(totalTimeF2) + " mins")
                
                
if option == 'EMS':
    for x in range(0, 135):
        if data[x][4] == 'EMS:':
            st.text(" * ")
            st.text("Time call was placed: " + str(data[x][6]))
            st.text("Type of emergency: " + str(data[x][5]))
            st.text("District: " + str(data[x][7]))
            distanceE1 = math.sqrt( ((hospital1lat-float(data[x][0]))**2)+((hospital1long-float(data[x][1]))**2) )*111
            distanceE2= math.sqrt( ((hospital2lat-float(data[x][0]))**2)+((hospital2long-float(data[x][1]))**2) )*111
            if distanceE1 > distanceE2:
                st.text("Distance to Hospital (Hospital 1): "+ str(distanceE1)+ " km")
                time = 7+4+2*distanceE1
                st.text("Time to complete (in mins): " + str(time)+"\n\n")
            else:
                st.text("Distance to Hospital (Hospital 2): "+ str(distanceE2) + " km")
                time = 7+4+2*distanceE2
                st.text("Time to complete (in mins): " + str(time)+"\n\n")


if option == 'Fire':
    for x in range(0, 135):
        if data[x][4] == 'Fire:':
            st.text(" * ")
            st.text("Time call was placed: " + str(data[x][6]))
            st.text("Type of emergency: " + str(data[x][5]))
            st.text("District: " + str(data[x][7]))
            distanceF1 = math.sqrt(
                ((firestation1lat - float(data[x][0])) ** 2) + ((firestation1long - float(data[x][1])) ** 2)) * 111
            distanceF2 = math.sqrt(
                ((firestation2lat - float(data[x][0])) ** 2) + ((firestation2long - float(data[x][1])) ** 2)) * 111
            if distanceF1 > distanceF2:
                st.text("Distance to Fire Station (Fire Station 1): " + str(distanceF1) + " km")
                time = 10 + 30 + 2 * distanceF1 / 0.833
                st.text("Time to complete (in mins): " + str(time) + "\n\n")
            else:
                st.text("Distance to Fire Station (Fire Station 2): " + str(distanceF2) + " km")
                time = 10 + 30 + 2 * distanceF2 / 0.833
                st.text("Time to complete (in mins): " + str(time) + "\n\n")


if option == 'Traffic':
    for x in range(0, 135):
        if data[x][4] == 'Traffic:':
            st.text(" * ")
            st.text("Time call was placed: " + str(data[x][6]))
            st.text("Type of emergency: " + str(data[x][5]))
            st.text("District: " + str(data[x][7]))
            distanceT1 = math.sqrt(
                ((hospital1lat - float(data[x][0])) ** 2) + ((hospital1long - float(data[x][1])) ** 2)) * 111
            distanceT2 = math.sqrt(
                ((hospital2lat - float(data[x][0])) ** 2) + ((hospital2long - float(data[x][1])) ** 2)) * 111
            if distanceT1 > distanceT2:
                st.text("Distance to Hospital (Hospital 1): " + str(distanceT1) + " km")
                time = 7 + 4 + 2 * distanceT1
                st.text("Time to complete (in mins): " + str(time) + "\n\n")
            else:
                st.text("Distance to Hospital (Hospital 2): " + str(distanceT2) + " km")
                time = 7 + 4 + 2 * distanceT2
                st.text("Time to complete (in mins): " + str(time) + "\n\n")

st.text(' * ')

