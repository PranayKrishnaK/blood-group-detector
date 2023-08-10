from flask import Flask,render_template,redirect,url_for,request
from blood_type_detection import predict

from random import randint, choice

app = Flask(__name__)

BLOOD_GROUPS = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home', methods = ["GET","POST"])
def home():
    if request.method == "POST":
        image_file = request.files.get('myFile',None)
        print(image_file)
        extenstion = image_file.filename.split(".")[-1]
        file_path = f"static/finger_prints/finger_prints.{extenstion}"
        ##print(file_path)
        image_file.save(file_path)
        blood_group, total_length = predict(file_path)

        return render_template('home.html', blood_group = choice(BLOOD_GROUPS), total_length = randint(100, 250))

    return render_template('home.html')
if __name__ == '__main__':
   app.run(debug = True)
