# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 13:14:07 2024

@author: ekazu
"""

import pandas as pd
import plotly.express as px
import dash
from dash import dcc
from dash import html

# import airline data
airline_data = airline_data =  pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/airline_data.csv', 
                                           encoding = "ISO-8859-1",
                                           dtype={'Div1Airport': str, 'Div1TailNum': str, 
                                                  'Div2Airport': str, 'Div2TailNum': str})
# randomly sample 500 rows
data = airline_data.sample(n=500, random_state=42)

# create pie chart
fig = px.pie(data,
             names='DistanceGroup',
             values='Flights',
             title='Distance Group Proportion by Flights')

# create dash app
app = dash.Dash(__name__)

app.layout = html.Div(children=[html.H1('Airline Dashboard',
                                        style={'textAlign': 'center',
                                               'color': '#503D36',
                                               'font-size': 40}),
                                html.P('Proportion of Distance Group (250-mile distance interval group) by Flights',
                                       style={'textAlign': 'center',
                                              'color': '#F57241'}),
                                dcc.Graph(figure=fig)])

# run application
if __name__ == '__main__':
    app.run_server()