from flask import Flask,render_template,redirect,url_for,request
from blood_type_detection import predict

app = Flask(__name__)

@app.route('/', methods = ["GET", "POST"])
def home():
    if request.method == "POST":
        
        image_file = request.files.get('myFile', None)
        print(image_file)
        # print(request.form)

        file_path = f"static/finger_prints/{image_file.filename}"
        image_file.save(file_path)
        
        blood_group, total_length = predict(file_path)
        return render_template('home.html', blood_group = blood_group, total_length = total_length)

    return render_template('home.html')


if __name__ == '__main__':
   app.run(debug = True)
