import cv2

def capture_image():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        cv2.imshow('Press Space to Capture', frame)
        if cv2.waitKey(1) & 0xFF == ord(' '):
            break
    cap.release()
    cv2.destroyAllWindows()
    return frame

if __name__ == "__main__":
    user_image = capture_image()
    cv2.imwrite('../data/user_images/user_image.jpg', user_image)

