from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc
import dash_cytoscape as cyto
import module_data 

neutral_node_styling = {
        'color': "gray",
        "font-size": "20px",
        'width': "20px",
        'height': "20px",
        'opacity': .3
         }

neutral_edge_styling = {
        'color': "lightgray",
        'opacity': .15,
        'width': '3px'
         }

default_stylesheet = [
    #### Have every node labeled with its title, and initially gray:
    {'selector': 'node', 'style': neutral_node_styling},
    {'selector': 'node',
    'style': {
        'background-color': 'lightgray',
        'color': 'gray',
        #'label': 'data(title)',
        'opacity': 0.3
        }
    },
    #### Make the edges also opaque
    {
    'selector': 'edge',
    'style': neutral_edge_styling
    },
    #### Highlight the good_first_module modules
    {
    'selector': '[good_first_module *= "true"]',
    'style': {
        'background-color': 'gray',
        'color': 'black',
        'opacity': 1,
        'label': 'data(title)'
        }
    }
]