from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc
import module_data

search_panel = dbc.Col([
    dcc.Input(id="search_input", placeholder="Search... add submit button?")

], width=2, style={'background-color': '#ADD8E6'})

def search_results(value):
    matches = []
    if value:
        for module in module_data.df.index:
            if value.lower() in str(module_data.df.loc[module,'title']).lower():
                matches.append(module)
            elif value.lower() in str(module_data.df.loc[module,'comment']).lower():
                matches.append(module)
            elif value.lower() in str(module_data.df.loc[module,'long_description']).lower():
                matches.append(module)
            elif value.lower() in str(module_data.df.loc[module,'learning_objectives']).lower():
                matches.append(module)
    return matches