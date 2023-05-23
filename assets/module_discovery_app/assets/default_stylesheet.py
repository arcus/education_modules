from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc
import dash_cytoscape as cyto
import module_data 

neutral_node_styling = {
        'color': "gray",
        "font-size": "20px",
        'width': "20px",
        'height': "20px",
        'opacity': .3,
        'label': " "
         }

neutral_edge_styling = {
        'color': "lightgray",
        'opacity': .15,
        'width': '3px'
         }

selected_styling = {
                'label': 'data(title)',
                'color': 'black',
                'background_color': 'gray',
                'opacity': 1
                    }

unselected_styling = {
                    'color': 'black',
                    'label': ' ',
                        }


default_stylesheet = [
    # make all the nodes neutrally styled
    {'selector': 'node', 'style': neutral_node_styling},
    {'selector': 'node',
    'style': {
        'background-color': 'lightgray',
        'color': 'gray',
        'label': ' ',
        'opacity': 0.3
        }
    },
    # make all the edges neutrally styled
    {
    'selector': 'edge',
    'style': neutral_edge_styling
    },
]