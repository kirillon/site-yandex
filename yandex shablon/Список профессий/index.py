from flask import Flask, render_template

app = Flask(__name__)



@app.route('/list_prof/<prof>')
def index(prof):
    lst = ["инженер","врач", "техник","Ильич"]
    if "ol" in prof:
        print(1)
        return render_template('image_mars.html', prof="ol",lst= lst)
    else:
        return render_template('image_mars.html', prof="ul",lst= lst)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')