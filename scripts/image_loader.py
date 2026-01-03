import os
import cv2
import numpy as np

# Paths
IMAGE_DIR = "data/images"
OUTPUT_DIR = "data/processed"

# Target size for all images
TARGET_SIZE = (256, 256)

# Create output directory if not exists
os.makedirs(OUTPUT_DIR, exist_ok=True)


def process_image(image_path):
    """
    Load image, convert to grayscale, resize,
    and compute basic statistics.
    """
    image = cv2.imread(image_path)

    if image is None:
        print(f"Could not read image: {image_path}")
        return

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Resize image
    resized = cv2.resize(gray, TARGET_SIZE)

    # Statistics
    height, width = resized.shape
    mean_intensity = np.mean(resized)

    # Save processed image
    filename = os.path.basename(image_path)
    output_path = os.path.join(OUTPUT_DIR, filename)
    cv2.imwrite(output_path, resized)

    # Print results
    print(f"Image: {filename}")
    print(f"Resolution: {width} x {height}")
    print(f"Mean Pixel Intensity: {mean_intensity:.2f}")
    print("-" * 40)


def main():
    for file in os.listdir(IMAGE_DIR):
        if file.lower().endswith((".jpg", ".jpeg", ".png")):
            image_path = os.path.join(IMAGE_DIR, file)
            process_image(image_path)


if __name__ == "__main__":
    main()
