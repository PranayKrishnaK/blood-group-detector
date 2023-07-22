import cv2
import numpy as np

def preprocess_image(image_path):
    # Load the fingerprint image
    fingerprint = cv2.imread(image_path, 0)
    
    # Apply thresholding to convert it into binary image
    _, thresholded = cv2.threshold(fingerprint, 127, 255, cv2.THRESH_BINARY_INV)
    
    # Perform morphological operations to enhance fingerprint details
    kernel = np.ones((3, 3), np.uint8)
    processed_image = cv2.morphologyEx(thresholded, cv2.MORPH_CLOSE, kernel)
    
    return processed_image

def extract_minutiae(image):
    # Use a fingerprint feature extraction algorithm (e.g., Minutiae-based) to detect minutiae points
    
    # Placeholder code for demonstration purposes
    minutiae = [
        {'x': 100, 'y': 150, 'type': 'ridge-ending'},
        {'x': 200, 'y': 300, 'type': 'bifurcation'},
        # Add more minutiae points as per your requirements
    ]
    
    return minutiae

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
    fingerprint_image_path = "C:/Users/91939/Downloads/archive (5)/SOCOFing/Real/9__M_Left_little_finger.BMP"
    
    # Preprocess the image
    processed_image = preprocess_image(fingerprint_image_path)
    
    # Extract minutiae from the preprocessed image
    minutiae = extract_minutiae(processed_image)
    
    # Predict the blood group based on the extracted minutiae
    blood_group = predict_blood_group(minutiae)
    
    # Display the predicted blood group
    print("Predicted Blood Group:", blood_group)
    print(len(minutiae))

if __name__ == '__main__':
    main()
