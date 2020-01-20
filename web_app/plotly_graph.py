"""Скрипт обработки данных для посторения графика плотли"""

import csv

import pandas as pd
import plotly.graph_objects as go
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



    # возвращает div с данными для построения графика на html странице
    div = plotly.offline.plot(fig, include_plotlyjs=False, output_type='div')

    return div
