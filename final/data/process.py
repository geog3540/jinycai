import pandas as pd
import json

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv(r'D:\BaiduSyncdisk\note\research\03-Projects\1-Study\6-PhD\1-Iowa\1-Courses\GEOG5540 Geographic Visualization\final\data\sensitivity variables.csv')

# Convert the DataFrame to a dictionary
data_dict = df.to_dict(orient='list')

# Convert the dictionary to a JSON string
json_string = json.dumps(data_dict)

# Write the JSON string to a file
with open(r'D:\BaiduSyncdisk\note\research\03-Projects\1-Study\6-PhD\1-Iowa\1-Courses\GEOG5540 Geographic Visualization\final\data\sensitivity variables.json', 'w') as outfile:
    json.dump(json_string, outfile)