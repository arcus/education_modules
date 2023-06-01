from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc
import dash_cytoscape as cyto

# Import the module data as a dataframe
import module_data
df = module_data.df

# Import styling from assets directory
from assets import default_stylesheet 

# Import app components and their internal callbacks
from components.center_nav_bar import center_nav_bar, center_nav_bar_callbacks 
center_nav_bar = center_nav_bar.center_nav_bar

from components.visualization_panel import visualization_panel
visualization_panel = visualization_panel.visualization_panel

from components.app_title import app_title
app_title = app_title.app_title

from components.heading_tabs import heading_tabs
heading_tabs = heading_tabs.heading_tabs

from components.clickable_module_list import clickable_module_list, clickable_module_list_callbacks
clickable_module_list_panel = clickable_module_list.clickable_module_list

# Import the hidden components that keep track of the filtered modules and the active module
from components import hidden_filtered_modules, hidden_active_module
hidden_filtered_modules = hidden_filtered_modules.hidden_filtered_modules
hidden_active_module = hidden_active_module.hidden_active_module

# Import inter-component callbacks
import callbacks.turn_nodes_on_off_callbacks
import callbacks.determine_active_node
import callbacks.active_node_updates
import callbacks.filter_modules
import callbacks.debugger





# Initialize the app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server


# Set up the layout of the app
app.layout = html.Div([
    dbc.Row(children=[
        app_title,
        heading_tabs]
        ),
    html.Hr(),
    dbc.Row(children=[
        dbc.Col(children=[visualization_panel, html.Br(), clickable_module_list_panel],width=5),
        center_nav_bar,
        #information_panel
        ]),
    html.Div(hidden_filtered_modules), # visible for debugging purposes, change to 'display': 'none' for production purposes.
    html.Div(hidden_active_module), # visible for debugging purposes, change to 'display': 'none' for production purposes.
    #html.Div(children=["blue"], id="debugger"),     html.Div(children=["blue"], id="debugger2")
    ],
    style={'padding' : '25px'}
    )

# Initialize all INTRAcomponent callbacks
center_nav_bar_callbacks.get_center_nav_bar_callbacks(app)

# Initialize all INTERcomponent callbacks next...
callbacks.turn_nodes_on_off_callbacks.turn_nodes_on_off(app)
callbacks.filter_modules.update_hidden_filtered_modules(app)
clickable_module_list_callbacks.create_clickable_module_list(app)
callbacks.determine_active_node.determine_active_node(app)
#callbacks.active_node_updates.active_node_updates(app)
callbacks.debugger.debugger(app)

if __name__ == '__main__':
    app.run_server(debug=True)