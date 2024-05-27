import os
from PIL import Image
import numpy as np
import cv2

def find_object_bounds(image_path):
    # load as greyscale
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    _, thresh = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)
  
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        # biggest contour as obeject
        c = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(c)
        return x, y, x + w, y + h
    return 0, 0, image.shape[1], image.shape[0]  

def normalize_coordinates(img_width, img_height, bbox):
    x_min, y_min, x_max, y_max = bbox
    bb_width = x_max - x_min
    bb_height = y_max - y_min
    bb_center_x = x_min + bb_width / 2
    bb_center_y = y_min + bb_height / 2

    # YOLO Formation
    norm_center_x = bb_center_x / img_width
    norm_center_y = bb_center_y / img_height
    norm_width = bb_width / img_width
    norm_height = bb_height / img_height
    
    return norm_center_x, norm_center_y, norm_width, norm_height

def process_images(folder_path):
    results = []
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(folder_path, filename)
            bbox = find_object_bounds(image_path)
            image = Image.open(image_path)
            norm_coords = normalize_coordinates(image.width, image.height, bbox)
            results.append((filename, norm_coords))
    return results


folder_path = 'path_to_images'
bounding_boxes = process_images(folder_path)
for file, bbox in bounding_boxes:
    print(f"File: {file}, BBox: {bbox}")
