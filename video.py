from ultralytics import YOLO
import time
import cv2
import os

source = ""         #Define video source path
model = YOLO("")    #Define YOLOv8 model path

start_time = time.time()
videosource = "E:/odisGPU/dataset/videos/1080p_Strawberry_60fps - Trim.mp4"
vidresults = model(videosource, save=True, device=0, show_labels=True, show_conf=False, boxes=True, conf=0.6)
end_time = time.time()
processing_time = end_time - start_time
print(f"Processing time for video: {processing_time} seconds")


cap = cv2.VideoCapture(videosource)
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*'XVID')  
out = cv2.VideoWriter('output_half_speed.avi', fourcc, fps / 2, (width, height))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    out.write(frame)

cap.release()
out.release()
cv2.destroyAllWindows()
