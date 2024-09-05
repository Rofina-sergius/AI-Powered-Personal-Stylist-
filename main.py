# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 19:36:33 2024

@author: DELL
"""
import cv2
from capture_image import capture_image
from detect_skin_tone import detect_skin_tone
from estimate_body_type import estimate_body_type
from recommend import recommend

def main():
    user_image = capture_image()
    image_path = '../data/user_images/user_image.jpg'
    cv2.imwrite(image_path, user_image)
    
    skin_tone = detect_skin_tone(image_path)
    body_type = estimate_body_type(image_path)
    
    clothing, accessories = recommend(skin_tone, body_type)
    print("Detected Skin Tone (HSV):", skin_tone)
    print("Estimated Body Type:", body_type)
    print("Recommended Clothing:", clothing)
    print("Recommended Accessories:", accessories)

if __name__ == "__main__":
    main()
