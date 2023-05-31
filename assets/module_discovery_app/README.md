# Module Discovery App

## File structure
There are three main folders, 
- `assets` for stylesheets and other visual settings, 
- `components` which contains each of the panels/components of the app. Any callbacks that are internal to a component, e.g. expanding and hiding the component or something within the component, is in the component's directory. For example `components/center_nav_bar/` contains `center_nav_bar.py` as well as `center_nav_bar_callbacks.py`.
- `callbacks` for any callbacks that transmit information between different components. Note that these callbacks will filter through the hidden components of `hidden_active_module` and `hidden_filtered_modules`. In the future there may be a third hidden component (possibly visible) for `my_modules`.

## Module data
The script `process_data.sh` runs through all the modules on this branch and creates the `module_data.py` file which contains a pandas dataframe with some (soon to be all) of the metadata for each module. 

## Dockerization
The `Dockerfile`, `docker-compose.yml`, and `requirements.txt` are not yet sufficient to run this app in Docker. If these are necessary for deploying the app, we will need to update them.