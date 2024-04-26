import os
import json
import base64
from tqdm import tqdm

path = "/path/to/txt_files"  # directory path that contains yolo txt file

image_dir = "/path/to/images"   # directory path that contains images

# label = ['person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus', 'train', 'truck', 'boat', 'traffic light', 'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear', 'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball', 'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard', 'tennis racket', 'bottle', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple', 'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza', 'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed', 'dining table', 'toilet', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone', 'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'book', 'clock', 'vase', 'scissors', 'teddy bear', 'hair drier', 'toothbrush']  

label = ['person', 'ball']

poly_point = 10  # the higher the number, the lesser the polygon point (!even numbers only)
img_width = 1920  # img size
img_height = 1080

sorted_labels = sorted(os.listdir(path))

for i in tqdm(sorted_labels):
    if i.endswith(".txt"):
        file = open(path+"/"+i, 'r')
        Lines = file.readlines()
        point = []
        for c, line in enumerate(Lines):
            content = line.split(" ")
            label = content[0]

            if label == '0':       # for person
                xy = []
                for r in range(1, len(content), poly_point):
                    xy.append([float(content[r]) * img_width, float(content[r+1]) * img_height])
                point.append({
                    "label": label,
                    "points": [x for x in xy],
                    "group_id": 0,
                    "description": "",
                    "shape_type": "polygon",
                    "flags": {}
                })

        with open(image_dir +"/"+ i.split(".")[0]+".png", "rb") as image_file:
            base64format = (base64.b64encode(image_file.read())).decode("utf-8")

        x = {
            "version": "5.2.1",
            "flags": {},
            "shapes": [x for x in point],
            "imagePath": i.split(".")[0] + ".jpg",
            "imageData": base64format,
            "imageHeight": img_height,
            "imageWidth": img_width
        }

        json_object = json.dumps(x)
        # Writing to sample.json
        with open(image_dir +"/"+ i.split(".")[0] + ".json", "w") as outfile:
            outfile.write(json_object)