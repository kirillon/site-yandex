from flask import Flask, render_template

app = Flask(__name__)



@app.route('/training/<prof>')
def index(prof):
    inj = "../static/img/professiya-inzhener-735x400.jpg"
    other = "../static/img/300px-OSIRIS_Mars_true_color.jpg"
    if "инженер" in prof or "строитель" in prof:
        return render_template('image_mars.html', img=inj)
    else:
        return render_template('image_mars.html', img=other)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')