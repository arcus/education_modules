from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc

hidden_filtered_modules = html.Div(children=[dcc.Markdown("this is where we will hide the list of modules so it is always in one place")
    ], 
    id = 'hidden_filtered_modules_list', 
    style= {'display': 'none'} # make this 'none' to hide it for final version, 'block' shows this data on the app
    )