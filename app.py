import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import base64
from dash.dependencies import Input, Output, State

strategies = ['strategy1']
options = [{'label': strategy, 'value': strategy} for strategy in strategies]
app = dash.Dash(external_stylesheets=[dbc.themes.DARKLY])
server = app.server
app.layout = html.Div([
    html.H1("STRAGEY", style={'text-align': 'center','color': '#CD5C5C'}),
    # html.Hr(),
    # html.Img(
    #     src='https://images.squarespace-cdn.com/content/5c036cd54eddec1d4ff1c1eb/1557908564936-YSBRPFCGYV2CE43OHI7F/GlobalAI_logo.jpg?content-type=image%2Fpng',
    #     style={
    #         'height': '20%',
    #         'width': '20%',
    #         'float': 'right',
    #         'position': 'relative',
    #         'margin-top': 9,
    #         'margin-right': 0}
    # ),
    html.Hr(),
    html.Div([
        dbc.Row([
                dbc.Col(html.Div([html.H3('Enter a Stategy to demonstrate:', style={'paddingRight': '30px'}),
                                  dcc.Dropdown(id='labels', value='strategy1', options=options)],
                                 style={'verticalAlign': 'top', 'display': 'inline-block'}))
                ])]),
    html.Hr(),
    dbc.Button("Generate Results", color="primary",
               block=True, id="button", className="mb-3", style={'fontSize': 50}),
    html.Br(),
    dbc.Row([html.Div([html.Img(id='image1')]), ],
            style={'textAlign': 'center'}),
    html.Br(),
    dbc.Row([html.Div([html.Img(id='image2')]), ],
            style={'textAlign': 'center'})
    ])


@app.callback(
    [Output("image1", "src"),
     Output("image2", "src")],
    [Input("button", "n_clicks")],
    [State("labels", "value")])
def update_graph(n_clicks, label):
    if label == 'strategy1':
        image_filenames = ['first1.png', 'first2.png']
    image_filename0 = image_filenames[0]
    encoded_image0 = base64.b64encode(open(image_filename0, 'rb').read())
    image0 = 'data:image/png;base64,{}'.format(encoded_image0.decode())
    image_filename1 = image_filenames[1]
    encoded_image1 = base64.b64encode(open(image_filename1, 'rb').read())
    image1 = 'data:image/png;base64,{}'.format(encoded_image1.decode())
    
    return image0, image1


if __name__ == '__main__':
    app.run_server(debug=True)
