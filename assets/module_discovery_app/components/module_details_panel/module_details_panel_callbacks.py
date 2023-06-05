# This callback is a function that takes one input (a module id like citizen_science)
# and returns the details with all the information we want to display about that module
# if no module name is given, this function should return some generic instruction text.


from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc
import module_data 
from .title_link import title_link
from .connected_modules import connected_modules
from .tags import find_tags
from .learning_objectives import learning_objectives
from .pre_reqs import pre_reqs

# This is the automatically displayed metadata about the active module:
def module_info(active_node):
    if active_node in list(module_data.df.index):
        module_info_panel = [title_link(active_node),
                        find_tags(active_node),
                        dcc.Markdown("By " + module_data.df.loc[active_node,'author']),
                        dcc.Markdown("Estimated length: " + module_data.df.loc[active_node,'estimated_time_in_minutes']+"."),
                        dcc.Markdown(module_data.df.loc[active_node,'comment']),
                        dcc.Markdown(learning_objectives(active_node)),
                        html.Hr(),
                        pre_reqs(active_node),
                        html.Hr(),
                        html.Div(connected_modules(active_node)),
                        ]
        return module_info_panel
    else:
        initialize_buttons = [html.Button(module_data.df.loc[module,"title"], id=module+"_nottub", n_clicks=0, style = dict(display='none')) for module in list(module_data.df.index)]
        return html.Div([dcc.Markdown("##### Use the buttons or click on a module's node in the graph to learn more about it. \n --- "), html.Div(initialize_buttons)])



def update_module_info_panel(app):
    @app.callback(
            Output('active_module_details_panel', 'children'),
            Input('hidden_active_module', 'children'))
    def update_module_info_panel(active_node):
        return module_info(active_node)
