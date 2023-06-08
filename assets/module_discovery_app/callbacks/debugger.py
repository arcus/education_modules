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
                Input('search_input', 'value'))
    def search_results(value):
        matches = []
        if value:
            for module in module_data.df.index:
                if value in str(module_data.df.loc[module,'title']):
                    matches.append(module)
                elif value in str(module_data.df.loc[module,'comment']):
                    matches.append(module)
                elif value in str(module_data.df.loc[module,'long_description']):
                    matches.append(module)
                elif value in str(module_data.df.loc[module,'learning_objectives']):
                    matches.append(module)
        return matches