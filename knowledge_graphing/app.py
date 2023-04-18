from dash import Dash, html, Input, Output, dcc
import dash_bootstrap_components as dbc
import dash_cytoscape as cyto

app = Dash(__name__)

styles = {
    'pre': {
        'border': 'thin lightgrey solid',
        'overflowX': 'scroll'
    }
}


nodes = [
    {
        'data': {'id': short, 'title': title, 'author': author, 'time': time, 'comment': comment},#'selected': True
        ### Use classes here for all fo the data!!! 'classes': author
        #'position': {'x': 20*lat, 'y': -20*long}
    }
    for short, title, author, time, comment in (
('bash_103_combining_commands', 'Bash: Combining Commands', 'Elizabeth Drellich and Nicole Feldman', '30 minutes','This module will teach you how to combine two or more commands in bash to create more complicated pipelines in Bash.'),
('bash_command_line_101', 'Bash / Command Line 101', 'Nicole Feldman and Elizabeth Drellich', '40 minutes','This course teaches learners to navigate their computer, as well as view and edit files, from the command line using Bash.'),
('bash_command_line_102', 'Bash: Searching and Organizing Files', 'Nicole Feldman and Elizabeth Drellich', '30 minutes','This module will teach you how to use the bash shell to search and organize your files.'),
('bash_conditionals_loops', 'Bash: Conditionals and Loops', 'Elizabeth Drellich', '1 hour','This module teaches you how to iterate through "for" loops and write conditional statements in Bash.'),
('bash_scripts', 'Bash: Reusable Scripts', 'Elizabeth Drellich', '1 hour','This module will teach you how to create and use simple Bash scripts to make repetitive tasks as simple as possible. '),
('citizen_science', 'Citizen Science', 'Rose Hartman', '45 minutes','This is an overview of citizen science for biomedical researchers.'),
('data_management_basics', 'Research Data Management Basics', 'Ene Belleh', '40 minutes','Learn the basics about research data management.'),
('data_storage_models', 'Types of Data Storage Solutions', 'Nicole Feldman', '','This course will focus on different data storage solutions available to an end user and the unique characteristics of each type. This course will also cover how each storage type impacts one\'s access to data and computing capabilities.'),
('data_visualization_in_ggplot2', 'Data Visualization in ggplot2', 'Rose Hartman', '60 min','This module includes code and explanations for several popular data visualizations, using R\'s ggplot2 package. It also includes examples of how to modify ggplot2 plots to customize them for different uses (e.g. adhering to journal requirements for visualizations).'),
('data_visualization_in_open_source_software', 'Data Visualization in Open Source Software', 'Rose Hartman', '20 minutes','Introduction to principles of data vizualization and typical data vizualization workflows using two common open source libraries: ggplot2 and seaborn.'),
('data_visualization_in_seaborn', 'Data Visualization in seaborn', 'Rose Hartman', '1 hour','This module includes code and explanations for several popular data visualizations using python\'s seaborn library. It also includes examples of how to modify seaborn plots to customize them for different uses.  '),
('database_normalization', 'Database Normalization', 'Joy Payton', '40 minutes','Learn about the concept of normalization and why it\'s important for organizing complicated data in relational databases.'),
('demystifying_geospatial_data', 'Demystifying Geospatial Data', 'Elizabeth Drellich', '15 minutes','This module is a brief introduction to geospatial (location) data.'),
('demystifying_python', 'Demystifying Python', 'Meredith Lee', '20m','This module introduces the Python programming language, explores why Python is useful in research, and describes how to download Python and Jupyter.'),
('demystifying_sql', 'Demystifying SQL', 'Peter Camacho', '40 minutes','SQL is a relational database solution that has been around for decades.  Learn more about this technology at a high level, without having to write code.'),
('directories_and_file_paths', 'Directories and File Paths', 'Meredith Lee', '15m','In this module, learners will explore what a directory is and how to describe the location of a file using its file path.   '),
('elements_of_maps', 'The Elements of Maps', 'Elizabeth Drellich', '45 minutes','This is a general overview of ways that geospatial data can be communicated visually using maps.'),
('geocode_lat_long', 'Encoding Geospatial Data: Latitude and Longitude', 'Elizabeth Drellich', '15 minutes','This is an introduction to latitude and longitude and the importance of geocoding - encoding geospatial data in the coordinate system.'),
('git_creation_and_tracking', 'Creating a Git Repository', 'Elizabeth Drellich', '1 hour','Create a new Git repository and get started with version control.'),
('git_history_of_project', 'Exploring the History of your Git Repository', 'Elizabeth Drellich', '30 minutes','This module will teach you how to look at past versions of your work on Git and compare your project with previous versions.'),
('git_intro', 'Intro to Version Control', 'Rose Hartman', '10 min','An introduction to what version control systems do and why you might want to use one.'),
('git_setup_mac_and_linux', 'Setting Up Git on Mac and Linux', 'Rose Hartman', '15 min','This module provides recommendations and examples to help new users configure git on their computer for the first time on a Mac or Linux computer.'),
('git_setup_windows', 'Setting Up Git on Windows', 'Elizabeth Drellich', '25 min','This module provides recommendations and examples to help new users configure Git on their Windows computer for the first time.'),
('how_to_troubleshoot', 'How to Troubleshoot', 'Joy Payton', '30 minutes','Learning to use technical methods like coding and version control in your research inevitably means running into problems.  Learn practical methods for troubleshooting and moving past error codes and other difficulties.'),
('learning_to_learn', 'Learning to Learn Data Science', 'Rose Franzen', '20 minutes','Discover how learning data science is different than learning other subjects.'),
('omics_orientation', 'Omics Orientation', 'Meredith Lee', '15m','This module provides a brief introduction to omics and its associated fields.'),
('pandas_transform', 'Transform Data with pandas', 'Elizabeth Drellich', '1 hour','This is an introduction to transforming data using a Python library named pandas.'),
('python_basics_writing_python_code', 'Python Basics: Writing Python Code', 'Meredith Lee', '1 hour','Learn the foundations of writing Python code.'),
('python_practice', 'Python Practice', 'Meredith Lee', '1 hour','Use the basics of Python coding, data transformation, and data visualization to work with real data. '),
('r_basics_introduction', 'R Basics: Introduction', 'Joy Payton', '1 hour','Introduction to R and hands-on first steps for brand new beginners.'),
('r_basics_transform_data', 'R Basics: Transforming Data With dplyr', 'Joy Payton', '1 hour','Learn how to transform (or wrangle) data using R\'s `dplyr` package.'),
('r_basics_visualize_data', 'R Basics: Visualizing Data With ggplot2', 'Joy Payton', '1 hour','Learn how to visualize data using R\'s `ggplot2` package.'),
('r_missing_values', 'Missing Values in R', 'Rose Hartman', '45 min','A practical demonstration of how missing values show up in R and how to deal with them. Note that this module does **not** cover statistical approaches for handling missing data, but instead focuses on the code you need to find, work with, and assign missing values in R.'),
('r_practice', 'R Practice', 'Meredith Lee', '1 hour','Use the basics of R coding, data transformation, and data visualization to work with real data. '),
('r_reshape_long_wide', 'Reshaping Data in R: Long and Wide Data', 'Joy Payton', '1 hour','A module that teaches how to reshape tabular data in R, concentrating on some typical shapes known as "long" and "wide" data.'),
('reproducibility', 'Reproducibility, Generalizability, and Reuse', 'Joy Payton', '1 hour','This module provides learners with an approachable introduction to the concepts and impact of **research reproducibility**, **generalizability**, and **data reuse**, and how technical approaches can help make these goals more attainable.'),
('sql_basics', 'SQL Basics', 'Peter Camacho', '1 hour','Structured Query Language, or SQL, is a relational database solution that has been around for decades.  Learn how to do basic SQL queries on single tables, by using code, hands-on.'),
('sql_intermediate', 'SQL, Intermediate Level', 'Peter Camacho', '1 hour','Learn how to do intermediate SQL queries on single tables, by using code, hands-on.'),
('sql_joins', 'SQL Joins', 'Joy Payton', '1 hour','Learn about SQL joins: what they accomplish, and how to write them.'),
('statistical_tests', 'Statistical Tests in Open Source Software', 'Rose Hartman', '20 minutes (although reading through the linked tutorials may take much longer, depending on which tests you choose to read about)','This module provides an overview of the most commonly used kinds of statistical tests and links to code for running many of them in both R and python.'),
('tidy_data', 'Tidy Data', 'Joy Payton', '45 minutes','Tidy is a technical term in data analysis and describes an optimal way for organizing data that will be analyzed computationally.'),
('using_redcap_api', 'Using the REDCap API', 'Joy Payton', '1 hour','REDCap is a research data capture tool used by many researchers in basic, translational, and clinical research efforts.  Learn how to use the REDCap API in this module.')


    )
]

