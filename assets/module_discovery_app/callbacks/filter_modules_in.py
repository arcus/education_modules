### The filter_modules_in function takes the checklist and radio buttons from the left_hand_nav_bar and returns a list of all modules that match the given filters.
from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc
import module_data 

def filter_modules_in(general_options_value, coding_language_value, coding_level_value, data_task_value, data_domain_value):
    matching_modules = list(module_data.df.index).copy()
    non_matching_modules = []
    for module in module_data.df.index:
        tracker = 1
        if general_options_value and 'good_first_module' in general_options_value:
            if "true" not in str(module_data.df.loc[module, "good_first_module"]).lower():# allow for True, true, or trailing spaces in data entry.
                tracker = tracker*0
        if general_options_value and 'no_coding_required' in general_options_value:
            if "true" in str(module_data.df.loc[module, "coding_required"]).lower():
                tracker = tracker*0
        if coding_language_value:
          if coding_language_value.lower() not in str(module_data.df.loc[module,'coding_language']): # coding language is a radio button, so the output is a string, not a list of strings
                tracker = tracker*0
        if coding_level_value: # coding level is a radio button, so the output is a string, not a list of strings
            if coding_level_value not in str(module_data.df.loc[module,'coding_level']).lower():
                tracker = tracker*0
        if data_task_value: # coding level is a radio button, so the output is a string, not a list of strings
            if data_task_value not in str(module_data.df.loc[module,'data_task']).lower():
                tracker = tracker*0
        if data_domain_value: # coding level is a radio button, so the output is a string, not a list of strings
            if data_domain_value not in str(module_data.df.loc[module,'data_domain']).lower():
                tracker = tracker*0
        if tracker == 0:
            matching_modules.remove(module)
            non_matching_modules.append(module)
    return matching_modules, non_matching_modules
            

def update_hidden_filtered_modules(app):
    @app.callback(Output('hidden_filtered_modules_list', 'children'),
                Input('general_options_checklist', 'value'),
                Input('coding_language_checklist', 'value'),
                Input('coding_level_checklist', 'value'),
                Input('data_task_checklist', 'value'),
                Input('data_domain_checklist', 'value')
                )
    def filtering(value, coding_language_value, coding_level_value, data_task_value, data_domain_value):
        return filter_modules_in(value, coding_language_value, coding_level_value, data_task_value, data_domain_value)[0]
