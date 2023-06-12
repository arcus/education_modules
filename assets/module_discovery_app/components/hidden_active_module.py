from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc

hidden_active_module = [#dcc.Markdown("current active node"),
    html.Div(children=["dummy"], 
    id = 'hidden_active_module', 
    style= {'display': 'none'} # make this 'none' to hide it for final version, 'block' shows this data on the app
    )]