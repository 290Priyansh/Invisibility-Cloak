import numpy as np
import cv2
import time

cap = cv2.VideoCapture(0)
time.sleep(2)
background = 0

# Capture background
for i in range(50):
    ret, background = cap.read()

while (cap.isOpened()):
    ret, img = cap.read()
    if not ret:
        break

    # Convert the image to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Setting the values for cloak and making mask (for red color in this case)
    lower_red1 = np.array([0, 120, 70])
    upper_red1 = np.array([10, 255, 255])
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)

    lower_red2 = np.array([170, 120, 70])
    upper_red2 = np.array([180, 255, 255])
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)

    # Combine mask
    mask = mask1 + mask2
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8), iterations=2)
    mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, np.ones((3, 3), np.uint8), iterations=1)

    # Create the inverse of the mask
    mask2 = cv2.bitwise_not(mask)

    # Replace the cloak with the background
    res1 = cv2.bitwise_and(background, background, mask=mask)

    # Keep the rest of the image intact
    res2 = cv2.bitwise_and(img, img, mask=mask2)

    # Combine the background and the original image (without the cloak)
    final_output = cv2.addWeighted(res1, 1, res2, 1, 0)

    # Show the final output
    cv2.imshow('Invisible Cloak', final_output)
s
    # Exit on pressing the 'Esc' key
    k = cv2.waitKey(10)
    if k == 27:  # ASCII value for ESC key
        break

cap.release()
cv2.destroyAllWindows()
