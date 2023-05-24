from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc

hidden_active_module = html.Div(children=[dcc.Markdown("this is where we hide the id of the single active module")
    ], 
    id = 'hidden_active_module', 
    style= {'display': 'block'} # make this 'none' to hide it for final version, 'block' shows this data on the app
    )