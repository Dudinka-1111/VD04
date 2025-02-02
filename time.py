from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def home():
    # Получаем текущие дату и время
    now = datetime.now()
    # Форматируем дату и время в строку
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return f"<h1>Текущие дата и время: {current_time}</h1>"


if __name__ == '__main__':
    app.run(debug=True)