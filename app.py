!pip install dash plotly pyngrok pandas

import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc
from pyngrok import ngrok

ngrok.set_auth_token("3BJH2gCvp05stCrvkjU3QGr9yQ2_32wSLDsdiiR4fowCKs7yE")

url = "https://raw.githubusercontent.com/Samradyni/quantium-starter-repo/main/formatted_sales_data.csv"
df = pd.read_csv(url)

df['date'] = pd.to_datetime(df['date'])
df = df.sort_values('date')

fig = px.line(df, x='date', y='sales', title='Daily Sales Trend')

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Sales Data Visualizer", style={'textAlign': 'center'}),
    dcc.Graph(figure=fig)
])

public_url = ngrok.connect(addr=8050)
print("Click this link to view your app:", public_url)

app.run(host="0.0.0.0", port=8050)