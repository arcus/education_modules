import pandas as pd 

#url="https://raw.githubusercontent.com/arcus/education_modules/d267bb8084d552d6d7de7a8a43abb24bfdc0acdb/assets/metadata/module_data.csv"

education_modules_df = pd.read_json("module_data.json") #read in metadata from education_modules repository
print(education_modules_df.shape)
print(education_modules_df.keys())
education_modules_df= education_modules_df.set_index("module_id")

print(education_modules_df.head())

check=education_modules_df.loc["bash_scripts", "pre_reqs"]
print(check)