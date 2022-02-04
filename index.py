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
    return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Привет, Марс!</title>
</head>
<body>
    <h1>Жди нас, Марс!</h1>
    
        <p><img src="static/img/300px-OSIRIS_Mars_true_color.jpg" alt="qwerty" ></p>
        <p>Вот она какая, красная планета.</p>
    

        
    
</body>
</html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')