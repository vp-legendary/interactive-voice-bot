import pyttsx3
import random
engine=pyttsx3.init()
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
print("bot: ",reply)
engine.say(reply)
engine.runAndWait()
response1={
    "how was your day":["it was very hectic","it was quite normal","disguisting"],
    "what are you doing":["nothing much","just chilling with friends","just enjoying the view"]
}
engine=pyttsx3.init()
user1=(input("you: ")).lower()
if user1 in response1:
    reply1=(random.choice(response1[user1]))
else:
    reply1=("sorry! i'm not trained to response to that text, try again with different text")
print("bot: ",reply1)
engine.say(reply1)
engine.runAndWait()
