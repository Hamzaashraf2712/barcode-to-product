import cv2
import matplotlib.pyplot as plt
from pyzbar.pyzbar import decode

def select_camera(camera_name):
    # Iterate over available cameras and find the one with the specified name
    for index in range(10):
        cap = cv2.VideoCapture(index)
        if cap.isOpened():
            _, frame = cap.read()
            cap.release()
            if frame is not None:
                cap = cv2.VideoCapture(index)
                return cap
    return None

def read_barcodes(frame):
    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Decode barcodes
    barcodes = decode(gray)
    
    if len(barcodes) > 0:
        # Extract information of the first detected barcode
        barcode = barcodes[0]
        
        # Extract barcode data
        x, y, w, h = barcode.rect
        barcode_info = barcode.data.decode('utf-8')
        
        # Draw a rectangle around the barcode
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        
        # Display barcode data
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, barcode_info, (x + 6, y - 6), font, 0.5, (255, 0, 0), 1)
        
        return barcode_info, frame
    
    return None, frame

def main():
    # Specify the camera name
    camera_name = "Your Camera Name Here"
    
    # Select the camera
    cap = select_camera(camera_name)
    if cap is None:
        print("Camera not found.")
        return
    
    try:
        while True:
            # Capture frame-by-frame
            ret, frame = cap.read()
            if not ret:
                continue
            
            # Detect barcode in the frame
            barcode_info, frame = read_barcodes(frame)
            
            # If barcode detected, print and break
            if barcode_info:
                print("Barcode detected:", barcode_info)
                break
    except KeyboardInterrupt:
        pass
    finally:
        # Release the capture
        cap.release()
    
    # Display confirmation message
    print("Barcode found! Exiting...")

if __name__ == "__main__":
    main()
