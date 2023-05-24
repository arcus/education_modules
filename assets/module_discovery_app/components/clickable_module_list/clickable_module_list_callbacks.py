from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc
import module_data 

def create_clickable_module_list(app):
   @app.callback(Output('clickable_module_links', 'children'),
               Input('hidden_filtered_modules_list', 'children'))
   def create_module_links(matching_modules):
      matches = []
      for module_id in matching_modules:
         title = module_data.df.loc[module_id, 'title']
         button = dbc.Button(title, value=module_id)
         matches.append(button)
      return matches