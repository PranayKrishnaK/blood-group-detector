import cv2
import numpy as np

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
def predict(fingerprint_image_path):
    # Provide the path to the fingerprint image
    # fingerprint_image_path ="C:/Users/91939/Downloads/archive (5)/SOCOFing/Real/9__M_Left_little_finger.BMP"

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
    return blood_group, total_length
    print("Predicted Blood Group:", blood_group)
    print("Total Length between Minutiae (in pixels):", total_length)

if __name__ == '__main__':
    predict()
