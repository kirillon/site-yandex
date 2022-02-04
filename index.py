from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
        return "Миссия Колонизация Марса"
@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"
@app.route('/promotion')
def promotion():
    return """<p>Человечество вырастает из детства.</p>

            <p>Человечеству мала одна планета.</p>

            <p>Мы сделаем обитаемыми безжизненные пока планеты.</p>

            <p>И начнем с Марса!</p>

            <p>Присоединяйся!</p>"""
@app.route("/image")
def image_mars():
    return render_template("image_mars.html")


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')