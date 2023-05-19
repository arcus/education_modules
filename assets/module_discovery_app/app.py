from dash import Dash, html, Input, Output, dcc, ctx
import dash_bootstrap_components as dbc
import dash_cytoscape as cyto
import module_data 

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

styles = {
    'pre': {
        'border': 'thin lightgrey solid',
        'overflowX': 'scroll'
    }
}

df = module_data.df

### Question to consider: does it make sense to keep this data in the definition of the node itself (possibly easier for stylilng the graph) or is it redundant and we should probably just keep refering back to the dataframe?
nodes = [
    {
        'data': {
            'id': row, 
            'title': df.loc[row,'title'], 
            'author': df.loc[row, 'author'], 
            'estimated_time_in_minutes': df.loc[row,'estimated_time_in_minutes'], 
            'comment': df.loc[row,'comment'], 
            'long_description': df.loc[row,'long_description'],
            'learning_objectives': df.loc[row,'learning_objectives'],
            'good_first_module': df.loc[row,'good_first_module'],
            'coding_required': df.loc[row,'coding_required'],
            'coding_language': df.loc[row,'coding_language'],
            'coding_level': df.loc[row,'coding_level'],
            },#'selected': True
        ### Use classes here for all fo the data!!! 'classes': author
        #'position': {'x': 20*lat, 'y': -20*long}
    }
    for row in df.index 
]

### Once relationship metadata is incorporated into the front matter, update process_data.sh to pull it into the dataframe and import it directly to here. In the meantime these relationships can remain definted by what links to what. 
### Note that when there are other link types, those can also be categorized by 'relationship' tags.

edges = []
for row in df.index:
    for linked_module in df.loc[row, 'Linked Courses']:
        edges.append({'data': {'source': linked_module, 'target': row, 'relationship': 'internal_link', 'selectable': False}})


neutral_node_styling = {
        'color': "gray",
        "font-size": "20px",
        'width': "20px",
        'height': "20px"
         }

neutral_edge_styling = {
        'color': "lightgray",
        'opacity': .15,
        'width': '3px'
         }

default_stylesheet = [
    #### Have every node labeled with its title, and initially gray:
    {'selector': 'node', 'style': neutral_node_styling},
    {'selector': 'node',
    'style': {
        'background-color': 'lightgray',
        'color': 'gray',
        'label': 'data(title)',
        'opacity': 0.3
        }
    },
    #### Make the edges also opaque
    {
    'selector': 'edge',
    'style': neutral_edge_styling
    },
    #### Highlight the good_first_module modules
    {
    'selector': '[good_first_module *= "true"]',
    'style': {
        'background-color': 'gray',
        'color': 'black',
        'opacity': 1,
        }
    }
]

active_node = [dcc.Markdown("none selected", id= "active_node")]

### Create a function that changes the stylesheet based on user selecting an author.

def author_selected(author_name):
    ### Create a stylesheet based on the selected author
    select_author_modules = []
    
    ### Turn on nodes corresponding to that author
    selection=str('[author *= "')+ str(author_name) + str('" ]')
    turned_on = {}
    turned_on['selector'] = selection
    turned_on['style'] = {'shape': 'circle', 'background-color':'darkblue', 'label': 'data(title)', 'color': '#000000', 'opacity': 1}
    select_author_modules.append(turned_on)

    ### Turn off nodes not corresponding to that author
    selection=str('[author !*= "')+ str(author_name) + str('" ]')
    turned_off = {}
    turned_off['selector'] = selection
    turned_off['style'] = {'opacity': 0.3, 'background-color':'lightgray'}
    select_author_modules.append(turned_off)

    return select_author_modules

### Create a function that changes the stylesheet based on user selecting "my modules"
def highligh_my_modules(my_modules):
    new_style_sheet= []
    for module in my_modules:
        selector = "[id *= \"" + module + "\"]"
        stylesheet_update = {
        'selector': selector,
        'style': {
            'background-color': "blue",
            'shape': 'circle',
            'color': "black",
            'label': 'data(title)'
        }
        }
        new_style_sheet.append(stylesheet_update)
    return new_style_sheet

### turn on a selected node

def node_select(node_id):
    non_selected_nodes =[]
    selected_node = []
    for module in nodes:
        if module['data']['id'] == node_id:
            select_module = module
            select_module['selected'] = True
            module_name = module['data']['title']
            select_module['style'] = {'shape': 'triangle'}
            selected_node.append(select_module)
        else:
            un_select_module = module
            un_select_module['selected'] = False
            non_selected_nodes.append(un_select_module)
    newly_selected_nodes = non_selected_nodes+selected_node
    return newly_selected_nodes

### What appears when the "explore modules" tab is clicked

