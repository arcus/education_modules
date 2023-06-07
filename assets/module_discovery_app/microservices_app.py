from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc
import dash_cytoscape as cyto

# Import the module data as a dataframe
import module_data
df = module_data.df

# Import styling from assets directory
from assets import default_stylesheet 

# Import app components and their internal callbacks
from components.left_hand_nav_bar import left_hand_nav_bar, left_hand_nav_bar_callbacks 
left_hand_nav_bar = left_hand_nav_bar.left_hand_nav_bar

from components.visualization_panel import visualization_panel
visualization_panel = visualization_panel.visualization_panel

from components.app_title import app_title
app_title = app_title.app_title

from components.heading_tabs import heading_tabs
heading_tabs = heading_tabs.heading_tabs

from components.clickable_module_list import clickable_module_list, clickable_module_list_callbacks
clickable_module_list_panel = clickable_module_list.clickable_module_list

from components.module_details_panel import module_details_panel, module_details_panel_callbacks
module_information = module_details_panel.module_details_panel

from components.left_hand_nav_bar import search_panel
search_panel = search_panel.search_panel

# Import the hidden components that keep track of the filtered modules and the active module
from components import hidden_filtered_modules, hidden_active_module
hidden_filtered_modules = hidden_filtered_modules.hidden_filtered_modules
hidden_active_module = hidden_active_module.hidden_active_module

# Import inter-component callbacks
import callbacks.stylesheet_callbacks
import callbacks.active_node_in
import callbacks.active_node_out
import callbacks.filter_modules_in
import callbacks.debugger





# Initialize the app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP],suppress_callback_exceptions=True) ## suppress_callback_exceptions prevents all of the errors from callbacks calling things not yet set up by other callbacks.
server = app.server


# Set up the layout of the app
app.layout = html.Div([
    dbc.Row(children=[
        app_title,
        ]
        ),
    html.Hr(),
    dbc.Row(children=[
        left_hand_nav_bar,
        dbc.Col([clickable_module_list_panel, html.Hr(), html.Br(),module_information], width=5),
        dbc.Col(children=[visualization_panel
        ],width=5),
        
        
        ]),
    html.Hr(), html.Hr(),
    html.Div(hidden_filtered_modules), # DONT COMMENT OUT this is visible for debugging purposes, change to 'display': 'none' for production purposes. 
    html.Div(hidden_active_module), # DONT COMMENT OUT this is visible for debugging purposes, change to 'display': 'none' for production purposes.
    html.Div(children=["blue"], id="debugger"),     html.Div(children=["blue"], id="debugger2")
    ],
    style={'padding' : '25px'}
    )

# Initialize all INTRAcomponent callbacks
left_hand_nav_bar_callbacks.get_left_hand_nav_bar_callbacks(app)
module_details_panel_callbacks.update_module_info_panel(app)

# Initialize all INTERcomponent callbacks next...
callbacks.stylesheet_callbacks.turn_nodes_on_off(app)
callbacks.filter_modules_in.update_hidden_filtered_modules(app)
clickable_module_list_callbacks.create_clickable_module_list(app)
callbacks.active_node_in.active_node_in(app)
#callbacks.active_node_out.active_node_out(app)
callbacks.debugger.debugger(app)

if __name__ == '__main__':
    app.run_server(debug=True)