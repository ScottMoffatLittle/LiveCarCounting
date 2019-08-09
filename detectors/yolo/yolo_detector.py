import cv2
import numpy as np
import os


__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

def get_bounding_boxes(image):
    # get object classes
    classes = None
    with open(os.path.join(__location__, 'classes.txt'), 'r') as classes_file:
        classes = [line.strip() for line in classes_file.readlines()]
    classes_of_interest = ['bicycle', 'car', 'motorcycle', 'bus', 'truck']
    
    # create a YOLO v3 DNN model using pre-trained weights
    net = cv2.dnn.readNet(os.path.join(__location__, 'yolov3.weights'), os.path.join(__location__, 'yolov3.cfg'))
    
    # create image blob
    scale = 0.00392
    image_blob = cv2.dnn.blobFromImage(image, scale, (416, 416), (0, 0, 0), True, crop=False)

    # detect objects
    net.setInput(image_blob)
    layer_names = net.getLayerNames()
    output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
    outputs = net.forward(output_layers)

    class_ids = []
    confidences = []
    boxes = []
    conf_threshold = 0.5
    nms_threshold = 0.4

    for output in outputs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5 and classes[class_id] in classes_of_interest:
                width = image.shape[1]
                height = image.shape[0]
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)
                x = center_x - w / 2
                y = center_y - h / 2
                class_ids.append(class_id)
                confidences.append(float(confidence))
                boxes.append([x, y, w, h])

    # remove overlapping bounding boxes
    indices = cv2.dnn.NMSBoxes(boxes, confidences, conf_threshold, nms_threshold)

    _bounding_boxes = []
    for i in indices:
        i = i[0]
        _bounding_boxes.append(boxes[i])

    return _bounding_boxes