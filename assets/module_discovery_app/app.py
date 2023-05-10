from dash import Dash, html, Input, Output, dcc
import dash_bootstrap_components as dbc
import dash_cytoscape as cyto
import module_data 

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

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
            'time': df.loc[row,'time'], 
            'comment': df.loc[row,'comment'], 
            'long_description': df.loc[row,'long_description'],
            'Learning Objectives': df.loc[row,'Learning Objectives']
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
        edges.append({'data': {'source': linked_module, 'target': row, 'relationship': 'internal_link'}})



default_stylesheet = [
    {
        
        #### Have every node labeled with its title:
        'selector': 'node',
        'style': {
            #'background-color': '#BFD7B5',
            'label': 'data(title)',
        }
    },
    {
        
        #### Make nodes by my a different shape:
        'selector': '[author *= "Elizabeth Drellich"]',
        'style': {
            #'background-color': '#BFD7B5',
            'shape': 'square',
            'selected': True
        }
    }
    ,
    {
        
        #### Make nodes by my a different shape:
        'selector': '[author !*= "Elizabeth Drellich"]',
        'style': {
            #'background-color': '#BFD7B5',
            'shape': 'triangle',
            'opacity': 0.2
            
        }
    }
]

### Create a function that changes the stylesheet based on user inputs.

def author_selected(author_name):
    ### Create a stylesheet based on the selected author
    select_author_modules = []
    
    ### Turn on nodes corresponding to that author
    selection=str('[author *= "')+ str(author_name) + str('" ]')
    turned_on = {}
    turned_on['selector'] = selection
    turned_on['style'] = {'shape': 'square', 'color':'#BFD7B5', 'label': 'data(title)', 'color': '#000000'}
    select_author_modules.append(turned_on)

    ### Turn off nodes not corresponding to that author
    selection=str('[author !*= "')+ str(author_name) + str('" ]')
    turned_off = {}
    turned_off['selector'] = selection
    turned_off['style'] = {'shape': 'square', 'color':'#BFD7B5', 'opacity': 0.3}
    select_author_modules.append(turned_off)

    return select_author_modules


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

### What appears when the "Explore Categories" tab is clicked
categories_tab_content = [dcc.Markdown("### Content here for how to explore by categories. \n For example, maybe you want to see all of the modules by a particular author"),
                                dcc.Markdown("Pick an author to see their modules."),
    dcc.Dropdown(
    id='author_selector',
    #value='Joy Payton',
    clearable=True,
    options=[
        {'label': name, 'value': name}
        for name in ['Elizabeth Drellich', 'Joy Payton', 'Rose Franzen', 'Rose Hartman', 'Meredith Lee', 'Nicole Feldman', 'Ene Belleh', 'Peter Camacho']
    ]
),]

### What appears when the "Explore Pathways" tab is clicked
pathways_tab_content = [dcc.Markdown("content hear showing different pre-made pathways")]

### What appears when the "Search" tab is clicked
search_tab_content = [dcc.Markdown("search box to search for modules by entering a keyword")]


### Create My Modules lists:

my_modules_list = [
    dcc.Markdown("Select the modules you are interested in:"),
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
    dbc.Row( children=[
        dbc.Col(html.Div(["DART Module Discovery Tool"]), style={'textAlign': 'center','font-size':'40px'}, align='end', width=6),
        dbc.Col(html.Div(      
            dbc.Tabs([
                dbc.Tab(label="Explore Categories", tab_id='categories'),
                dbc.Tab(label="Explore Modules", tab_id='modules'),
                dbc.Tab(label="Explore Pathways", tab_id='pathways'),
                dbc.Tab(label="Search", tab_id='search'),
            ],
            id="tab_options",
            active_tab="modules"
            )
                ),  
            align='end')
    ]
    ),
    html.Hr(),
        dbc.Row(
            [
                dbc.Col(
                    cyto.Cytoscape(
                    id='module_visualization',
                    layout={'name': 'cose'},
                    elements=edges+nodes,
                    stylesheet=default_stylesheet,
                    style={'width': '100%', 'height': '450px'},
                    userZoomingEnabled=False
                     ), width=6
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
        [dbc.Col(html.Div(my_modules_list), width=6),
        dbc.Col(html.Div("My pathway display goes here. Use/create induced subgraph from selected modules?"), width=6)]
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

### When an author is selected from the dropdown menu, that author's modules are made darker and labeled.
@app.callback(Output('module_visualization', 'stylesheet'),
              Input('author_selector', 'value'))
def update_author_selection(author_name):
    return author_selected(author_name)


### When a module node is selected (either clicked on or selected via a menu) information about it is displayed.
@app.callback(Output('selected_module_text', 'children'),
              Input('module_visualization', 'selectedNodeData')
              )
def displayTapNodeData(data):
    if data:
        return  "### [**" + data[0]['title'] + "**](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/"+ data[0]['id']+"/" +data[0]['id'] + ".md) \n \n  By " + data[0]['author'] +" \n \n Estimated length: " + data[0]['time']+". \n \n" + data[0]['comment'] + "\n --- \n "
    else:
        return "### Click on a node in the graph to see information about that module. \n --- "

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
    if active_tab == "modules":
        return module_tab_content
    elif active_tab == "categories":
        return categories_tab_content
    elif active_tab == "pathways":
        return pathways_tab_content
    elif active_tab == "search":
        return search_tab_content
    else:
        return dcc.Markdown("How did you turn off ALL of the tabs? time to debug something!")


### When a module is selected in the my_module_list panel, it turns green in the graph and has its name turned on.
@app.callback(
    Output("module_visualization","stylesheet", allow_duplicate=True), [Input("my_modules", "value")], prevent_initial_call=True
)
def highligh_my_modules(my_modules):
    new_style_sheet= []
    for module in my_modules:
        selector = "[id *= \"" + module + "\"]"
        make_green = {
        'selector': selector,
        'style': {
            'background-color': "#454B1B",
            'shape': 'square',
            'color': "black",
            'label': 'data(title)'
        }
        }
        new_style_sheet.append(make_green)
    return new_style_sheet



### When a module is selected from the list of all modules, it becomes selected.
### TODO: When a module is selected from ANY dropdown menu it becomes selected
@app.callback(Output('module_visualization', 'elements'),
                Input('list_of_all_modules', 'value'))
def select_node_from_dropdown(id):
    new_nodes=node_select(id)
    return new_nodes+edges



if __name__ == '__main__':
    app.run_server(debug=True)

#### TODO CHECKLIST:
#### make all of the stylesheet updates a single callback that updates default_stylesheet rather than overwriting it
#### Replace incoming and outgoing module dropdowns with dbc.Buttons
#### Make those buttons "select" the module noded
#### Ensure only one node can be selected (the active node?) at a time
#### Add a button to add the selected module to the "my modules" panel (or remove it if it is already there?)
#### Move node and edge data to another file so it can be automatically generated.