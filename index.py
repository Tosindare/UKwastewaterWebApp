import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

from jupyter_dash import JupyterDash

#Import cleaned Dataset
effl_data = pd.read_csv('effluent_df.csv')
infl_data = pd.read_csv('influent_data.csv')



#Build app

app = dash.Dash(__name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}])
#app = JupyterDash(__name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}])


app.layout = html.Div([
    html.Div([
        html.Div([
            html.H3()
        ],
            className="one-third column"),

        html.Div([
            html.H3("UK Sewage Treatment Quality", style={"margin-bottom": "0px", 'color': 'white'}),
            html.H6("Interactive Web Visualisation App", style={"margin-top": "0px", 'color': '#ff8a8a'})
        ],
            className="one-half column", id="title"),

        html.Div([
            html.H3()
        ],
            className="one-third column")

    ], id="header", className="row flex-display", style={"margin-bottom": "25px"}),

    html.Div([
        html.Div([
            html.P('Select Parameter:', className='fix_label', style={'color': 'white'}),

            dcc.Dropdown(id='parameters',
                                  multi=False,
                                  clearable=True,
                                  value='Biochemical Oxygen Demand',
                                  placeholder='Select...',
                                  options=[{'label': c, 'value': c}
                                           for c in (effl_data['NameDeterminandName'].unique())], className='dcc_compon'),

            html.P('Select Treatment Plants (5 max):', className='fix_label', style={'color': 'white'}),

            dcc.Dropdown(id='swt',
                                  multi=True,
                                  clearable=True,
                                  value='Nuneaton STW',
                                  placeholder='Select...',
                                  options=[{'label': c, 'value': c}
                                           for c in (effl_data['TreatmentPlant'].unique())], className='dcc_compon'),

        ], className="create_container four columns", id="cross-filter-options1"),

        html.Div([
            dcc.Graph(id="line_chart")], className="create_container seven columns")

    ]),


    html.Div([
        html.Label('Timeline', className='fix_label', style={'color': 'white'}), #'font-weight': 'bold'}),
        dcc.Slider(
            id = 'slider-timeline',
            min = 1,
            max = 36,
            step = 1,
            value = 10,
            dots = True,
            marks={
                1: {'label': 'Jan 2015', 'style': {'color': 'white'}},
                4: {'label': 'Apr 2015', 'style': {'color': 'white'}},
                7: {'label': 'Jul 2015', 'style': {'color': 'white'}},
                10: {'label': 'Oct 2015', 'style': {'color': 'white'}},
                13: {'label': 'Jan 2016', 'style': {'color': 'white'}},
                16: {'label': 'Apr 2016', 'style': {'color': 'white'}},
                19: {'label': 'Jul 2016', 'style': {'color': 'white'}},
                22: {'label': 'Oct 2016', 'style': {'color': 'white'}},
                25: {'label': 'Jan 2017', 'style': {'color': 'white'}},
                28: {'label': 'Apr 2017', 'style': {'color': 'white'}},
                31: {'label': 'Jul 2017', 'style': {'color': 'white'}},
                34: {'label': 'Oct 2017', 'style': {'color': 'white'}},
                36: {'label': 'Jan 2018'}
            },
            included = False

        )

    ], className="card_container"),

    html.Div([
        html.Div([
            dcc.Graph(id="map")], className="create_container1 twelve columns")

        ])






    ], id="mainContainer",style={"display": "flex", "flex-direction": "column"})






if __name__ == '__main__':
    app.run_server(debug=True)
