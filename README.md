# AICTE-STEGO
Priject Title: Secure data hiding in image using steganography
This project is carried for partial fulfillment of AICTE-IBM-Edunet 6 week online intership.
# Secure Data Hiding in Image Using Steganography

## Overview
Steganography is the practice of concealing secret information within an image file in such a way that it is not noticeable to an observer. This project demonstrates a method for securely hiding data within an image using steganographic techniques.

## Features
- Hide secret text messages within an image
- Extract hidden messages from a stego-image
- Encryption support for added security
- Supports common image formats (PNG, JPEG, BMP)
- User-friendly interface for encoding and decoding

## Requirements
- Python 3.x
- Required libraries:
  - OpenCV (`cv2`)
  - NumPy
  - PIL (Pillow)
  - Cryptography (for encryption support, optional)

## Usage
### Hiding a Message
Run the script to encode a message into an image:
```bash
python encode.py --image input.png --message "Secret Message" --output stego_image.png
```
Options:
- `--image` : Input image file
- `--message` : Secret message to hide
- `--output` : Output stego-image file

### Extracting a Message
Run the script to extract a hidden message from an image:
```bash
python decode.py --image stego_image.png
```
Options:
- `--image` : Stego-image file containing the hidden message

## Example
1. Hide a message:
   ```bash
   python encryptblock.py --image cover.png --message "Hello, World!" --output CS.jpeg
   ```
2. Extract the hidden message:
   ```bash
   python decryptblock.py --image encryptedImage.png
   ```

## Author
L S Veisounii | lsveisouniishomai@gmail.com

## Acknowledgments
- Open-source libraries used: OpenCV, NumPy, Pillow, Cryptography
- Inspired by various steganography techniques and cryptographic principles


To read my message please enter password to decrypt it.
Password:1234
