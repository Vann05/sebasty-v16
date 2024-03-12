import cv2

def main():
    # Loop through camera indexes from 0 to 10
    for i in range(10):
        cap = cv2.VideoCapture(i)
        if not cap.isOpened():
            print(f"No camera found at index {i}")
        else:
            print(f"Camera found at index {i}")
            cap.release()

if __name__ == '__main__':
    main()
