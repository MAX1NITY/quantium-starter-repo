from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import os

app = Dash()

file_path = os.path.join('data', 'single_formatted_output.csv')

df = pd.read_csv(file_path)

fig = px.line(df, x="Date", y="Sales", title="Pink Morsel Sales per Day")

app.layout = html.Div(children=[
    dcc.Graph(
        id='sales-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)
    