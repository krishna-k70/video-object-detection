# upload_video.py
import os
from google.colab import files

# Create output directory if not exists
output_dir = "cropped_objects"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Upload video
uploaded = files.upload()
