import cv2
from pyzbar.pyzbar import decode
import time

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

        # Decode the QR code(s) in the frame
        decoded_objects = decode(frame)

        for obj in decoded_objects:
            # Extract the data from the QR code
            data = obj.data.decode('utf-8')

            # Store the data in the variable
            qr_code_data = data

            # You can add further processing or validation here
            
            # Break out of the loop once a QR code is detected
            break

        # Display the frame for troubleshooting
        cv2.imshow('QR Code Scanner', frame)
        cv2.waitKey(1)

        if qr_code_data:
            break  # Break out of the while loop if a QR code is detected

        # Delay for a short time (e.g., 100 milliseconds)
        time.sleep(0.1)

    # Release the camera and close the OpenCV window
    cap.release()
    cv2.destroyAllWindows()

    return qr_code_data

if __name__ == "__main__":
    qr_code_data = scan_qr_code()
    
    if qr_code_data:
        print("QR Code Data:", qr_code_data)
    else:
        print("No QR code detected or data found.")
