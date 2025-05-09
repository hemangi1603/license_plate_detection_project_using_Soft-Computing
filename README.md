🔍 License Plate Detection using Soft Computing

This project aims to detect and recognize license plates from vehicles (cars, bikes, and auto-rickshaws) in a video using a combination of deep learning and image processing techniques. It was developed as part of my Soft Computing subject.

A Convolutional Neural Network (CNN) is used for detecting vehicles and license plates, while Optical Character Recognition (OCR) is applied to extract the alphanumeric text from the plates. The system is capable of processing real-time video input and saving both the cropped plate images and their recognized text.

The motivation behind this project is the growing demand for automated vehicle monitoring systems used in traffic management, toll booths, smart parking, and surveillance. Through this work, I have implemented a simplified version of such intelligent systems using neural networks and soft computing principles.

📁 Features

Detects license plates from cars, bikes, autos using Haar Cascades.
Extracts and reads plate numbers using Tesseract OCR.
Saves cropped plate images and their text.
Sharpens plate images for better accuracy.

🛠️ Tech Stack & Libraries

  Python
  
  OpenCV
  
  Tesseract OCR
  
  Haar Cascade Classifier
  
  pytesseract
  
  Custom utility functions (for saving images and text)


▶️ How to Run

  1. Install dependencies:
    pip install opencv-python pytesseract
  2. Set Tesseract path (in detect.py):
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
  3. Run the detection:
     
    python detect.py
    Press q to quit the video

       OR

    python gui.py

📌 Output

  Detected plate images saved in output/plates/
  
  Extracted plate numbers saved as .txt files

🧠 Why Soft Computing?

  Soft Computing allows handling of uncertainty in image data.
  OCR uses fuzzy logic-like decision-making.
  Image processing is enhanced using neural network techniques.

📌 Example Output

  Detected Plate Text: GJ01AB1234
  
  Saved: plate_15_0.png
  
  Saved Text: plate_text_15_0.txt

🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first.

📧 Contact

Hemangi Solanki
📍 Gujarat, India
📧 hemangi.solanki2003@gmail.com
