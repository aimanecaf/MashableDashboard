# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 11:26:13 2019

@author: aimanecaf
"""
from dash import html,dcc
#import dash_core_components as dcc
#import dash_html_components as html
import plotly.graph_objs as go
from zipfile import ZipFile

from utils import Header, make_dash_table

import pandas as pd
import pathlib

#__file__ ='C:/Users/Aymane/Desktop/EBDS/Dash/app/pages/page_customers.py'
# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()

# Load ZipFile
zf = ZipFile(DATA_PATH.joinpath("uci-online-news-popularity-data-set.zip"))
online_news = pd.read_csv(zf.open('DATA_ONLINES.csv'), encoding='latin', low_memory=False)
table1 = round(online_news.groupby('Channel')['shares'].mean(),2).reset_index()
kpi1 = round(online_news['shares'].max(), 2)
kpi2 = round(online_news['shares'].mean(), 2)
a=online_news.groupby(['POPULARITY','Channel']).agg(
    {'shares': 'sum',
     }).reset_index()
import plotly.graph_objects as go

fig1 = go.Figure()
fig1.add_trace(go.Bar(
    x=a.loc[:5,'Channel'],
    y=a.loc[:5,'shares'],
    name='Popular',
    marker_color='indianred'
))
fig1.add_trace(go.Bar(
     x=a.loc[6:,'Channel'],
    y=a.loc[6:,'shares'],
    name='Unpopular',
    marker_color='lightsalmon'
))

# Here we modify the tickangle of the xaxis, resulting in rotated labels.
fig1.update_layout(barmode='group', xaxis_tickangle=-45,title_text='The number of shares per channel and popularity', title_x=0.5)



#values = table1['shares'].tolist()
#labels = table1['Channel'].tolist()
#fig1 = go.Figure([go.Bar(y=values, x=labels)])
a=online_news.groupby(by='month')['shares'].sum().reset_index()
a=pd.DataFrame(a)
a['id']=[4,8,12,2,1,7,6,3,5,11,10,9]
a=a.sort_values(by='id',ascending=True)
a.shape
a
import plotly.graph_objects as go
fig = go.Figure(data=go.Scatterpolar(
  r=round(a['shares'],2),
  theta=a['month'],
  fill='toself',marker_color='indianred',
    hovertemplate='Month : %{theta}<br>Number of shares : %{r}<extra></extra>'
))

fig.update_layout(
  polar=dict(
    radialaxis=dict(
      visible=True
    ),
  ),
  showlegend=False
)
fig.update_layout(title_text='Number of shares per month', title_x=0.5)
 
a=online_news.groupby(by='Date')['shares'].mean().reset_index()
a=pd.DataFrame(a)
a.shape
import plotly.express as px
import pandas as pd

fig2 = px.line(a, x='Date', y='shares',color_discrete_sequence=px.colors.qualitative.Set1)
fig2.update_layout(title_text='Evolution of the average number of shares per day', title_x=0.5)

#kpi_nb_unique_customers = customers['customer_unique_id'].nunique()
#kpi_nb_unique_customers_str = '{:,}'.format(kpi_nb_unique_customers).replace(',', ' ')

#kpi_nb_cities_covered = round((customers['customer_city'].unique().shape[0] / 5570 * 100), 1)
#kpi_nb_cities_covered_str = str(kpi_nb_cities_covered) + ' %'

#nb_customers_per_country = (
#    customers.drop_duplicates('customer_unique_id')['customer_state'].value_counts()
#)
#pct_customers_per_country = (
#    nb_customers_per_country.div(kpi_nb_unique_customers).mul(100).round(2).head(10)
#)
#
#tab_customers_per_country = (
#    nb_customers_per_country.head(10).reset_index().rename(columns={'index': 'country', 'customers_state': 'Nb customers'})
#)
#
#labels = pct_customers_per_country.index.tolist()
#values = pct_customers_per_country.tolist()
#colors = ['lightslategray',] * len(values)
#colors[0:3] = ['crimson'] * 3
#graph_pct_customers_per_country = go.Figure(
#    [
#        go.Bar(
#            x=labels, 
#            y=values,
#            text=values, 
#            textposition='auto',
#            marker_color=colors,
#        )
#    ]
#)
#graph_pct_customers_per_country.update_layout(
#    plot_bgcolor='rgb(255,255,255)',
#    paper_bgcolor='rgb(255,255,255)',
#    title_text='Top 10 customer provenance', 
#)

def create_layout(app):
    # Page layouts
    return html.Div(
        className="page",
        children=[
            html.Div(
                children=[
                    Header(app)
                ]
            ),
            # page 1
            html.Div(
                className="sub_page",
                children=[
                    # Row 1
                    html.Div(
                        className="row",
                        style={"margin-bottom": "35px"},
                        children=[
                            html.Div(
                                className="six columns",
                                children=[
                                    html.H6(
                                        children=["The average number of shares per channel"], 
                                        className="subtitle padded"
                                    ),
                                    html.Table(make_dash_table(table1)),
                                ],
                            ),
                            html.Div(
                                className="six columns",
                                children=[
                                    html.H6(
                                        "Key Performance Indicators",
                                        className="subtitle padded",
                                    ),
                                    html.Div(
                                        className='row',
                                        style={'margin': 'auto',
                                               'width': '50%',
                                               'border': '3px solid black',
                                               'background-color': 'lightsalmon',
                                               'padding': '10px',
                                               'text-align': 'center'
                                        },
                                        children=[
                                            html.H2(kpi1),
                                            html.P('Max of shares')
                                        ]
                                    ),
                                    html.Br([]),
                                    html.Div(
                                        className='row',
                                        style={'margin': 'auto',
                                               'width': '50%',
                                               'border': '3px solid black',
                                               'background-color': 'indianred',
                                               'padding': '10px',
                                               'text-align': 'center',
                                               
                                        },
                                        children=[
                                            html.H2(kpi2),
                                            html.P('Average of shares')
                                        ]
                                    ),
                                ],
                            ),
                        ],
                    ),
                    html.Div(
                        className="row",
                        style={"margin-bottom": "35px"},
                        children=[
                            html.Div(
                                className="twelve columns",
                                children=[
                                    html.H6(
                                        "The most widespread category at Mashable is World, and Technology with roughly 13 Million and 10 Million shares, respectively.",
                                        className="subtitle padded",
                                    ),
                                    dcc.Graph(
                                        id="graph-1",
                                        figure=fig1,
                                        config={"displayModeBar": False},
                                    ),
                                ],
                            ),
                        ],
                    ),
html.Div(
                        className="row",
                        style={"margin-bottom": "35px"},
                        children=[
                            html.Div(
                                className="twelve columns",
                                children=[
                                    html.H6(
                                        "The radar chart shows a monthly distribution according to the number of sharing of articles. We note that, for two years, the most shared articles were in October, with more than 5 million number of shares.",
                                        className="subtitle padded",
                                    ),
                                    dcc.Graph(
                                        id="graph-1",
                                        figure=fig,
                                        config={"displayModeBar": False},
                                    ),
                                ],
                            ),
                        ],
                    ),
                                        html.Div(
                        className="row",
                        style={"margin-bottom": "35px"},
                        children=[
                            html.Div(
                                className="twelve columns",
                                children=[
                                    html.H6(
                                        "Through this graph below, we can see the average evolution of the number of shares per day. We note the existence of fluctuations and a deterioration in the average number of sharing per day over time. After July 2014, we start to revolve around the range of 1000 to 2000 shares per day.",
                                        className="subtitle padded",
                                    ),
                                    dcc.Graph(
                                        id="graph-1",
                                        figure=fig2,
                                        config={"displayModeBar": False},
                                    ),
                                ],
                            ),
                        ],
                    ),
                ],
            ),
        ],
    )