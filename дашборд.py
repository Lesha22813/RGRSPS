from dash import Dash, html, dcc, dash_table, callback, Output, Input
import pandas as pd
import plotly.express as px

# Укажите путь к вашему новому файлу CSV
file_path = r'D:/учёба/дашборд/fin.csv'

# Чтение данных из нового CSV файла
df = pd.read_csv(file_path)

app = Dash(__name__)

app.layout = html.Div([
    html.H1(children='Информация о финансовых данных'),

    dcc.Dropdown(
        id='dropdown',
        options=[
            {'label': 'Дата', 'value': 'Дата'},
            {'label': 'Сумма', 'value': 'Сумма'}
        ],
        value='Дата'
    ),

    dash_table.DataTable(
        id='table',
        columns=[{'name': col, 'id': col} for col in df.columns],
        data=df.to_dict('records')
    ),

    dcc.Graph(id='graph'),

    dcc.Graph(id='scatter-plot')
])

@app.callback(
    Output('graph', 'figure'),
    [Input('dropdown', 'value')]
)
def update_graph(selected_value):
    fig = px.line(df, x='Дата', y=selected_value, title=f'График {selected_value} по времени')
    return fig

@app.callback(
    Output('scatter-plot', 'figure'),
    [Input('dropdown', 'value')]
)
def update_scatter_plot(selected_value):
    scatter_fig = px.scatter(df, x='Карта', y=selected_value, title='График рассеяния')
    return scatter_fig

if __name__ == '__main__':
    app.run_server(debug=True)
