import cv2
import numpy as np

def detect_skin_tone(image_path):
    image = cv2.imread(image_path)
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    center_region = hsv_image[image.shape[0] // 2 - 50:image.shape[0] // 2 + 50, image.shape[1] // 2 - 50:image.shape[1] // 2 + 50]
    average_color = np.mean(center_region, axis=(0, 1))
    return average_color

if __name__ == "__main__":
    skin_tone = detect_skin_tone('../data/user_images/user_image.jpg')
    print("Detected Skin Tone (HSV):", skin_tone)
