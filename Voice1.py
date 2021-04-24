import speech_recognition as sr
import pyttsx3
import wikipedia
import PIL
import pyaudio
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 130)
def speak(text):
    engine.say(text)
    engine.runAndWait()
def wiki():
    r = sr.Recognizer()
    mic = sr.Microphone()
    engine.say("What do you want to search about?")
    engine.runAndWait()
    print("What do you want to search about?")
    with mic as source:
        audio = r.listen(source)
        MyText = r.recognize_google(audio)
        MyText = MyText.lower()
        print(wikipedia.summary(MyText, sentences=4))
        x = wikipedia.summary(MyText, sentences = 4)
        engine.say(x)
        engine.runAndWait()
    engine.say("Anything else?")
    engine.runAndWait()
    with mic as source:
     audio = r.listen(source)
     MyText = r.recognize_google(audio)
     MyText = MyText.lower()
    if MyText == "no":
        engine.say("okay bye")
        engine.runAndWait()
        exit()
    if MyText == "yes":
        wiki()

def vc():
   language = 'en-us'
   engine.say("let's begin!")
   engine.runAndWait()
   print("Let's begin")
   print("Listening.....")
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

        engine.say(f)
        engine.runAndWait()
        print("Tell me your first number")
        audio1 = r.listen(source)
        a = r.recognize_google(audio1)
        a = int(a)
        print(a)
        engine.say(g)
        engine.runAndWait()
        print("Tell me your second number")
        audio1 = r.listen(source)
        b = r.recognize_google(audio1)
        b = int(b)
        print(b)
        print("Your answer is", a+b)
        c = a+b
        c = "Your answer is " + str(c)
        engine.say(c)
        engine.runAndWait()
    elif MyText == "subtract":

        engine.say(f)
        engine.runAndWait()
        print("Tell me your first number")
        audio1 = r.listen(source)
        a = r.recognize_google(audio1)
        a = int(a)
        print(a)

        engine.say(g)
        engine.runAndWait()
        print("Tell me your second number")
        audio1 = r.listen(source)
        b = r.recognize_google(audio1)
        b = int(b)
        print(b)
        print("Your answer is", a - b)
        c = a - b
        c = "Your answer is " + str(c)
        engine.say(c)
        engine.runAndWait()
    elif MyText == "multiply":

        engine.say(f)
        engine.runAndWait()
        print("Tell me your first number")
        audio1 = r.listen(source)
        a = r.recognize_google(audio1)
        a = int(a)
        print(a)

        engine.say(g)
        engine.runAndWait()
        print("Tell me your second number")
        audio1 = r.listen(source)
        b = r.recognize_google(audio1)
        b = int(b)
        print(b)
        print("Your answer is", a * b)
        c = a * b
        c = "Your answer is " + str(c)
        engine.say(c)
        engine.runAndWait()
    elif MyText == "divide":

        engine.say(f)
        engine.runAndWait()
        print("Tell me your first number")
        audio1 = r.listen(source)
        a = r.recognize_google(audio1)
        a = int(a)
        print(a)
        language = 'en-us'
        engine.say(g)
        engine.runAndWait()
        print("Tell me your second number")
        audio1 = r.listen(source)
        b = r.recognize_google(audio1)
        b = int(b)
        print(b)
        print("Your answer is", a / b)
        c = a / b
        c = "Your answer is " + str(c)
        engine.say(c)
        engine.runAndWait()
    else:
        print("You said", MyText)
language = 'en-us'
print("Hi there!")

engine.say("Hi there!")
engine.runAndWait()
def intro():
 print("What do you want to do?")
 engine.say("What do you want to do?Calculate or wiki?")
 engine.runAndWait()
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
        print("Didn't quiet get you. Try again!")
        engine.say("Didn't quiet get you. Try again!")
        engine.runAndWait()
        intro()
    elif MyText == None:
     print("Didn't quiet get you. Try again!")
     engine.say("Didn't quiet get you. Try again!")
     engine.runAndWait()
     intro()
""" except Exception as e:
      print("Didn't quiet get you. Try again!")
      myobj = gTTS(text="Didn't quiet get you. Try again!", lang=language, slow=False)
      myobj.save("ggg.mp3")
      playsound('ggg.mp3')
      os.remove("ggg.mp3")
intro()"""
intro()
engine.say("Do you want to continue?")
engine.runAndWait()
r = sr.Recognizer()
yo = sr.Microphone()
with yo as source:
    audio =  r.listen(source)
    MyText = r.recognize_google(audio)
    MyText = MyText.lower()
    if MyText == "yes" or MyText == "yeah" or MyText == "yep" or MyText == "haan" or MyText == "haa" or MyText == "bilkul":
        language = 'en-us'
        engine.say("Okay")
        engine.runAndWait()
        vc()
    elif MyText == "no" or "nahi" or "nah" or "wiki":

      engine.say("Do you want to do a quick wiki search?")
      engine.runAndWait()
      audio = r.listen(source)
      MyText = r.recognize_google(audio)
      MyText = MyText.lower()
      if MyText == "yes" or MyText == "yeah" or MyText == "yep" or MyText == "haan" or MyText == "haa" or MyText == "bilkul":
          language = 'en-us'
          engine.say("Okay")
          engine.runAndWait()
          wiki()
      elif MyText == "no" or MyText == "nahi" or MyText == "wiki" or MyText == "nai" or MyText == "nah" or MyText == "na":
          engine.say("Okay bye")
          engine.runAndWait()
      else:
          exit()

    else:
        exit()
