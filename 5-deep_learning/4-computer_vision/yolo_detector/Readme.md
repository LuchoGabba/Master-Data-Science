# YOLO Detector

In this exercise, you’ll learn how to load and use a pre-trained ML model for object detection. You’ll use a YOLO V3 Model along with its precalculated Neural Network weights.

## Python Objectives

- Use the OS Terminal.
- Build a Python environment using conda or venv.
- Code a ShellScript to launch the program.
- Pass parameters from the Shell Script to the Python program.

## Questions

1. What’s the purpose of the coco.names file?
2. What’s the cv.dnn.blobFromImage(..) method?
3. What happens when playing with the confidence variable? What's it for?
    Hint: Try extreme values like: —   if confidence > 0.9:
4. The method cv.dnn.NMSBoxes is strange. What’s its function?
5. Play with other images with different colors
6. If we want fewer false positives, what can we do?
7. If we want fewer false negatives, what can we do?

**Explain everything in your own words.**

## Computer Vision Insights

### Purpose of the coco.names File

The `coco.names` file contains the names of the object classes that the YOLO model can detect. It's used to map the detection predictions from the model (which are outputted as class IDs) to human-readable class names. This mapping allows us to understand which objects have been detected in an image by the model.

### The cv.dnn.blobFromImage(..) Method

This method is used to prepare the input image for the neural network. It performs mean subtraction, scaling, and optionally channel swapping on the image. It creates a 4D blob (N, C, H, W) from the image that can be fed into the neural network, where N is the number of images, C is the number of channels, H is the height, and W is the width.

### Playing with the Confidence Variable

The confidence variable represents how confident the model is that the detected object is accurate. Adjusting the confidence threshold (e.g., `if confidence > 0.9:`) can help reduce false positives (by increasing the threshold) or reduce false negatives (by decreasing the threshold). It's a critical parameter for balancing precision and recall.

### The cv.dnn.NMSBoxes Method

Non-Maximum Suppression (NMS) is a technique used to ensure that each detected object is represented by only one bounding box. `cv.dnn.NMSBoxes` takes the boxes and their confidence scores, and eliminates overlapping boxes, keeping only the ones with the highest confidence for each object.

### Experimenting with Images of Different Colors

Different images might reveal how well the model can generalize across various contexts and backgrounds. Experimenting with images of different colors and scenes can help understand the model's robustness and limitations.

### Managing False Positives and False Negatives

- **To reduce false positives**: Increase the confidence threshold. This means you're telling the model to be more "sure" before making a detection.
- **To reduce false negatives**: Decrease the confidence threshold or adjust the NMS threshold. This allows more potential detections to be considered, at the risk of increasing false positives.

## Resources

- YOLO GitHub: [YOLOv3 GitHub](https://github.com/ultralytics/yolov3/releases)
- YOLO V3 Overview: [Virtual Environment Setup](https://python.land/virtual-environments/virtualenv)
- OpenCV: [OpenCV Official Site](https://opencv.org/)


## Instructions & Set up

1. **Set Up Your Python Environment**: Use conda or venv to create a new environment for this project. Install necessary packages, including OpenCV.
2. **Download YOLOv3 Weights (mandatory!)**: Use the YOLO GitHub link provided in the resources to download the pre-trained weights (`yolov3.weights`).
3. **Implement Your Detector**: Code your Python program to use the YOLOv3 model for object detection. Utilize the `coco.names` for class names, adjust the confidence threshold as needed, and apply NMS.
4. **Shell Script (optional)**: Write a ShellScript to easily run your Python program. Ensure it can pass parameters (like image path or confidence threshold) to the Python script.
5. **Experiment**: Try running your detector on various images to see how it performs. Adjust confidence and NMS thresholds based on your needs.

Remember, the key to mastering computer vision techniques is experimentation and understanding the impact of different parameters on your model's performance. Good luck!