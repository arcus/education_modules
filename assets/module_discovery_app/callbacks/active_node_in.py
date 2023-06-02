### Take input from all over the app to determine the unique node that is currently the ACTIVE NODE
from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc
import module_data 

### Use ctx to determine whether the last thing clicked was a button or a node on the graph, then make that thing the ACTIVE NODE
def active_node_in(app):
    @app.callback(Output('hidden_active_module', 'children'),
                Input('module_visualization', 'tapNodeData'),
                [Input(module_id+"_button", 'n_clicks') for module_id in module_data.df.index], #these buttons are the buttons for the filtered module list
                [Input(module_id+"_nottub", 'n_clicks') for module_id in module_data.df.index], #these "nottub"s are modules connected to the current active node
                prevent_initial_call=True)
    def activate(data, *args):
        trigger = ctx.triggered_id
        if trigger == "module_visualization":
            return data['id']
        elif sum(args) != 0:
             return trigger[:-7]
        else:
            return "no_active_module"

