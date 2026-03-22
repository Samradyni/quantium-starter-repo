!pip install dash plotly pyngrok pandas

import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc, Input, Output
from pyngrok import ngrok

ngrok.set_auth_token("3BJH2gCvp05stCrvkjU3QGr9yQ2_32wSLDsdiiR4fowCKs7yE")

url = "https://raw.githubusercontent.com/Samradyni/quantium-starter-repo/main/formatted_sales_data.csv"
df = pd.read_csv(url)

df['date'] = pd.to_datetime(df['date'])
df = df.sort_values('date')

app = Dash(__name__)

app.layout = html.Div(
    style={
        'backgroundColor': '#f4f6f9',
        'padding': '20px',
        'fontFamily': 'Arial'
    },
    children=[

        html.H1(
            "Soul Foods - Pink Morsel Sales",
            style={
                'textAlign': 'center',
                'color': '#2c3e50'
            }
        ),

        html.Div([
            html.Label("Select Region:", style={'fontWeight': 'bold'}),

            dcc.RadioItems(
                id='region-filter',
                options=[
                    {'label': 'All', 'value': 'all'},
                    {'label': 'North', 'value': 'north'},
                    {'label': 'East', 'value': 'east'},
                    {'label': 'South', 'value': 'south'},
                    {'label': 'West', 'value': 'west'}
                ],
                value='all',
                labelStyle={'display': 'inline-block', 'margin-right': '15px'}
            )
        ], style={'marginBottom': '20px'}),

        dcc.Graph(id='line-chart')
    ]
)

@app.callback(
    Output('line-chart', 'figure'),
    Input('region-filter', 'value')
)
def update_chart(selected_region):
    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'] == selected_region]

    fig = px.line(
        filtered_df,
        x='date',
        y='sales',
        title='Pink Morsel Sales Over Time'
    )

    fig.update_layout(
        plot_bgcolor='white',
        paper_bgcolor='white'
    )

    return fig

public_url = ngrok.connect(8050)
print("Click this link to view your app:", public_url)

app.run(host="0.0.0.0", port=8050)
