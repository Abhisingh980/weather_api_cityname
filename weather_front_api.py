import streamlit as st
#!pip install plotly
import plotly.express as px
import backend_weather as bw

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
            figure = px.line(x=date, y=temperature, labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)
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
