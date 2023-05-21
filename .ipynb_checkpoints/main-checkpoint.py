# import libraries
import json
import pandas as pd
from datetime import timedelta

# import helper function
from fetch import fetch_raw_data

# (1) Retrieve data and write into json file for later reference
raw = fetch_raw_data()
with open('raw.json', 'w') as outfile: 
    outfile.write(json.dumps(raw))

# (2) Format the retrieved data into df with specified columns
df_raw = pd.DataFrame.from_dict(raw['list'])
df_temps = pd.DataFrame(list(df_raw['main']))[['temp', 'temp_min', 'temp_max']]
df_dt = df_raw[['dt']]
df_wind = pd.DataFrame(list(df_raw['wind']))[['speed']]
df = pd.concat([df_dt, df_temps, df_wind], axis=1)

# (3) Print a message if there is any missing data
if df.empty:
	print('\nOH NO!! No data was returned. \n') 
elif df.isna().sum().sum() > 0: 
	print(f'\nWARNING: {df.isna().sum().sum() / (len(df) * len(df.columns)) * 100} percent of values are missing.\n')
else: 
	print('\nSUCCESS! There is no missing data.\n')

# (4) format the dt column as YYYY-MM-DD HH:MM:SS
df['dt'] = pd.to_datetime(df['dt'], unit='s')

# (5) create a new column with one hour subtracted from the timestamps
hrs_offset = -1 
df['dt-1hr'] = pd.to_datetime(df['dt'] + timedelta(hours=hrs_offset))

# (6) convert temp column from Celsius to Farenheit
df['temp'] = 9 / 5 * df['temp'] + 32

# (7) save the result to a csv
df.to_csv('forecast-5d-3h.csv', index=False)
