import cv2

def main():
    # Create a VideoCapture object
    cap = cv2.VideoCapture(0)  # 0 is the default camera index, change if you have multiple cameras

    # Check if camera opened successfully
    if not cap.isOpened():
        print("Error: Could not open webcam")
        return

    print("Webcam testing. Press 'q' to exit.")

    # Loop to capture frames from the webcam
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Display the resulting frame
        cv2.imshow('Webcam', frame)

        # Check for the 'q' key to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the VideoCapture object and close all windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
