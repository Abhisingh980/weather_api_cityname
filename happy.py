import streamlit as st
import pandas as pd
import graph_function as gf

df = pd.read_csv("happy.csv")
columns_x = list(df.columns)
columns_y = []

st.title("In search for Happiness ")

option1 = st.selectbox("select the data for the X-axis",
                       columns_x, help="select any one of them", placeholder="select from given", index=None)

if option1 is not None:
    index = columns_x.index(option1)
    item = columns_x[index]
    for list_item in columns_x:
        if list_item != item:
            columns_y.append(list_item)
option2 = st.selectbox("select the data for the Y-axis",
                       columns_y, help="select any one of them", placeholder="select from given", index=None, )

st.subheader(f"you selected x-axis {option1} and y-axis {option2}")
if option1 and option2:
    figure = gf.plot_graph(option1, option2)
    st.plotly_chart(figure)
