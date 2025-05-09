import cv2
import os

def save_plate(plate_img, filename):
    output_path = os.path.join("../output/plates", filename)
    cv2.imwrite(output_path, plate_img)

def save_plate_text(plate_text, filename):
    output_path = os.path.join("../output/plates", filename)
    with open(output_path, 'w') as f:
        f.write(plate_text)
