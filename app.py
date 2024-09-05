from flask import Flask, request, jsonify, send_from_directory
import cv2
import os
from capture_image import capture_image
from detect_skin_tone import detect_skin_tone
from estimate_body_type import estimate_body_type
from recommend import recommend

app = Flask(__name__)

# Directory to store user images and recommendations
USER_IMAGES_DIR = 'data/user_images'
RECOMMENDATIONS_DIR = 'data/recommendations'

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    image_path = os.path.join(USER_IMAGES_DIR, 'captured_image.jpg')
    file.save(image_path)

    # Process the image
    user_image = cv2.imread(image_path)
    skin_tone = detect_skin_tone(user_image)
    body_type = estimate_body_type()
    recommendations = recommend(skin_tone, body_type)

    # Save recommendations as images (dummy implementation)
    recommendation_images = []
    for i, item in enumerate(recommendations):
        recommendation_image_path = os.path.join(RECOMMENDATIONS_DIR, f'{i}.jpg')
        cv2.imwrite(recommendation_image_path, user_image)  # Replace with actual image for recommendations
        recommendation_images.append(f'/recommendations/{i}.jpg')

    return jsonify({'recommendations': recommendation_images})

@app.route('/recommendations/<filename>')
def get_recommendation(filename):
    return send_from_directory(RECOMMENDATIONS_DIR, filename)

if __name__ == '__main__':
    if not os.path.exists(USER_IMAGES_DIR):
        os.makedirs(USER_IMAGES_DIR)
    if not os.path.exists(RECOMMENDATIONS_DIR):
        os.makedirs(RECOMMENDATIONS_DIR)
    app.run(debug=True)

