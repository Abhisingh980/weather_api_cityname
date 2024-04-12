from os import times
from sys import modules
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import backend_weather as bw
import datetime as dt
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
import numpy as np


# import of city data to better expreance on seach the city
city_name = pd.read_csv("/Users/abhisingh/Downloads/weather_api_cityname/simplemaps_worldcities_basicv1/worldcities.csv",usecols=['city'])

# city dataframe consider  city column
city_name = city_name.sort_values('city',axis=0,kind='meargesort')

st.set_page_config(page_title="Weather Forcast", page_icon="🌦️", layout="wide")

city_name_list = [i for i in city_name['city']]
st.title("weather forcast for the next days".title())
place = st.selectbox(label="Select A City Name" ,options=city_name_list,
    placeholder="Enter A City Name",index=None,kwargs={'color':'red'})

if place is not None:
    frequency = st.slider("forcast days", min_value=1, max_value=5,
                          help="select the number of forcast days")

    option = st.selectbox("select the data to view",
                          ("Temperature", "sky"))

    st.subheader(f"{option} for the next {frequency} days in {place}")
    data, date, sky_dict = bw.get_detail(place, frequency)
    if date:
        if option in "Temperature":
# convert acording to no of temperature value
# / 10 for floting point for better understandin
            temperature = [data[index]['temp'] for index in range(len(data))]
            temperature = [temperature[i] / 10 for i in range(len(data))]
            temperature = [round(i,2) for i in temperature]
            print(temperature)
            #print(temperature)

# remove only day and time from the date
            date = [dt.datetime.strptime(i, '%Y-%m-%d %H:%M:%S').strftime('%d %H:%M:%S') for i in date]

#convert data into data fram to plot the graph for better calculation
            data_plot = pd.DataFrame({'date': date, 'temperature': temperature})

            fig, ax = plt.subplots(figsize=(20, 10))

            sns.set_style(style='darkgrid',rc={'axes.facecolor':'#fadfca','figure.facecolor':'#0ee39f'})
# plot the graph
            sns.lineplot(data_plot,x='date', y='temperature', marker='o',ax=ax,hue=temperature,
                         linestyle=":",markersize=15,markeredgecolor='black',palette='plasma',
                         )

            ax.set(xlabel='Date', ylabel='Temperature (c)',title='Temperature for the next days',
                ylim=[min(data_plot['temperature'])-0.3,max(data_plot['temperature'])+0.5],adjustable='datalim',mouseover=True,)
# min of temperature dat and max of temperature data

            ax.legend(loc='upper right',bbox_to_anchor=(1.1,1),fontsize=15,shadow=True,
                facecolor='white',edgecolor='black',title='Temperature',title_fontsize=20,
                labelspacing=1.2,ncol=1)

# perform some operation on axises
            l = ['top', 'right']
            b = ['bottom', 'left']
            for i,j in zip(l,b):
                ax.spines[j].set_color('red')
                ax.spines[i].set_visible(False)

            plt.xticks(rotation=45,fontsize=12,fontweight='bold',color='red')
            plt.yticks(fontsize=12,fontweight='bold',color='blue')

# set the title color to blue and font size to 20 and font weight to bold
            ax.title.set_color('#000000')
            ax.title.set_fontsize(30)
            ax.title.set_fontweight('bold')

# set the xlabe; color to red and font size to 15 and font weight to bold
            ax.xaxis.label.set_color('white')
            ax.xaxis.label.set_fontsize(20)
            ax.xaxis.label.set_fontweight('bold')

# ylabel set the color to blue and font size to 15 and font weight to bold
            ax.yaxis.label.set_color('blue')
            ax.yaxis.label.set_fontsize(20)
            ax.yaxis.label.set_fontweight('bold')

# final plot of grapgh is hear

            st.pyplot(fig,clear_figure=True,use_container_width=True)

        else:
            # heat map for the sky
            humidity = [str(data[index]['humidity']) for index in range(len(data))]
            pressure = [str(data[index]['pressure']) for index in range(len(data))]

            hp = pd.DataFrame({'Humidity':humidity,'Pressure':pressure})
            hp = hp.corr()

            sky = [value[0]['description'] for value in sky_dict]
            sky.append(humidity)
            encode = TransactionEncoder()
            encode_data = encode.fit_transform(sky)
            sky_data = pd.DataFrame(encode_data, columns=encode.columns_)
            sky_data = sky_data.corr()
            # mearge sky_data and humidity
            fig, ax = plt.subplots(figsize=(20, 10))
            sns.set_style(style='darkgrid',rc={'axes.facecolor':'#fadfca','figure.facecolor':'#0ee39f'})
            sns.heatmap(hp, ax=ax, cmap='plasma')
            ax.set(title='pressure and humidity')
            ax.title.set_color('#000000')
            ax.title.set_fontsize(30)
            ax.title.set_fontweight('bold')
            ax.xaxis.label.set_color('white')
            ax.xaxis.label.set_fontsize(20)
            ax.xaxis.label.set_fontweight('bold')
            ax.yaxis.label.set_color('blue')
            ax.yaxis.label.set_fontsize(20)
            ax.yaxis.label.set_fontweight('bold')
            st.pyplot(fig,clear_figure=True,use_container_width=True)



    else:
        st.write(data.title())
