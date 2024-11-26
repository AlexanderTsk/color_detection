import cv2
import numpy as np
from PIL import Image

def get_limits(color):
    c = np.uint8([[color]])
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    lower_limit = hsvC[0][0][0] - 10, 100, 100
    upper_limit = hsvC[0][0][0] + 10, 255, 255

    lower_limit = np.array(lower_limit, dtype=np.uint8)
    upper_limit = np.array(upper_limit, dtype=np.uint8)

    return lower_limit, upper_limit

while True:
    try:
        r = int(input("Type red value "))
        g = int(input("Type green value "))
        b = int(input("Type blue value "))
    except ValueError:
        print("Incorrect input data. Please enter integer values.")
        continue

    if not (0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255):
        print("Values must be in the range 0 to 255.")
        continue
    
    break

cap = cv2.VideoCapture(1)

input_color = (r ,g, b)
lower_limit, upper_limit = get_limits(input_color)
while True:
    ret, frame = cap.read()

    hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv_image, lower_limit, upper_limit)
    mask_ = Image.fromarray(mask)

    bbox = mask_.getbbox()

    if bbox is not None: 
        x1, y1, x2, y2 = bbox 
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 255), 5)

    cv2.imshow('Stream Title', frame)

    if cv2.waitKey(1) &  0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
