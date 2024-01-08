import cv2
import keyboard
from PIL import Image
import Listen
import gemini


# Function to analyze image using your AI model
def analyze_image(image, query):
    # Your code to process the image and get a description
    # Replace this with your actual AI model integration
    description = gemini.anaylyze(image, query)
    return description


import speechV2

# Open the camera
cap = cv2.VideoCapture(1)  #
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 960)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 536)
i = 0
font = cv2.FONT_HERSHEY_SIMPLEX
position = (5, 50)
font_size = 0.7
font_color = (0, 0, 255)
font_thickness = 2
text = "data"
while True:
    # Capture frame-by-frame

    ret, frame = cap.read()

    # Save the frame to the specified path
    output_path = 'image.jpg'

    if keyboard.is_pressed('esc'):
        # Put text on the frame
        data=Listen.recognize_speech()

        cv2.imwrite(output_path, frame)
        text = analyze_image('image.jpg',data)
        print(text)
        speechV2.speak(text)

    # break


    # Process the frame using your AI model

    # Display the frame and description
    cv2.putText(frame, text, position, font, font_size, font_color, font_thickness)
    cv2.imshow('Video Feed', frame)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()


