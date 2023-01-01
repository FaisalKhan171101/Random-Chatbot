#importing required libraries
from tkinter import *
import tkinter as tk
import random
import os
import pyttsx3 

#importing module for jokes
import pyjokes

#importing module for facts
import randfacts

#importing module for articles
#imporing modules for videos
import webbrowser as wb

#import game files
import guessme
import Numcrick
import RockPaperScissor
import whatthecolor
import Jumbbled


#making chatbot speak
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 130) 
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#send button function
def send():
	send = "You: "+e.get()
	txt.insert(END,"\n"+send)


	greeting = ['hi','hello','hey','what you can do?','hi bot','hello random','hi random']
	games = ['game','lets play a game','1','give me a game to play']
	jokes = ['joke','tell me a joke','2','can you be funny']
	articles = ['article','read','article to read','5','give me a article to read']
	facts = ['fact','3','tell me a fact']
	music = ['music','play music','4']
	vedios = ['video','funny video','6','play a video']
	movies = ['movie','7','play a movie']

	if e.get().lower() in greeting:
		txt.insert(END,"\n"+"Random: Hi I am Random\n\tThis what I can Do\n\t 1.Play games with you\n\t 2.Tell You a Joke\n\t 3.Tell You a random fact\n\t 4.Play music for you\n\t 5.Random Article to read\n\t 6.Play a funny video\n\t 7.Play a movie")
		speak(" Hi I am Random your chat bot see on screen to know what i can do for you")

	elif e.get().lower() in games:
		txt.insert(END,"\n"+"Random: Opening a random game for you to play")
		speak(' Opening a random game for you to play')
		ch = random.randint(1,5)
		if ch == 1:
			guessme.main()
		elif ch == 2:
			Numcrick.main()
		elif ch == 3:
			RockPaperScissor.main()
		elif ch == 4:
			whatthecolor.main()
		elif ch == 5:
			Jumbbled.main()

	#Jokes
	elif e.get().lower() in jokes:
		txt.insert(END,"\n"+"Random: Here is a random joke for you")
		joke = pyjokes.get_joke(language = 'en',category = "neutral")
		txt.insert(END,"\n"+f"Random: {joke}")
		speak(f" Here is a random joke for you {joke}")

	#Facts
	elif e.get().lower() in facts:
		txt.insert(END,"\n"+"Random: Here is a random fact for you")
		fact = randfacts.getFact()
		txt.insert(END,"\n"+f"Random: {fact}")
		speak(f" Here is a random fact for you{fact}")

	#playing music
	elif e.get().lower() in music:
		txt.insert(END,"\n"+"Random: Playing a random song for you")
		speak(' Playing a random song for you')
		music_dir = 'D:\\songs'
		songs = os.listdir(music_dir)
		i = random.randint(1,3)
		os.startfile(os.path.join(music_dir, songs[i]))

	#articles
	elif e.get().lower() in articles:
		txt.insert(END,"\n"+"Random: Opening a random Article for you")
		speak(' Opening a random Article for you to read')
		wb.open('https://en.wikipedia.org/wiki/Special:Random')

	#vedio
	elif e.get().lower() in vedios:
		txt.insert(END,"\n"+"Random: Playing a random Funny video for you")
		speak(' Playing a funny vedio for you')
		url = ['https://youtu.be/VNPClMMa418','https://youtu.be/68-g_VczjYA','https://youtu.be/aEsO894eXbQ','https://youtu.be/o8hd_l3S-mo','https://youtu.be/hIpU2TGEt10']
		random.shuffle(url)
		wb.open(url[1])

	#movies
	elif e.get().lower() in movies:
		txt.insert(END,"\n"+"Random: Opening a random movie for you")
		wb.open('https://www.netflix.com/browse/my-list')
		speak(' Playing a movie for you')

	#quit
	elif 'bye' in e.get().lower() or 'quit' in e.get().lower():
		txt.insert(END,"\n",'Bye Have a good day')
		speak('Bye Have a good day')
		root.destroy()


	else:
		txt.insert(END,"\n"+"Random: I Didnt recogniz that")
		speak('Sorry i Did not recogniz that')
	txt.insert(END,"\n"+"Random: Do you want me to do anything else?")

	e.delete(0,END)


root = Tk()
root.title('Random')
root.geometry('400x500')
root.iconbitmap("icon.ico")

txt = Text(root,bd = 1,bg = 'black',width = 50,height=8, fg='white')
txt.place(x=6,y=6,height=385,width=370)

e = Entry(root,bg = 'black',width=30,fg='white')
e.place(x = 128,y=400,height=88,width=260)

b = Button(root,text = 'Send',bg='blue',activebackground='light blue',width=12,height=5,font=('Arial',15),command=send)
b.place(x=6,y=400,height=88,width=120)

scrollbar = Scrollbar(root,command=txt.yview())
scrollbar.place(x = 375,y=5,height=385)
scrollbar.config( command = txt.yview )


root.mainloop()