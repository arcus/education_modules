import pandas as pd
df=pd.DataFrame()

df.loc["bash_103_combining_commands", "title"] = "Bash: Combining Commands"
df.loc["bash_103_combining_commands", "author"] = "Elizabeth Drellich and Nicole Feldman"
df.loc["bash_103_combining_commands", "estimated_time_in_minutes"] = "30 minutes"
df.loc["bash_103_combining_commands", "good_first_module"] = "false" 
df.loc["bash_103_combining_commands", "coding_required"] = "true"
df.loc["bash_103_combining_commands", "coding_language"] = "bash"
df.loc["bash_103_combining_commands", "coding_level"] = "intermediate"
df.loc["bash_103_combining_commands", "sequence_name"] = "Learn Bash"
df.loc["bash_103_combining_commands", "comment"] = "This module will teach you how to combine two or more commands in bash to create more complicated pipelines in Bash." 
df.loc["bash_103_combining_commands", "long_description"] = "This module is for learners who can use some basic Bash commands and want to learn to how to use the output of one command as the input for another command." 
df.loc["bash_103_combining_commands", "Learning Objectives"] = "&After completion of this module, learners will be able to:&&- Write the output of a command to a file using `>` and `>>`&- Chain commands directly using the pipe `|`&" 
df.loc["bash_103_combining_commands", "Prerequisties"] = "&Learners should be familiar with using a bash shell and [navigating a file system from the command line and look at the contents of a file](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/bash_command_line_101/bash_command_line_101.md).&&The only commands that will be assumed are the navigation commands `cd`, `ls`, and `pwd` and `cat`, all of which are explained in the [Bash / Command Line 101](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/bash_command_line_101/bash_command_line_101.md) module.&&" 
df.loc["bash_103_combining_commands", "Sets You Up For"] = "   bash_scripts  " 
df.loc["bash_103_combining_commands", "Depends On Knowledge In"] = "   bash_command_line_101   bash_command_line_102  " 
df.loc["bash_command_line_101", "title"] = "Bash / Command Line 101"
df.loc["bash_command_line_101", "author"] = "Nicole Feldman and Elizabeth Drellich"
df.loc["bash_command_line_101", "estimated_time_in_minutes"] = "40 minutes"
df.loc["bash_command_line_101", "good_first_module"] = "true" 
df.loc["bash_command_line_101", "coding_required"] = "true"
df.loc["bash_command_line_101", "coding_language"] = "bash"
df.loc["bash_command_line_101", "coding_level"] = "basic"
df.loc["bash_command_line_101", "sequence_name"] = "Learn Bash"
df.loc["bash_command_line_101", "comment"] = "This course teaches learners to navigate their computer, as well as view and edit files, from the command line using Bash." 
df.loc["bash_command_line_101", "long_description"] = "This course is designed to be both an introduction to bash / command line for those who are total newbies as well as refresher for those some with experience running code who want a more solid command of the basics." 
df.loc["bash_command_line_101", "Learning Objectives"] = "&After completion of this module, learners will be able to:&&- Describe what bash scripting is and why they might want to learn it for data management and research&- Navigate their file system using the bash shell&- View and edit the contents of a file from the bash shell&" 
df.loc["bash_command_line_101", "Prerequisties"] = "&Learners should be familiar with locating files and folders stored in a directory system.  Our [Directories and File Paths](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/directories_and_file_paths/directories_and_file_paths.md#1) module can provide some help with gaining these skills.&&" 
df.loc["bash_command_line_101", "Sets You Up For"] = "   bash_command_line_102   bash_103_combining_commands   bash_conditionals_loops   bash_scripts  " 
df.loc["bash_command_line_101", "Depends On Knowledge In"] = "   git_setup_windows  " 
df.loc["bash_command_line_102", "title"] = "Bash: Searching and Organizing Files"
df.loc["bash_command_line_102", "author"] = "Nicole Feldman and Elizabeth Drellich"
df.loc["bash_command_line_102", "estimated_time_in_minutes"] = "30 minutes"
df.loc["bash_command_line_102", "good_first_module"] = "false" 
df.loc["bash_command_line_102", "coding_required"] = "true"
df.loc["bash_command_line_102", "coding_language"] = "bash"
df.loc["bash_command_line_102", "coding_level"] = "basic"
df.loc["bash_command_line_102", "sequence_name"] = "Learn Bash"
df.loc["bash_command_line_102", "comment"] = "This module will teach you how to use the bash shell to search and organize your files." 
df.loc["bash_command_line_102", "long_description"] = "This module is for people who have a bit of experience with bash scripting and want to learn to use its power to organize their file and folders." 
df.loc["bash_command_line_102", "Learning Objectives"] = "&After completion of this module, learners will be able to:&&- Search existing files for particular character strings.&- Search folders for files with certain titles.&- Move files to new locations in a directory system.&- Copy files and directories.&- Delete files and directories.&" 
df.loc["bash_command_line_102", "Prerequisties"] = "&Learners should be familiar with using a bash shell to navigate a directory system. Learners will get the most out of this lesson if they can also create directories and files, write text to files, and read files from their bash shell command line interface.&&" 
df.loc["bash_command_line_102", "Sets You Up For"] = "   bash_103_combining_commands   bash_conditionals_loops   bash_scripts  " 
df.loc["bash_command_line_102", "Depends On Knowledge In"] = "   bash_command_line_101  " 
df.loc["bash_conditionals_loops", "title"] = "Bash: Conditionals and Loops"
df.loc["bash_conditionals_loops", "author"] = "Elizabeth Drellich"
df.loc["bash_conditionals_loops", "estimated_time_in_minutes"] = "1 hour"
df.loc["bash_conditionals_loops", "good_first_module"] = "false" 
df.loc["bash_conditionals_loops", "coding_required"] = "true"
df.loc["bash_conditionals_loops", "coding_language"] = "bash"
df.loc["bash_conditionals_loops", "coding_level"] = "intermediate"
df.loc["bash_conditionals_loops", "sequence_name"] = "Leanr Bash"
df.loc["bash_conditionals_loops", "comment"] = "This module teaches you how to iterate through +for+ loops and write conditional statements in Bash." 
df.loc["bash_conditionals_loops", "long_description"] = "This lesson teaches the basics of loops (for all x, do y) and conditional statements (if x is true, do y) in Bash. Since the grammar of Bash can be non-intuitive this module is appropriate both for learners who have experience with conditionals and loops in other languages, as well as learners who are learning about these kinds of commands for the first time." 
df.loc["bash_conditionals_loops", "Learning Objectives"] = "&After completion of this module, learners will be able to:&&- Understand how a +for loop+ works&- Write a +for loop+ in Bash  &- Understand how an +if/then+ statement works&- Recognize and reuse +if/then+ statements in Bash&&" 
df.loc["bash_conditionals_loops", "Prerequisties"] = "&Only basic exposure to Bash is expected. The following is a list of actions and commands that will be used without explanation in this module. Each includes a link to help you brush up on the commands or learn them for the first time.&&* [Navigating](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/bash_command_line_101/bash_command_line_101.md) a filesystem from a command line interface&* Reading the contents of files with [`cat`](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/bash_command_line_101/bash_command_line_101.md#15)&* Writing text to files with [`echo` and `>>`](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/bash_command_line_101/bash_command_line_101.md#14)&* Matching character strings with the [character wildcard `*`](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/bash_command_line_102/bash_command_line_102.md#4)&&" 
df.loc["bash_conditionals_loops", "Depends On Knowledge In"] = "   bash_command_line_101   bash_command_line_102  " 
df.loc["bash_scripts", "title"] = "Bash: Reusable Scripts"
df.loc["bash_scripts", "author"] = "Elizabeth Drellich"
df.loc["bash_scripts", "estimated_time_in_minutes"] = "1 hour"
df.loc["bash_scripts", "good_first_module"] = "false" 
df.loc["bash_scripts", "coding_required"] = "true"
df.loc["bash_scripts", "coding_language"] = "bash"
df.loc["bash_scripts", "coding_level"] = "intermediate"
df.loc["bash_scripts", "sequence_name"] = "Learn Bash"
df.loc["bash_scripts", "comment"] = "This module will teach you how to create and use simple Bash scripts to make repetitive tasks as simple as possible. " 
df.loc["bash_scripts", "long_description"] = "If you have some experience with Bash and want to learn how to save and reuse Bash processes, this lesson will teach you how to write your own Bash scripts and understand and use simple scripts written by others." 
df.loc["bash_scripts", "Learning Objectives"] = "&After completion of this module, learners will be able to:&&- Identify the structure of a Bash script&- Run existing Bash scripts&- Write simple Bash scripts&" 
df.loc["bash_scripts", "Prerequisties"] = "&Learners should be familiar with using a Bash shell to navigate a directory system. Learners will get the most out of this lesson if they can also create directories and files, write text to files, and read files from their Bash shell command line interface.&&Bash commands that will be used without explanation include:&&- `ls`&- `cat`&- `>` and `>>`&- `echo`&- `grep`&- `wc`&&" 
df.loc["bash_scripts", "Sets You Up For"] = "   bash_scripts  " 
df.loc["bash_scripts", "Depends On Knowledge In"] = "   bash_command_line_101   bash_command_line_102   bash_103_combining_commands  " 
df.loc["citizen_science", "title"] = "Citizen Science"
df.loc["citizen_science", "author"] = "Rose Hartman"
df.loc["citizen_science", "estimated_time_in_minutes"] = "45 minutes"
df.loc["citizen_science", "good_first_module"] = "true" 
df.loc["citizen_science", "comment"] = "This is an overview of citizen science for biomedical researchers." 
df.loc["citizen_science", "long_description"] = "This module covers the what, who, why, and how of citizen science research: what citizen science is, who volunteers, why citizen science might be a good choice for your research, and options for how to get started. Throughout, it highlights several examples of real citizen science projects being used in biomedical research and related fields. No prior knowledge is assumed." 
df.loc["citizen_science", "Learning Objectives"] = "&After completion of this module, learners will be able to:&&- list several ways members of the public can contribute to scientific projects&- recognize several different factors that motivate people to volunteer in citizen science&- identify research questions that may be a particularly good fit for citizen science&- examine published materials from citizen science projects for things like policies on collaboration and strategies for implementation&&" 
df.loc["citizen_science", "Prerequisties"] = "&None&&" 
df.loc["data_management_basics", "title"] = "Research Data Management Basics"
df.loc["data_management_basics", "author"] = "Ene Belleh"
df.loc["data_management_basics", "estimated_time_in_minutes"] = "40 minutes"
df.loc["data_management_basics", "good_first_module"] = "false" 
df.loc["data_management_basics", "comment"] = "Learn the basics about research data management." 
df.loc["data_management_basics", "long_description"] = "If you conduct research or work with research data or researchers, it's likely that research data management topics affect you.  Learn what research data management is, how to think about it in a structured way, and understand its scientific importance." 
df.loc["data_management_basics", "Learning Objectives"] = "&After completion of this module, learners will be able to:&&- Define research data management&- Explain why data management forms an important part of the responsible conduct of research&- Explain how various research stakeholders share responsibility for research data management&- Give examples of research data management tasks within various stages of the research lifecycle&&" 
df.loc["data_management_basics", "Prerequisties"] = "&The only pre-requisite suggested for this module is experience working in research in any capacity.&&" 
df.loc["data_management_basics", "Depends On Knowledge In"] = "   reproducibility  " 
df.loc["data_storage_models", "title"] = "Types of Data Storage Solutions"
df.loc["data_storage_models", "author"] = "Nicole Feldman"
df.loc["data_storage_models", "estimated_time_in_minutes"] = ""
df.loc["data_storage_models", "comment"] = "This course will focus on different data storage solutions available to an end user and the unique characteristics of each type. This course will also cover how each storage type impacts one's access to data and computing capabilities." 
df.loc["data_storage_models", "long_description"] = "This module is for people interested in understanding the types of data storage solutions available to them at their institution and why they might want to store their files or perform certain computational tasks in each." 
df.loc["data_storage_models", "Learning Objectives"] = "&After completion of this module, learners will be able to:&&- Identify and describe different data storage solutions&- Understand the benefits and the limitations of each covered storage solution&- Describe what computational tasks are best suited to the described data storage types&- Know the upfront costs and ongoing maintenance the various storage solutions require&&" 
df.loc["data_visualization_in_ggplot2", "title"] = "Data Visualization in ggplot2"
df.loc["data_visualization_in_ggplot2", "author"] = "Rose Hartman"
df.loc["data_visualization_in_ggplot2", "estimated_time_in_minutes"] = "60 min"
df.loc["data_visualization_in_ggplot2", "comment"] = "This module includes code and explanations for several popular data visualizations, using R's ggplot2 package. It also includes examples of how to modify ggplot2 plots to customize them for different uses (e.g. adhering to journal requirements for visualizations)." 
df.loc["data_visualization_in_ggplot2", "long_description"] = "You can use the ggplot2 library in R to make many different kinds of data visualizations (also called plots, or charts), including scatterplots, histograms, line plots, and trend lines. This module provides an example of each of these kinds of plots, including R code to make them using the ggplot2 library. It may be hard to follow if you are brand new to R, but it is appropriate for beginners with at least a small amount of R experience." 
df.loc["data_visualization_in_ggplot2", "Learning Objectives"] = "&After completion of this module, learners will be able to:&&- use ggplot2 to create several common data visualizations&- customize some elements of a plot, and know where to look to learn how to customize others&&" 
df.loc["data_visualization_in_open_source_software", "title"] = "Data Visualization in Open Source Software"
df.loc["data_visualization_in_open_source_software", "author"] = "Rose Hartman"
df.loc["data_visualization_in_open_source_software", "estimated_time_in_minutes"] = "20 minutes"
df.loc["data_visualization_in_open_source_software", "good_first_module"] = "false" 
df.loc["data_visualization_in_open_source_software", "comment"] = "Introduction to principles of data vizualization and typical data vizualization workflows using two common open source libraries: ggplot2 and seaborn." 
df.loc["data_visualization_in_open_source_software", "long_description"] = "This module introduces ggplot2 and seaborn, popular data visualization libraries in R and python, respectively. It lays the groundwork for using ggplot2 and seaborn by 1) highlighting common features of plots that can be manipulated in plot code, 2) discussing a typical data visualization workflow and best practices, and 3) discussing data preparation for plotting. This content will be most useful for people who have some experience creating data visualizations and/or reading plots presented in research articles or similar contexts. Some prior exposure to R and/or python is helpful but not required. This is appropriate for beginners." 
df.loc["data_visualization_in_open_source_software", "Learning Objectives"] = "&After completion of this module, learners will be able to:&&* identify key elements in a plot that communicate information about the data&* describe the role ggplot2 and seaborn play in the R and python programming languages, respectively&* describe a typical data vizualization workflow&* list some best practices for creating accessible vizualizations&&" 
df.loc["data_visualization_in_open_source_software", "Prerequisties"] = "&This module assumes some familiarity with data and statistics, in particular&&* familiarity with some different kinds of plots, although deep understanding is not needed --- people who are used to seeing plots presented in research articles will be sufficiently prepared&* the distinction between [continuous and categorical variables](https://education.arcus.chop.edu/variable-types/)&&This module also assumes some basic familiarity with either R or python, but is appropriate for beginners.&&" 
df.loc["data_visualization_in_open_source_software", "Sets You Up For"] = "   data_visualization_in_ggplot2   data_visualization_in_seaborn  " 
df.loc["data_visualization_in_open_source_software", "Depends On Knowledge In"] = " " 
df.loc["data_visualization_in_seaborn", "title"] = "Data Visualization in seaborn"
df.loc["data_visualization_in_seaborn", "author"] = "Rose Hartman"
df.loc["data_visualization_in_seaborn", "estimated_time_in_minutes"] = "1 hour"
df.loc["data_visualization_in_seaborn", "good_first_module"] = "false" 
df.loc["data_visualization_in_seaborn", "coding_required"] = "true"
df.loc["data_visualization_in_seaborn", "coding_language"] = "Python"
df.loc["data_visualization_in_seaborn", "coding_level"] = "intermediate"
df.loc["data_visualization_in_seaborn", "sequence_name"] = "Python"
df.loc["data_visualization_in_seaborn", "comment"] = "This module includes code and explanations for several popular data visualizations using python's seaborn library. It also includes examples of how to modify seaborn plots to customize them for different uses.  " 
df.loc["data_visualization_in_seaborn", "long_description"] = "You can use the seaborn module in python to make many different kinds of data visualizations (also called plots or charts), including scatterplots, histograms, line plots, and trend lines. This module provides an example of each of these kinds of plots, including python code to make them using the seaborn module. It may be hard to follow if you are brand new to python, but it is appropriate for beginners with at least a small amount of python experience." 
df.loc["data_visualization_in_seaborn", "Learning Objectives"] = "&After completion of this module, learners will be able to:&&- use seaborn to create several common data visualizations&- customize some elements of a plot, and know where to look to learn how to customize others&&" 
df.loc["data_visualization_in_seaborn", "Prerequisties"] = "&This module assumes some familiarity with statistical concepts like distributions, outliers, and linear regression, but even if you don't understand those concepts well you should be able to learn and apply the data visualization content.&When statistical concepts are referenced in the lesson, links to learn more are generally provided.&&This module also assumes some basic familiarity with python, including&&* installing and importing python modules&* reading in data&* manipulating data frames, including calculating new columns&&If you are brand new to python (or want a refresher) consider starting with [Demystifying Python](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/demystifying_python/demystifying_python.md) first.&&" 
df.loc["data_visualization_in_seaborn", "Sets You Up For"] = "   python_practice  " 
df.loc["data_visualization_in_seaborn", "Depends On Knowledge In"] = "   demystifying_python   python_basics_writing_python_code   pandas_transform  " 
df.loc["database_normalization", "title"] = "Database Normalization"
df.loc["database_normalization", "author"] = "Joy Payton"
df.loc["database_normalization", "estimated_time_in_minutes"] = "40 minutes"
df.loc["database_normalization", "good_first_module"] = "false" 
df.loc["database_normalization", "sequence_name"] = "SQL"
df.loc["database_normalization", "comment"] = "Learn about the concept of normalization and why it's important for organizing complicated data in relational databases." 
df.loc["database_normalization", "long_description"] = "Usually, data in a relational database like SQL is organized into multiple interrelated tables with as little data repetition as possible. This concept can be useful to apply in other areas as well, such as organizing data in .csvs or in data frames in R or Python.  This module teaches underlying data considerations and explains how data can be efficiently organized by introducing the concepts of one-to-many data relationships and normalization." 
df.loc["database_normalization", "Learning Objectives"] = "After completion of this module, learners will be able to:&&- Explain the significance of +one to many+ data relationships and how these relationships affect data organization&- Describe how a normalized database is typically organized&- Explain how data can be linked between tables and define +primary keys+ and +foreign keys+&&" 
df.loc["database_normalization", "Prerequisties"] = "&Learners should have experience working with data in tables.  This could included working with .csv files, SQL databases, R data frames, REDCap instruments, or other ways that data can be collected in tables. &&" 
df.loc["database_normalization", "Sets You Up For"] = "   sql_joins  " 
df.loc["demystifying_geospatial_data", "title"] = "Demystifying Geospatial Data"
df.loc["demystifying_geospatial_data", "author"] = "Elizabeth Drellich"
df.loc["demystifying_geospatial_data", "estimated_time_in_minutes"] = "15 minutes"
df.loc["demystifying_geospatial_data", "comment"] = "This module is a brief introduction to geospatial (location) data." 
df.loc["demystifying_geospatial_data", "long_description"] = "This module will survey some of the benefits of using geospatial data for research purposes. No previous exposure to geospatial data is expected. If you have any interest in maps or are wondering if using geospatial data might be helpful for your work, this lesson is designed to help you decide whether learning more about geospatial techniques is right for you and your project." 
df.loc["demystifying_geospatial_data", "Learning Objectives"] = "&After completion of this module, learners will be able to:&&- Define geospatial data&- Describe some of the benefits of using geospatial data&- Recognize some of the issues learners may encounter when using geospatial data&&" 
df.loc["demystifying_python", "title"] = "Demystifying Python"
df.loc["demystifying_python", "author"] = "Meredith Lee"
df.loc["demystifying_python", "estimated_time_in_minutes"] = "20m"
df.loc["demystifying_python", "comment"] = "This module introduces the Python programming language, explores why Python is useful in research, and describes how to download Python and Jupyter." 
df.loc["demystifying_python", "long_description"] = "Python is a versatile programming language that is frequently used for data analysis, machine learning, web development, and more. If you are interested in using Python (or even just trying it out), and are looking for how to get set up, this module is a good place to start. This is appropriate for someone at the beginner level, including those with no prior knowledge of or experience with Python." 
df.loc["demystifying_python", "Learning Objectives"] = "&After completion of this module, learners will be able to:&&- Describe what Python is and why they might want to use it for research&- Identify several ways to write Python code&- Understand the purpose and utility of a Jupyter notebook&- Download Python and Jupyter, and access a Python notebook in Google Colab&&" 
df.loc["demystifying_sql", "title"] = "Demystifying SQL"
df.loc["demystifying_sql", "author"] = "Peter Camacho"
df.loc["demystifying_sql", "estimated_time_in_minutes"] = "40 minutes"
df.loc["demystifying_sql", "comment"] = "SQL is a relational database solution that has been around for decades.  Learn more about this technology at a high level, without having to write code." 
df.loc["demystifying_sql", "long_description"] = "Do you have colleagues who use SQL or refer to +databases+ or +the data warehouse+ and you're not sure what it all means?  This module will give you some very high level explanations to help you understand what SQL is and some basic concepts for working with it.  There is no code or hands-on application in this module, so it's appropriate for people who have zero experience and want an overview of SQL." 
df.loc["demystifying_sql", "Learning Objectives"] = "&After completion of this module, learners will be able to:&&- Define the acronym +SQL+&- Explain the basic organization of data in relational databases&- Explain what +relational+ means in the phrase +relational database+&- Give an example of what kinds of tasks SQL is ideal for&&" 
df.loc["directories_and_file_paths", "title"] = "Directories and File Paths"
df.loc["directories_and_file_paths", "author"] = "Meredith Lee"
df.loc["directories_and_file_paths", "estimated_time_in_minutes"] = "15m"
df.loc["directories_and_file_paths", "comment"] = "In this module, learners will explore what a directory is and how to describe the location of a file using its file path.   " 
df.loc["directories_and_file_paths", "long_description"] = "When doing data analysis in a programming language like R or Python, figuring out how to point the program to the file you need can be confusing. This module will help you learn about how files and folders are organized on your computer, how to describe the location of your file in a couple of different ways, and name files and folders in a descriptive and systematic way." 
df.loc["directories_and_file_paths", "Learning Objectives"] = "&After completion of this module, learners will be able to:&&- Describe what a directory is&- Distinguish between a relative file path and an absolute file path&- Describe the location of a file using its file path&- Describe a few best practices and conventions of naming files and folders&&" 
df.loc["elements_of_maps", "title"] = "The Elements of Maps"
df.loc["elements_of_maps", "author"] = "Elizabeth Drellich"
df.loc["elements_of_maps", "estimated_time_in_minutes"] = "45 minutes"
df.loc["elements_of_maps", "comment"] = "This is a general overview of ways that geospatial data can be communicated visually using maps." 
df.loc["elements_of_maps", "long_description"] = "Raw geospatial data can be particularly tricky for humans to read. However the shapes, colors, sizes, symbols, and language that make up a good map can effectively communicate a variety of detailed data even to readers looking at the map with only minimum specialized background knowledge. This module will demystify how raw data becomes a map and explain common components of maps. It is appropriate for anyone considering making maps from geospatial data." 
df.loc["elements_of_maps", "Learning Objectives"] = "&After completion of this module, learners will be able to:&&- recognize the elements of maps&- describe types of maps that focus on particular elements.&&" 
df.loc["geocode_lat_long", "title"] = "Encoding Geospatial Data: Latitude and Longitude"
df.loc["geocode_lat_long", "author"] = "Elizabeth Drellich"
df.loc["geocode_lat_long", "estimated_time_in_minutes"] = "15 minutes"
df.loc["geocode_lat_long", "comment"] = "This is an introduction to latitude and longitude and the importance of geocoding - encoding geospatial data in the coordinate system." 
df.loc["geocode_lat_long", "long_description"] = "If you use any geospatial data, such as patient or participant addresses, it is important that that location data be in a usable form. This means using the same coordinate system that Global Positioning Systems use: latitude and longitude. This module is appropriate, as either an introduction or review, for anyone considering using geospatial data in their analysis. " 
df.loc["geocode_lat_long", "Learning Objectives"] = "&After completion of this module, learners will be able to:&&- Understand the importance of geocoding addresses&- Understand the latitude and longitude coordinate system&- Geocode single addresses.  &&" 
df.loc["git_creation_and_tracking", "title"] = "Creating a Git Repository"
df.loc["git_creation_and_tracking", "author"] = "Elizabeth Drellich"
df.loc["git_creation_and_tracking", "estimated_time_in_minutes"] = "1 hour"
df.loc["git_creation_and_tracking", "good_first_module"] = "false" 
df.loc["git_creation_and_tracking", "coding_required"] = "true"
df.loc["git_creation_and_tracking", "coding_language"] = "git"
df.loc["git_creation_and_tracking", "coding_level"] = "basic"
df.loc["git_creation_and_tracking", "sequence_name"] = "Git"
df.loc["git_creation_and_tracking", "comment"] = "Create a new Git repository and get started with version control." 
df.loc["git_creation_and_tracking", "long_description"] = "If you have Git set up on your computer and are ready to start tracking your files, then this module is for you. This module will teach you how to create a Git repository, add files to it, update files in it, and keep track of those changes in a clear and organized manner." 
df.loc["git_creation_and_tracking", "Learning Objectives"] = "&After completion of this module, learners will be able to:&&- Create a Git repository&- Add and make changes to files in the repository&- Write short helpful descriptions, called +commit messages+ to track the changes&- Use `.gitignore`&- Understand the `add` and `commit` workflow.&&&" 
df.loc["git_creation_and_tracking", "Prerequisties"] = "&Before you start this module, make sure you&&* Know how to access a command line interface (CLI) on your computer.&* Have Git configured on your computer. If Git is not yet configured, see the module on setting up Git on a [Mac, Linux](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/git_setup_mac_and_linux/git_setup_mac_and_linux.md), or [Windows](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/git_setup_windows/git_setup_windows.md) machine.&* Can edit plain text `.txt` documents. A text editor is different from a word processor (i.e. Microsoft Word or Google Docs), in that text editors create files that consist only of text, no formatting at all. Here is a [tutorial on editing text files using `nano`](https://swcarpentry.github.io/shell-novice/03-create/#create-a-text-file), one of many text editors that you can access directly from the command line interface (CLI).&&" 
df.loc["git_creation_and_tracking", "Sets You Up For"] = "   git_history_of_project  " 
df.loc["git_creation_and_tracking", "Depends On Knowledge In"] = "   git_setup_windows   git_setup_mac_and_linux  " 
df.loc["git_history_of_project", "title"] = "Exploring the History of your Git Repository"
df.loc["git_history_of_project", "author"] = "Elizabeth Drellich"
df.loc["git_history_of_project", "estimated_time_in_minutes"] = "30 minutes"
df.loc["git_history_of_project", "good_first_module"] = "false" 
df.loc["git_history_of_project", "coding_required"] = "true"
df.loc["git_history_of_project", "coding_language"] = "git"
df.loc["git_history_of_project", "coding_level"] = "basic"
df.loc["git_history_of_project", "sequence_name"] = "Git"
df.loc["git_history_of_project", "comment"] = "This module will teach you how to look at past versions of your work on Git and compare your project with previous versions." 
df.loc["git_history_of_project", "long_description"] = "You know that version control is important. You know how to save your work to your Git repository. Now you are ready to look at and compare different versions of your work. In this module you will you will learn how to navigate through the commits you have made to Git. You will also learn how to compare current code with past code." 
df.loc["git_history_of_project", "Learning Objectives"] = "After completion of this module, learners will be able to:&&- Identify and use the `HEAD` of a repository.&- Identify and use Git commit numbers.&- Compare versions of tracked files.&&" 
df.loc["git_history_of_project", "Prerequisties"] = "&To best learn from this module make sure that you:&&* have Git configured on your computer,&* can view and edit `.txt` files, and&* can make changes to a Git repository using `add` and `commit` from a command line interface (CLI).&&" 
df.loc["git_history_of_project", "Depends On Knowledge In"] = "   git_setup_windows   git_setup_mac_and_linux   git_creation_and_tracking  " 
df.loc["git_intro", "title"] = "Intro to Version Control"
df.loc["git_intro", "author"] = "Rose Hartman"
df.loc["git_intro", "estimated_time_in_minutes"] = "10 min"
df.loc["git_intro", "comment"] = "An introduction to what version control systems do and why you might want to use one." 
df.loc["git_intro", "long_description"] = "Version control systems allow you to keep track of the history of changes to a text document (e.g. writing, code, and more). Version control is an increasingly important tool for scientists and scientific writers of all disciplines; it has the potential to make your work more transparent, more reproducible, and more efficient. This module is appropriate for beginners with no previous exposure to version control." 
df.loc["git_intro", "Learning Objectives"] = "&After completion of this module, learners will be able to:&&- Understand the benefits of an automated version control system&- Understand the basics of how automated version control systems work&&" 
df.loc["git_setup_mac_and_linux", "title"] = "Setting Up Git on Mac and Linux"
df.loc["git_setup_mac_and_linux", "author"] = "Rose Hartman"
df.loc["git_setup_mac_and_linux", "estimated_time_in_minutes"] = "15 min"
df.loc["git_setup_mac_and_linux", "good_first_module"] = "false" 
df.loc["git_setup_mac_and_linux", "coding_required"] = "true"
df.loc["git_setup_mac_and_linux", "coding_language"] = "git"
df.loc["git_setup_mac_and_linux", "coding_level"] = "getting started"
df.loc["git_setup_mac_and_linux", "sequence_name"] = "Git"
df.loc["git_setup_mac_and_linux", "comment"] = "This module provides recommendations and examples to help new users configure git on their computer for the first time on a Mac or Linux computer." 
df.loc["git_setup_mac_and_linux", "long_description"] = "If you're ready to start using the Git version control system, this lesson will walk you through how to get set up. This lesson should be a good fit for people who already have an idea of what version control is (although may not have any experience using it yet), and know how to open the command line interface (CLI) on their computer. No previous experience with Git is expected." 
df.loc["git_setup_mac_and_linux", "Learning Objectives"] = "&After completion of this module, learners will be able to:&&- Configure `git` the first time it is used on a computer&- Understand the meaning of the `--global` configuration flag&&" 
df.loc["git_setup_mac_and_linux", "Prerequisties"] = "&- Have used the command line interface (CLI) on your computer before&- Have Git installed on your computer (note that it is probably installed already even if you've never used it)&- Have an account on github.com (you can [sign up now](https://github.com/signup) if you haven't yet --- it's free)&&" 
df.loc["git_setup_mac_and_linux", "Sets You Up For"] = "   git_creation_and_tracking   git_history_of_project  " 
df.loc["git_setup_windows", "title"] = "Setting Up Git on Windows"
df.loc["git_setup_windows", "author"] = "Elizabeth Drellich"
df.loc["git_setup_windows", "estimated_time_in_minutes"] = "25 min"
df.loc["git_setup_windows", "good_first_module"] = "false" 
df.loc["git_setup_windows", "coding_required"] = "true"
df.loc["git_setup_windows", "coding_language"] = "git"
df.loc["git_setup_windows", "coding_level"] = "getting started"
df.loc["git_setup_windows", "sequence_name"] = "Git"
df.loc["git_setup_windows", "comment"] = "This module provides recommendations and examples to help new users configure Git on their Windows computer for the first time." 
df.loc["git_setup_windows", "long_description"] = "If you're ready to start using the Git version control system, this lesson will walk you through how to get set up. This lesson should be a good fit for people who already have an idea of what version control is but may not have any experience using it yet. No previous experience with Git is expected. This lesson is specific to Windows machines, If you are using Mac or Linux, please follow along with the [set-up guide for those computers](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/git_setup_mac_and_linux/git_setup_mac_and_linux.md)." 
df.loc["git_setup_windows", "Learning Objectives"] = "&After completion of this module, learners will be able to:&&- Configure `git` the first time it is used on a computer&- Understand the meaning of the `--global` configuration flag&&" 
df.loc["git_setup_windows", "Prerequisties"] = "&- Have an account on github.com (you can [sign up now](https://github.com/signup) if you haven't yet --- it's free)&&" 
df.loc["git_setup_windows", "Sets You Up For"] = "   git_creation_and_tracking   git_history_of_project   bash_command_line_101  " 
df.loc["how_to_troubleshoot", "title"] = "How to Troubleshoot"
df.loc["how_to_troubleshoot", "author"] = "Joy Payton"
df.loc["how_to_troubleshoot", "estimated_time_in_minutes"] = "30 minutes"
df.loc["how_to_troubleshoot", "comment"] = "Learning to use technical methods like coding and version control in your research inevitably means running into problems.  Learn practical methods for troubleshooting and moving past error codes and other difficulties." 
df.loc["how_to_troubleshoot", "long_description"] = "When technical methods, such as writing code, using version control, and creating data visualizations are used, there will moments when a cryptic error message appears or the code simply doesn't do what it was intended to do.  This module will help people at various levels of technical expertise learn how to troubleshoot in tech more effectively." 
df.loc["how_to_troubleshoot", "Learning Objectives"] = "&After completion of this module, learners will be able to:&&- Describe technical problems more effectively&- Explain why a +reproducible example+ is critical to asking for help&- Find potentially helpful answers in Stack Overflow&&&" 
df.loc["learning_to_learn", "title"] = "Learning to Learn Data Science"
df.loc["learning_to_learn", "author"] = "Rose Franzen"
df.loc["learning_to_learn", "estimated_time_in_minutes"] = "20 minutes"
df.loc["learning_to_learn", "comment"] = "Discover how learning data science is different than learning other subjects." 
df.loc["learning_to_learn", "long_description"] = "The process of learning data science can be different from that of learning other subjects. This module goes over some of those differences and provides advice for navigating this potentially unfamiliar territory." 
df.loc["learning_to_learn", "Learning Objectives"] = "&After completion of this module, learners will be able to:&&- recognize ways in which learning data science and coding may be different than other educational experiences&- identify ways to extend their learning beyond module content&- recognize how to understand when to ask for help&&" 
df.loc["omics_orientation", "title"] = "Omics Orientation"
df.loc["omics_orientation", "author"] = "Meredith Lee"
df.loc["omics_orientation", "estimated_time_in_minutes"] = "15m"
df.loc["omics_orientation", "comment"] = "This module provides a brief introduction to omics and its associated fields." 
df.loc["omics_orientation", "long_description"] = "Omics is a wide-reaching field, with many different subfields. This module aims to disambiguate several omics-related terms and topics, discuss some of the most popular omics research fields, and examine the challenges of and caveats for omics research." 
df.loc["omics_orientation", "Learning Objectives"] = "&After completion of this module, learners will be able to:&&- Define what omics is and explain why a researcher might choose an omics approach&- Identify several popular omics domains&- Describe some challenges and caveats of omics research&&&" 
df.loc["pandas_transform", "title"] = "Transform Data with pandas"
df.loc["pandas_transform", "author"] = "Elizabeth Drellich"
df.loc["pandas_transform", "estimated_time_in_minutes"] = "1 hour"
df.loc["pandas_transform", "good_first_module"] = "false" 
df.loc["pandas_transform", "coding_required"] = "true"
df.loc["pandas_transform", "coding_language"] = "Python"
df.loc["pandas_transform", "coding_level"] = "intermediate"
df.loc["pandas_transform", "sequence_name"] = "Python"
df.loc["pandas_transform", "comment"] = "This is an introduction to transforming data using a Python library named pandas." 
df.loc["pandas_transform", "long_description"] = "This module is for learners who have some familiarity with Python, and want to learn how the pandas library can handle large tabular data sets. No previous experience with pandas is required, and only an introductory level understanding of Python is assumed." 
df.loc["pandas_transform", "Learning Objectives"] = "&After completion of this module, learners will be able to:&&- Import `pandas` and use functions from the `pandas` package.&- Load data into a `pandas` DataFrame.&- Use the `.loc` method to explore the contents of a DataFrame&- Filter a DataFrame using conditional statements.&- Transform data in a DataFrame.&&" 
df.loc["pandas_transform", "Prerequisties"] = "&Before starting this module it is useful for you to:&&* have some familiarity with tabular data: data stored in an array of rows and columns.&&* have an introductory level exposure to coding in [Python](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/python_basics_writing_python_code/python_basics_writing_python_code.md)&&" 
df.loc["pandas_transform", "Sets You Up For"] = "   data_visualization_in_seaborn   python_practice  " 
df.loc["pandas_transform", "Depends On Knowledge In"] = "   demystifying_python   python_basics_writing_python_code  " 
df.loc["python_basics_writing_python_code", "title"] = "Python Basics: Writing Python Code"
df.loc["python_basics_writing_python_code", "author"] = "Meredith Lee"
df.loc["python_basics_writing_python_code", "estimated_time_in_minutes"] = "1 hour"
df.loc["python_basics_writing_python_code", "comment"] = "Learn the foundations of writing Python code." 
df.loc["python_basics_writing_python_code", "long_description"] = "Before using Python for data analysis, there are some basics to learn that will set the foundation for more advanced Python coding. This module will teach you about functions and methods, how to define and use variables, how to create and edit lists and dictionaries, and how use loops and conditional statements to perform tasks with these basic data structures." 
df.loc["python_basics_writing_python_code", "Learning Objectives"] = "&After completion of this module, learners will be able to:&&- Identify and use functions and methods&- Assign values to variables&- Create and edit lists&- Iterate through lists using loops&- Utilize conditional statements&- Create and edit dictionaries&&" 
df.loc["python_practice", "title"] = "Python Practice"
df.loc["python_practice", "author"] = "Meredith Lee"
df.loc["python_practice", "estimated_time_in_minutes"] = "1 hour"
df.loc["python_practice", "good_first_module"] = "false" 
df.loc["python_practice", "coding_required"] = "true"
df.loc["python_practice", "coding_language"] = "Python"
df.loc["python_practice", "coding_level"] = "practice exercise"
df.loc["python_practice", "sequence_name"] = "Python"
df.loc["python_practice", "comment"] = "Use the basics of Python coding, data transformation, and data visualization to work with real data. " 
df.loc["python_practice", "long_description"] = "When learning Python for data science, the ultimate goal is to be able to put all of the pieces together to analyze a dataset. This module aims to provide a data science task in order to help learners practice Python skills in a real-world context. " 
df.loc["python_practice", "Learning Objectives"] = "&After completion of this module, learners will be able to:&&- Import a dataset from an online database&- Recode data and change variable types in a dataframe&- Use exploratory data visualization to identify trends in data and generate hypotheses&&" 
df.loc["python_practice", "Prerequisties"] = "&Learners should be familiar with [the basics of Python coding](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/python_basics_writing_python_code/python_basics_writing_python_code.md), including [data transformation with pandas](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/pandas_transform/pandas_transform.md) and [data visualization with matplotlib and seaborn](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/data_visualization_in_seaborn/data_visualization_in_seaborn.md). Learners should also have access to Python, either on their own computer or in the cloud. &&" 
df.loc["python_practice", "Sets You Up For"] = " " 
df.loc["python_practice", "Depends On Knowledge In"] = "   demystifying_python   python_basics_writing_python_code   pandas_transform   data_visualization_in_seaborn  " 
df.loc["r_basics_introduction", "title"] = "R Basics: Introduction"
df.loc["r_basics_introduction", "author"] = "Joy Payton"
df.loc["r_basics_introduction", "estimated_time_in_minutes"] = "1 hour"
df.loc["r_basics_introduction", "comment"] = "Introduction to R and hands-on first steps for brand new beginners." 
df.loc["r_basics_introduction", "long_description"] = "Are you brand new to R, and ready to get started?  This module teaches concepts and vocabulary related to R, RStudio, and R Markdown.  It also includes some introductory-level hands-on work in RStudio.  This is a good course if you know that you want to use R but haven't ever used it, or you've barely used it and need a refresher on the basics." 
df.loc["r_basics_introduction", "Learning Objectives"] = "&After completion of this module, learners will be able to:&&- Define and differentiate +R+, +RStudio+, and +R Markdown+&- Install and load packages in R&- Create a simple R Markdown file and its associated output document&- Import a .csv file as a data frame&&&" 
df.loc["r_basics_transform_data", "title"] = "R Basics: Transforming Data With dplyr"
df.loc["r_basics_transform_data", "author"] = "Joy Payton"
df.loc["r_basics_transform_data", "estimated_time_in_minutes"] = "1 hour"
df.loc["r_basics_transform_data", "comment"] = "Learn how to transform (or wrangle) data using R's `dplyr` package." 
df.loc["r_basics_transform_data", "long_description"] = "Do you want to learn how to work with tabular (table-shaped, with rows and columns) data in R?  In this module you'll learn in particular how to select just the rows and columns you want to work with, how to create new columns, and how to create multi-step transformations to get your data ready for visualization or statistical analysis.  This module teaches the use of the `dplyr` package, which is part of the `tidyverse` suite of packages." 
df.loc["r_basics_transform_data", "Learning Objectives"] = "&After completion of this module, learners will be able to:&&- Write R code that uses the `dplyr` package to select only desired columns from a data frame&- Write R code that uses the `dplyr` package to filter only rows that meet a certain condition from a data frame&- Write R code that uses the `dplyr` package to create a new column in a data frame&&" 
df.loc["r_basics_visualize_data", "title"] = "R Basics: Visualizing Data With ggplot2"
df.loc["r_basics_visualize_data", "author"] = "Joy Payton"
df.loc["r_basics_visualize_data", "estimated_time_in_minutes"] = "1 hour"
df.loc["r_basics_visualize_data", "comment"] = "Learn how to visualize data using R's `ggplot2` package." 
df.loc["r_basics_visualize_data", "long_description"] = "Do you want to learn how to make some basic data visualizations (graphs) in R?  In this module you'll learn about the +grammar of graphics+ and the base code that you need to get started.  We'll use the basic ingredients of a tidy data frame, a geometric type, and some aesthetic mappings (we'll explain what all of those are).  This module teaches the use of the `ggplot2` package, which is part of the `tidyverse` suite of packages." 
df.loc["r_basics_visualize_data", "Learning Objectives"] = "&After completion of this module, learners will be able to:&&- Write R code that creates basic data visualizations&- Identify geometric plot types available in `ggplot2`&- Map columns of data to visual elements like color or position&&" 
df.loc["r_missing_values", "title"] = "Missing Values in R"
df.loc["r_missing_values", "author"] = "Rose Hartman"
df.loc["r_missing_values", "estimated_time_in_minutes"] = "45 min"
df.loc["r_missing_values", "comment"] = "A practical demonstration of how missing values show up in R and how to deal with them. Note that this module does **not** cover statistical approaches for handling missing data, but instead focuses on the code you need to find, work with, and assign missing values in R." 
df.loc["r_missing_values", "long_description"] = "This is a beginner's guide to handling missing values in R. It covers what `NA` values are and how to check for them, how to mark values as missing, how to work around missing values in your analysis, and how to filter your data to remove missingness. This module is appropriate for learners who feel comfortable with R basics and are ready to get into the realities of data analysis, like dealing with missing values." 
df.loc["r_missing_values", "Learning Objectives"] = "&After completion of this module, learners will be able to:&&- check the number and location of missing values in a dataframe&- mark values as missing&- use common arguments like `na.rm` and `na.action` to control how functions handle missingness&- remove cases with missing values from a dataframe&&" 
df.loc["r_practice", "title"] = "R Practice"
df.loc["r_practice", "author"] = "Meredith Lee"
df.loc["r_practice", "estimated_time_in_minutes"] = "1 hour"
df.loc["r_practice", "comment"] = "Use the basics of R coding, data transformation, and data visualization to work with real data. " 
df.loc["r_practice", "long_description"] = "When learning R for data science, the ultimate goal is to be able to put all of the pieces together to analyze a dataset. This module aims to provide a data science task in order to help learners practice R skills in a real-world context. " 
df.loc["r_practice", "Learning Objectives"] = "&After completion of this module, learners will be able to:&&- Import a dataset from an online database&- Recode data and change variable types in a dataframe&- Use exploratory data visualization to identify trends in data and generate hypotheses&&" 
df.loc["r_reshape_long_wide", "title"] = "Reshaping Data in R: Long and Wide Data"
df.loc["r_reshape_long_wide", "author"] = "Joy Payton"
df.loc["r_reshape_long_wide", "estimated_time_in_minutes"] = "1 hour"
df.loc["r_reshape_long_wide", "comment"] = "A module that teaches how to reshape tabular data in R, concentrating on some typical shapes known as +long+ and +wide+ data." 
df.loc["r_reshape_long_wide", "long_description"] = "Reshaping data is one of the essential skills in getting your data in a tidy format, ready to visualize, analyze, and model.  This module is appropriate for learners who feel comfortable with R basics and are ready to take on the challenges of real life data, which is often messy and requires considerable effort to tidy." 
df.loc["r_reshape_long_wide", "Learning Objectives"] = "&After completion of this module, learners will be able to:&&- Define and differentiate +long data+ and +wide data+&- Use tidyr and dplyr tools to reshape data effectively&&&" 
df.loc["reproducibility", "title"] = "Reproducibility, Generalizability, and Reuse"
df.loc["reproducibility", "author"] = "Joy Payton"
df.loc["reproducibility", "estimated_time_in_minutes"] = "1 hour"
df.loc["reproducibility", "good_first_module"] = "true " 
df.loc["reproducibility", "comment"] = "This module provides learners with an approachable introduction to the concepts and impact of **research reproducibility**, **generalizability**, and **data reuse**, and how technical approaches can help make these goals more attainable." 
df.loc["reproducibility", "long_description"] = "**If you currently conduct research or expect to in the future**, the concepts we talk about here are important to grasp.  This material will help you understand much of the current literature and debate around how research should be conducted, and will provide you with a starting point for understanding why some practices (like writing code, even for researchers who have never programmed a computer) are gaining traction in the research field.  **If research doesn't form part of your future plans, but you want to *use* research** (for example, as a clinician or public health official), this material will help you form criteria for what research to consider the most rigorous and useful and help you understand why science can seem to vacillate or be self-contradictory." 
df.loc["reproducibility", "Learning Objectives"] = "&After completion of this module, learners will be able to:&&* Explain the importance of conducting research that is **reproducible** (can be re-done by a different, unaffiliated scientist)&* Argue in support of a data analysis method that helps research be more reproducible&* Argue in support of a method in the organization and description of documents, datasets, and other files that helps research be more reproducible&&" 
df.loc["reproducibility", "Prerequisties"] = "&It is helpful if learners have conducted research, are familiar with -- by reading or writing -- peer-reviewed literature, and have experience using data and methods developed by other people.  There is no need to have any specific scientific or medical domain knowledge or technical background.  &&" 
df.loc["reproducibility", "Sets You Up For"] = " " 
df.loc["reproducibility", "Depends On Knowledge In"] = " " 
df.loc["sql_basics", "title"] = "SQL Basics"
df.loc["sql_basics", "author"] = "Peter Camacho"
df.loc["sql_basics", "estimated_time_in_minutes"] = "1 hour"
df.loc["sql_basics", "good_first_module"] = "true" 
df.loc["sql_basics", "coding_required"] = "true"
df.loc["sql_basics", "coding_language"] = "SQL"
df.loc["sql_basics", "coding_level"] = "basic"
df.loc["sql_basics", "sequence_name"] = "SQL"
df.loc["sql_basics", "comment"] = "Structured Query Language, or SQL, is a relational database solution that has been around for decades.  Learn how to do basic SQL queries on single tables, by using code, hands-on." 
df.loc["sql_basics", "long_description"] = "Do you want to learn basic Structured Query Language (SQL) either to understand concepts or prepare for access to a relational database?  This module will give you hands on experience with simple queries using keywords including SELECT, WHERE, FROM, DISTINCT, and AS.  We'll also briefly cover working with empty (NULL) values using IS NULL and IS NOT NULL.  This module is appropriate for people who have little or no experience in SQL and are ready to practice with real queries." 
df.loc["sql_basics", "Learning Objectives"] = "&After completion of this module, learners will be able to:&&- Use SELECT, FROM, and WHERE to do a basic query on a SQL table&- Use IS NULL and IS NOT NULL operators to work with empty values&- Explain the use of DISTINCT and how it can be useful&- Use AS and ORDER BY to change how query results appear&- Explain why the LIMIT keyword can be useful&&&" 
df.loc["sql_basics", "Prerequisties"] = "&Experience working with rectangular data (data in rows and columns) is required, as is some exposure to the idea of SQL and its use of tables with rows and columns.  No experience writing SQL code is expected or required for this module.  If you would like a code-free overview to SQL we recommend our module [Demystifying SQL](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/demystifying_sql/demystifying_sql.md).&&" 
df.loc["sql_basics", "Sets You Up For"] = "   sql_intermediate  " 
df.loc["sql_basics", "Depends On Knowledge In"] = "   demystifying_sql  " 
df.loc["sql_intermediate", "title"] = "SQL, Intermediate Level"
df.loc["sql_intermediate", "author"] = "Peter Camacho"
df.loc["sql_intermediate", "estimated_time_in_minutes"] = "1 hour"
df.loc["sql_intermediate", "good_first_module"] = "false" 
df.loc["sql_intermediate", "coding_required"] = "true"
df.loc["sql_intermediate", "coding_language"] = "SQL"
df.loc["sql_intermediate", "coding_level"] = "intermediate"
df.loc["sql_intermediate", "sequence_name"] = "SQL"
df.loc["sql_intermediate", "comment"] = "Learn how to do intermediate SQL queries on single tables, by using code, hands-on." 
df.loc["sql_intermediate", "long_description"] = "Do you want to learn intermediate Structured Query Language (SQL) for more precise and complex data querying on single tables?  This module will give you hands on experience with single-table queries using keywords including CASE, LIKE, REGEXP_LIKE, GROUP BY, HAVING, and WITH, along with a number of aggregate functions like COUNT and AVG.  This module is appropriate for people who are comfortable writing basic SQL queries and are ready to practice more advanced sklls." 
df.loc["sql_intermediate", "Learning Objectives"] = "&After completion of this module, learners will be able to:&&* Create new data classifications using `CASE` statements&* Find text that matches a given pattern using `LIKE` and `REGEXP_LIKE` statements&* Use `GROUP BY` and `HAVING` statements along with aggregate functions to understand group characteristics&* Use `WITH` to create sub queries&&" 
df.loc["sql_intermediate", "Prerequisties"] = "&Some experience writing basic SQL code (SELECT, FROM, WHERE) is expected in this module.  If you would like a code-free overview to SQL we recommend our module [Demystifying SQL](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/demystifying_sql/demystifying_sql.md).  If you need to develop basic SQL fluency we recommend our module [SQL Basics](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/sql_basics/sql_basics.md).&&" 
df.loc["sql_intermediate", "Sets You Up For"] = "   sql_joins  " 
df.loc["sql_intermediate", "Depends On Knowledge In"] = "   sql_basics  " 
df.loc["sql_joins", "title"] = "SQL Joins"
df.loc["sql_joins", "author"] = "Joy Payton"
df.loc["sql_joins", "estimated_time_in_minutes"] = "1 hour"
df.loc["sql_joins", "good_first_module"] = "false" 
df.loc["sql_joins", "coding_required"] = "true"
df.loc["sql_joins", "coding_language"] = "SQL"
df.loc["sql_joins", "coding_level"] = "intermediate"
df.loc["sql_joins", "sequence_name"] = "SQL"
df.loc["sql_joins", "comment"] = "Learn about SQL joins: what they accomplish, and how to write them." 
df.loc["sql_joins", "long_description"] = "Usually, data in a SQL database is organized into multiple interrelated tables.  This means you will often have to bring data together from two or more tables into a single dataset to answer your research questions.  This +join+ action is accomplished using `JOIN` commands.  This module teaches types of joins, join criteria, and how to write `JOIN` code." 
df.loc["sql_joins", "Learning Objectives"] = "After completion of this module, learners will be able to:&&- Understand the parts of a JOIN&- Describe the +shapes+ of SQL JOINs: inner, left, right, and full&- Explain what +join criteria+ are&&" 
df.loc["sql_joins", "Prerequisties"] = "&Learners should have experience writing SQL code on single tables.  If you have successfully used a +SELECT... FROM... WHERE+ SQL statement on a single table, and have at least seen +GROUP BY+ commands in action, even if you would need help writing the GROUP BY code, you have enough code ability.  We also highly recommend that you understand the concepts of one-to-many data relationships and database normalization to get the most out of this module. &&If you need to develop basic SQL fluency we recommend our module [SQL Basics](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/sql_basics/sql_basics.md).  For more intermediate topics, we suggest our module [SQL Intermediate](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/sql_intermediate/sql_intermediate.md).  Finally, to learn about one-to-many data relationships and database normalization, consider our [Database Normalization](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/database_normalization/database_normalization.md) module.&&" 
df.loc["sql_joins", "Depends On Knowledge In"] = "   sql_basics   sql_intermediate   database_normalization  " 
df.loc["statistical_tests", "title"] = "Statistical Tests in Open Source Software"
df.loc["statistical_tests", "author"] = "Rose Hartman"
df.loc["statistical_tests", "estimated_time_in_minutes"] = "20 minutes (although reading through the linked tutorials may take much longer, depending on which tests you choose to read about)"
df.loc["statistical_tests", "good_first_module"] = "false" 
df.loc["statistical_tests", "comment"] = "This module provides an overview of the most commonly used kinds of statistical tests and links to code for running many of them in both R and python." 
df.loc["statistical_tests", "long_description"] = "This module contains a curated list of links to tutorials and examples of many common statistical tests in both R and python. If you want to use R or python for data analysis but aren't sure how to write code for the statistical tests you want to run, this is a great place to start. This will be an especially valuable resource for people who have experience conducting analysis in other software (e.g. SAS, SPSS, MPlus, Matlab) and are looking to move to R and/or python. If you are new to data analysis, this module provides some structure to help you think about which statistical tests to run, and examples of code to execute them. It doesn't cover the statistical theory itself, though, so you'll need to do some additional reading before applying the code for any tests you don't already understand (there are recommended resources for learning statistical techniques at the end of the module)." 
df.loc["statistical_tests", "Learning Objectives"] = "&After completion of this module, learners will be able to:&&- Use four key questions to help determine which statistical tests will be most appropriate in a given situation&- Discuss general differences between running statistical tests in R vs. python&- Quickly find the code they need to be able to run most common statistical tests in R or python&&" 
df.loc["statistical_tests", "Prerequisties"] = "&* Learners should already be familiar with the purpose and assumptions of any test they intend to run --- this module covers the +how+ only, not the +why+.&* This module also assumes some basic familiarity with either R or python. If you are brand new to one or both (or want a refresher) consider starting with [Intro to R](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/r_basics_introduction/r_basics_introduction.md) or [Python Basics](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/python_basics_writing_python_code/python_basics_writing_python_code.md) first and then coming back here.&&" 
df.loc["statistical_tests", "Depends On Knowledge In"] = "   r_basics_introduction   python_basics_writing_python_code  " 
df.loc["tidy_data", "title"] = "Tidy Data"
df.loc["tidy_data", "author"] = "Joy Payton"
df.loc["tidy_data", "estimated_time_in_minutes"] = "45 minutes"
df.loc["tidy_data", "good_first_module"] = "true" 
df.loc["tidy_data", "comment"] = "Tidy is a technical term in data analysis and describes an optimal way for organizing data that will be analyzed computationally." 
df.loc["tidy_data", "long_description"] = "Are you concerned about how to organize your data so that it's easier to work with in a computational solution like R, Python, or other statistical software?  This module will explain the concept of +tidy data+, which will help make analysis and data reuse a bit simpler." 
df.loc["tidy_data", "Learning Objectives"] = "&After completion of this module, learners will be able to:&&- Describe the three characteristics of tidy data&- Describe how messy data could be transformed into tidy data&- Describe the three tenets of tidy analysis&&&" 
df.loc["tidy_data", "Prerequisties"] = "&Experience working with rectangular data (data in rows and columns) will be helpful.  For example, experience working in Excel, Google Sheets, or other software that helps organize data into rows and columns is sufficient expertise to take this module.&&" 
df.loc["tidy_data", "Sets You Up For"] = " " 
df.loc["tidy_data", "Depends On Knowledge In"] = " " 
df.loc["using_redcap_api", "title"] = "Using the REDCap API"
df.loc["using_redcap_api", "author"] = "Joy Payton"
df.loc["using_redcap_api", "estimated_time_in_minutes"] = "1 hour"
df.loc["using_redcap_api", "comment"] = "REDCap is a research data capture tool used by many researchers in basic, translational, and clinical research efforts.  Learn how to use the REDCap API in this module." 
df.loc["using_redcap_api", "long_description"] = "If your institution provides access to REDCap, this module is right for you.  REDCap is a convenient and powerful way to collect and store research data.  This module will teach you how to interact with the REDCap API, or +Application Programming Interface,+ which can help you automate your data analysis. This will also help you understand APIs in general and what makes their use so appealing for reproducible research efforts." 
df.loc["using_redcap_api", "Learning Objectives"] = "&After completion of this module, learners will be able to:&&- Define what an API is and why it's useful to researchers&- Enable API usage on REDCap projects&- Use the REDCap API to pull data into an R or Python data analysis&&&" 
df["Linked Courses"] = [list() for x in range(len(df.index))]
a = df.loc["bash_103_combining_commands", "Linked Courses"]
a.append("bash_command_line_101")
a.append("bash_command_line_102")
a.append("bash_scripts")
a.append("directories_and_file_paths")
df.at["bash_103_combining_commands", "Linked Courses"] = list(a)
a = df.loc["bash_command_line_101", "Linked Courses"]
a.append("bash_103_combining_commands")
a.append("bash_command_line_102")
a.append("bash_conditionals_loops")
a.append("bash_scripts")
a.append("directories_and_file_paths")
a.append("git_setup_windows")
df.at["bash_command_line_101", "Linked Courses"] = list(a)
a = df.loc["bash_command_line_102", "Linked Courses"]
a.append("bash_103_combining_commands")
a.append("bash_command_line_101")
a.append("bash_conditionals_loops")
a.append("bash_scripts")
a.append("directories_and_file_paths")
df.at["bash_command_line_102", "Linked Courses"] = list(a)
a = df.loc["bash_conditionals_loops", "Linked Courses"]
a.append("bash_103_combining_commands")
a.append("bash_command_line_101")
a.append("bash_command_line_102")
a.append("directories_and_file_paths")
df.at["bash_conditionals_loops", "Linked Courses"] = list(a)
a = df.loc["bash_scripts", "Linked Courses"]
a.append("bash_103_combining_commands")
a.append("bash_command_line_101")
a.append("bash_command_line_102")
a.append("bash_conditionals_loops")
a.append("reproducibility")
df.at["bash_scripts", "Linked Courses"] = list(a)
a = df.loc["citizen_science", "Linked Courses"]
df.at["citizen_science", "Linked Courses"] = list(a)
a = df.loc["data_management_basics", "Linked Courses"]
a.append("reproducibility")
df.at["data_management_basics", "Linked Courses"] = list(a)
a = df.loc["data_storage_models", "Linked Courses"]
df.at["data_storage_models", "Linked Courses"] = list(a)
a = df.loc["data_visualization_in_ggplot2", "Linked Courses"]
a.append("data_visualization_in_open_source_software")
a.append("data_visualization_in_seaborn")
a.append("r_basics_introduction")
a.append("statistical_tests")
df.at["data_visualization_in_ggplot2", "Linked Courses"] = list(a)
a = df.loc["data_visualization_in_open_source_software", "Linked Courses"]
a.append("data_visualization_in_ggplot2")
a.append("data_visualization_in_seaborn")
a.append("demystifying_python")
a.append("r_basics_introduction")
df.at["data_visualization_in_open_source_software", "Linked Courses"] = list(a)
a = df.loc["data_visualization_in_seaborn", "Linked Courses"]
a.append("data_visualization_in_ggplot2")
a.append("demystifying_python")
a.append("pandas_transform")
a.append("python_basics_writing_python_code")
a.append("python_practice")
a.append("statistical_tests")
df.at["data_visualization_in_seaborn", "Linked Courses"] = list(a)
a = df.loc["database_normalization", "Linked Courses"]
a.append("sql_intermediate")
a.append("sql_joins")
df.at["database_normalization", "Linked Courses"] = list(a)
a = df.loc["demystifying_geospatial_data", "Linked Courses"]
df.at["demystifying_geospatial_data", "Linked Courses"] = list(a)
a = df.loc["demystifying_python", "Linked Courses"]
a.append("bash_command_line_101")
a.append("python_basics_writing_python_code")
df.at["demystifying_python", "Linked Courses"] = list(a)
a = df.loc["demystifying_sql", "Linked Courses"]
a.append("reproducibility")
df.at["demystifying_sql", "Linked Courses"] = list(a)
a = df.loc["directories_and_file_paths", "Linked Courses"]
df.at["directories_and_file_paths", "Linked Courses"] = list(a)
a = df.loc["elements_of_maps", "Linked Courses"]
df.at["elements_of_maps", "Linked Courses"] = list(a)
a = df.loc["geocode_lat_long", "Linked Courses"]
df.at["geocode_lat_long", "Linked Courses"] = list(a)
a = df.loc["git_creation_and_tracking", "Linked Courses"]
a.append("git_history_of_project")
a.append("git_setup_mac_and_linux")
a.append("git_setup_windows")
df.at["git_creation_and_tracking", "Linked Courses"] = list(a)
a = df.loc["git_history_of_project", "Linked Courses"]
a.append("git_creation_and_tracking")
a.append("git_setup_mac_and_linux")
a.append("git_setup_windows")
df.at["git_history_of_project", "Linked Courses"] = list(a)
a = df.loc["git_intro", "Linked Courses"]
df.at["git_intro", "Linked Courses"] = list(a)
a = df.loc["git_setup_mac_and_linux", "Linked Courses"]
a.append("git_creation_and_tracking")
a.append("git_history_of_project")
a.append("git_intro")
a.append("git_setup_windows")
df.at["git_setup_mac_and_linux", "Linked Courses"] = list(a)
a = df.loc["git_setup_windows", "Linked Courses"]
a.append("bash_command_line_101")
a.append("git_creation_and_tracking")
a.append("git_history_of_project")
a.append("git_intro")
a.append("git_setup_mac_and_linux")
df.at["git_setup_windows", "Linked Courses"] = list(a)
a = df.loc["how_to_troubleshoot", "Linked Courses"]
df.at["how_to_troubleshoot", "Linked Courses"] = list(a)
a = df.loc["learning_to_learn", "Linked Courses"]
a.append("reproducibility")
df.at["learning_to_learn", "Linked Courses"] = list(a)
a = df.loc["omics_orientation", "Linked Courses"]
df.at["omics_orientation", "Linked Courses"] = list(a)
a = df.loc["pandas_transform", "Linked Courses"]
a.append("data_visualization_in_seaborn")
a.append("demystifying_python")
a.append("python_basics_writing_python_code")
a.append("python_practice")
df.at["pandas_transform", "Linked Courses"] = list(a)
a = df.loc["python_basics_writing_python_code", "Linked Courses"]
a.append("demystifying_python")
df.at["python_basics_writing_python_code", "Linked Courses"] = list(a)
a = df.loc["python_practice", "Linked Courses"]
a.append("data_visualization_in_seaborn")
a.append("demystifying_python")
a.append("pandas_transform")
a.append("python_basics_writing_python_code")
a.append("r_practice")
df.at["python_practice", "Linked Courses"] = list(a)
a = df.loc["r_basics_introduction", "Linked Courses"]
a.append("r_basics_transform_data")
a.append("r_basics_visualize_data")
a.append("reproducibility")
df.at["r_basics_introduction", "Linked Courses"] = list(a)
a = df.loc["r_basics_transform_data", "Linked Courses"]
a.append("r_basics_introduction")
a.append("r_basics_visualize_data")
df.at["r_basics_transform_data", "Linked Courses"] = list(a)
a = df.loc["r_basics_visualize_data", "Linked Courses"]
a.append("data_visualization_in_ggplot2")
a.append("r_basics_introduction")
a.append("r_basics_transform_data")
a.append("tidy_data")
df.at["r_basics_visualize_data", "Linked Courses"] = list(a)
a = df.loc["r_missing_values", "Linked Courses"]
a.append("r_basics_introduction")
a.append("r_basics_transform_data")
df.at["r_missing_values", "Linked Courses"] = list(a)
a = df.loc["r_practice", "Linked Courses"]
a.append("data_visualization_in_ggplot2")
a.append("python_practice")
a.append("r_basics_introduction")
a.append("r_basics_transform_data")
df.at["r_practice", "Linked Courses"] = list(a)
a = df.loc["r_reshape_long_wide", "Linked Courses"]
a.append("r_basics_introduction")
a.append("r_basics_transform_data")
a.append("tidy_data")
df.at["r_reshape_long_wide", "Linked Courses"] = list(a)
a = df.loc["reproducibility", "Linked Courses"]
df.at["reproducibility", "Linked Courses"] = list(a)
a = df.loc["sql_basics", "Linked Courses"]
a.append("demystifying_sql")
a.append("sql_intermediate")
df.at["sql_basics", "Linked Courses"] = list(a)
a = df.loc["sql_intermediate", "Linked Courses"]
a.append("demystifying_sql")
a.append("sql_basics")
a.append("sql_joins")
df.at["sql_intermediate", "Linked Courses"] = list(a)
a = df.loc["sql_joins", "Linked Courses"]
a.append("database_normalization")
a.append("sql_basics")
a.append("sql_intermediate")
df.at["sql_joins", "Linked Courses"] = list(a)
a = df.loc["statistical_tests", "Linked Courses"]
a.append("data_visualization_in_open_source_software")
a.append("python_basics_writing_python_code")
a.append("r_basics_introduction")
df.at["statistical_tests", "Linked Courses"] = list(a)
a = df.loc["tidy_data", "Linked Courses"]
a.append("reproducibility")
df.at["tidy_data", "Linked Courses"] = list(a)
a = df.loc["using_redcap_api", "Linked Courses"]
a.append("reproducibility")
df.at["using_redcap_api", "Linked Courses"] = list(a)
