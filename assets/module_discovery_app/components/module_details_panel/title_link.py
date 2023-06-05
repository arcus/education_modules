from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc
import module_data 

def title_link(active_node):
    return html.P([html.A(module_data.df.loc[active_node,'title'],href="https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/"+ active_node +"/" + active_node + ".md" , target="_blank")], style={'font-size':'200%', "font-weight": "bold"})