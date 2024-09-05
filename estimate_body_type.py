# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 19:34:49 2024

@author: DELL
"""

import cv2

def estimate_body_type(image_path):
    image = cv2.imread(image_path)
    height, width, _ = image.shape
    ratio = height / width
    if ratio > 1.5:
        return "Tall and Slim"
    elif ratio > 1.2:
        return "Average"
    else:
        return "Short and Broad"

if __name__ == "__main__":
    body_type = estimate_body_type('../data/user_images/user_image.jpg')
    print("Estimated Body Type:", body_type)
