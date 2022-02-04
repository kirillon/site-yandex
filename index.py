from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
        return "Миссия Колонизация Марса"
@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"
@app.route('/promotion')
def promotion():
    return """<h3>Человечество вырастает из детства.

            Человечеству мала одна планета.

            Мы сделаем обитаемыми безжизненные пока планеты.

            И начнем с Марса!

            Присоединяйся!</h3>"""
@app.route("/image_mars")
def image_mars():
    return render_template('image_mars.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')