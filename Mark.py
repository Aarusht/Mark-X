import pyttsx3 #importing pyttsx3, a module by microsoft 
#which alows us to take out voice out of your speakers
import speech_recognition as sr#importing speech_recognition, a module in python 
#which alows us to acces microphone and use speech to text

engine = pyttsx3.init('sapi5') #Setting engine
voices = engine.getProperty('voices') #getting the voices
engine.setProperty('voices',voices[0].id)#setting voice gender (0)male (1)female
engine.setProperty('rate',170)#How fast to speak
def Say(Text):
    print("     ")
    print(f'Mark X: {Text}')
    engine.say(text=Text)#Says the text
    engine.runAndWait()#Waits for code to end
    print("     ")

def Listen():

    r= sr.Recognizer()
    with sr.Microphone(0) as source: # Microphone(0) means the deafault mic
        r.pause_threshold = 1
        audio = r.listen(source,0 ,2) # Giving mic as source , then 
        #Timeout as 0 , and time limit as 2 
        #(so that mark dosent stop listening as soon as he starts to listen....)

    try:
        query = r.recognize_google(audio,language='en-in')
        print(f'you: {query}')
    except Exception as Error:
        return ''
    query = str(query)
    return query.lower()
def MainTasks():
    Say('Mark X , at your assistance')
    while True:
        word = Listen()
        if("sleep" in word):
            Say("Okay sir....")
            Say('Just say Wake up to wake me up')
            break

        if("hello" in word):
            Say("Hello sir!")

MainTasks()
