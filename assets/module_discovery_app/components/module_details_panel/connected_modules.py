# This callback is a function that takes one input (a module id like citizen_science)
# and returns the details with all the information we want to display about that module
# if no module name is given, this function should return some generic instruction text.


from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc
import module_data 

# Create buttons for all of the connected modules using module_data.df info
def connected_modules(active_node):
    if active_node in list(module_data.df.index):
        sets_you_up_button_list = []
        sets_you_up_for = str(module_data.df.loc[active_node, "Sets You Up For"])
        depends_on_button_list = []
        depends_on_knowledge_in = str(module_data.df.loc[active_node, "Depends On Knowledge In"])
        hidden_button_list = []
        ## add an is_parallel_to optional set of buttons when that metadata is in module_data
        for module in list(module_data.df.index):
            if module in sets_you_up_for or active_node in str(module_data.df.loc[module,"Depends On Knowledge In"]): #ensure that if the link is only in one of the modules, it still shows up here (symmetry in metadata not required)
                button = html.Button(module_data.df.loc[module,"title"], id=module+"_nottub", n_clicks=0) #this is to ensure the buttons created here don't clash with buttons created by filtering, but are still essentially called the same thing for my human brain: module_id_button/module_id_nottub
                sets_you_up_button_list.append(button)
            elif module in depends_on_knowledge_in or active_node in str(module_data.df.loc[module,"Sets You Up For"]):
                button = html.Button(module_data.df.loc[module,"title"], id=module+"_nottub", n_clicks=0) #same button/nottub idea here
                depends_on_button_list.append(button)
            else:
                button = html.Button(module_data.df.loc[module,"title"], id=module+"_nottub", n_clicks=0, style = dict(display='none'))
                hidden_button_list.append(button)
        left_subpanel = dbc.Col([html.Div("Not quite ready for this module? Check out these first:"),html.Div(depends_on_button_list)], width=6) if len(depends_on_button_list)>0 else dbc.Col([html.Div("This module doesn't require any specialized knowledge to get started, so check it out now!")], width=6)
        right_subpanel = dbc.Col([html.Div("Already familiar with this material? Try these next:"),html.Div(sets_you_up_button_list)], width=6) if len(sets_you_up_button_list)>0 else dbc.Col([html.Div("Not sure what we want to put here... encourage people to explore related modules using other metadata connections?")], width=6)
        return [dbc.Row([left_subpanel, right_subpanel]), html.Div(hidden_button_list)]
    else:
        return "no current active node"
