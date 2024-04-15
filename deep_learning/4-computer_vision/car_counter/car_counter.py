import cv2
import imutils
import numpy as np
import time

# Detection boxes
class Box:
    def __init__(self, name,  start_point, width_height):
        self.name = name
        self.start_point = start_point
        self.end_point = (start_point[0] + width_height[0], start_point[1] + width_height[1])
        self.counter = 0
        self.frame_countdown = 0

    def overlap(self, start_point, end_point):
        if self.start_point[0] >= end_point[0] or self.end_point[0] <= start_point[0] or \
                self.start_point[1] >= end_point[1] or self.end_point[1] <= start_point[1]:
            return False
        else:
            return True

# Mistery method. What's its purpose?
def non_max_suppression(_boxes, _overlapThresh):
    if len(_boxes) == 0:
        return []
    if _boxes.dtype.kind == "i":
        _boxes = _boxes.astype("float")
    pick = []
    x1 = _boxes[:, 0]
    y1 = _boxes[:, 1]
    x2 = _boxes[:, 2]
    y2 = _boxes[:, 3]
    area = (x2 - x1 + 1) * (y2 - y1 + 1)
    idxs = np.argsort(y2)
    while len(idxs) > 0:
        last = len(idxs) - 1
        i = idxs[last]
        pick.append(i)
        xx1 = np.maximum(x1[i], x1[idxs[:last]])
        yy1 = np.maximum(y1[i], y1[idxs[:last]])
        xx2 = np.minimum(x2[i], x2[idxs[:last]])
        yy2 = np.minimum(y2[i], y2[idxs[:last]])
        w = np.maximum(0, xx2 - xx1 + 1)
        h = np.maximum(0, yy2 - yy1 + 1)
        overlap = (w * h) / area[idxs[:last]]
        idxs = np.delete(idxs, np.concatenate(([last],
                                               np.where(overlap > _overlapThresh)[0])))
    return _boxes[pick].astype("int")


print('OpenCV Ver: ', cv2.__version__)

###################################
# Read video from webcam RTSP
# cap = cv2.VideoCapture("rtsp://127.0.0.1:554/stream1")
###################################

###################################
# Read video from attached webcam
# cap = cv2.VideoCapture(0)
###################################

###################################
# Read video from stored video
cap = cv2.VideoCapture("../video/cars.mp4")
###################################

last_frame = None
text = ""
textTerm = ""
boxes = []
boxes.append(Box('Up', (700, 250), (50, 50)))
boxes.append(Box('Down', (600, 380), (50, 50)))

while cap.isOpened():
    contourBoxes = []
    # Sleep for 3 seconds
    # What happens if we comment the time.sleep line?
    time.sleep(0.02) 
    _, frame = cap.read()

    # Frame / Image resize
    width = 848
    height = 480
    dim = (width, height)
    frame = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)

    # Convert to Gray Scale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Blur image
    # Why we want to blur the image?
    # Ehat's the size of the blurring kernel?
    gray = cv2.GaussianBlur(gray, (5, 5), 1)
    
    if last_frame is None or last_frame.shape != gray.shape:
        last_frame = gray
        continue
    
    # Get the difference from the last frame
    delta_frame = cv2.absdiff(last_frame, gray)
    last_frame = gray

    # Put a threshold on what is enough movement
    thresh = cv2.threshold(delta_frame, 25, 255, cv2.THRESH_BINARY)[1]

    # Image dilation
    thresh = cv2.dilate(thresh, None, iterations=2)

    # Find moving things
    contours = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)

    # Loops over all objects found
    for contour in contours:
        # Skip if contour area is too small (play with this value))
        if cv2.contourArea(contour) < 50:
            continue

        # Get's a bounding box and puts it on the frame
        (x, y, w, h) = cv2.boundingRect(contour)
        contourBoxes.append([x, y, x + w, y + h])
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # The text string we will build up
        text = "Cars:"
        textTerm = "Cars:"
        # Go through all the boxes
        for box in boxes:
            box.frame_countdown -= 1
            if box.overlap((x, y), (x + w, y + h)):
                if box.frame_countdown <= 0:
                    box.counter += 1
                box.frame_countdown = 20
            text += " (" + box.name + ": " + str(box.counter) + ")"
            textTerm += " (" + box.name + ": " + str(box.counter) + ")"


    # Annotate the frame with text and boxes
    cv2.putText(frame, text, (10, 20), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
    for box in boxes:
        cv2.rectangle(frame, box.start_point, box.end_point, (255, 255, 255), 2)

    # Show the frame
    cv2.imshow("Car Counter", frame)

    # What for 'q' press to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Clean the room
cap.release()
cv2.destroyAllWindows()
