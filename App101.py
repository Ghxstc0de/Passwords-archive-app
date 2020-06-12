from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox

root = Tk()
root.title("PassBook")
root.geometry("640x640+0+0")

#Where the client enter the password firstly:


def gclick():
    global googlepass
    googlepass = simpledialog.askstring("Password","Enter your Google Password")

def iclick():
    global instapass
    instapass = simpledialog.askstring("Password","Enter your Instagram Password")

def eclick():
    global epicpass
    epicpass = simpledialog.askstring("Password","Enter your Epic Password")

def revealgp():
    new.showinfo("password: ", googlepass)

mylabel = Label(root, text="Welcome to your passwords archive", font=("arial", 25, "bold"), fg= "#ed2b34"  )
mylabel2 = Label(root, text="Choose a website:", font=("arial", 10, "bold"), fg= "#000000")

# The buttons and their customisation:

Googlebutton = Button(root, text = "Google", padx = 50, command = gclick, bg="#275e43", fg="white")
Instagrambutton = Button(root, text = "Instagram", padx = 43, command = iclick, bg="#275e43", fg="white")
Epicbutton = Button(root, text = "Epic games", padx = 40, command = eclick, bg="#275e43", fg="white")
Revealg = Button(root, text = "Reveal", padx = 50, command = revealgp, bg="#1ff042", fg="white" )

#button positions in the app

mylabel.place(x=15, y=0)
mylabel2.place(x=230, y=50)

Googlebutton.place(x=215, y=100)
Revealg.place(x=415, y=100)

Instagrambutton.place(x=215, y=150)
Epicbutton.place(x=215, y=200)


root.mainloop()



