from flask import Flask, render_template

from web_app.model import retrieving_table_data
from web_app.plotly_graph import graph_plotly_candle


def create_app():
    app = Flask(__name__)

    # для проверки соединения
    @app.route('/')
    def conect_db():
        title = "Расчет данных"
        data = retrieving_table_data('data_btc')
        data = data[-10:]

        return render_template('index.html', page_title=title, news_lists=data)

    # Обработка полученных данных через ссылку и вывод результата на html страницу
    @app.route('/plotly&<database_table_title>', methods=['GET'])
    def create_plot(database_table_title):
        title = f"График: {database_table_title[-3:]}"
        # Получение данных из базы данных(data). Данные для построения графика(div)
        data = retrieving_table_data(database_table_title)
        div = graph_plotly_candle(data)

        return render_template("plotly.html", graph=div, title=title)

    return app


if __name__ == "__main__":
    create_app().run(debug=True)
