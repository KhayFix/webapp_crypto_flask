"""Скрипт обработки данных для посторения графика плотли"""

import csv

import pandas as pd
import plotly.graph_objects as go
# from plotly.offline.offline import plot
import plotly


def graph_plotly_candle(getting_data_database):
    # создание csv файла
    with open('export.csv', 'w', newline='', encoding='utf-8') as my_files:
        fields = ['id', 'Timestamp', 'Open', 'Close', 'High', 'Low', 'Volume']
        writer = csv.DictWriter(my_files, fields, delimiter=',')
        writer.writeheader()
        for user in getting_data_database:
            writer.writerow(user)

    df = pd.read_csv('export.csv')

    fig = go.Figure(data=[go.Candlestick(x=df['Timestamp'],
                                         open=df['Open'],
                                         high=df['High'],
                                         low=df['Low'],
                                         close=df['Close'])])

    # создание полного файла
    # fig.write_html("file.html")

    # создает новый файл и открывает его
    # plotly.offline.plot(fig, filename='file.html')

    # возвращает div с данными для построения графика на html странице
    div = plotly.offline.plot(fig, include_plotlyjs=False, output_type='div')

    return div
