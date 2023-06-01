from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc
import module_data 

def create_clickable_module_list(app):
   @app.callback(Output('clickable_module_links', 'children'),
               Input('hidden_filtered_modules_list', 'children'))
   def create_module_links(matching_modules):
      matches = []
      for module_id in module_data.df.index:
         title = module_data.df.loc[module_id, 'title']
         button_id = str(module_id)+"_button"
         if module_id in matching_modules:
            button = dbc.Button(title, id=button_id, n_clicks=0)
            matches.append(button)
         else:
            button = html.Button(module_id, id=button_id, n_clicks=0, style = dict(display='none'))
            matches.append(button)
      return matches
