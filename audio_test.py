from socket import AI_PASSIVE
import speech_recognition as sr

recognizer = sr.Recognizer()
microphone = sr.Microphone()

def listen(recognizer,microphone):
    while True:
        try:
            with microphone as source:
                print("Listening")
                recognizer.adjust_for_ambient_noise(source)
                recognizer.dynamic_energy_threshold = 3000
                audio = recognizer.listen(source, timeout=5.0)
                response = recognizer.recognize_google(audio)
                print(response)
                return(response)
        except sr.WaitTimeoutError:
            pass
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            print("Network error")



while True:
    listen(recognizer, microphone)