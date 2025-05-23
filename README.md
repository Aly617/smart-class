# Voice Controlled Smart Class - Website and QR Code

This repository contains the website and QR code generator for the Voice Controlled Smart Class project.

## Website

The website is a simple, responsive HTML/CSS site that showcases your Smart Class project. It includes:
- Project overview
- Key features
- Technology stack
- Modern, responsive design

To view the website locally:
1. Simply open the `index.html` file in a web browser
2. The website is responsive and will work on all device sizes

## QR Code Generator

The QR code generator is a Python script that creates a QR code linking to your website.

### Prerequisites
- Python 3.x
- Required packages (install using pip):
  ```
  pip install -r requirements.txt
  ```

### Generating the QR Code
1. Edit the `generate_qr.py` file to update the `website_url` variable with your actual hosted website URL
2. Run the script:
   ```
   python generate_qr.py
   ```
3. The QR code will be generated as `smart_class_qr.png`

## Hosting the Website

To make the QR code functional, you'll need to:
1. Host the website on a web hosting service
2. Update the URL in the QR code generator script
3. Generate a new QR code with the actual URL

## Files Included
- `index.html` - The main website file
- `styles.css` - Website styling
- `generate_qr.py` - QR code generator script
- `requirements.txt` - Python dependencies
- `README.md` - This documentation file 