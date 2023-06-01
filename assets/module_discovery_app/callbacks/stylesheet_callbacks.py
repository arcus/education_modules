### Eventually this will be folded into a single callback that incorporates filtered_modules, active_node, and then spits out the approriate stylesheet for the visualization panel.

from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc
import dash_cytoscape as cyto
from assets import default_stylesheet
import module_data


def turn_nodes_on_off(app):
    @app.callback(Output('module_visualization', 'stylesheet'),
                Input('hidden_filtered_modules_list','children'),
                Input('hidden_active_module', 'children'))
    def update_stylesheet(filtered_module_list,active_node):
        ## Edges need to be restyled each time
        new_stylesheet = [ {'selector': 'edge', 'style': default_stylesheet.neutral_edge_styling}]
        for module_id in module_data.df.index:
            selector = str('[id *= "')+str(module_id)+str('" ]')
            if module_id == active_node:
                new_stylesheet +=[{'selector': selector, 'style': default_stylesheet.active_node_styling}]
            else:            
                if module_id in filtered_module_list:
                    new_stylesheet += [{'selector': selector,
                                    'style': default_stylesheet.selected_styling
                                        }]
                else:
                    new_stylesheet +=[{'selector': selector,
                                    'style': default_stylesheet.unselected_styling
                                        }]
        return new_stylesheet

