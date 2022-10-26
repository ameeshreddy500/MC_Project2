from flask import Flask
from flask import request
import base64
from PIL import Image
import io
import datetime
import os

app=Flask(__name__)

@app.route('/')
def welcome():
    return 'You are now connected to the server'


@app.route('/upload',methods=['POST'])
def upload():
       text=request.form['category'] 
       type = request.form['type'] 

       # Failure to return a redirect or render_template       
       image = base64.b64decode(text) 
       fileName = f'{type}-{datetime.datetime.now().strftime("%Y-%m-%d--%H-%M-%S")}.jpeg'
       dirPath = ('/Users/ameesh/Documents/untitled folder/MC Project/'+type)
       isExist = os.path.exists(dirPath)

       # Create a new directory because it does not exist 
       if not isExist:
              os.makedirs(dirPath,mode = 0o666)
       imagePath = (dirPath+"/"+fileName)
       img = Image.open(io.BytesIO(image))
       img.save(imagePath, 'jpeg')
       print("image uploaded successfully")
       return "success"

if __name__=="__main__":
   app.run(host='0.0.0.0',debug=True,port=8000)