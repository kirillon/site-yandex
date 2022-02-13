
from flask import Flask, render_template,request,redirect

app = Flask(__name__)



@app.route('/login', methods=["GET"])
def index():
   
        return render_template('image_mars.html')
    
@app.route('/login', methods=['POST'])
def my_form_post():
    print(request.form.to_dict(flat=False))
    return redirect('/login')
    
    


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')