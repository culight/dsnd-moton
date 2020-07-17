import plotly.graph_objs as go

from .creds import plotly_token


def create_map_dropdown(data: dict):
    """
    Incoporate input data to create interactive map figure
    Input:
        data: ipnut data for the map
    Output:
        plotly map incorporating input data
    """

    # add the figures
    event_list = list(data.keys())
    event_data = [plot for plot in data.values()]
    fig = go.Figure()
    fig.add_trace(event_data[0].data[0])
    for plot in event_data[1:]:
        plot.data[0].visible = False
        fig.add_trace(plot.data[0])
        fig.layout = plot.layout
        
    # setup layout
    fig.update_layout(
        width=800,
        height=800,
        mapbox = dict(
            center= dict(lat=47.6, lon= -122.3),
            accesstoken=plotly_token,
            zoom=10
        ),
        title={
            'yanchor': 'top',
            'xanchor': 'center',
            'x': 0.5
        }
    )

    # Add dropdown
    fig.update_layout(
        updatemenus=[
            dict(
                x=-0.05,
                y=1,
                yanchor='top',
                xanchor='right',
                # pad={"r": 10, "t": 10},
                buttons=list([
                    dict(
                        args=['visible', [True, False, False, False]],
                        label=event_list[0],
                        method='restyle'
                    ),
                    dict(
                        args=['visible', [False, True, False, False]],
                        label=event_list[1],
                        method='restyle'
                    ),
                    dict(
                        args=['visible', [False, False, True, False]],
                        label=event_list[2],
                        method='restyle'
                    ),
                    dict(
                        args=['visible', [False, False, False, True]],
                        label=event_list[3],
                        method='restyle'
                    )
                ]),
            ),
        ]
    )

    # add annotation
    fig.update_layout(
        annotations=[
            dict(
                text="Neighborhood:",
                showarrow=False,
                x=-0.28,
                y=1.04,
                yref="paper",
                align="left"
            )
        ]
    )

    return fig