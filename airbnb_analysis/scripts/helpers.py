import pandas as pd

def time_slice(df, timeframe, beginning, end):
    return df[(df[timeframe] >= beginning) & (df[timeframe] <= end)]
