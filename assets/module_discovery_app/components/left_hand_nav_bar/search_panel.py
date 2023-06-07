from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc

search_panel = dbc.Col([
    dcc.Input(id="search_input", placeholder="Not yet working... Search modules")

], width=2, style={'background-color': '#ADD8E6'})

