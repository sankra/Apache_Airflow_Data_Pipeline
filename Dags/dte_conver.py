import pandas as pd
from datetime import datetime, timedelta

query = "(deleteindicator == 'N') or (deleteindicator == 'Y' and lastupdatedate.dt.date > |month|)"

data = {'deletedindicator': ['N', 'Y', 'Y', 'N'], 'lastupdatedate': ['2024-08']}