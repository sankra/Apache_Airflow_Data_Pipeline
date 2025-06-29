import os
import sys
import pandas as pd 
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


query = """(deletedindicator == 'N') or (deletedindicator == 'Y' and lastupdatedate.dt.date > @lst_3months)"""

data = {'deletedindicator': ['N' 'Y', 'Y', 'N'], 'lastupdatedate': ['2025-01-10 02:02:03.677', '2025-02-20 16:50:03.677','2025-03-15 23:08:03.677']}
df = pd.DataFrame(data)
df['lastupdatedate'] = pd.to_datetime(df['lastupdatedate'])
lst_3months= (pd.Timestamp.today() - pd.DateOffset(months=3)).date()
print (lst_3months)

required_month = df.query (query)
print (required_month)
print (type(required_month))
print(required_month.shape[0])
print (required_month.shape[1])
print (required_month.columns)