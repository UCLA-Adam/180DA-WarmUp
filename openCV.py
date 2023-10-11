import cv2
import numpy as np
from PIL import Image

# function to get the limits for the box 
# provided by computervisioneng
def get_limits(color):
    c = np.uint8([[color]])  # BGR values
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    hue = hsvC[0][0][0]  # Get the hue value

    # Handle red hue wrap-around
    if hue >= 165:  # Upper limit for divided red hue
        lowerLimit = np.array([hue - 10, 100, 100], dtype=np.uint8)
        upperLimit = np.array([180, 255, 255], dtype=np.uint8)
    elif hue <= 15:  # Lower limit for divided red hue
        lowerLimit = np.array([0, 100, 100], dtype=np.uint8)
        upperLimit = np.array([hue + 10, 255, 255], dtype=np.uint8)
    else:
        lowerLimit = np.array([hue - 10, 100, 100], dtype=np.uint8)
        upperLimit = np.array([hue + 10, 255, 255], dtype=np.uint8)

    return lowerLimit, upperLimit

targetColor = [0,255,255] # this is blue in BRB
cap = cv2.VideoCapture(1)
while True: 
    ret, frame = cap.read()

    hsvImage = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    # # define range of blue color in HSV
    # lower_blue = np.array([110,50,50])
    # upper_blue = np.array([130,255,255])
    # # Threshold the HSV image to get only blue colors
    # mask = cv2.inRange(hsvImage, lower_blue, upper_blue)

    lowerLimit, upperLimit = get_limits(color = targetColor)

    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

    mask_ = Image.fromarray(mask)

    bbox = mask_.getbbox()

    print(bbox)

    if bbox is not None:
        x1, y1, x2, y2 = bbox

        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

    imS = cv2.resize(frame, (960, 540)) # Resize image to fit screen
    cv2.imshow('frame', imS)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break;

cap.reelease()
cv2.destoryAllWindows()
