from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc

heading_tabs = dbc.Col(html.Div(      
            dbc.Tabs([
                dbc.Tab(label="Home", tab_id='instructions'),
                #dbc.Tab(label="Explore Categories", tab_id='categories'),
                dbc.Tab(label="Explore Pathways", tab_id='pathways'),
                dbc.Tab(label="Search", tab_id='search'),
            ],
            id="tab_options",
            active_tab="instructions"
            )
                ),  
            align='end')