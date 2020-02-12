from flask import Flask, render_template, request

from web_app.model import retrieving_table_data
from web_app.plotly_graph import graph_plotly_candle


def create_app():
    app = Flask(__name__)

    @app.route('/', methods=['GET', 'POST'])
    def index():
        """Главная страница"""

        title = "Golden"
        return render_template('index/index.html', page_title=title)

    @app.route('/plotly&data_btc', methods=['GET'])
    @app.route('/plotly&<database_table_title>', methods=['GET'])
    def create_plot(database_table_title='data_btc'):
        """Обработка полученных данных через ссылку и вывод результата на html страницу"""

        if database_table_title:
            title = f"График: {database_table_title[-3:]}"
            # Получение данных из базы данных(data). Данные для построения графика(div)
            data = retrieving_table_data(database_table_title)[-100:]
            div = graph_plotly_candle(data)

            return render_template("chart/plotly.html", graph=div, title=title)

    return app


if __name__ == "__main__":
    create_app().run(debug=True, use_reloader=True)
