# download_yolo.py
import os

# Download YOLO files
os.system("wget -q https://pjreddie.com/media/files/yolov3.weights")
os.system("wget -q https://raw.githubusercontent.com/pjreddie/darknet/master/cfg/yolov3.cfg")
os.system("wget -q https://raw.githubusercontent.com/pjreddie/darknet/master/data/coco.names")