module_tab_content = [
                    dbc.Row(html.Div(dcc.Markdown(id='selected_module_text'))),
                    dbc.Row([
                        dbc.Col(html.Div([
                                dcc.Markdown("Modules that the selected module links to:"),
                                dcc.Dropdown(
                                    id='modules_incoming',
                                    options=[
                                        {'label': module["data"]["title"], 'value': module["data"]["id"]}
                                        for module in nodes
                                    ]
                                )
                        ])),
                dbc.Col(html.Div([        
                    dcc.Markdown("Modules that link to the selected module:"),
                    dcc.Dropdown(
                    id='modules_outgoing',
                    options=[ ]
                    ),
    ]))
                    ], align = 'start'),
            ]

### Basic instructions for using this app
instructions_tab_content = [dcc.Markdown("### How to use this tool \n - click around \n - try things out \n - better instructions comming soon!")]

### What appears when the "Explore Categories" tab is clicked
categories_tab_content = [dcc.Markdown("### Content here for how to explore by categories. \n For example, maybe you want to see all of the modules by a particular author"),
                                dcc.Markdown("Pick an author to see their modules."),
    dcc.Dropdown(
    id='author_selector',
    clearable=True,
    options=[
        {'label': name, 'value': name}
        for name in ['Choose an author to see thier modules','Elizabeth Drellich', 'Joy Payton', 'Rose Franzen', 'Rose Hartman', 'Meredith Lee', 'Nicole Feldman', 'Ene Belleh', 'Peter Camacho']
    ],
    value='Choose an author to see thier modules'
),]

### What appears when the "Explore Pathways" tab is clicked
pathways_tab_content = [dcc.Markdown("content hear showing different pre-made pathways")]

### What appears when the "Search" tab is clicked
search_tab_content = [dcc.Markdown("search box to search for modules by entering a keyword")]


### Create My Modules lists:

my_modules_list = [
    dcc.Markdown("### My modules: \n Select modules from the dropdown menu (or yet to be created other buttons) to create your personalized list of modules."),
    dcc.Dropdown(
        id='my_modules',
        options=[
            {'label': module["data"]["title"], 'value': module["data"]["id"]}
            for module in nodes
        ],
        multi=True

    )]

#### The app itself:

app.layout = html.Div([
    dbc.Row(active_node),
    dbc.Row( children=[
        dbc.Col(html.Div(["DART Module Discovery Tool"]), style={'textAlign': 'center','font-size':'40px'}, align='end', width=6),
        dbc.Col(html.Div(      
            dbc.Tabs([
                dbc.Tab(label="Home", tab_id='instructions'),
                dbc.Tab(label="Explore Categories", tab_id='categories'),
                dbc.Tab(label="Explore Pathways", tab_id='pathways'),
                dbc.Tab(label="Search", tab_id='search'),
            ],
            id="tab_options",
            active_tab="instructions"
            )
                ),  
            align='end')
    ]
    ),
    html.Hr(),
        dbc.Row(
            [
                dbc.Col(
                    children=[
                    dcc.Markdown("To learn more about a module, click on its node:"),
                    cyto.Cytoscape(
                    id='module_visualization',
                    layout={'name': 'cose'},
                    elements=edges+nodes,
                    stylesheet=default_stylesheet,
                    style={'width': '100%', 'height': '450px'},
                    userZoomingEnabled=False
                     )], width=6
                ),
                dbc.Col(html.Div(
                    children= dcc.Markdown("click on a tab to see what it does"),
                    id='tab_selection'
                    ),
                    width=6
                )],
            
        ),
    html.Hr(),   
    dbc.Row(
        [dbc.Col(html.Div(
                    children= dcc.Markdown("### Module details \n When you select a module, this panel will display information about that module. \n --- "),
                    id='module_details_panel'
                    ),
                    width=6
                ),
            dbc.Col(html.Div(my_modules_list), width=6),
        #dbc.Col(html.Div("My pathway display goes here. Use/create induced subgraph from selected modules?"), width=6)
        ]
    ),
    ### Stuff below here isn't front-end format yet
    html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),html.Hr(), html.Hr(), html.Hr(), html.Br(),html.Br(),html.Br(),

    dcc.Markdown("Select a module from the dropdown menu to select it on the graph."),
    dcc.Markdown("List of all modules:"),
    dcc.Dropdown(
        id='list_of_all_modules',
        options=[
            {'label': module["data"]["title"], 'value': module["data"]["id"]}
            for module in nodes
        ]

    )
    
],
            style={
            'padding' : '25px'
            },)

### Put all of the "update stylesheet" callbacks in one callback.
@app.callback(Output('module_visualization', 'stylesheet'),
              Input("my_modules", "value"),
              Input('author_selector', 'value'),
              Input('module_visualization', 'selectedNodeData'))
