import speech_recognition as sr

# function for audio recording and speech generation
def record_text():
    
   # creating an instance
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Adjusting for ambient noise, please wait...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Please speak now...")

       #collecting audio data
        audio_data = recognizer.listen(source)

        try:
            print("Recognizing...")
            text = recognizer.recognize_google(audio_data)
            print(f"You said: {text}")
            return text
            
        except sr.RequestError:
            print("Error: Could not request results from the speech recognition service.")

        except sr.UnknownValueError:
            print("Error: Could not understand the audio.")

    return None

# function for writing text in output file 
def output_text(text):
    if text:
        with open("output.txt", "a") as f:
            f.write(text + "\n")
        print("Text written to file.")
    else:
        print("No text to write")


while True:
    text = record_text()
    if text:  
        output_text(text)
        print("Speech converted to text and written to file")