edges = [
    {'data': {'source': source, 'target': target}}
    for source, target in (
        
       ('bash_103_combining_commands', 'bash_command_line_101'),
('bash_103_combining_commands', 'bash_command_line_102'),
('bash_103_combining_commands', 'directories_and_file_paths'),
('bash_command_line_101', 'directories_and_file_paths'),
('bash_command_line_101', 'git_setup_windows'),
('bash_command_line_102', 'bash_command_line_101'),
('bash_command_line_102', 'directories_and_file_paths'),
('bash_conditionals_loops', 'bash_command_line_101'),
('bash_conditionals_loops', 'bash_command_line_102'),
('bash_conditionals_loops', 'directories_and_file_paths'),
('bash_scripts', 'bash_command_line_101'),
('bash_scripts', 'reproducibility'),
('data_management_basics', 'reproducibility'),
('data_visualization_in_ggplot2', 'data_visualization_in_open_source_software'),
('data_visualization_in_ggplot2', 'data_visualization_in_seaborn'),
('data_visualization_in_ggplot2', 'r_basics_introduction'),
('data_visualization_in_ggplot2', 'statistical_tests'),
('data_visualization_in_open_source_software', 'data_visualization_in_ggplot2'),
('data_visualization_in_open_source_software', 'data_visualization_in_seaborn'),
('data_visualization_in_open_source_software', 'demystifying_python'),
('data_visualization_in_open_source_software', 'r_basics_introduction'),
('data_visualization_in_seaborn', 'data_visualization_in_ggplot2'),
('data_visualization_in_seaborn', 'demystifying_python'),
('data_visualization_in_seaborn', 'statistical_tests'),
('demystifying_python', 'bash_command_line_101'),
('demystifying_python', 'python_basics_writing_python_code'),
('demystifying_sql', 'reproducibility'),
('git_creation_and_tracking', 'git_setup_mac_and_linux'),
('git_creation_and_tracking', 'git_setup_windows'),
('git_history_of_project', 'git_creation_and_tracking'),
('git_setup_mac_and_linux', 'git_setup_windows'),
('git_setup_windows', 'git_setup_mac_and_linux'),
('learning_to_learn', 'reproducibility'),
('pandas_transform', 'python_basics_writing_python_code'),
('python_basics_writing_python_code', 'demystifying_python'),
('python_practice', 'data_visualization_in_seaborn'),
('python_practice', 'demystifying_python'),
('python_practice', 'pandas_transform'),
('python_practice', 'python_basics_writing_python_code'),
('python_practice', 'r_practice'),
('r_basics_introduction', 'r_basics_transform_data'),
('r_basics_introduction', 'r_basics_visualize_data'),
('r_basics_introduction', 'reproducibility'),
('r_basics_transform_data', 'r_basics_introduction'),
('r_basics_transform_data', 'r_basics_visualize_data'),
('r_basics_visualize_data', 'data_visualization_in_ggplot2'),
('r_basics_visualize_data', 'r_basics_introduction'),
('r_basics_visualize_data', 'r_basics_transform_data'),
('r_basics_visualize_data', 'tidy_data'),
('r_missing_values', 'r_basics_introduction'),
('r_missing_values', 'r_basics_transform_data'),
('r_practice', 'data_visualization_in_ggplot2'),
('r_practice', 'python_practice'),
('r_practice', 'r_basics_introduction'),
('r_practice', 'r_basics_transform_data'),
('r_reshape_long_wide', 'r_basics_introduction'),
('r_reshape_long_wide', 'r_basics_transform_data'),
('r_reshape_long_wide', 'tidy_data'),
('sql_basics', 'demystifying_sql'),
('sql_intermediate', 'demystifying_sql'),
('sql_intermediate', 'sql_basics'),
('sql_joins', 'database_normalization'),
('sql_joins', 'sql_basics'),
('sql_joins', 'sql_intermediate'),
('statistical_tests', 'data_visualization_in_open_source_software'),
('statistical_tests', 'python_basics_writing_python_code'),
('statistical_tests', 'r_basics_introduction'),
('tidy_data', 'reproducibility'),
('using_redcap_api', 'reproducibility')
    )
]


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
            selected_node.append(select_module)
        else:
            un_select_module = module
            un_select_module['selected'] = False
            non_selected_nodes.append(un_select_module)
    newly_selected_nodes = non_selected_nodes+selected_node
    return newly_selected_nodes

