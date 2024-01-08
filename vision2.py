import cv2
import keyboard
from PIL import Image
import Listen
import gemini



def analyze_image(image, query):
    description = gemini.anaylyze(image, query)
    return description


import speechV2


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
    ret, frame = cap.read()
    output_path = 'image.jpg'
    if keyboard.is_pressed('esc'):
       
        data=Listen.recognize_speech()

        cv2.imwrite(output_path, frame)
        text = analyze_image('image.jpg',data)
        print(text)
        speechV2.speak(text)

    cv2.putText(frame, text, position, font, font_size, font_color, font_thickness)
    cv2.imshow('Video Feed', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()


