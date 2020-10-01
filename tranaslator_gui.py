
from googletrans import Translator
import pyttsx3
import tkinter as tk

root=tk.Tk()
root.geometry("800*400")
root.title("Translator")
en=tk.StringVar()

def trans():
	global speech
	x=en.get()
	translator = Translator()
	translated = translator.translate(x)
	speech = translated.text
	T.insert('end',speech)
  
 def speak():
 	engine = pyttsx3.init()
	engine.say(speech)
	engine.runAndWait()
label = tk.Label(root,text="Text").grid(row=0,column=0)
label2 = tk.Label(root,text="Output:").grid(row=3,column=0)
entry = tk.Entry(root,textvariable=en).grid(row=0,column=1,padx=5,pady=10,ipadx=150,ipady=20)


T = tk.Text(root, height=30,width=30)
T.grid(row=4,column=1,padx=5,pady=10,ipadx=30,ipady=10)
button=tk.Button(root,text="Translate",fg="Red",bg="Black",command=tran).grid(row=1,column=0,padx=10,pady=10,ipadx=30,ipady=10)
button2=tk.Button(root,text="Speak",fg="Red",bg="Black",command=speak).grid(row=4,column=1,padx=10,pady=10,ipadx=30,ipady=10)
root.mainloop()
