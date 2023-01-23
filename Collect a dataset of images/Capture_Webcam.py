import cv2

# Start the webcam
cap = cv2.VideoCapture(0)

for i in range(1000):
    # Capture a frame from the webcam
    ret, frame = cap.read()

    # Get the coordinates of the object
    x, y, w, h = cv2.selectROI(frame)

    # Save the image and the coordinates to a file
    cv2.imwrite(f'webcam_images/image{i}.jpg', frame)
    with open(f'webcam_images/coordinates{i}.txt', 'w') as f:
        f.write(f'{x}, {y}, {w}, {h}')

# Release the webcam
cap.release()
