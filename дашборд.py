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
        id='period-dropdown',
        options=[
            {'label': 'Месяц', 'value': 'Месяц'},
            {'label': 'Квартал', 'value': 'Квартал'},
            {'label': 'Год', 'value': 'Год'}
        ],
        value='Месяц'
    ),

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

    dcc.Graph(id='scatter-plot'),

    dcc.Graph(id='pie-chart'),

    dcc.Graph(id='histogram'),

    dash_table.DataTable(
        id='financial-metrics',
        columns=[{'name': metric, 'id': metric} for metric in ['Прибыль', 'Выручка', 'Расходы']],  # Необходимо указать необходимые ключевые показатели
        data=[]  # Начальные данные для таблицы
    )
])

@app.callback(
    Output('graph', 'figure'),
    [Input('dropdown', 'value')]
)
def update_graph(selected_value):
    fig = px.line(df, x='Дата', y='Сумма', title='Динамика доходов и расходов')
    return fig

@app.callback(
    Output('scatter-plot', 'figure'),
    [Input('dropdown', 'value')]
)
def update_scatter_plot(selected_value):
    scatter_fig = px.scatter(df, x='Дата', y='Сумма', title='График рассеяния')
    return scatter_fig

@app.callback(
    Output('pie-chart', 'figure'),
    [Input('dropdown', 'value')]
)
def update_pie_chart(selected_value):
    pie_fig = px.pie(df, names='Категория', values='Сумма', title='Структура расходов по категориям')
    return pie_fig

@app.callback(
    Output('histogram', 'figure'),
    [Input('dropdown', 'value')]
)
def update_histogram(selected_value):
    hist_fig = px.histogram(df, x='Дата', y='Сумма', title='Анализ прибыли и ее распределения')
    return hist_fig

@app.callback(
    Output('financial-metrics', 'data'),
    [Input('dropdown', 'value')]
)
def update_financial_metrics(selected_value):
    # Здесь вам нужно написать логику для расчета ключевых финансовых показателей и предоставления их в виде данных для таблицы
    # Ниже приведен пример с использованием фиктивных значений для демонстрации
    data = [
        {
            'Прибыль': 10000,
            'Выручка': 30000,
            'Расходы': 20000
        }
    ]
    return data

if __name__ == '__main__':
    app.run_server(debug=True)
