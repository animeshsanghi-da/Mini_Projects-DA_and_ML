"""
Prerequisites:
    1. Install the required library:
        pip install qrcode[pil]
"""
import qrcode

def generate_qr(data, filename="my_qrcode.png"):
    # Configure QR code settings
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save the image
    img.save(filename)
    print(f"QR Code successfully generated and saved as '{filename}'")

if __name__ == "__main__":
    # Example usage
    user_input = input("Enter the text or URL for the QR code: ")
    generate_qr(user_input, "generated_qr.png")

"""
Steps to Test:
1. Run: Execute python qr_generator.py.
2. Input: Enter any text (e.g., your LinkedIn profile URL or a personal message) when prompted.
3. View: Open the directory; you will find a new file named 'generated_qr.png'.
4. Verify: Scan this image using your phone's camera or the scanner script you created previously.
"""