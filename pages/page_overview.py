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

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()


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
                    # Row 3
                    html.Div(
                        className="row",
                        children=[
                            html.Div(
                                className="product",
                                children=[
                                    html.H5("Project Description"),
                                    html.Br([]),
                                    html.P(
                                        """
                                         Predicting the popularity of online information has remarkable practical values in many areas. For example, using the benefits of popularity prediction, news organizations can better understand the different types of online news consumption by users. As a result, the news organization can proactively deliver more relevant and engaging content, just as the organization can allocate resources more wisely to develop stories throughout their life cycle. It is in this context that this study is part of an analysis of the popularity of online news on behalf of Mashable.
                                        """,
                                        style={"color": "#ffffff"},
                                        className="row",
                                    ),
                                ],
                            )
                        ],
                    ),
                    # Row 4
                    html.Div(
                        className="row",
                        children=[
                            html.Div(
                                className="twelve columns",
                                children=[
                                    html.H6(["Project Summary"], className="subtitle"),
                                    html.Br([]),
                                    html.Div(
                                        className="fees",
                                        children=[
                                            html.Div(
                                                className="row",
                                                style={
                                                    "background-color": "#f9f9f9",
                                                    "padding-top": "20px",
                                                },
                                                children=[
                                                    html.Div(
                                                        className="three columns right-aligned",
                                                        children=[
                                                            html.Strong(
                                                                ["Project Title"],
                                                                style={"color": "#515151"},
                                                            )
                                                        ],
                                                    ),
                                                    html.Div(
                                                        className="nine columns",
                                                        children=[
                                                            html.P(
                                                                ["Online News Popularity Analysis for Mashable Articles"],
                                                                style={"color": "#7a7a7a"},
                                                            ),
     html.Img(
                        src=app.get_asset_url("Mashable.png"),
                        className="row",
                    ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            html.Div(
                                                className="row",
                                                style={"background-color": "#f9f9f9"},
                                                children=[
                                                    html.Div(
                                                        className="three columns right-aligned",
                                                        children=[
                                                            html.Strong(
                                                                ["Project Lead"],
                                                                style={"color": "#515151"},
                                                            )
                                                        ],
                                                    ),
                                                    html.Div(
                                                        className="nine columns",
                                                        children=[
                                                            html.P(
                                                                ["CAF Aimane"],
                                                                style={"color": "#7a7a7a"},
                                                            )
                                                        ],
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    html.Div(
                                        className="row",
                                        style={
                                            "background-color": "#f9f9f9",
                                            "padding-bottom": "30px",
                                        },
                                        children=[
                                            html.Div(
                                                className="three columns right-aligned",
                                                children=[
                                                    html.Strong(
                                                        ["Project Goal"],
                                                        style={"color": "#515151"},
                                                    )
                                                ],
                                            ),
                                            html.Div(
                                                className="nine columns",
                                                children=[
                                                    html.Strong(
                                                        ["Process"],
                                                        style={"color": "#515151"},
                                                    ),
                                                    html.P(
                                                        ["There was not a division of tasks, we tried to carry out each task jointly"],
                                                        style={"color": "#7a7a7a"},
                                                    ),
                                                    html.Br([]),
                                                    html.Strong(
                                                        ["Data"],
                                                        style={"color": "#515151"},
                                                    ),
                                                    html.P(
                                                        ["The data is provided by Fernandes, Vinagre and Cortez in 2015. They retrieved the news published by Mashable from the year 2013 to 2015. 39,644 articles in total were downloaded. They have obtained 60 features and 1 target (Number of shares) from these articles. For analysis purposes, we had created new variables and the target variable were categorized into two groups (Popular and Unpopular) based on the median."],
                                                        style={"color": "#7a7a7a"},
                                                    ),
                                                    html.Br([]),
                                                    html.Strong(
                                                        ["Goal"],
                                                        style={"color": "#515151"},
                                                    ),
                                                    html.P(
                                                        ["The objective of this project is to provide the Mashable site with a predictive model of the popularity of news before their publication."],
                                                        style={"color": "#7a7a7a"},
                                                    ),
                                                    html.Br([]),
                                                    html.Strong(
                                                        ["Techniques"],
                                                        style={"color": "#515151"},
                                                    ),
                                                    html.P(
                                                        ["In this work, we were interested in predicting the popularity of online news based on a set of their characteristics. In this context, we used parametric methods & those of machine learning. To take into account the problems related to dimensionality & multicollinearity, we performed regularized logistic regression based on Elastic Net, on GETS (General to Specific) & on Principal Component Analysis (PCA). The machine learning methods used are CART, bagging, Random Forest, K-Nearest Neighbors, Support Vector Machine & Neural networks. Each of the methods are evaluated on a test sample to evaluate & to compare each of the methods. The choice of the best method was made on the basis of the overall accuracy rate."],
                                                        style={"color": "#7a7a7a"},
                                                    ),
                                                    html.Br([]),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                            )
                        ],
                    ),                    
                ],
            ),
        ],
    )