import speech_recognition as sr
import pyttsx3

# initialise the recognizer
r = sr.Recognizer()

def record_text():
    # loop in case of errors
    while(1):
        try:
            # use the mic as the i/p source
            with sr.Microphone() as source2:
                # prepare recognizer to recieve input
                r.adjust_for_ambient_noise(source2, duration=0.2)
                
                # listen for user i/p
                audio2=r.listen(source2)

                # use google to recognize audio
                MyText=r.recognize_google(audio2)

        except sr.RequestError as e:
            print("could not request result; {0}". format(e))
        
        except sr.UnknownValueError:
            print("Unknown error occured")
    
    return

def output_text():
    # create a file that will have our o/p and in that file append the generated o/p at the end if more o/p is generated
    f=open("output.txt", "a")
    f.write(text)

    # \n as when we say multiple things we will have the thing in new line always
    f.write("\n")
    f.close()
    return

while(1):
    text=record_text()
    output_text(text)
    print("speech converted to text")
