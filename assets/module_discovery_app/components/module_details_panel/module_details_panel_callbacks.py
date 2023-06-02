# This callback is a function that takes one input (a module id like citizen_science)
# and returns the details with all the information we want to display about that module
# if no module name is given, this function should return some generic instruction text.


from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc
import module_data 

# TODO create buttons for all of the connected modules using module_data.df info
def connected_modules(active_node):
    if active_node in list(module_data.df.index):
        sets_you_up_button_list = []
        sets_you_up_for = str(module_data.df.loc[active_node, "Sets You Up For"])
        depends_on_button_list = []
        depends_on_knowledge_in = str(module_data.df.loc[active_node, "Depends On Knowledge In"])
        hidden_button_list = []
        ## add an is_parallel_to optional set of buttons when that metadata is in module_data
        for module in list(module_data.df.index):
            if module in sets_you_up_for:
                button = html.Button(module_data.df.loc[module,"title"], id=module+"_nottub", n_clicks=0) #this is to ensure the buttons created here don't clash with buttons created by filtering, but are still essentially called the same thing for my human brain: module_id_button/module_id_nottub
                sets_you_up_button_list.append(button)
            elif module in depends_on_knowledge_in:
                button = html.Button(module_data.df.loc[module,"title"], id=module+"_nottub", n_clicks=0) #same button/nottub idea here
                depends_on_button_list.append(button)
            else:
                button = html.Button(module_data.df.loc[module,"title"], id=module+"_nottub", n_clicks=0, style = dict(display='none'))
                hidden_button_list.append(button)        
        return [dbc.Row([dbc.Col([html.Div("Not quite ready for this module? Check out these first:"),html.Div(depends_on_button_list)], width=6), dbc.Col([html.Div("Already familiar with this material? Try these next:"),html.Div(sets_you_up_button_list)], width=6) ])]
    else:
        return "no current active node"


# This is the automatically displayed metadata about the active module:
def module_info(active_node):
    if active_node in list(module_data.df.index):
        learning_objectives = module_data.df.loc[active_node,'learning_objectives']
        learning_objectives = learning_objectives.replace("&", "\n")
        return  [dcc.Markdown("### [**" + module_data.df.loc[active_node,'title'] + "**](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/"+ active_node +"/" + active_node + ".md) \n \n  By " + module_data.df.loc[active_node,'author'] +" \n \n Estimated length: " + module_data.df.loc[active_node,'estimated_time_in_minutes']+". \n \n" + module_data.df.loc[active_node,'comment'] + "\n \n" + learning_objectives),
        html.Hr(),
        html.Hr(),
        html.Div(connected_modules(active_node))]
    else:
        return dcc.Markdown("##### Use the buttons or click on a module's node in the graph to learn more about it. \n --- ")





def update_module_info_panel(app):
    @app.callback(
            Output('active_module_details_panel', 'children'),
            Input('hidden_active_module', 'children'))
    def update_module_info_panel(active_node):
        return module_info(active_node)
