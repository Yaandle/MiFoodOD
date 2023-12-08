from ultralytics import YOLO
import time
import os

source = ""             #Define the path to the folder of images.
model = YOLO("")        #Define the path to the YOLOv8 model.

start_time = time.time()
results = model(source, save=True, save_txt=True, conf=0.75, device=0)
end_time = time.time()
processing_time = end_time - start_time
print(f"Processing time for images: {processing_time} seconds")
time.sleep(0.2)

start_time = time.time()
videosource = ""                       #Define path to video source.
vidresults = model(videosource, save=True, device=0)
end_time = time.time()
processing_time = end_time - start_time
print(f"Processing time for video: {processing_time} seconds")
