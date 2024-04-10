import random
import pandas as pd
#!pip install plotly
import plotly.express as px

plot_list = ['bar', 'bar_polar', 'density_heatmap', 'line', 'scatter', 'scatter_polar']


df = pd.read_csv("happy.csv")


def plot_graph(x_axis, y_axis):
    graph_name = plot_list[random.randint(0, len(plot_list)-1)]
    if graph_name in 'bar':
        figure = getattr(px, graph_name)(df, x=x_axis, y=y_axis, color=x_axis, height=550, hover_data=df.columns)
        return figure
    elif graph_name in 'bar_polar':
        figure = getattr(px, graph_name)(df, r=x_axis, theta=y_axis, color=y_axis, template="plotly_dark",
                                         color_discrete_sequence=px.colors.sequential.Plasma_r, hover_data=df.columns)
        figure = figure.update_layout(font_size=15,
                                      legend_font_size=14,
                                      polar_angularaxis_rotation=90)
        return figure
    elif graph_name in 'density_heatmap':
        figure = getattr(px, graph_name)(df, x=x_axis, y=y_axis, hover_data=df.columns, marginal_x="histogram",
                                         marginal_y="histogram", height=600)
        return figure
    elif graph_name in 'line':
        figure = getattr(px, graph_name)(df, x=x_axis, y=y_axis, hover_data=df.columns, height=600,
                                         color=x_axis, text=y_axis)
        return figure

    elif graph_name in 'scatter':
        figure = getattr(px, graph_name)(df, x=x_axis, y=y_axis, hover_data=df.columns, height=600,
                                         color=y_axis, symbol=x_axis)
        return figure
    else:
        if graph_name in 'scatter_polar':
            figure = getattr(px, graph_name)(df, r=x_axis, theta=y_axis, hover_data=df.columns, height=600,
                                             color=x_axis, symbol=y_axis, size=y_axis,
                                             color_discrete_sequence=px.colors.sequential.Plasma_r,
                                             template="plotly_dark")
            return figure