def update_stylesheet(selected_modules,author_name, data):
    new_stylesheet = default_stylesheet 
    if author_name:
        new_stylesheet += author_selected(author_name)

    ### If a node is selected, restyle it highlight it on the graph
    if data:
        module_id = data[0]["id"]
        selector = "[id *= \"" + module_id +"\"]" 
        deselector = "[id !*= \"" + module_id +"\"]" 
        highlight_selected_node = {
            'selector': selector,
            'style': {
                #'background-color': "red",
                'opacity': 1,
                'color': "black",
                'label': 'data(title)',
                "font-size": "30px",
                'width': "40px",
                'height': "40px"
            }
            }
        deselect_other_nodes = {
            'selector': deselector,
            'style': neutral_node_styling
            }
        new_stylesheet.append(highlight_selected_node)
        new_stylesheet.append(deselect_other_nodes)
        
        #### Not sure if edges need to be restated here, but they seem to be important...
        new_stylesheet.append({'selector': 'edge','style':neutral_edge_styling})
    # if selected_modules:
    #     new_stylesheet += highligh_my_modules(selected_modules)
    return new_stylesheet

### Keep track of the "active" node can dash.callback_context help? 
### Going to take some more work...
@app.callback(Output('active_node', 'children'),
              Input('module_visualization', 'selectedNodeData'),
              Input('list_of_all_modules', 'value')
              )
def get_active_node(data, value):
    if data:
        if value:
            return data[0]['id'] + value +ctx.triggered_id
        else:
            return data[0]['id'] + " no drop down value" + ctx.triggered_id
    elif value:
        return "no click data" + value +ctx.triggered_id
    else:
        return "no data at all" + ctx.triggered_id



### Don't display module data if no module is selected yet
@app.callback(Output('module_details_panel', 'children'),
              Input('module_visualization', 'selectedNodeData')
              )
def turn_on_module_details_panel(data):
    if data:
        return module_tab_content
    else:
        return dcc.Markdown("### Module details \n When you select a module, this panel will display information about that module. \n --- ")

### When a module node is selected (either clicked on or selected via a menu) information about it is displayed.
@app.callback(Output('selected_module_text', 'children'),
              Input('module_visualization', 'selectedNodeData')
              )
def displayTapNodeData(data):
    if data:
        learning_objectives = data[0]['learning_objectives']
        learning_objectives = learning_objectives.replace("&", "\n")
        return  "### [**" + data[0]['title'] + "**](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/"+ data[0]['id']+"/" +data[0]['id'] + ".md) \n \n  By " + data[0]['author'] +" \n \n Estimated length: " + data[0]['estimated_time_in_minutes']+". \n \n" + data[0]['comment'] + "\n \n" + learning_objectives + "\n --- \n "
    else:
        return "### Module details \n When you select a module, this panel will display information about that module. \n --- "

### When a module node is selected, the modules it links to appear in a drop down menu of their own.
@app.callback(Output('modules_incoming','options'),
                Input('module_visualization','selectedNodeData')
                )
def update_incoming_modules(data):
    new_options=[]
    if data: 
        for module in nodes:
            check_edge = {'data': {'source': data[0]["id"], 'target': module['data']['id']}}
            if check_edge in edges:
                new_options.append({'label': module['data']['title'], 'value': module['data']['id']})
    return new_options

### When a module node is selected, the modules that link to it appear in a drop down menu of their own.
@app.callback(Output('modules_outgoing','options'),
                Input('module_visualization','selectedNodeData')
                )
def update_incoming_modules(data):
    new_options=[]
    if data: 
        for module in nodes:
            check_edge = {'data': {'source': module['data']['id'], 'target': data[0]["id"]}}
            if check_edge in edges:
                new_options.append({'label': module['data']['title'], 'value': module['data']['id']})
    return new_options

### Update selected tab info when tabs are clicked:
@app.callback(
    Output("tab_selection", "children"), Input("tab_options", "active_tab")
)
def tab_content(active_tab):
    if active_tab  == "instructions":
        return instructions_tab_content
    elif active_tab == "categories":
        return categories_tab_content
    elif active_tab == "pathways":
        return pathways_tab_content
    elif active_tab == "search":
        return search_tab_content
    else:
        return dcc.Markdown("How did you turn off ALL of the tabs? time to debug something!")



### When a module is selected from the list of all modules, it becomes selected.
### TODO: When a module is selected from ANY dropdown menu it becomes selected
# @app.callback(Output('module_visualization', 'elements'),
#                 Input('list_of_all_modules', 'value'))
# def select_node_from_dropdown(id):
#     new_nodes=node_select(id)
#     return new_nodes+edges



if __name__ == '__main__':
    app.run_server(debug=True)

#### TODO CHECKLIST:
#### make all of the stylesheet updates a single callback that updates default_stylesheet rather than overwriting it 
### PROBLEM: IF EVERYTHING IS IN A SINGLE STYLESHEET, CALLBACK, THE CALLBACK WON'T WORK IF ONE OF THE INPUTS (EG AUTHOR) IS MISSING
#### Replace incoming and outgoing module dropdowns with dbc.Buttons
#### Make those buttons "select" the module noded
#### Ensure only one node can be selected (the active node?) at a time
        ### possibly acheived? Needs to be tested more thoroughly
#### Add a button to add the selected module to the "my modules" panel (or remove it if it is already there?)
#### Move node and edge data to another file so it can be automatically generated.