# put the module details panel information here
# this should be a function that takes one input (a module id like citizen_science)
# and returns the details with all the information we want to display about that module
# if no module name is given, this function should return some generic instruction text.


from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc
import module_data 


module_details_panel=html.Div(children=[html.Div("some text goes here about selecting a module to learn more about it")], id='active_module_details_panel')

