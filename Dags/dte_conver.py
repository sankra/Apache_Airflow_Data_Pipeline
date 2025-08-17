import os
import sys
import pandas as pd 
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import json
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(current_dir))


query = """(deletedindicator == 'N') or (deletedindicator == 'Y' and lastupdatedate.dt.date > @lst_3months)"""

data = {'deletedindicator': ['N' 'Y', 'Y', 'N'], 'lastupdatedate': ['2025-01-10 02:02:03.677', '2025-02-20 16:50:03.677','2025-03-15 23:08:03.677']}
df = pd.DataFrame(data)
df['lastupdatedate'] = pd.to_datetime(df['lastupdatedate'])
lst_3months = (pd.Timestamp.today() - pd.DateOffset(months=3)).date()
lst_3months= (pd.Timestamp.today() - pd.DateOffset(months=3)).date()

print (lst_3months)
print (type(lst_3months))
print (df)
# Filter the DataFrame based on the query
# Ensure the 'lastupdatedate' column is in datetime format

required_month = df.query (query)
print (required_month)
print (type(required_month))
print(required_month.shape[0])
print (required_month.shape[1])
print (required_month.columns)