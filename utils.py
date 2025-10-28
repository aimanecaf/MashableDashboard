# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 09:46:23 2019

@author: aimanecaf
"""
from dash import html,dcc
#import dash_html_components as html
#import dash_core_components as dcc


def Header(app):
    return html.Div([get_header(app), html.Br([]), get_menu()])


def get_header(app):
    header = html.Div(
        [
            html.Div(
                [
                    html.Img(
                        src=app.get_asset_url("amse_logo.png"),
                        className="logo",
                    ),
                    html.A(
                        html.Button("On the data", id="learn-more-button"),
                        href="https://archive.ics.uci.edu/ml/datasets/Online+News+Popularity",
                        target='_blank'
                    ),
                ],
                className="row",
            ),
            html.Div(
                [
                    html.Div(
                        [html.H5("Online News Popularity Analysis for Mashable Articles")],
                        className="seven columns main-title",
                    ),
                    html.Div(
                        [
                            dcc.Link(
                                "Full View",
                                href="/amse-project/full-view",
                                className="full-view-link",
                            )
                        ],
                        className="five columns",
                    ),
                ],
                className="twelve columns",
                style={"padding-left": "0"},
            ),
        ],
        className="row",
    )
    return header


def get_menu():
    menu = html.Div(
        [
            dcc.Link(
                "Overview",
                href="/amse-project/overview",
                className="tab first",
            ),
            dcc.Link(
                "Shares",
                href="/amse-project/shares",
                className="tab",
            ),
            dcc.Link(
                "Methods",
                href="/amse-project/methods",
                className="tab",
            ),
        ],
        className="row all-tabs",
    )
    return menu


def make_dash_table(df):
    """ Return a dash definition of an HTML table for a Pandas dataframe """
    table = []
    for index, row in df.iterrows():
        html_row = []
        for i in range(len(row)):
            html_row.append(html.Td([row[i]]))
        table.append(html.Tr(html_row))
    return table