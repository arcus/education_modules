from dash import Dash, html, Input, Output
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
        'data': {'id': short, 'title': title, 'author': author, 'time': time},
        ### Use classes here for all fo the data!!! 'classes': author
        #'position': {'x': 20*lat, 'y': -20*long}
    }
    for short, title, author, time in (
('bash_103_combining_commands', 'Bash: Combining Commands', 'Elizabeth Drellich and Nicole Feldman', '30 minutes'),
('bash_command_line_101', 'Bash / Command Line 101', 'Nicole Feldman and Elizabeth Drellich', '40 minutes'),
('bash_command_line_102', 'Bash: Searching and Organizing Files', 'Nicole Feldman and Elizabeth Drellich', '30 minutes'),
('bash_conditionals_loops', 'Bash: Conditionals and Loops', 'Elizabeth Drellich', '1 hour'),
('bash_scripts', 'Bash: Reusable Scripts', 'Elizabeth Drellich', '1 hour'),
('citizen_science', 'Citizen Science', 'Rose Hartman', '45 minutes'),
('data_management_basics', 'Research Data Management Basics', 'Ene Belleh', '40 minutes'),
('data_storage_models', 'Types of Data Storage Solutions', 'Nicole Feldman', ''),
('data_visualization_in_ggplot2', 'Data Visualization in ggplot2', 'Rose Hartman', '60 min'),
('data_visualization_in_open_source_software', 'Data Visualization in Open Source Software', 'Rose Hartman', '20 minutes'),
('data_visualization_in_seaborn', 'Data Visualization in seaborn', 'Rose Hartman', '1 hour'),
('database_normalization', 'Database Normalization', 'Joy Payton', '40 minutes'),
('demystifying_geospatial_data', 'Demystifying Geospatial Data', 'Elizabeth Drellich', '15 minutes'),
('demystifying_python', 'Demystifying Python', 'Meredith Lee', '20m'),
('demystifying_sql', 'Demystifying SQL', 'Peter Camacho', '40 minutes'),
('directories_and_file_paths', 'Directories and File Paths', 'Meredith Lee', '15m'),
('elements_of_maps', 'The Elements of Maps', 'Elizabeth Drellich', '45 minutes'),
('geocode_lat_long', 'Encoding Geospatial Data: Latitude and Longitude', 'Elizabeth Drellich', '15 minutes'),
('git_creation_and_tracking', 'Creating a Git Repository', 'Elizabeth Drellich', '1 hour'),
('git_history_of_project', 'Exploring the History of your Git Repository', 'Elizabeth Drellich', '30 minutes'),
('git_intro', 'Intro to Version Control', 'Rose Hartman', '10 min'),
('git_setup_mac_and_linux', 'Setting Up Git on Mac and Linux', 'Rose Hartman', '15 min'),
('git_setup_windows', 'Setting Up Git on Windows', 'Elizabeth Drellich', '25 min'),
('how_to_troubleshoot', 'How to Troubleshoot', 'Joy Payton', '30 minutes'),
('learning_to_learn', 'Learning to Learn Data Science', 'Rose Franzen', '20 minutes'),
('omics_orientation', 'Omics Orientation', 'Meredith Lee', '15m'),
('pandas_transform', 'Transform Data with pandas', 'Elizabeth Drellich', '1 hour'),
('python_basics_writing_python_code', 'Python Basics: Writing Python Code', 'Meredith Lee', '1 hour'),
('python_practice', 'Python Practice', 'Meredith Lee', '1 hour'),
('r_basics_introduction', 'R Basics: Introduction', 'Joy Payton', '1 hour'),
('r_basics_transform_data', 'R Basics: Transforming Data With dplyr', 'Joy Payton', '1 hour'),
('r_basics_visualize_data', 'R Basics: Visualizing Data With ggplot2', 'Joy Payton', '1 hour'),
('r_missing_values', 'Missing Values in R', 'Rose Hartman', '45 min'),
('r_practice', 'R Practice', 'Meredith Lee', '1 hour'),
('r_reshape_long_wide', 'Reshaping Data in R: Long and Wide Data', 'Joy Payton', '1 hour'),
('reproducibility', 'Reproducibility, Generalizability, and Reuse', 'Joy Payton', '1 hour'),
('sql_basics', 'SQL Basics', 'Peter Camacho', '1 hour'),
('sql_intermediate', 'SQL, Intermediate Level', 'Peter Camacho', '1 hour'),
('sql_joins', 'SQL Joins', 'Joy Payton', '1 hour'),
('statistical_tests', 'Statistical Tests in Open Source Software', 'Rose Hartman', '20 minutes (although reading through the linked tutorials may take much longer, depending on which tests you choose to read about)'),
('tidy_data', 'Tidy Data', 'Joy Payton', '45 minutes'),
('using_redcap_api', 'Using the REDCap API', 'Joy Payton', '1 hour')

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
    }
]


app.layout = html.Div([
    cyto.Cytoscape(
        id='cytoscape-event-callbacks-2',
        layout={'name': 'cose'},
        elements=edges+nodes,
        stylesheet=default_stylesheet,
        style={'width': '100%', 'height': '450px'}
    ),
    html.P(id='cytoscape-tapNodeData-output'),
    html.P(id='cytoscape-tapEdgeData-output'),
    html.P(id='cytoscape-mouseoverNodeData-output'),
    html.P(id='cytoscape-mouseoverEdgeData-output')
])


@app.callback(Output('cytoscape-tapNodeData-output', 'children'),
              Input('cytoscape-event-callbacks-2', 'tapNodeData'))
def displayTapNodeData(data):
    if data:
        return "You recently clicked/tapped the module: " + data['title'] + " which was written by " + data['author'] +"."


@app.callback(Output('cytoscape-tapEdgeData-output', 'children'),
              Input('cytoscape-event-callbacks-2', 'tapEdgeData'))
def displayTapEdgeData(data):
    if data:
        return "You recently clicked/tapped the edge between " + \
               data['source'].upper() + " and " + data['target'].upper()


@app.callback(Output('cytoscape-mouseoverNodeData-output', 'children'),
              Input('cytoscape-event-callbacks-2', 'mouseoverNodeData'))
def displayTapNodeData(data):
    if data:
        return "You recently hovered over the city: " + data['title']


@app.callback(Output('cytoscape-mouseoverEdgeData-output', 'children'),
              Input('cytoscape-event-callbacks-2', 'mouseoverEdgeData'))
def displayTapEdgeData(data):
    if data:
        return "You recently hovered over the edge between " + \
               data['source'].upper() + " and " + data['target'].upper()


if __name__ == '__main__':
    app.run_server(debug=True)
