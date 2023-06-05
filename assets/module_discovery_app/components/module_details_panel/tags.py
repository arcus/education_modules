from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc
import module_data 


# TODO Create buttons for the categories that this module is tagged as
def find_tags(active_module):
    tags = []
    for tag_key in ["good_first_module","coding_required", "coding_language","coding_level"]:
        if len(str(module_data.df.loc[active_module, tag_key]))>0:
            tags.append(module_data.df.loc[active_module, tag_key])
        
    return dcc.Markdown(tags)