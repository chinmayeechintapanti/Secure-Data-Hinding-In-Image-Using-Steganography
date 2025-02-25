import cv2

def encrypt_image(image_path, secret_message, passcode):
    img = cv2.imread(image_path)

    if img is None:
        print("Error: Image not found!")
        return

    secret_message += "EOF"  # Append end-of-message marker
    n, m = 0, 0  # Start from pixel (0,0)

    for char in secret_message:
        img[n, m, 0] = ord(char)  # Store ASCII value in the Red channel
        m += 1
        if m >= img.shape[1]:  # Move to next row if end of column
            m = 0
            n += 1
        if n >= img.shape[0]:  # If message is too long for image, stop
            print("Error: Message too long for this image.")
            return

    cv2.imwrite("encryptedImage.png", img)  # Save in PNG format to prevent corruption
    print("Encryption complete! Encrypted image saved as 'encryptedImage.png'.")

if __name__ == "__main__":
    img_path = "stego.jpg"  # Ensure this file exists
    secret_msg = input("Enter secret message: ")
    passcode = input("Set a passcode: ")
    encrypt_image(img_path, secret_msg, passcode)
