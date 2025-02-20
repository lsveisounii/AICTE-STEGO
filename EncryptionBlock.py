import cv2
import os

def encrypt_image(image_path, message, password, output_path="encryptedImage.png"):
    img = cv2.imread(image_path)

    if img is None:
        print("Error: Unable to load image.")
        return

    rows, cols, _ = img.shape
    msg_len = len(message)

    if msg_len + 16 > rows * cols:
        print("Error: Message is too large to fit in the image.")
        return

   
    length_str = f"{msg_len:08d}"  
    password = password.ljust(8, '*')[:8]  

    message = length_str + password + message  

    index = 0
    for i in range(rows):
        for j in range(cols):
            if index < len(message):
                img[i, j, 0] = ord(message[index])  
                index += 1

    cv2.imwrite(output_path, img)
    print(f"Message encrypted and saved as {output_path}")
    os.system(f"start {output_path}")  

if __name__ == "__main__":
    image_path = "CS.jpeg" 
    message = input("Enter secret message: ")
    password = input("Enter a passcode : ")
    encrypt_image(image_path, message, password)
