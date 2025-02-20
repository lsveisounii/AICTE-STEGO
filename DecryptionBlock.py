import cv2

def decrypt_image(image_path, password):
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Unable to load image.")
        return
    rows, cols, _ = img.shape
    length_str = ""
    for i in range(8):
        row, col = divmod(i, cols)
        length_str += chr(img[row, col, 0])
    try:
        msg_length = int(length_str)
    except ValueError:
        print("Error: Failed to extract message length.")
        return
    stored_password = ""
    for i in range(8, 16):
        row, col = divmod(i, cols)
        stored_password += chr(img[row, col, 0])

    if stored_password.strip('*') != password:
        print("Authentication failed. Incorrect password.")
        return
    message = ""
    for i in range(16, msg_length + 16): 
        row, col = divmod(i, cols)
        message += chr(img[row, col, 0])  
    print("Decrypted message:", message)
if __name__ == "__main__":
    image_path = "encryptedImage.png"
    password = input("Enter passcode for decryption: ")
    decrypt_image(image_path, password)
