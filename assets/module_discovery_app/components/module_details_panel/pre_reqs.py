from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc
import module_data 


# expandable/collabsible pre_reqs
def pre_reqs(active_module):       
    text = str(module_data.df.loc[active_module, "Prerequisties"])
    text = text.replace("&", "\n")
    text = text.replace("+", '"')
    return     dbc.Accordion(
        [
            dbc.AccordionItem(
                [
                    dcc.Markdown(text),
                ],
                title="Wondering if you are ready for this module? Click here to see what prerequistes it has, if any:",
            ),], start_collapsed=True,)