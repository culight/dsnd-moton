import calendar
import pandas as pd


# numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
# NUMER_LIST_DF = list_df.select_dtypes(include=numerics)


def time_slice(df, beginning, end):
    return df[(df.index >= beginning) & (df.index <= end)]


def format_dollar_field(field: pd.Series, to_dollar=False):
    """
    Convert given dollar field into a float
    Input:
        df: dataframe, field_name: name of mentary field_name
    Output:
        Panda series with updated field
    """
    if to_dollar:
        field_updated = field.apply(
            lambda x: '${:.2f}'.format(round(x, 2))
        )
    else:
        field_updated = field.str.replace(
            '$',''
        ).str.replace(
            ',',''
        ).astype(
            'float'
        ).fillna(0.0)
    
    return field_updated


def format_percent_field(field: pd.Series, to_percent=False):
    """
    Convert given dollar field into a float
    Input:
        df: dataframe, field_name: name of mentary field_name
    Output:
        Panda series with updated field
    """
    if to_percent:
        field_updated = field.apply(
            lambda x: '{:.2f}%'.format(round(float(x) * 100, 2))
        )
    else:
        pass
    
    return field_updated


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