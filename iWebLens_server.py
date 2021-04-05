from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse, abort
import json
import numpy as np
import sys
import time
import cv2
import os

app = Flask(__name__)
api = Api(app)

# construct the argument parse and parse the arguments
confthres = 0.3
nmsthres = 0.1

def get_labels(labels_path):
    # load the COCO class labels our YOLO model was trained on
    lpath=os.path.sep.join([yolo_path, labels_path])
    
    #print(yolo_path)
    LABELS = open(lpath).read().strip().split("\n")
    return LABELS


def get_weights(weights_path):
    # derive the paths to the YOLO weights and model configuration
    weightsPath = os.path.sep.join([yolo_path, weights_path])
    return weightsPath

def get_config(config_path):
    configPath = os.path.sep.join([yolo_path, config_path])
    return configPath

def load_model(configpath,weightspath):
    # load our YOLO object detector trained on COCO dataset (80 classes)
    print("[INFO] loading YOLO from disk...")
    net = cv2.dnn.readNetFromDarknet(configpath, weightspath)
    return net

def do_prediction(image,net,LABELS):

    (H, W) = image.shape[:2]
    # determine only the *output* layer names that we need from YOLO
    ln = net.getLayerNames()
    ln = [ln[i[0] - 1] for i in net.getUnconnectedOutLayers()]

    # construct a blob from the input image and then perform a forward
    # pass of the YOLO object detector, giving us our bounding boxes and
    # associated probabilities
    blob = cv2.dnn.blobFromImage(image, 1 / 255.0, (416, 416),
                                 swapRB=True, crop=False)
    net.setInput(blob)
    start = time.time()
    layerOutputs = net.forward(ln)
    #print(layerOutputs)
    end = time.time()

    # show timing information on YOLO
    print("[INFO] YOLO took {:.6f} seconds".format(end - start))

    # initialize our lists of detected bounding boxes, confidences, and
    # class IDs, respectively
    boxes = []
    confidences = []
    classIDs = []

    # loop over each of the layer outputs
    for output in layerOutputs:
        # loop over each of the detections
        for detection in output:
            # extract the class ID and confidence (i.e., probability) of
            # the current object detection
            scores = detection[5:]
            # print(scores)
            classID = np.argmax(scores)
            # print(classID)
            confidence = scores[classID]

            # filter out weak predictions by ensuring the detected
            # probability is greater than the minimum probability
            if confidence > confthres:
                # scale the bounding box coordinates back relative to the
                # size of the image, keeping in mind that YOLO actually
                # returns the center (x, y)-coordinates of the bounding
                # box followed by the boxes' width and height
                box = detection[0:4] * np.array([W, H, W, H])
                (centerX, centerY, width, height) = box.astype("int")

                # use the center (x, y)-coordinates to derive the top and
                # and left corner of the bounding box
                x = int(centerX - (width / 2))
                y = int(centerY - (height / 2))

                # update our list of bounding box coordinates, confidences,
                # and class IDs
                boxes.append([x, y, int(width), int(height)])
                confidences.append(float(confidence))
                classIDs.append(classID)

    # apply non-maxima suppression to suppress weak, overlapping bounding boxes
    idxs = cv2.dnn.NMSBoxes(boxes, confidences, confthres, nmsthres)

    objects = {}
    arr = []
    # TODO Prepare the output as required to the assignment specification
    # ensure at least one detection exists
    if len(idxs) > 0:
        # loop over the indexes we are keeping
        for i in idxs.flatten():
            objects[i] = {}
            objects[i]["abel"] = LABELS[classIDs[i]]
            objects[i]["accuracy"] = confidences[i]
            objects[i]["rectangle"] = {}
            objects[i]["rectangle"]["height"] = boxes[i][3]
            objects[i]["rectangle"]["left"] = boxes[i][0]
            objects[i]["rectangle"]["top"] = boxes[i][1] + boxes[i][3]
            objects[i]["rectangle"]["width"] = boxes[i][2]
            arr.append(objects[i])
            # print("detected item:{}, accuracy:{}, X:{}, Y:{}, width:{}, height:{}".format(LABELS[classIDs[i]],
            #                                                                                  confidences[i],
            #                                                                                  boxes[i][0],
            #                                                                                  boxes[i][1],
            #                                                                                  boxes[i][2],
            #                                                                                  boxes[i][3]))
    return arr


yolo_path  = "yolo_tiny_configs"

## Yolov3-tiny versrion
labelsPath= "coco.names"
cfgpath= "yolov3-tiny.cfg"
wpath= "yolov3-tiny.weights"

Lables=get_labels(labelsPath)
CFG=get_config(cfgpath)
Weights=get_weights(wpath)


@app.route('/api/object_detection', methods=['POST'])
def main():
    try:
        imagefile = json.loads(request.json)['image']
        # imagefile = request.files["image"].read()
        # image = Image.open(BytesIO(imagefile))
        img = cv2.imread(imagefile)
        npimg = np.array(img)
        image = npimg.copy()
        image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
        # load the neural net.  Should be local to this method as its multi-threaded endpoint
        # nets = load_model(CFG, Weights)
        # object_arr = do_prediction(image, nets, Lables)
        
        result = {}
        result["id"] = imgae_id
        result["objects"] = object_arr
        image_id = json.loads(request.json)['id']
        return result

    except Exception as e:
        print("Exception  {}".format(e))

# class Image(Resource):
#   def post(self):
#     image_id = json.loads(request.json)['id']
#     #result = json.dumps('{"id": {}, "object": [{"label": "book"}]}'.format(image_id))
#     #image = Image.open(ByteIO(i))
#     #image = np.array(image)
#           #request.get_json()
#     return image_id
# api.add_resource(Image, "/api/object_detection")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)