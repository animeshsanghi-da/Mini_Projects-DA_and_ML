# QR Code Generator & Scanner

A collection of Python scripts designed to generate custom QR codes from text/URLs and scan them either in real-time using your computer's webcam or by analyzing an existing image file.

## Prerequisites

To run these scripts, you need to have Python installed on your system. Install the required dependencies using the following command:

``` bash
pip install opencv-python pyzbar qrcode[pil] numpy
```

## How to Use

### 1. Generating a QR Code
Use this script to convert any text or URL into a scannable QR code image.

``` bash
python qr_generator.py
```

- When prompted, enter the text or URL you wish to encode.
- The script will generate a file named `generated_qr.png` in your current directory.

### 2. Scanning a QR Code
Use this script to decode QR codes using your webcam or from a saved image file.

``` bash
python qr_scanner.py
```

Upon running the script, you will be prompted to choose a scanning method:

**Option 1: Use Webcam**
- Ensure your webcam is connected.
- Hold a QR code in front of the camera.
- The script will draw a green border around the detected code and print the decoded information to your terminal.
- Press **'q'** on your keyboard (while focused on the video window) to stop the scanner and close the application.

**Option 2: Upload an Image File**
- Ensure your image containing the QR code is copied or saved into the exact same folder as the script.
- Enter the exact filename (including the extension, e.g., `qrcode.png` or `image.jpg`) when prompted.
- The script will decode the data, highlight the QR code in a popup window, and print the decoded text to your terminal.
- Press **ANY key** on your keyboard (while focused on the image window) to close it.

## Project Structure

- `qr_generator.py`: Handles QR code generation using the `qrcode` library.
- `qr_scanner.py`: Handles webcam access, local image processing, and decoding using `opencv`, `numpy`, and `pyzbar`.
- `README.md`: This documentation file.

## Author
**Animesh Sanghi** | *Google Certified Data Analyst*  
[LinkedIn](https://www.linkedin.com/in/animeshsanghi-da/) | [GitHub](https://github.com/animeshsanghi-da)  
Email: animeshsanghi.da@gmail.com

## License

This project is open-source and free to use.