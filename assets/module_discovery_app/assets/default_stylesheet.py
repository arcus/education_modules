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
                'background-color': 'blue',
                'label': 'data(title)',
                'opacity': 1,

                    }

unselected_styling = {
                   'background-color': '#FF4136',
                    'label': ' ',
                    'opacity': .3,
                        }

active_node_styling = {
                   'background-color': 'green',
                    'label': 'data(title)',
                    'opacity': 1,
                        }


default_stylesheet = [
    # make all the nodes neutrally styled
    {'selector': 'node', 'style': neutral_node_styling},
    # make all the edges neutrally styled
    {'selector': 'edge', 'style': neutral_edge_styling},
    ]