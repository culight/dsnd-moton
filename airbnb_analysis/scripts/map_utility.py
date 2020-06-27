from pathlib import Path
import plotly_express as px


def create_map_dropdown(data: dict):
    """
    Incoporate input data to create interactive map figure
    Input:
        data: ipnut data for the map
    Output:
        plotly map incorporating input data
    """
    event_list = list(data.keys())
    event_data = list(data.values())

    # add the figures
    fig = event_data[0]
    fig.add_trace(event_data[1].data[0])
    fig.add_trace(event_data[2].data[0])
    fig.add_trace(event_data[3].data[0])
        
    # setup layout
    fig.update_layout(
        width=800,
        height=800,
        mapbox = dict(
            center= dict(lat=47.6, lon= -122.3),
            accesstoken="pk.eyJ1IjoiZG1vdG9uMzE0IiwiYSI6ImNrYjVpdjhqbTBzaW4yenBpaHBlM3U3YmUifQ.DV5PwTAD_ZYi0qO1Nu105A",
            zoom=10
        )
    )

    # Add dropdown
    fig.update_layout(
        updatemenus=[
            dict(
                x=-0.05,
                y=1,
                yanchor='top',
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
            dict(text="Neighborhood:", showarrow=False,
            x=-0.28, y=1.04, yref="paper", align="left")
        ]
    )

    return fig