#### The app itself:

app.layout = html.Div([
    cyto.Cytoscape(
        id='module_visualization',
        layout={'name': 'cose'},
        elements=edges+nodes,
        stylesheet=default_stylesheet,
        style={'width': '100%', 'height': '450px'}
    ),
    dcc.Markdown("Pick an author to see their modules."),
    dcc.Dropdown(
    id='author_selector',
    #value='Joy Payton',
    clearable=True,
    options=[
        {'label': name, 'value': name}
        for name in ['Elizabeth Drellich', 'Joy Payton', 'Rose Franzen', 'Rose Hartman', 'Meredith Lee', 'Nicole Feldman', 'Ene Belleh', 'Peter Camacho']
    ]
),

    dcc.Markdown(id='selected_module_text'),

    dcc.Markdown("Select a module from the dropdown menu to select it on the graph."),
    dcc.Markdown("Modules that the selected module links to:"),
    dcc.Dropdown(
        id='modules_incoming',
        options=[
            {'label': module["data"]["title"], 'value': module["data"]["id"]}
            for module in nodes
        ]
    ),
        dcc.Markdown("Modules that link to the selected module:"),
    dcc.Dropdown(
        id='modules_outgoing',
        options=[
            #{'label': module["data"]["title"], 'value': module["data"]["id"]}
            #for module in nodes
        ]
    ),
    dcc.Markdown("List of all modules:"),
    dcc.Dropdown(
        id='list_of_all_modules',
        options=[
            {'label': module["data"]["title"], 'value': module["data"]["id"]}
            for module in nodes
        ]
    )
    
])

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
        return  "### [**" + data[0]['title'] + "**](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/"+ data[0]['id']+"/" +data[0]['id'] + ".md) \n \n  By " + data[0]['author'] +" \n \n Estimated length: " + data[0]['time']+". \n \n" + data[0]['comment'] + "\n #### Connected modules: \n "
    else:
        return "Click on a node in the graph to see information about that module."

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

### When a module is selected from the list of all modules, it becomes selected.
### TODO: When a module is selected from ANY dropdown menu it becomes selected
@app.callback(Output('module_visualization', 'elements'),
                Input('list_of_all_modules', 'value'))
def select_node_from_dropdown(id):
    new_nodes=node_select(id)
    return new_nodes+edges



if __name__ == '__main__':
    app.run_server(debug=True)
