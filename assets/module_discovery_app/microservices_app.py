from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc
import dash_cytoscape as cyto
import module_data
from microservices import heading_tabs, visualization_panel, default_stylesheet, center_nav_bar


app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

styles = {
    'pre': {
        'border': 'thin lightgrey solid',
        'overflowX': 'scroll'
    }
}

### Set up panels of the app by importing components from the microservices files
df = module_data.df
app_title = dbc.Col(html.Div(["DART Module Discovery Tool"]), style={'textAlign': 'center','font-size':'40px'}, align='end', width=7)
heading_tabs = heading_tabs.heading_tabs
visualization_panel = visualization_panel.visualization_panel
center_nav_bar = center_nav_bar.center_nav_bar


app.layout = html.Div([
    dbc.Row(children=[
        app_title,
        heading_tabs]
        ),
    html.Hr(),
    dbc.Row(children=[
        visualization_panel,
        center_nav_bar,
        #information_panel
        ])
    ],
    style={'padding' : '25px'}
    )

### center_nav_bar expands and contracts based on user interactions
@app.callback(
    Output("coding_language_collapse_checklist", "is_open"),
    [Input("coding_collapse_button", "n_clicks")],
    [State("coding_language_collapse_checklist", "is_open")],
    )
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("general_options_collapse_checklist", "is_open"),
    [Input("general_options_collapse_button", "n_clicks")],
    [State("general_options_collapse_checklist", "is_open")],
    )
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("coding_level_collapse_checklist", "is_open"),
    [Input("coding_level_collapse_button", "n_clicks")],
    [State("coding_level_collapse_checklist", "is_open")],
    )
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open
    
if __name__ == '__main__':
    app.run_server(debug=True)