
import os
from flask import Flask, render_template,request,redirect
UPLOAD_FOLDER = '/static/img'
ALLOWED_EXTENSIONS = { 'png', 'jpg', 'jpeg', 'gif'}
app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
paints = []

@app.route('/galery', methods=["GET"])
def index():
   
        return render_template('image_mars.html')
    
@app.route('/galery', methods=['POST'])
def my_form_post():
    file = request.files['file']
    filename = file.filename
    print(filename)
    if 'file' not in request.files:
            
            return redirect(request.url)
    file = request.files['file']
    
    if file.filename == '':
        
        return redirect('/galery')
    if file:
        
        filename = file.filename
        
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
             
    
    return redirect('/galery')
    
    


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')