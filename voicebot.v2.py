import pyttsx3
import random
import datetime
engine=pyttsx3.init()
maxi=int(datetime.datetime.now().hour)
mini=("Jarvis has been started at:")
response={
    "hi":["hello","hola","what's up"],
    "hello":["what's up!","hellooo","hieeee"],
    "good morning":["goodiee morning","morning","mood gorning"]
}
user=input("you: ").lower()
if user in response:
    reply=random.choice(response[user])
else:
    reply=("sorry! i'm not trained to response to that text, try again with different text")
print("bot: ",mini,maxi)
print("bot: ",reply)
engine.say(mini)
engine.say(maxi)
engine.say(reply)
engine.runAndWait()
response1={
    "how was your day":["it was very hectic","it was quite normal","disguisting"],
    "what are you doing":["nothing much","just chilling with friends","just enjoying the view"]
}
engine1=pyttsx3.init()
user1=(input("you: ")).lower()
if user1 in response1:
    reply1=(random.choice(response1[user1]))
else:
    reply1=("sorry! i'm not trained to response to that text, try again with different text")
print("bot: ",reply1)
engine1.say(reply1)
engine1.runAndWait()
