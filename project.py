import cv2
import numpy as np
from flask import Flask ,render_template,request,send_file
from keras.models import  load_model

app = Flask(__name__)
UPLOAD_FOLDER = 'static\\uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/result',methods=['GET','POST'])

def submit():
    global prediction,a
    prediction=""
    if request.method == 'POST':
        if request.files:
            image = request.files['image']
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], image.filename))
            print(image.filename)
            img= cv2.imread(os.path.join(app.config['UPLOAD_FOLDER'], image.filename))
            tempimg = img
            img = cv2.resize(img,(300,300))
            img = img/255.0
            img = img.reshape(1,300,300,3)
            a=model.predict(img)
            prediction = model.predict(img) >= 0.5
            if prediction>=0.5:
                prediction = "Pneumonia"
            else:
                prediction = "Normal"
        return render_template('result.html',accuracy_pneumonia=a[0],result_pneumonia=prediction)
    return render_template('result.html')
def preprocess_image(image_path):
    # Load the fingerprint image
    fingerprint = cv2.imread(image_path, 0)

    # Apply thresholding to convert it into a binary image
    _, thresholded = cv2.threshold(fingerprint, 127, 255, cv2.THRESH_BINARY_INV)

    # Perform morphological operations to enhance fingerprint details
    kernel = np.ones((3, 3), np.uint8)
    processed_image = cv2.morphologyEx(thresholded, cv2.MORPH_CLOSE, kernel)

    return processed_image

def extract_minutiae(image):
    # Use a fingerprint feature extraction algorithm (e.g., Minutiae-based) to detect minutiae points
    # Placeholder code for demonstration purposes
    # This is just an example of detected minutiae points
    minutiae = [
        {'x': 100, 'y': 150, 'type': 'ridge-ending'},
        {'x': 200, 'y': 300, 'type': 'bifurcation'},
        # Add more minutiae points as per your requirements
    ]

    return minutiae

def calculate_distance(point1, point2):
    return np.sqrt((point2['x'] - point1['x'])**2 + (point2['y'] - point1['y'])**2)

def predict_blood_group(minutiae):
    # Placeholder code for demonstration purposes
    # Assign a random blood group based on the number of detected minutiae
    if len(minutiae) < 5:
        blood_group = 'A'
    elif len(minutiae) >= 5 and len(minutiae) < 10:
        blood_group = 'B'
    else:
        blood_group = 'O'

    return blood_group

# Main function
def main():
    # Provide the path to the fingerprint image
    fingerprint_image_path =

    # Preprocess the image
    processed_image = preprocess_image(fingerprint_image_path)

    # Extract minutiae from the preprocessed image
    minutiae = extract_minutiae(processed_image)

    # Calculate the length between minutiae points
    total_length = 0
    for i in range(len(minutiae) - 1):
        total_length += calculate_distance(minutiae[i], minutiae[i + 1])

    # Predict the blood group based on the extracted minutiae
    blood_group = predict_blood_group(minutiae)

    # Display the predicted blood group and total length between minutiae
    print("Predicted Blood Group:", blood_group)
    print("Total Length between Minutiae (in pixels):", total_length)

if __name__ == '__main__':
    main()
