import speech_recognition as sr

def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something:")
  
        sr.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language='en-in')
        return (text)
    except sr.UnknownValueError:
        return ("skipped")
    except sr.RequestError as e:
        return (f"Error with the speech recognition service: {e}")

