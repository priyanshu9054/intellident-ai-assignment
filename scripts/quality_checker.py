import os
import cv2
import numpy as np

# Directory containing processed grayscale images
IMAGE_DIR = "data/processed"

# Thresholds (simple + explainable)
BLUR_THRESHOLD = 100.0        # lower = more blurry
BRIGHTNESS_THRESHOLD = 40.0   # very dark images


def check_image_quality(image_path):
    """
    Checks image quality using:
    1. Variance of Laplacian (blur detection)
    2. Mean pixel intensity (brightness)
    """
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    if image is None:
        return "Unreadable"

    # Blur detection
    blur_score = cv2.Laplacian(image, cv2.CV_64F).var()

    # Brightness check
    brightness = np.mean(image)

    if blur_score < BLUR_THRESHOLD or brightness < BRIGHTNESS_THRESHOLD:
        return "Poor"
    else:
        return "Good"


def main():
    print("Image Quality Report")
    print("-" * 40)

    for file in os.listdir(IMAGE_DIR):
        if file.lower().endswith((".jpg", ".jpeg", ".png")):
            image_path = os.path.join(IMAGE_DIR, file)
            status = check_image_quality(image_path)
            print(f"{file} → {status}")


if __name__ == "__main__":
    main()
