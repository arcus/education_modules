# This callback is a function that takes one input (a module id like citizen_science)
# and returns the details with all the information we want to display about that module
# if no module name is given, this function should return some generic instruction text.


from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc
import module_data 


def module_info(active_node):
    if active_node in list(module_data.df.index):
        learning_objectives = module_data.df.loc[active_node,'learning_objectives']
        learning_objectives = learning_objectives.replace("&", "\n")
        return  dcc.Markdown("### [**" + module_data.df.loc[active_node,'title'] + "**](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/"+ active_node +"/" + active_node + ".md) \n \n  By " + module_data.df.loc[active_node,'author'] +" \n \n Estimated length: " + module_data.df.loc[active_node,'estimated_time_in_minutes']+". \n \n" + module_data.df.loc[active_node,'comment'] + "\n \n" + learning_objectives + "\n --- \n ")
    else:
        return dcc.Markdown("##### Use the buttons or click on a module's node in the graph to learn more about it. \n --- ")


def update_module_info_panel(app):
    @app.callback(
            Output('active_module_details_panel', 'children'),
            Input('hidden_active_module', 'children'))
    def update_module_info_panel(active_node):
        return module_info(active_node)
