from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc
import module_data 

def learning_objectives(active_node):
    learning_objectives = module_data.df.loc[active_node,'learning_objectives']
    learning_objectives = learning_objectives.replace("&", "\n") # remnants of a fight I had with bash and quotations/newlines.
    learning_objectives = learning_objectives.replace("+", '"') # remnants of a fight I had with bash and quotations/newlines.
    return learning_objectives