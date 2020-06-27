import pandas as pd

bumbershoot_date_range = (
    pd.to_datetime("2016-09-4", format="%Y-%m-%d"),
    pd.to_datetime("2016-09-6", format="%Y-%m-%d"),
)
siff_date_range = (
    pd.to_datetime("2016-05-19", format="%Y-%m-%d"),
    pd.to_datetime("2016-06-12", format="%Y-%m-%d"),
)
hempfest_date_range = (
    pd.to_datetime("2016-08-14", format="%Y-%m-%d"),
    pd.to_datetime("2016-08-18", format="%Y-%m-%d"),
)
pride_date_range = (
    pd.to_datetime("2016-06-20", format="%Y-%m-%d"),
    pd.to_datetime("2016-06-28", format="%Y-%m-%d"),
)
summer_date_range = (
    pd.to_datetime("2016-05-20", format="%Y-%m-%d"),
    pd.to_datetime("2016-09-15", format="%Y-%m-%d"),
)

bumbershoot_dates = {
    "day_start": bumbershoot_date_range[0],
    "day_end": bumbershoot_date_range[1],
    "week_start": bumbershoot_date_range[0].week,
    "week_end": bumbershoot_date_range[1].week,
    "month_start": bumbershoot_date_range[0].month,
    "month_end": bumbershoot_date_range[1].month,
}
siff_dates = {
    "day_start": siff_date_range[0],
    "day_end": siff_date_range[1],
    "week_start": siff_date_range[0].week,
    "week_end": siff_date_range[1].week,
    "month_start": siff_date_range[0].month,
    "month_end": siff_date_range[1].month,
}
hempfest_dates = {
    "day_start": hempfest_date_range[0],
    "day_end": hempfest_date_range[1],
    "week_start": hempfest_date_range[0].week,
    "week_end": hempfest_date_range[1].week,
    "month_start": hempfest_date_range[0].month,
    "month_end": hempfest_date_range[1].month,
}
pride_dates = {
    "day_start": pride_date_range[0],
    "day_end": pride_date_range[1],
    "week_start": pride_date_range[0].week,
    "week_end": pride_date_range[1].week,
    "month_start": pride_date_range[0].month,
    "month_end": pride_date_range[1].month,
}
summer_dates = {
    "day_start": summer_date_range[0],
    "day_end": summer_date_range[1],
    "week_start": summer_date_range[0].week,
    "week_end": summer_date_range[1].week,
    "month_start": summer_date_range[0].month,
    "month_end": summer_date_range[1].month,
}

all_events = {
    "bumbershoot": bumbershoot_dates,
    "siff": siff_dates,
    "hempfest": hempfest_dates,
    "pride": pride_dates,
}