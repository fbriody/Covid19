import glob
import os

from datetime import datetime

import pandas as pd

#csv_files = glob.glob(DATA_DIR + "/*.csv")
csv_files = glob.glob("daily_data" + "/*.csv")

def extract_date(file_name):
    date_str = os.path.basename(file_name)[:-4]
    
    date = datetime.strptime(date_str, '%m-%d-%Y').date()
    
    return date

world_df = None

fields_mapping_dic = {
    "Province/State":"Province_State",
    "Country/Region":"Country_Region",
    "Last Update":"Last_Update",
    "Confirmed":"Confirmed",
    "Deaths":"Deaths",
    "Recovered":"Recovered",
    "Latitude":"Lat",
    "Longitude":"Long_"
}

for csv_file in csv_files:
    
    df = pd.read_csv(csv_file)
    date = extract_date(csv_file)
    
    if date >= datetime.strptime("03-23-2020", '%m-%d-%Y').date():
        for k, v in fields_mapping_dic.items():
            df[k] = df[v]
        pass
        
    
    df['Date'] = date
    
    if world_df is None:
        world_df = df
    else:
        world_df = pd.concat((world_df, df), ignore_index=True)

#print(world_df)
world_df.to_csv('covid.csv', index = False)