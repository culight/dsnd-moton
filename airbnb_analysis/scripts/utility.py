import calendar
import pandas as pd

# numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
# NUMER_LIST_DF = list_df.select_dtypes(include=numerics)


def time_slice(df, beginning, end):
    return df[(df.index >= beginning) & (df.index <= end)]


def format_dollar_field(field: pd.Series):
    """
    Convert given dollar field into a float
    Input:
        df: dataframe, field_name: name of mentary field_name
    Output:
        Panda series with updated field
    """

    return field.str.replace(
        '$',''
    ).str.replace(
        ',',''
    ).astype(
        'float'
    ).fillna(0.0)


def create_ordered_months(cal_df: pd.DataFrame) -> pd.Series:
    """
    Convert numerical months into an ordered Series of month names
    Input:
        df: dataframe
    Output:
        Panda series with updated field
    """
    month_name = cal_df['date'].map(lambda date: calendar.month_abbr[date.month])
    return pd.Categorical(
        month_name,
        calendar.month_abbr[1:],
        ordered=True
    )