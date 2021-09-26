
import pyttsx3 
# from pyttsx3 import
import speech_recognition as sr
import datetime 
import webbrowser   
import wikipedia
import sys
import os
import phonenumbers
from phonenumbers import geocoder
import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
from opencage.geocoder import OpenCageGeocode




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')


engine.setProperty( 'voice' , voices[1].id)

def speak(audio):
      engine.say(audio)
      engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)  
    if hour>=0 and hour<12:
        speak("Good evening!")

    elif hour>=12 and hour<18:
        speak("Good afternoon!")

    

    else:
        speak("Good moring!")  
    
    speak("I am SIRI your new vurtual friend, Tell me how can I help you")   





def takecammand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("...lisening...") 
        r.pause_threshold = 1.5
        audio = r.listen(source)

    try:
        print("recognizing...")
        text = r.recognize_google( audio , language ='en-in')
        print(f"you said : {text}\n")
        
    
    except Exception as e:
        speak("say that again please....")
        return "none"
    return text

    

 

if __name__ == "__main__":
    # wishme()
    _l_ = input("please enter the name of the birthday boy or girl")
    a_d_f = "nikky"
    b_song = "happy     birthday      " + a_d_f + "may    god     bless    to   dear"

    speak (b_song)

    

    # print('''you can ask me these commands: "what's the Time, open my portal, open Gmail, open Amazon, open Google, open Web  store, open Youtube, open maps, open Google Duo, open zoom, open chrome, open VS code And tell 'quit' to turn off " ''')
    # speak('''you can ask me these commands: "what's the Time, open my portal, open Gmail, open Amazon, open Google, open Web  store, open Youtube, open maps, open Google Duo, open zoom, open chrome, open VS code And tell 'quit' to turn off " ''')
    print("created by Yadavelly Gunashekar reddy")
    user_who = input("please enter your name")
    speak("please enter your name")
    print("please enter your name")
    dob = input("please enter your date of birth")
    speak("please enter your date of birth")
    print("please enter your date of birth")
    while True:
        text =takecammand().lower()
        if 'wikipedia' in text:
            speak("searching in wikipedia")
            text = text.replace("wikipedia", "")
            results = wikipedia.summary(text, sentences=3)
            speak("according to wikipedia")
            print(results)
            speak(results)

        
        number = "+918309735275"


    
        if 'hi' in text:
                speak("HI!")

        if 'sara hi' in text:
                    speak("HI!")

        if 'hi sara' in text:
                    speak("HI!")

        if 'hello' in text:
                    speak("Hello!")

        if 'hello' in text:
                    speak("Hello!")

        if ' hello' in text:
                    speak("Hello!")

        if 'your birthday' in text:
            speak("my birthday is on 27 of January 2021")

        if 'you born' in text:
            speak("my birthday is on 27 of January 2021")

        if 'who user' in text:
            speak(user_who)

        if 'my birthday' in text:
            speak(dob)

 
      

                
                

        if 'how are you' in text:
                    speak("I am Good, How Are You My Dear Friend")


        if 'how are you sara' in text:
                    speak("I am Good, How Are You My Dear Friend")

        if 'sara how are you' in text:
                    speak("I am Good, How Are You My Dear Friend")

        if 'how are you my friend' in text:
                    speak("I am Good, How Are You My Dear Friend")







        if 'time' in text:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    print(strTime)
                    speak(f"the time is {strTime} ")

        if ' your name is nice' in text:
                    speak("oH! is it, thank you so much")


        if 'can you hear me' in text:
                    speak("yes, I can hear you")
                

        if 'open youtube' in text:
                    speak("please wait...")
                    print("please wait...")
                    webbrowser.open('youtube.com')

        if 'vs code' in text:
                    speak("please wait...")
                    print("please wait...")
                    codepath = "C:\\Users\\LUKY SHARATH\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                    os.startfile(codepath)
                
        if 'zoom' in text:
                    speak("please wait...") 
                    print("please wait...")
                    zoompath = "C:\\Users\\\LUKY SHARATH\\AppData\Roaming\\Zoom\\bin\\Zoom.exe"
                    os.startfile(zoompath)

        if 'chrome' in text:
                    speak("please wait...")
                    print("please wait...")
                    p = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                    os.startfile(p)


        if 'open google duo' in text:
                    speak("please wait...")
                    print("please wait...")
                    webbrowser.open('google duo.com')

                
        if 'open maps' in text:
                    speak("please wait...")
                    print("please wait...")
                    webbrowser.open('maps.com')

        if  'open web store' in text:
                    speak("please wait...")
                    print("please wait...")
                    webbrowser.open('Webstore.com')

        if 'open amazon' in text:
                    speak("please wait...")
                    print("please wait...")
                    webbrowser.open('Amazon.com')   
                                
        if 'open google' in text:
                    speak("please wait...")
                    print("please wait...")
                    webbrowser.open('google.com')

        if 'open gmail' in text:
                    speak("please wait...")
                    print("please wait...")
                    webbrowser.open('gmail.com')

        if 'open my portal' in text:
                    speak("please wait...")
                    print("please wait...")
                    webbrowser.open('www.reqelfordinternationalschool.com')

        if 'open school' in text:
                    speak("please wait...")
                    print("please wait...")
                    webbrowser.open('www.reqelfordinternationalschool.com')

        if 'quit' in text:
                    speak('Bye bye!')
                    sys.exit(0)

        

        if 'calculation' in text:
            speak("select any arithmetic operation, by saying it's name")
        
        if 'calulate' in text:
            speak("select any arithmetic operation, by saying it's name")
        
        if 'calculator' in text:
            speak("select any arithmetic operation, by saying it's name")


        if "addition" in text:
            speak("Enter the first number")
            n1 = input("Enter the first number")
            speak("Enter the second number")
            n2 = input("Enter the second number")
            Ret = "The sum is " + str(int(n1) + int(n2))
            speak(Ret)
            print(Ret)

        if "subtraction" in text:
            speak("Enter the second number")
            n1 = input("Enter the first number")
            speak("Enter the second number")
            n2 = input("Enter the second number")
            Ret = "The difference is " + str(int(n1) - int(n2))
            speak(Ret)
            print(Ret)

        if "subtract" in text:
            speak("Enter the first number")            
            n1 = input("Enter the first number")
            speak("Enter the second number")
            n2 = input("Enter the second number")
            Ret = "The difference is " + str(int(n1) - int(n2))
            speak(Ret)
            print(Ret)

        if "multiply" in text:
            speak("Enter the first number")
            n1 = input("Enter the first number")
            speak("Enter the second number")
            n2 = input("Enter the second number")
            Ret = "The product is " + str(int(n1) * int(n2))
            speak(Ret)
            print(Ret)

        if "multiplication" in text:
            speak("Enter the first number")
            n1 = input("Enter the first number")
            speak("Enter the second number")
            n2 = input("Enter the second number")
            Ret = "The product is " + str(int(n1) * int(n2))
            speak(Ret)
            print(Ret)

        if "division" in text:
            speak("Enter the first number")
            n1 = input("Enter the first number")
            speak("Enter the second number")
            n2 = input("Enter the second number")
            Ret = "The quotient is " + str(int(n1) / int(n2))
            speak(Ret)
            print(Ret)

        if "divide" in text:
            speak("Enter the first number")
            n1 = input("Enter the first number")
            speak("Enter the second number")    
            n2 = input("Enter the second number")
            Ret = "The quotient is " + str(int(n1) / int(n2))
            speak(Ret)
            print(Ret)
            
                       

           


        key = '72bcadabcfaf499295ba87bc134074cd'
            
            
            
            
        sannumber = phonenumbers.parse(number)
        if 'trace' in text:
                test  = input("Pls enter the phonenumber along with contry code")
                number=test 
   
                yourlocation = geocoder.description_for_number(sannumber, "en")
                print(yourlocation)
                speak(yourlocation)
                
                
                
                
                service_provider = phonenumbers.parse(number)
                speak(carrier.name_for_number(service_provider,"en"))
    
                print(carrier.name_for_number(service_provider,"en"))
                geocoder = OpenCageGeocode(key)
                        
