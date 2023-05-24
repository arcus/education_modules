### Take input from all over the app to determine the unique node that is currently the ACTIVE NODE
from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc
import module_data 

### Use ctx to determine whether the last thing clicked was a button or a node on the graph, then make that thing the ACTIVE NODE
def determine_active_node(app):
    @app.callback(Output('hidden_active_module', 'children'),
                 Input('module_visualization', 'selectedNodeData')
                )
    def filtering(data):
        if data:
            return data[0]['id']