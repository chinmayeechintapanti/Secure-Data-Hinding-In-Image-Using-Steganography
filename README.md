# Secure-Data-Hinding-In-Image-Using-Steganography

Problem Statement:
In the modern digital world, where cyber threats are increasing, ensuring the secure transmission of sensitive information is crucial. Traditional communication channels are vulnerable to interception, making it difficult to send confidential messages securely. This project addresses this issue by implementing image-based steganography, where secret messages are embedded into an image and later retrieved only by authorized users.

Technology Used:
Operating System: Windows 11
Programming Language: Python 3.12.8
Python Libraries: OpenCV (cv2), NumPy (numpy)
IDE: Visual Studio Code
Version Control: Git/GitHub

Project Overview:
This project consists of two Python scripts:

encrypt.py – Encrypts (hides) a secret message inside an image.
decrypt.py – Decrypts (retrieves) the hidden message from the image.
The sender encrypts a message inside an image and shares the encrypted image with the receiver. The passcode is communicated offline between the sender and receiver to ensure security.

Passcode: 1234 (shared offline)
Message Length: Dynamically determined

encrypt.py (Encryption Script)

Description:
The encrypt.py script embeds a secret message into an image using steganography by modifying the Red color channel of the image’s pixels.

Imports:
cv2 – Used for image processing.
os – Used to interact with the operating system.
Workflow:
1. Reading the Image:

The script loads an image (mypic.jpg) using OpenCV (cv2.imread).
Ensure the correct image path is provided.

2. User Inputs:

The user enters a secret message to be hidden.
The user sets a passcode for authentication during decryption.

3. Message Encoding:

The secret message is appended with "EOF" as an end-of-message marker to signal where extraction should stop.
Each character of the message is converted into its ASCII value and embedded into the Red color channel of the image.

4. Modifying Pixel Values:

The script iterates over the pixels of the image and modifies the Red channel (R) to store the ASCII values of the message characters.
If the message is too long for the image, an error message is displayed.

5. Saving the Encrypted Image:

The modified image is saved as encryptedImage.png in lossless PNG format to prevent data corruption.
A confirmation message is displayed to indicate successful encryption.

6. Run the script:
python encrypt.py

Enter the secret message and passcode when prompted.
The encrypted image is saved as encryptedImage.png.

decrypt.py (Decryption Script)

Description:
The decrypt.py script extracts the hidden message from the encrypted image by reading the modified Red color channel of the image pixels.

Imports:
cv2 – Used for image processing.
Workflow:

1. Reading the Encrypted Image:

The script loads the encrypted image (encryptedImage.png) using OpenCV (cv2.imread).
If the image file is not found, an error message is displayed.

2. User Authentication:

The user is prompted to enter a passcode.
If the passcode is incorrect, access is denied, and the script terminates.

3. Extracting the Hidden Message:

The script reads the Red channel values of the pixels, converting them back to characters using ASCII decoding.
The process stops when the "EOF" marker is detected, ensuring no extra or corrupted data is retrieved.

4. Displaying the Message:

The decrypted message (without "EOF") is displayed on the screen.

5. Run the script:
   
python decrypt.py
Enter the correct passcode when prompted.
If the passcode is correct, the hidden message is displayed.

Conclusion:

This project successfully demonstrates a secure and efficient method for hiding secret messages inside images using steganography. By leveraging image processing techniques, it provides a covert way to transmit sensitive data, ensuring that only the intended recipient with the correct passcode can retrieve the message.

This method can be further enhanced with encryption algorithms for added security, making it an effective solution for secure communication in cybersecurity, defense, and confidential communication systems.
