### Take input from all over the app to determine the unique node that is currently the ACTIVE NODE
from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc
import module_data 

### Use ctx to determine whether the last thing clicked was a button or a node on the graph, then make that thing the ACTIVE NODE
def determine_active_node(app):
    @app.callback(Output('hidden_active_module', 'children'),
                 Input('module_visualization', 'tapNodeData'),
                 [Input(module_id+"_button", 'n_clicks') for module_id in module_data.df.index] ### this is super cludgy and requires us to create all the buttons for stuff we don't need and just hide them.
                )
    def activate(data, *args):
        trigger = ctx.triggered_id
        if trigger == "module_visualization":
            return data['id']
        else:
            return trigger[:-7]