from gtts import gTTS
from playsound import playsound
import os
import speech_recognition as sr
import pyttsx3
import wikipedia
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 130)
def speak(text):
    engine.say(text)
    engine.runAndWait()
    print(text)
def wiki():
    r = sr.Recognizer()
    mic = sr.Microphone()
    myobj = gTTS(text="What do you want to search about?", lang=language, slow=False)
    myobj.save("w.mp3")
    playsound('w.mp3')
    print("What do you want to search about?")
    with mic as source:
        audio = r.listen(source)
        MyText = r.recognize_google(audio)
        MyText = MyText.lower()
        print(wikipedia.summary(MyText, sentences=4))
        x = wikipedia.summary(MyText, sentences = 4)
        myobj = gTTS(text=x, lang=language, slow=False)
        myobj.save("k.mp3")
        playsound('k.mp3')
        os.remove("k.mp3")
    myobj = gTTS(text="anything else?", lang=language, slow=False)
    os.remove('w.mp3')
    myobj.save("w.mp3")
    playsound('w.mp3')
    with mic as source:
     audio = r.listen(source)
     MyText = r.recognize_google(audio)
     MyText = MyText.lower()
    if MyText == "no" or "nahi" or "nai" or "na":
        speak("Okay bye!")
        exit()
    if MyText == "yes" or "haan" or "haa" or "wapis":
        wiki()

def vc():
   speak("Let's begin!")
   r = sr.Recognizer()
   mic = sr.Microphone()
   with mic as source:
    audio =  r.listen(source)
    MyText = r.recognize_google(audio)
    MyText = MyText.lower()
    f = "Tell me your first number"
    g = "Tell me your second number"
    print(MyText)
    if MyText == "add":
        speak(f)
        audio1 = r.listen(source)
        a = r.recognize_google(audio1)
        a = int(a)
        print(a)
        speak(g)
        audio1 = r.listen(source)
        b = r.recognize_google(audio1)
        b = int(b)
        print(b)
        print("Your answer is", a+b)
        c = a+b
        c = "Your answer is " + str(c)
        myobj = gTTS(text=c , lang=language, slow=False)
        myobj.save("h.mp3")
        playsound('h.mp3')
        os.remove('h.mp3')
    elif MyText == "subtract":

        speak(f)
        audio1 = r.listen(source)
        a = r.recognize_google(audio1)
        a = int(a)
        print(a)
        speak(g)
        audio1 = r.listen(source)
        b = r.recognize_google(audio1)
        b = int(b)
        print(b)
        print("Your answer is", a - b)
        c = a - b
        c = "Your answer is " + str(c)
        myobj = gTTS(text=c, lang=language, slow=False)
        myobj.save("h.mp3")
        playsound('h.mp3')
    elif MyText == "multiply":
        speak(f)
        audio1 = r.listen(source)
        a = r.recognize_google(audio1)
        a = int(a)
        print(a)
        speak(g)
        audio1 = r.listen(source)
        b = r.recognize_google(audio1)
        b = int(b)
        print(b)
        print("Your answer is", a * b)
        c = a * b
        c = "Your answer is " + str(c)
        myobj = gTTS(text=c, lang=language, slow=False)
        myobj.save("h.mp3")
        playsound('h.mp3')
    elif MyText == "divide":

        speak(f)
        audio1 = r.listen(source)
        a = r.recognize_google(audio1)
        a = int(a)
        print(a)
        speak(g)
        audio1 = r.listen(source)
        b = r.recognize_google(audio1)
        b = int(b)
        print(b)
        print("Your answer is", a / b)
        c = a / b
        c = "Your answer is " + str(c)
        myobj = gTTS(text=c, lang=language, slow=False)
        myobj.save("h.mp3")
        playsound('h.mp3')
    else:
        print("You said", MyText)
speak("Hi there!")
language = "en-us"
def intro():
 print("What do you want to do?")
 myobj = gTTS(text="What do you want to do?Calculate or wiki?", lang=language, slow=False)
 myobj.save("g.mp3")
 playsound('g.mp3')
 os.remove("g.mp3")
 r = sr.Recognizer()
 mic = sr.Microphone()
 with mic as source:
    ff = r.listen(source)
    MyText = r.recognize_google(ff)
    MyText = MyText.lower()
    print(MyText)
   #try:
    if MyText == "calculate":
      vc()
    elif MyText == "wiki":
        wiki()
    elif MyText == MyText:
        speak("Didn't quiet get you. Try again!")
        intro()
    elif MyText == None:
        speak("Didn't quiet get you. Try again!")
        intro()
""" except Exception as e:
      print("Didn't quiet get you. Try again!")
      myobj = gTTS(text="Didn't quiet get you. Try again!", lang=language, slow=False)
      myobj.save("ggg.mp3")
      playsound('ggg.mp3')
      os.remove("ggg.mp3")
intro()"""
intro()
speak("Do you want to continue?")
r = sr.Recognizer()
yo = sr.Microphone()
with yo as source:
    audio =  r.listen(source)
    MyText = r.recognize_google(audio)
    MyText = MyText.lower()
    if MyText == "yes" or MyText == "yeah" or MyText == "yep" or MyText == "haan" or MyText == "haa" or MyText == "bilkul":
        speak("Okay")
        vc()
    elif MyText == "no" or "nahi" or "nah" or "wiki":
      speak("Do you wanna do a quick wiki search?")
      audio = r.listen(source)
      MyText = r.recognize_google(audio)
      MyText = MyText.lower()
      if MyText == "yes" or MyText == "yeah" or MyText == "yep" or MyText == "haan" or MyText == "haa" or MyText == "bilkul":
          language = 'en-us'
          speak("Okay")
          wiki()
      elif MyText == "no" or MyText == "nahi" or MyText == "wiki" or MyText == "nai" or MyText == "nah" or MyText == "na":
          speak("Okay bye!")
          os.remove("h.mp3")
      else:
          exit()

    else:
        exit()
