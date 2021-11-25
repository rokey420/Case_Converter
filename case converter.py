from tkinter import * 
from tkinter.ttk import *
# Define a function new.
def new():
   g = ""
   # Get the string text into variable "g".
   g = e1.get()
   # If the given text is in upper case conver it into lower case formate.
   if g.isupper():
      y = ""
      y = g.lower()
      # Transfering the converted TEXT to equation. 
      equation.set(y)
   # If it is lower case conver it into upper case.   
   else:
      y = ""
      y = g.upper()
      equation.set(y)   

if __name__ == "__main__":
   # Create a tkinter window.
   window = Tk()
   window.title("GUI")
   window.geometry("400x200")
   window.configure(bg='#88ebeb')
   l1 = Label(window,text = "Enter Text :",background="#4ababa",font=("Arial Bold",20))    
   l1.grid(row = 0, column = 1, pady = 2)
   equation = StringVar()
   # Create a text window.
   e1 = Entry(window,textvariable=equation)
   e1.grid(row = 0, column = 8, pady = 2,padx=15)   
   b1 = Button(window, text = 'Click me !',command =new)
   b1.grid(row = 2, column = 2, sticky = E)
   window.mainloop()