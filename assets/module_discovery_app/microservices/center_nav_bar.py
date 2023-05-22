from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc
import dash_cytoscape as cyto
import module_data 

center_nav_bar = dbc.Col([dcc.Markdown("Use the checkboxes to find modules that may interest you:"),
    dbc.Button(
    "General options",
    id="general_options_collapse_button"),
    dbc.Collapse(dcc.Checklist(
           options=[
       {'label': ' Good first module', 'value': 'good_first_module'},
       {'label': ' Doesn\'t require coding', 'value': 'no_coding_required'}
       ],
          value=['good_first_module'],
          id='general_options_checklist'),
          id='general_options_collapse_checklist',
    is_open=True),

    html.Br(),
    dbc.Button(
        "Coding Language",
        id="coding_collapse_button"),
    dbc.Collapse([
    dbc.Col( 
    dcc.Checklist(
        options=[
        {'label': ' Bash', 'value': 'bash'},
        {'label': ' Python', 'value': 'python'},
        {'label': ' R', 'value': 'r'},
        {'label': ' SQL', 'value': 'SQL'},
        {'label': ' Git', 'value': 'git'},
        ],
        id='coding_language_checklist'
        )
        ),],
    id='coding_language_collapse_checklist',
    is_open=False,
    ),
    html.Br(),
    dbc.Button(
    "Coding Level",
    id="coding_level_collapse_button"),
        dbc.Collapse([
    dbc.Col([
        dcc.RadioItems(
        options=[
        {'label': ' Get started', 'value': 'getting_started'},
        {'label': ' Basic', 'value': 'basic'},
        {'label': ' Intermediate', 'value': 'intermediate'},
        {'label': ' Advanced', 'value': 'advanced'},
        {'label': ' Exercises', 'value': 'practice_exercise'},
        ],
        id='coding_level_checklist')
    ],)],
    id='coding_level_collapse_checklist',
    is_open=False,
    ),
], width=2)

