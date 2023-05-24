from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc

center_nav_bar = dbc.Col([dcc.Markdown("Use the checkboxes to find modules that may interest you:"),
    
    # GENERAL OPTIONS

    dbc.Button(
    "General Options",
    id="general_options_collapse_button", color="dark", outline=True),
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
    html.Br(),

    # CODING LANGUAGE

    dbc.Button(
        "Coding Language",
        id="coding_language_collapse_button", color="dark", outline=True),
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
    html.Br(),

    # CODING LEVEL

    dbc.Button(
    "Coding Level",
    id="coding_level_collapse_button", color="dark", outline=True),
        dbc.Badge("?", id="coding_level_info_button", pill=True,  color="light", text_color="dark"),
    dbc.Popover(
            dbc.PopoverBody(dcc.Markdown("Put something **about stuff** _here!_")),
            target="coding_level_info_button",
            trigger="click",
        ),
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
    html.Br(),
    html.Br(),

    # DATA TASK

    dbc.Button(
    "Data Task",
    id="data_task_collapse_button", color="light"),
    dbc.Badge("?", id="data_task_info_button", pill=True,  color="light", text_color="dark"),
    dbc.Popover(
            dbc.PopoverBody(dcc.Markdown("Put something **about stuff** _here!_")),
            target="data_task_info_button",
            trigger="click",
        ),
    dbc.Collapse([
    dbc.Col([
        dcc.Checklist(
        options=[
        {'label': ' Data Visualization', 'value': 'data_visualization'},
        {'label': ' Data Management', 'value': 'data_management'},
        {'label': ' Data Wrangling', 'value': 'data_wrangling'},
        {'label': ' Data Analysis', 'value': 'data_analysis'},
        ],
        id='data_task_checklist')
    ],)],
    id='data_task_collapse_checklist',
    is_open=False,
    ),
    html.Br(),
    html.Br(),

    # DATA DOMAIN

    dbc.Button(
    "Data Domain",
    id="data_domain_collapse_button", color="light"),
    dbc.Badge("?", id="data_domain_info_button", pill=True,  color="light", text_color="dark"),
    dbc.Popover(
            dbc.PopoverBody(dcc.Markdown("Put something **about stuff** _here!_")),
            target="data_domain_info_button",
            trigger="click",
        ),
        dbc.Collapse([
    dbc.Col([
        dcc.RadioItems(
        options=[
        {'label': ' Omics', 'value': 'omics'},
        {'label': ' Electronic Health Records', 'value': 'EHR'},
        {'label': ' Geospatial Data', 'value': 'geospatial'},
        ],
        id='data_domain_checklist')
    ],)],
    id='data_domain_collapse_checklist',
    is_open=False,
    ),
], width=2)

