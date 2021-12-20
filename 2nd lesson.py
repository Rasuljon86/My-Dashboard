import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State

import pandas as pd
import plotly.express as px
# data exploration
df = pd.read_csv("hududlar.csv")
print(df[:5])

# data visualization
#fig_pie = px.pie(data_frame=df, names='Hududlar nomi', values='Aholi soni ming kishi')
#fig_pie.show()

app = dash.Dash(__name__)
app.layout = html.Div([
    html.H1("Andijon oynasi", style={"textAlign":"center"}), #sarlavha
    html.Hr(),
    html.P("Tumanlar nomi"), #dropdown sarlavhasi
    dcc.Dropdown(
        id='demo-dropdown',
        options=[
            {'label': 'Shahrihon tumani', 'value': 'Shahrihon tumani'},
            {'label': 'Asaka tumani', 'value': 'Asaka tumani'},
            {'label': 'Qorgontepa tumani', 'value': 'Qorgontepa tumani'},
            {'label': 'Andijon tumani', 'value': 'Andijon tumani'},
            {'label': 'Baliqchi tumani', 'value': 'Baliqchi tumani'},
            {'label': 'Andijon shahar', 'value': 'Andijon shahar'},
            {'label': 'Oltinkol tumani', 'value': 'Oltinkol tumani'},
            {'label': 'Jalaquduq tumani', 'value': 'Jalaquduq tumani'},
            {'label': 'Izboskan tumani', 'value': 'Izboskan tumani'},
            {'label': 'Paxtaobod tumani', 'value': 'Paxtaobod tumani'},
            {'label': 'Marhamat tumani', 'value': 'Marhamat tumani'},
            {'label': 'Xojaobod tumani', 'value': 'Xojaobod tumani'},
            {'label': 'Buloqboshi tumani', 'value': 'Buloqboshi tumani'},
            {'label': 'Boston tumani', 'value': 'Boston tumani'},
            {'label': 'Ulugnor tumani', 'value': 'Ulugnor tumani'},
            {'label': 'Honobod shahar', 'value': 'Honobod shahar'}
        ],
        value=['Shahrihon tumani'],
        searchable=True,
        clearable=True


    ),
    html.Div(id='dd-output-container', children=[]),
])


@app.callback(
    Output('dd-output-container', 'children'),
    Input('demo-dropdown', 'value')
)
def update_output(value):
    return 'You have selected "{}"'.format(value)


if __name__ == '__main__':
    app.run_server(debug=True)