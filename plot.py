import plotly.plotly
import plotly.graph_objs as go
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/himanipasricha/usageindexdataset/master/70_countries%20-%2070countries.csv')

data = [go.Choropleth(
    locations = df['CODE'],
    z = df['Aggrgate_index_usage'],
    text = df['Country'],
    colorscale = [
        [0, "rgb(5, 10, 172)"],
        [0.2, "rgb(40, 60, 190)"],
        [0.4, "rgb(70, 100, 245)"],
        [0.6, "rgb(90, 120, 245)"],
        [0.8, "rgb(106, 137, 247)"],
        [1, "rgb(220, 220, 220)"]
    ],
    autocolorscale = False,
    reversescale = True,
    marker = go.choropleth.Marker(
        line = go.choropleth.marker.Line(
            color = 'rgb(180,180,180)',
            width = 0.5
        )),
    colorbar = go.choropleth.ColorBar(
        #tickprefix = '',
        title = 'Aggregate index usage'),
)]

layout = go.Layout(
    title = go.layout.Title(
        text = 'Usage Index'
    ),
    geo = go.layout.Geo(
        showframe = False,
        showcoastlines = False,
        projection = go.layout.geo.Projection(
            type = 'equirectangular'
        )
    ),
    annotations = [go.layout.Annotation(
        x = 0.55,
        y = 0.1,
        xref = 'paper',
        yref = 'paper',
        text='',
        showarrow = False
    )]
)

fig = go.Figure(data = data, layout = layout)
plotly.offline.plot(fig, filename = 'Usage index 70 countries')
