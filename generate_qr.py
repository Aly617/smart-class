import segno

def generate_qr_code(url, filename):
    # Create QR code
    qr = segno.make(url, error='h')
    
    # Save it with some styling
    qr.save(
        filename,
        scale=10,
        border=4,
        dark="black",
        light="white"
    )

if __name__ == "__main__":
    # Using a temporary URL - update this when you host the website
    website_url = "https://smart-class-project-2025.netlify.app"  # Example URL
    output_filename = "smart_class_qr.png"
    
    generate_qr_code(website_url, output_filename)
    print(f"QR Code has been generated and saved as {output_filename}") 