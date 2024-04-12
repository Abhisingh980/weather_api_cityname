from os import times
from sys import modules
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import backend_weather as bw
import datetime as dt
import pandas as pd

st.set_page_config(page_title="Weather Forcast", page_icon="🌦️", layout="wide")

st.title("weather forcast for the next days".title())
place = st.text_input("place:", placeholder="Enter A City Name")
if place:
    frequency = st.slider("forcast days", min_value=1, max_value=5,
                          help="select the number of forcast days")

    option = st.selectbox("select the data to view",
                          ("Temperature", "sky"))

    st.subheader(f"{option} for the next {frequency} days in {place}")
    data, date, sky_dict = bw.get_detail(place, frequency)
    if date:
        if option in "Temperature":
            temperature = [data[index]['temp'] for index in range(len(data))]
            temperature = [temperature[i] / 10 for i in range(len(data))]

            # remove only day and time from the date
            date = [dt.datetime.strptime(i, '%Y-%m-%d %H:%M:%S').strftime('%d %H:%M:%S') for i in date]

            #convert data into data fram to plot the graph for better calculation
            data_plot = pd.DataFrame({'date': date, 'temperature': temperature})

            fig, ax = plt.subplots(figsize=(10, 8))

            sns.set_style(style='darkgrid',rc={'axes.facecolor':'#b8eb9b','figure.facecolor':'#0ee39f'})

            sns.lineplot(data_plot,x='date', y='temperature', marker='o',ax=ax,hue=temperature,
                         linestyle="-",linewidth=5,markersize=10,markeredgecolor='black',palette='plasma',
                         )

            ax.set(xlabel='Date', ylabel='Temperature (c)',title='Temperature for the next days',
                ylim=[min(data_plot['temperature'])-0.3,max(data_plot['temperature'])+0.5],adjustable='datalim',mouseover=True,)
            # min of temperature dat and max of temperature data

            ax.legend(loc='upper right',bbox_to_anchor=(1.3,1),fontsize=15,shadow=True,
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

            st.pyplot(fig,clear_figure=True,use_container_width=True)

        else:
            sky_type = [sky_dict[index][0]['main'] for index in range(len(data))]
            sky_description = [sky_dict[index][0]['description'] for index in range(len(data))]
            image_name = {"Clouds": "image/cloudy.jpg", "Rain": "image/rain.jpg",
                          "Snow": "image/snow.jpeg", "Clear": "image/clear.png"}
            sky = []
            for image in sky_type:
                sky.append(image_name[image])

            st.image(sky, caption=sky_description, width=200)
    else:
        st.write(data.title())
