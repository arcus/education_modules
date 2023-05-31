### Take input from all over the app to determine the unique node that is currently the ACTIVE NODE
from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc
import module_data 

### Use ctx to determine whether the last thing clicked was a button or a node on the graph, then make that thing the ACTIVE NODE

module_buttons = [module_id+'_button' for module_id in module_data.df.index]

def debugger(app):
    @app.callback(Output('debugger2', 'children'), Input('using_redcap_api_button', 'n_clicks'))
    def help(n):
        if n is None:
            return "Not clicked."
        else:
            return f"Clicked {n} times."

    @app.callback(Output('debugger', 'children'),
                  [Input(button, 'n_clicks') for button in module_buttons] ### this is super cludgy and creates all the buttons for stuff we don't need...
                )
    def filtering(*args):
        trigger = ctx.triggered[0]
        return trigger
