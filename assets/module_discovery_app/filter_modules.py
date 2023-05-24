### The filter_modules function takes the checklist and radio buttons from the center_nav_bar and returns a list of all modules that match the given filters.

import module_data 

def filter_modules(general_options_value, coding_language_value, coding_level_value, data_task_value, data_domain_value):
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
        if coding_language_value and 'bash' in coding_language_value:
            if 'bash' not in str(module_data.df.loc[module,'coding_language']).lower():
                tracker = tracker*0
        if coding_language_value and 'python' in coding_language_value:
            if 'python' not in str(module_data.df.loc[module,'coding_language']).lower():
                tracker = tracker*0
        if coding_language_value and 'r' in coding_language_value:
            if 'r' not in str(module_data.df.loc[module,'coding_language']).lower(): # If we ever add a coding language that contains a r in its name, i.e. Ruby, this will need to be made more robust. 
                tracker = tracker*0
        if coding_language_value and 'SQL' in coding_language_value:
            if 'SQL' not in str(module_data.df.loc[module,'coding_language']).upper():
                tracker = tracker*0
        if coding_language_value and 'git' in coding_language_value:
            if 'git' not in str(module_data.df.loc[module,'coding_language']).lower():
                tracker = tracker*0
        if coding_level_value: # coding level is a radio button, so the output is a string, not a list of strings
            if coding_level_value not in str(module_data.df.loc[module,'coding_level']).lower():
                tracker = tracker*0
    #### INCLUDE DATA_TASK IN THE DATAFRAME IN ORDER FOR THIS TO WORK
        # if data_task_value and 'data_visualization' in data_task_value:
        #     if 'data_visualization' not in str(module_data.df.loc[module,'data_task']).lower():
        #         tracker = tracker*0
        # if data_task_value and 'data_management' in data_task_value:
        #     if 'data_management' not in str(module_data.df.loc[module,'data_task']).lower():
        #         tracker = tracker*0
        # if data_task_value and 'data_wrangling' in data_task_value:
        #     if 'data_wrangling' not in str(module_data.df.loc[module,'data_task']).lower():
        #         tracker = tracker*0
        # if data_task_value and 'data_analysis' in data_task_value:
        #     if 'data_analysis' not in str(module_data.df.loc[module,'data_task']).lower():
        #         tracker = tracker*0

        if tracker == 0:
            matching_modules.remove(module)
            non_matching_modules.append(module)
    return matching_modules, non_matching_modules
            

