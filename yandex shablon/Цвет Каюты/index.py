
import os
from flask import Flask, render_template,request,redirect, url_for
UPLOAD_FOLDER = '/static/img'
ALLOWED_EXTENSIONS = { 'png', 'jpg', 'jpeg', 'gif'}
app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
paints = []

@app.route('/table/<pol>/<voz>')
def index(pol,voz):
        if int(voz)>=21:
            img =url_for("static",filename="img/8QDSgbz.jpg")
            if pol=="male":
                
                
                col= "background-color:#0000FF;padding=100px;"
            else:
                col = "background-color:#FF1493;padding=100px;"
        else:
            img =url_for("static",filename="img/357491-admin.jpg")
            
            if pol=="male":
                
                col = "background-color:#00FFFF;padding=100px;"
            else:
                col = "background-color:#FFB6C1;padding=100px;"
        
        
            
        return render_template('image_mars.html',pol=pol,voz=int(voz),img=img, col=col)
    

    


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')