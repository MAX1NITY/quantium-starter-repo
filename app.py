from dash import Dash, html, dcc, Input, Output, callback
import plotly.express as px
import pandas as pd
import os

app = Dash(__name__)

file_path = os.path.join('data', 'single_formatted_output.csv')

df = pd.read_csv(file_path)

fig = px.line(df, x="Date", y="Sales", title="Pink Morsel Sales per Day")

regions = df['Region'].unique().tolist()

app.layout = html.Div([
    html.H1(children='Pink Morsel Sales Chart', className="heading", id="header"),

    dcc.Graph(
        id='sales-graph'
    ),

    html.Br(),
        html.Label('Select Region'),
        dcc.RadioItems(
        options=[{'label': r, 'value': r} for r in regions] + [{'label': 'All', 'value': 'All'}],
        value='All',
        id="radio-buttons",
        className="radio-buttons"
        )
    ])

@callback(
    Output('sales-graph', 'figure'),
    Input('radio-buttons', 'value'))
def update_region(selected_region):
    if selected_region == "All":
        filtered_df = df
    else:
        filtered_df = df[df['Region'] == selected_region]

    fig = px.line(filtered_df, x='Date', y='Sales', title=f'Sales - {selected_region}')
    return fig

if __name__ == '__main__':
    app.run(debug=True)