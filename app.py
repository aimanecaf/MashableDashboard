

# Import required libraries

import pathlib
import dash
import pandas as pd
import plotly.graph_objs as go
from zipfile import ZipFile
from dash.dependencies import Input, Output, State
from dash import html,dcc
#import dash_core_components as dcc
#import dash_html_components as html
from pages import (
    page_methods,
    page_overview,
    page_shares,
)

# Multi-dropdown options

#__file__ = r'C:\Users\Aymane\Desktop\EBDS\Dash\app\app.py'

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("data").resolve()

app = dash.Dash(
    __name__, 
    meta_tags=[{"name": "viewport", "content": "width=device-width"}]
)
app.title = ('Mashable News Popularity Dashboard')


# Create global chart template
mapbox_access_token = "pk.eyJ1IjoiamFja2x1byIsImEiOiJjajNlcnh3MzEwMHZtMzNueGw3NWw5ZXF5In0.fk8k06T96Ml9CLGgKmk81w"
layout = dict(
    autosize=True,
    automargin=True,
    margin=dict(l=30, r=30, b=20, t=40),
    hovermode="closest",
    plot_bgcolor="#F9F9F9",
    paper_bgcolor="#F9F9F9",
    legend=dict(font=dict(size=10), orientation="h"),
    title="Satellite Overview",
    mapbox=dict(
        accesstoken=mapbox_access_token,
        style="light",
        center=dict(lon=-78.05, lat=42.54),
        zoom=7,
    ),
)

# Describe the layout/ UI of the app
app.layout = html.Div(
    children=[
        dcc.Location(id="url", refresh=False), 
        html.Div(id="page-content")
    ]
)

# Update page
@app.callback(
    Output("page-content", "children"), 
    [Input("url", "pathname")]
)
def display_page(pathname):
    if pathname == "/amse-project/overview":
        return page_overview.create_layout(app)
    if pathname == "/amse-project/shares":
        return page_shares.create_layout(app)
    if pathname == "/amse-project/methods":
        return page_methods.create_layout(app)
    if pathname == "/amse-project/full-view":
        return (
            page_overview.create_layout(app),
            page_shares.create_layout(app),
            page_methods.create_layout(app),
        )
    else:
        return page_overview.create_layout(app)

# Main
#app = dash.Dash(__name__)
server = app.server
app.config['suppress_callback_exceptions']=True
if __name__ == '__main__':
    app.run(debug=True)
#from waitress import serve
#from app import server #so "app" is the name of my Dash script I want to serve

#serve(server)
    