import cv2 as cv
import numpy as np

net = cv.dnn.readNet(
			"./models/yolov3.weights",
			"./models/yolov3.cfg")
clasees = []

with open("./models/coco.names", 'r') as f:
    classes = [line.strip() for line in f.readlines()]

layer_name = net.getLayerNames()
output_layer = [layer_name[i - 1] for i in net.getUnconnectedOutLayers()]
colors = np.random.uniform(0, 255, size=(len(classes), 3))

# Change Images:
img = cv.imread("./images/restaurant.jpeg")
# img = cv.imread("./images/zielo.jpeg")
img = cv.resize(img, None, fx=0.7, fy=0.7)
height, width, channel = img.shape

blob = cv.dnn.blobFromImage(
    img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
net.setInput(blob)
outs = net.forward(output_layer)

class_ids = []
confidences = []
boxes = []
for out in outs:
    for detection in out:
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]
        # Play with the confidence level
        if confidence > 0.85:
            center_x = int(detection[0] * width)
            center_y = int(detection[1] * height)
            w = int(detection[2] * width)
            h = int(detection[3] * height)
            x = int(center_x - w/2)
            y = int(center_y - h/2)
            boxes.append([x, y, w, h])
            confidences.append(float(confidence))
            class_ids.append(class_id)

indexes = cv.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
print(indexes)

font = cv.FONT_HERSHEY_PLAIN
for i in range(len(boxes)):
    if i in indexes:
        x, y, w, h = boxes[i]
        label = str(classes[class_ids[i]])
        color = colors[0]
        cv.rectangle(img, (x, y), (x + w, y + h), color, 2)
        cv.putText(img, label, (x, y + 30), font, 3, color, 3)

cv.imshow("IMG", img)
cv.waitKey(0)
cv.destroyAllWindows()