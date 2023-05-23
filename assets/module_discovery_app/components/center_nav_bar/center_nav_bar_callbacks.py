from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc
import dash_cytoscape as cyto

### center_nav_bar expands and contracts based on user interactions
def get_center_nav_bar_callbacks(app):
    @app.callback(
        Output("coding_language_collapse_checklist", "is_open"),
        [Input("coding_collapse_button", "n_clicks")],
        [State("coding_language_collapse_checklist", "is_open")],
        )
    def toggle_collapse1(n, is_open):
        if n:
            return not is_open
        return is_open

    @app.callback(
        Output("general_options_collapse_checklist", "is_open"),
        [Input("general_options_collapse_button", "n_clicks")],
        [State("general_options_collapse_checklist", "is_open")],
        )
    def toggle_collapse2(n, is_open):
        if n:
            return not is_open
        return is_open

    @app.callback(
        Output("coding_level_collapse_checklist", "is_open"),
        [Input("coding_level_collapse_button", "n_clicks")],
        [State("coding_level_collapse_checklist", "is_open")],
        )
    def toggle_collapse3(n, is_open):
        if n:
            return not is_open
        return is_open
        