from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc
import dash_cytoscape as cyto
import module_data 
from assets import default_stylesheet 

df = module_data.df

nodes = [
    {
        'data': {
            'id': row, 
            'title': df.loc[row,'title'], 
            'author': df.loc[row, 'author'], 
            'estimated_time_in_minutes': df.loc[row,'estimated_time_in_minutes'], 
            'comment': df.loc[row,'comment'], 
            'long_description': df.loc[row,'long_description'],
            'learning_objectives': df.loc[row,'learning_objectives'],
            'good_first_module': df.loc[row,'good_first_module'],
            'coding_required': df.loc[row,'coding_required'],
            'coding_language': df.loc[row,'coding_language'],
            'coding_level': df.loc[row,'coding_level'],
            },
            'selected':True,
            #'selectable': True
    }
    for row in df.index 
]

edges = []
for row in df.index:
    for linked_module in df.loc[row, 'Linked Courses']:
        edges.append({'data': {'source': linked_module, 'target': row, 'relationship': 'internal_link'}})

default_stylesheet = default_stylesheet.default_stylesheet

visualization_panel = dbc.Col(
                    children=[
                    dcc.Markdown("To learn more about a module, click on its node:"),
                    cyto.Cytoscape(
                    id='module_visualization',
                    layout={'name': 'cose'},
                    elements=edges+nodes,
                    stylesheet=default_stylesheet,
                    style={'width': '100%', 'height': '450px'},
                    userZoomingEnabled=False
                     ),
                     ]
                )
