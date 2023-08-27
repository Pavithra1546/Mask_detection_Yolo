# Mask_detection_Yolo
#create virtual environment
conda create -n images pip python=3.8
#activate virtual environment
activate images
#requirements
pip install ultralytics
pip install opencv-python
#To run code after model downloads
yolo predict model=model_filename source="image_filename"(for image)
yolo predict model=model_filename source="video_filename"(for video)
