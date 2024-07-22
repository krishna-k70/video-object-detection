# process_video.py
import cv2
import os
from load_yolo_model import detect_objects, classes

# Open video
video_path = list(uploaded.keys())[0]
cap = cv2.VideoCapture(video_path)

# Get video frame rate
fps = cap.get(cv2.CAP_PROP_FPS)
print(f"Frames per second: {fps}")

# Set duration and calculate total frames
duration = 7  # in seconds
total_frames = int(fps * duration)
print(f"Total frames expected for 7 seconds: {total_frames}")

frame_count = 0

while frame_count < total_frames:
    ret, frame = cap.read()
    if not ret:
        break
    
    frame_count += 1
    objects = detect_objects(frame)
    
    for i, (class_id, confidence, box) in enumerate(objects):
        x, y, w, h = box
        # Check if the coordinates are valid
        if x < 0 or y < 0 or x + w > frame.shape[1] or y + h > frame.shape[0]:
            print(f"Invalid coordinates for cropping: x={x}, y={y}, w={w}, h={h}")
            continue
        
        cropped = frame[y:y+h, x:x+w]
        
        if cropped.size == 0:
            print(f"Empty cropped image at frame {frame_count}, object {i}, coordinates: {x}, {y}, {w}, {h}")
            continue
        
        obj_name = classes[class_id]
        save_path = f"{output_dir}/frame_{frame_count}_object_{i}_{obj_name}.jpg"
        cv2.imwrite(save_path, cropped)
        print(f"Saved cropped image to {save_path}")
    
    print(f"Processed frame {frame_count}")

cap.release()
cv2.destroyAllWindows()

# Print total frames processed
print(f"Total frames processed: {frame_count}")
