from dash import Dash, html, dcc, dash_table, callback, Output, Input
import pandas as pd
import plotly.express as px

# Укажи свой путь к файлу 'rgr.csv'. В данном случае, путь изменен на предложенный: C:\Users\79243\OneDrive\Рабочий стол\РГР СПС\rgr.csv
file_path = r'D:\RGR SPS\rgr.csv'

# Чтение данных из CSV файла
df = pd.read_csv(file_path)

app = Dash(__name__)

app.layout = html.Div([
    html.H1(children='Информация о книгах и выдаче'),

    dcc.Dropdown(
        id='dropdown',
        options=[
            {'label': 'Книги', 'value': 'Книги'},
            {'label': 'Автор', 'value': 'Автор'},
            {'label': 'Жанр', 'value': 'Жанр'},
            {'label': 'Дата выдачи', 'value': 'Дата выдачи'},
            {'label': 'Дата планируемого возврата', 'value': 'Дата планируемого возврата'},
            {'label': 'Фамилия сотрудника выдающего книгу', 'value': 'Фамилия сотрудника выдающего книгу'},
            {'label': 'Фамилия Читатель', 'value': 'Фамилия Читатель'}
        ],
        value='Книги'
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
    fig = px.line(df, x=df.index, y=selected_value, title=f'График {selected_value} бронирования')
    return fig

@app.callback(
    Output('scatter-plot', 'figure'),
    [Input('dropdown', 'value')]
)
def update_scatter_plot(selected_value):
    scatter_fig = px.scatter(df, x='Карточка выдачи', y=selected_value, title=f'График рассеяния')
    return scatter_fig

if __name__ == '__main__':
    app.run_server(debug=True)