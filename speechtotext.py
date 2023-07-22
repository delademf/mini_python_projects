import speech_recognition as sr
recording = sr.Recognizer()

with sr.Microphone() as source:
    print("Say Something: ")
    audio = recording.listen(source)
    try:
        text = recording.recognize_google(audio)
        print("You said: \n" + str(text))
    except:
        print("I didn't get you on that one...")