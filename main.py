import os
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

r = sr.Recognizer()
SECRET_KEY = "secret_Kq3dHOm0c7hq0E6SXWESdpnRFE6FHzFBaJVMbzcPYLL"
NOTE_COMMAND = "take some note"
CLOSE_COMMNAND = "close"
def get_audio():
    with sr.Microphone() as source:
        audio = r.listen(source)
    return audio

def audio_to_text(audio):
    text = ""
    # recognize speech using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        text = r.recognize_google(audio)
        print("Google Speech Recognition thinks you said: " + r.recognize_google(audio))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    return text

def text_to_audio(text):
    try:
        audio = gTTS(text)
        filename = "output.mp3"
        audio.save(filename)
        playsound(filename)
        os.remove(filename)
    except:
        print("Could not convert text to audio.")

def save_notion():
    pass

if __name__ == "__main__":

    while True:
        print("What can I do for you?")
        audio = get_audio()
        text = audio_to_text(audio)

        if CLOSE_COMMNAND in text:
            # play sound
            text_to_audio("See you later")
            break
        if NOTE_COMMAND in text:
            text_to_audio("What do you want to note?")
            audio = get_audio()
            text = audio_to_text(audio)
            text_to_audio("Your note is " + text)
            # save note on notion 
            save_notion()
            text_to_audio("Succefully note.")

    