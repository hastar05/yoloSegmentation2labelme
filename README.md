# yoloSegmentation2labelme
Converts output of YOLO segmentation detection txt files to Labelme format JSON files.

Note - use `save_txt=True` when detecting using YOLO model to save the detection or segmentation outputs in txt files.

Change `path` and `image_dir` in the code to your path for txt files and images.

Run `python3 yoloSeg2labelme.py` to save the JSON files in the same directory as the images.
