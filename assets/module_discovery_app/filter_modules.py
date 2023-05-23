###
import module_data 

# possible kwargs from the center nav bar: general_options_checklist coding_language_checklist coding_level_checklist data_task_checklist data_domain_checklist

## This will be incorporated into a callback with inputs in this order:               
# .         Input('general_options_checklist', 'value'),
#            Input('coding_language_collapse_button', 'value'),
#            Input('coding_level_checklist', 'value'),
#            Input('data_task_collapse_checklist', 'value'),
#            Input('data_domain_checklist', 'value'),

def filter_modules(general_options_value):#, coding_language_value, coding_level_value, data_task_value, data_domain_value):
    matching_modules = list(module_data.df.index).copy()
    non_matching_modules = []
    for module in module_data.df.index:
        if general_options_value and 'good_first_module' in general_options_value:
            if module_data.df.loc[module, "good_first_module"] != "true":
                matching_modules.remove(module)
                non_matching_modules.append(module)
        if general_options_value and 'no_coding_required' in general_options_value:
            if module_data.df.loc[module, "coding_required"] != "true":
                matching_modules.remove(module)
                non_matching_modules.append(module)
    return matching_modules
            

