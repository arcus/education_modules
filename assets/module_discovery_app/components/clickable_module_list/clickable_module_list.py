from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc
import module_data 

clickable_module_list = dbc.Col(
                    children=[
                     html.Div([
                        dcc.Markdown("Modules that match your filters:"),
                        #html.Div(create_module_buttons(nodes), id='matching_module_buttons')
                     ]),
                     html.Div([], id='clickable_module_links')
                     ]
                )
