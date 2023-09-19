import cv2
from pyzbar.pyzbar import decode
from gtts import gTTS
import os
import time
import platform
import pyttsx3
import subprocess

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def preprocess_image(frame):
    # Convert the frame to grayscale for thresholding
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Apply thresholding to create a binary image
    _, binary = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)
    
    # Enhance contrast
    enhanced = cv2.equalizeHist(binary)
    
    return enhanced

def play_audio(qr_code_data):
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Say "Hello"
    engine.say("Hello")

    # Wait for "Hello" to be spoken before saying the QR code data
    engine.runAndWait()

    # Say the QR code data
    engine.say(qr_code_data)
    engine.runAndWait()

def read_qr_code_content(qr_code_data):
    # Display the QR code data
    print("QR Code Data:", qr_code_data)

    # Play the audio
    play_audio(qr_code_data)

def scan_qr_code():
    # Initialize the camera
    cap = cv2.VideoCapture(0)
    
    qr_code_data = None  # Variable to store the QR code data

    while True:
        # Capture a frame from the camera
        ret, frame = cap.read()

        if not ret:
            print("Error: Could not access the camera.")
            break

        # Preprocess the captured frame
        processed_frame = preprocess_image(frame)

        # Decode the QR code(s) in the processed frame
        decoded_objects = decode(processed_frame)

        for obj in decoded_objects:
            # Extract the data from the QR code
            data = obj.data.decode('utf-8')

            # Store the data in the variable
            qr_code_data = data

            # You can add further processing or validation here
            
            # Break out of the loop once a QR code is detected
            break

        # Display the live camera feed in a window titled "Camera Preview"
        cv2.imshow('Camera Preview', frame)

        if qr_code_data:
            break  # Break out of the while loop if a QR code is detected

        # Check for user input to exit the preview
        key = cv2.waitKey(1)
        if key == ord('q'):  # Press 'q' to quit the preview
            break

    # Release the camera and close the OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

    return qr_code_data

def greet_user():
    engine.say("Hello! I am EDITH.")
    engine.runAndWait()

if __name__ == "__main__":
    greet_user()
    qr_code_data = scan_qr_code()
    
    if qr_code_data:
        read_qr_code_content(qr_code_data)
        subprocess.run(["python", "openai.py"])  # Replace with the filename of your second code
    else:
        print("No QR code detected or data found.")
