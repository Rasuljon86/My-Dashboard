import dash
from dash import dcc
from dash import html
import pandas as pd
from dash.dependencies import Output, Input
import plotly.express as px

df = pd.read_csv('uzb_admpop_adm1.csv')
# print(df[:5])
# print(df.ADM1_EN.nunique())
# print(df.ADM1_EN.unique())

# Data visualization with plotly
# fig_pie = px.pie(data_frame=df, names='ADM1_EN', values='Total_pop')
    # fig_pie = px.pie(data_frame=df, names='ADM1_EN', values='Male_pop')
    # fig_pie.show()

app = dash.Dash(__name__)
app.layout = html.Div([
    html.H1("Uzbekistan population analysis"),
    dcc.Graph(id='my_graph', figure=px.pie(data_frame=df, names='ADM1_EN', values='Total_pop'))

])

@app.callback(
    Output(component_id='my-graph', component_property='figure'),
    Input(component_id='ADM1_EN',component_property='value')
)

def interactive_graphing(value_ADM1_EN):
    print(value_ADM1_EN)
    dff = df[df.ADM1_EN==value_ADM1_EN]
    fig = px.pie(data_frame=dff, names='ADM1_EN', values='Total_pop')
    return fig



if __name__=='__main__':
    app.run_server()



