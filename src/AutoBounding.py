import os
from PIL import Image
import numpy as np
import cv2

def find_object_bounds(image_path):
    # 이미지를 그레이스케일로 로드
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    # 간단한 스레시홀딩으로 객체 검출
    _, thresh = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)
    # 컨투어 찾기
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        # 가장 큰 컨투어를 객체로 간주
        c = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(c)
        return x, y, x + w, y + h
    return 0, 0, image.shape[1], image.shape[0]  # 객체가 없다면 전체 이미지

def normalize_coordinates(img_width, img_height, bbox):
    x_min, y_min, x_max, y_max = bbox
    bb_width = x_max - x_min
    bb_height = y_max - y_min
    bb_center_x = x_min + bb_width / 2
    bb_center_y = y_min + bb_height / 2

    # YOLO 포맷으로 변환
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

# 폴더 경로 지정
folder_path = 'path_to_images'
bounding_boxes = process_images(folder_path)
for file, bbox in bounding_boxes:
    print(f"File: {file}, BBox: {bbox}")
