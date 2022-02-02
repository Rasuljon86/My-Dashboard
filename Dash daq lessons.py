import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
import dash_daq as daq

app = dash.Dash(__name__)

app.layout = html.Div([
    daq.BooleanSwitch(id='our-boolean-switch', on=False),
    html.Div(id='boolean-switch-result'),
daq.ColorPicker(
        id='our-color-picker',
        label='Color Picker',
        value=dict(hex='#119DFF')
    ),
    html.Div(id='color-picker-result'),
daq.Gauge(
        id='our-gauge',
        label="Default",
        value=6
    ),
dcc.Slider(
        id='our-gauge-slider',
        min=0,
        max=10,
        step=1,
        value=5
    ),
])
@app.callback(
    Output('boolean-switch-result', 'children'),
    Output('color-picker-result', 'children'),
    Output('our-gauge', 'value'),
    Input('our-boolean-switch', 'on'),
    Input('our-color-picker', 'value'),
    Input('our-gauge-slider', 'value')
)
def update_output(on):
    return 'The switch is {}.'.format(on,value,value)


if __name__ == '__main__':
    app.run_server(debug=True)
