import cv2
import os
import pytesseract
from utils import save_plate, save_plate_text

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

plate_cascade = cv2.CascadeClassifier("../model/haarcascade_russian_plate_number.xml")

if not os.path.exists("../output/plates"):
    os.makedirs("../output/plates")

def sharpen_image(image):
    """Apply sharpening to the image using a Laplacian filter."""
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    laplacian = cv2.Laplacian(gray, cv2.CV_64F)
    sharp = cv2.convertScaleAbs(laplacian)

    sharpened = cv2.addWeighted(gray, 1.5, sharp, -0.5, 0)
    
    return sharpened

def main():
    cap = cv2.VideoCapture("../input/cars.mp4")

    if not cap.isOpened():
        print("Error opening video file")
        return

    frame_count = 0
    saved_count = 0

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        frame_count += 1
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        plates = plate_cascade.detectMultiScale(gray, 1.1, 10)

        for (x, y, w, h) in plates:
            plate_img = frame[y:y+h, x:x+w]
            plate_img = cv2.resize(plate_img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
            plate_img = sharpen_image(plate_img)
            plate_filename = f"plate_{frame_count}_{saved_count}.png"
            save_plate(plate_img, plate_filename)

            plate_text = pytesseract.image_to_string(plate_img, config='--psm 8').strip()
            print(f"Detected Plate Text: {plate_text}")

            text_filename = f"plate_text_{frame_count}_{saved_count}.txt"
            save_plate_text(plate_text, text_filename)

            saved_count += 1

        resized_frame = cv2.resize(frame, (800, 600))
        cv2.imshow('License Plate Detection', resized_frame)
       

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
