# Ultimated this callback will display the nodes that match the filters selected in the center_nav_bar, turning on the nodes that match and turning off the nodes that do not match.
# Right now it is only listening for the good_first_module checkbox.

from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc
import dash_cytoscape as cyto
from assets import default_stylesheet


selected_styling = default_stylesheet.selected_styling 
unselected_styling = default_stylesheet.unselected_styling

def turn_nodes_on_off(app):
    @app.callback(Output('module_visualization', 'stylesheet'),
                Input('general_options_checklist','value'))
    def update_stylesheet(general_options_value):
        new_stylesheet = default_stylesheet.default_stylesheet
        good_first_module_selector = '[good_first_module *= \"true\"]'
        good_first_module_deselector = '[good_first_module !*= \"true\"]'
        if 'good_first_module' in general_options_value:
            new_stylesheet += [{'selector': good_first_module_selector,
                                'style': selected_styling
                                    },
                                {'selector': good_first_module_deselector,
                                'style': unselected_styling
                                    }  ]
        else:
            new_stylesheet += [{'selector': good_first_module_selector,
                                'style': unselected_styling
                                    },
                                    ]

        return new_stylesheet

