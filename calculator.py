from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.title("CAlCULATOR")
root.geometry("644x1100")

img=PhotoImage(file="calculator.png")
root.iconphoto(False,img)
root.config(background="grey")
scvalue=StringVar()
scvalue.set("")
screen = Entry(root, textvariable= scvalue , font="lucida 40 bold",fg="black",background="white",border=2)
screen.pack(fill=X , ipadx=8, pady=10,padx=10)

def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                print(e)
                value="Error"

        scvalue.set(value)
        screen.update()
    elif text == "Clear":
        scvalue.set("")
        screen.update()

    else:
        scvalue.set(scvalue.get() + text)
        screen.update()


    return

def lal():
    exit()

f = Frame(root,bg="white")

b = Button(f,text="7",pady=10,padx=10,font="Aerial 35 bold")
b.pack(side=LEFT,padx=3,pady=3)
b.bind("<Button-1>",click)

b = Button(f,text="8",pady=10 ,padx=10,font="Aerial 35 bold")
b.pack(side=LEFT,padx=3,pady=3)
b.bind("<Button-1>",click)

b = Button(f,text="9",pady=10,padx=10,font="Aerial 35 bold")
b.pack(side=LEFT,padx=3,pady=3)
b.bind("<Button-1>",click)
f.pack()
f = Frame(root,bg="white")

b = Button(f,text="4",pady=10,padx=10,font="Aerial 35 bold")
b.pack(side=LEFT,padx=3,pady=3)
b.bind("<Button-1>",click)

b = Button(f,text="5",pady=10,padx=10,font="Aerial 35 bold")
b.pack(side=LEFT,padx=3,pady=3)
b.bind("<Button-1>",click)

b = Button(f,text="6",pady=10,padx=10,font="Aerial 35 bold")
b.pack(side=LEFT,padx=3,pady=3)
b.bind("<Button-1>",click)
f.pack()

f = Frame(root,bg="white")
b = Button(f,text="1",pady=10,padx=10,font="Aerial 35 bold")
b.pack(side=LEFT,padx=3,pady=3)
b.bind("<Button-1>",click)

b = Button(f,text="2",pady=10,padx=10,font="Aerial 35 bold")
b.pack(side=LEFT,padx=3,pady=3)
b.bind("<Button-1>",click)

b = Button(f,text="3",pady=10,padx=10,font="Aerial 35 bold")
b.pack(side=LEFT,padx=3,pady=3)
b.bind("<Button-1>",click)
f.pack()

f = Frame(root,bg="white")
b = Button(f,text="0",pady=10,padx=10,font="Aerial 35 bold")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

b = Button(f,text=".",pady=10,padx=10,font="Aerial 35 bold")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

b = Button(f,text="-",pady=10,padx=10,font="Aerial 35 bold")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)
f.pack()

f = Frame(root,bg="black")
b = Button(f,text="+",pady=8,padx=8,font="Aerial 35 bold")
b.pack(side=LEFT,padx=2,pady=2)
b.bind("<Button-1>",click)

b = Button(f,text="*",pady=10,padx=10,font="Aerial 35 bold")
b.pack(side=LEFT,padx=3,pady=3)
b.bind("<Button-1>",click)

b = Button(f,text="/",pady=10,padx=10,font="Aerial 35 bold")
b.pack(side=LEFT,padx=3,pady=3)
b.bind("<Button-1>",click)
b = Button(f,text="=",pady=8,padx=8,font="Aerial 35 bold")
b.pack(side=LEFT,padx=2,pady=2)
b.bind("<Button-1>",click)
f.pack()

f = Frame(root,bg="black")


b = Button(f,text="Clear",pady=5,padx=5,font="Aerial 35 bold")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

b = Button(f,text="Exit",pady=5,padx=5,font="Aerial 35 bold",command=lal,background='red')
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)
f.pack()



root.mainloop()
