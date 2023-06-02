### Take input from all over the app to determine the unique node that is currently the ACTIVE NODE
from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc
import module_data 

### Use ctx to determine whether the last thing clicked was a button or a node on the graph, then make that thing the ACTIVE NODE

module_buttons = [module_id+'_button' for module_id in module_data.df.index]

def debugger(app):
    # @app.callback(Output('debugger2', 'children'), Input('using_redcap_api_button', 'n_clicks'))
    # def help(n):
    #     if n is None:
    #         return "Not clicked."
    #     else:
    #         return f"Clicked {n} times."

    @app.callback(Output('debugger', 'children'),
                [Input(module_id+"_nottub", 'n_clicks') for module_id in module_data.df.index], ## The nottub buttons are the buttons in the module details pannel about what links to the active node. They need to have separate ids hence the button/nottub thing
                )
    def filtering(*args):
        trigger = ctx.triggered_id
        return trigger
