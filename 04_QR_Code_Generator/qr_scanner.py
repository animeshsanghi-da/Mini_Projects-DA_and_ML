"""
Prerequisites
    1. Before running the script, ensure you have the necessary libraries installed:
        pip install opencv-python pyzbar numpy
"""
import cv2
import numpy as np
import os
from pyzbar.pyzbar import decode

def scan_qr_webcam():
    # Initialize the camera
    cap = cv2.VideoCapture(0)
    
    print("\n[INFO] Webcam active. Press 'q' on the video window to exit.")

    while True:
        # Read the current frame from the camera
        ret, frame = cap.read()
        
        if not ret:
            print("[ERROR] Failed to grab frame from webcam.")
            break

        # Decode the QR codes in the frame
        decoded_objects = decode(frame)

        for obj in decoded_objects:
            # Extract the data and draw a rectangle around the QR code
            data = obj.data.decode('utf-8')
            qr_type = obj.type
            
            # Print the data to console
            print(f"Detected {qr_type}: {data}")

            # Draw a box around the QR code for visual feedback
            pts = [(point.x, point.y) for point in obj.polygon]
            if len(pts) > 3:
                pts_array = np.array(pts, dtype=np.int32).reshape((-1, 1, 2))
                cv2.polylines(frame, [pts_array], True, (0, 255, 0), 3)

        # Show the video feed
        cv2.imshow('QR Code Scanner - Webcam', frame)

        # Exit the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release resources
    cap.release()
    cv2.destroyAllWindows()

def scan_qr_image():
    print("\n[INFO] Please ensure your image is copy-pasted into the same folder as this script.")
    filename = input("Enter the exact name of the image file (e.g., qrcode.png, image.jpg): ").strip()
    
    # Check if the file exists in the current directory
    if not os.path.exists(filename):
        print(f"\n[ERROR] Could not find '{filename}' in the current directory. Please check the name and try again.")
        return

    # Read the image
    frame = cv2.imread(filename)
    if frame is None:
        print("\n[ERROR] Could not read the image. The file might be corrupted or in an unsupported format.")
        return

    # Decode the QR codes in the image
    decoded_objects = decode(frame)

    if not decoded_objects:
        print("\n[INFO] No QR code detected in the provided image.")

    for obj in decoded_objects:
        # Extract the data
        data = obj.data.decode('utf-8')
        qr_type = obj.type
        
        # Print the data to console
        print(f"\nDetected {qr_type}: {data}")

        # Draw a box around the QR code for visual feedback
        pts = [(point.x, point.y) for point in obj.polygon]
        if len(pts) > 3:
            pts_array = np.array(pts, dtype=np.int32).reshape((-1, 1, 2))
            cv2.polylines(frame, [pts_array], True, (0, 255, 0), 3)

    # Show the image with the highlighted QR code
    cv2.imshow(f'QR Code Scanner - {filename}', frame)
    print("\n[INFO] Press ANY key on the image window to close it.")
    
    # Wait indefinitely until a key is pressed
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    print("=== QR Code Scanner ===")
    print("How would you like to provide the QR code?")
    print("1. Use Webcam")
    print("2. Upload an Image File")
    
    choice = input("Enter your choice (1 or 2): ").strip()
    
    if choice == '1':
        scan_qr_webcam()
    elif choice == '2':
        scan_qr_image()
    else:
        print("\n[ERROR] Invalid choice. Please run the script again and select 1 or 2.")

if __name__ == "__main__":
    main()