from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image

root = Tk()
root.title("Canvas")
root.geometry("900x700")
root.configure(bg = "#b7410e")

canvas = Canvas(root, width = 900, height = 500 , bg = "beige", highlightbackground= "gold2")
canvas.pack()

label = Label(root, text = "StartX", bg = "#b7410e", fg = "#30D5C8", font = ("Fixedsys", 10))
label.place(relx=0.03,rely=0.80,anchor=CENTER)

startx_get=StringVar()
startx=ttk.Combobox(root,textvariable=startx_get,state="readonly",values=[0,100,200,300,400,500,600,700,800])

starx=startx_get.get()
starty_get=StringVar()
starty=ttk.Combobox(root,textvariable=starty_get,state="readonly",values=[0,100,200,300,400,500])

label2 = Label(root, text = "StartY", bg = "#b7410e", fg = "#30D5C8", font = ("Fixedsys", 10))
label2.place(relx=0.27,rely=0.80,anchor=CENTER)

stary=starty_get.get()

endx_get=StringVar()
endx=ttk.Combobox(root,textvariable=endx_get,state="readonly",values=[0,100,200,300,400,500,600,700,800])

label3 = Label(root, text = "EndX", bg = "#b7410e", fg = "#30D5C8", font = ("Fixedsys", 10))
label3.place(relx=0.49,rely=0.80,anchor=CENTER)

enx=endx_get.get()
endy_get=StringVar()
endy=ttk.Combobox(root,textvariable=endy_get,state="readonly",values=[0,100,200,300,400,500])

label4 = Label(root, text = "EndY", bg = "#b7410e", fg = "#30D5C8", font = ("Fixedsys", 10))
label4.place(relx=0.72,rely=0.80,anchor=CENTER)

eny=endy_get.get()

fillcolour = ["red", "orange", "yellow", "green", "blue"]


colour_get=StringVar()
colour=ttk.Combobox(root,textvariable=colour_get,values=fillcolour, state = "readonly")

label5 = Label(root, text = "Choose Colour", bg = "#b7410e", fg = "#30D5C8", font = ("Fixedsys", 10))
label5.place(relx=0.68,rely=0.85,anchor=CENTER)

color=colour_get.get()

startx.insert(0," ")
starty.insert(0," ")
endx.insert(0," ")
endy.insert(0," ")
draw=""

def circle(event):
    global draw
    global starx
    global stary
    global enx
    global eny
    global color
    color=colour_get.get()
    drawing="circle"
    starx=startx_get.get()
    stary=starty_get.get()
    enx=endx_get.get()
    eny=endy_get.get()
    draw(drawing,stary,enx,starx,eny,color)
    
def rectangle(event):
    global draw
    global starx
    global stary
    global enx
    global eny
    global color
    color=colour_get.get()
    drawing="rect"
    starx=startx_get.get()
    stary=starty_get.get()
    enx=endx_get.get()
    eny=endy_get.get()
    draw(drawing,stary,starx,enx,eny,color)
    
def line(event):
    global draw
    global starx
    global stary
    global enx
    global eny
    global color
    color=colour_get.get()
    drawing="line"
    starx=startx_get.get()
    stary=starty_get.get()
    enx=endx_get.get()
    eny=endy_get.get()
    draw(drawing,stary,enx,starx,eny,color)
    
def draw(drawing,stary,starx,enx,eny,color):
    if(color==""):
        color="black"
    if(drawing=="rect"):
        canvas.create_rectangle(stary,starx,enx,eny,fill=color,width=3)
    elif(drawing=="circle"):
        canvas.create_oval(starx,stary,enx,eny,fill=color,width=3)
    elif(drawing=="line"):
        canvas.create_line(starx,stary,enx,eny,fill=color,width=3)
        

root.bind("<r>",rectangle)
root.bind("<c>",circle)
root.bind("<l>",line)

startx.place(relx=0.16,rely=0.80,anchor=CENTER)
starty.place(relx=0.38,rely=0.80,anchor=CENTER)
endx.place(relx=0.6,rely=0.80,anchor=CENTER)
endy.place(relx=0.83,rely=0.80,anchor=CENTER)
colour.place(relx=0.83,rely=0.85,anchor=CENTER)

root.mainloop()
