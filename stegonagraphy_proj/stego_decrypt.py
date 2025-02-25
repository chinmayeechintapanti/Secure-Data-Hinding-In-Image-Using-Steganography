import cv2

def decrypt_image(image_path, correct_passcode):
    img = cv2.imread(image_path)

    if img is None:
        print("Error: Encrypted image not found!")
        return

    passcode_attempt = input("Enter passcode for decryption: ")
    if passcode_attempt != correct_passcode:
        print("YOU ARE NOT AUTHORIZED")
        return

    n, m = 0, 0
    decrypted_message = ""

    while True:
        char = chr(img[n, m, 0])  # Read from Red channel
        if decrypted_message.endswith("EOF"):  # Stop at EOF marker
            decrypted_message = decrypted_message[:-3]  # Remove EOF
            break
        decrypted_message += char
        m += 1
        if m >= img.shape[1]:  # Move to next row if end of column
            m = 0
            n += 1
        if n >= img.shape[0]:  # Stop if reached end of image
            break

    print("Decrypted message:", decrypted_message)

if __name__ == "__main__":
    img_path = "encryptedImage.png"  # Must match saved encrypted image
    correct_pass = input("Enter the original passcode: ")
    decrypt_image(img_path, correct_pass)
