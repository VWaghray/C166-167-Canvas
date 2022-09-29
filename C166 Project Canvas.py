from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image

root = Tk()
root.title("Canvas")
root.geometry("700x700")
root.configure(bg = "#b7410e")

canvas = Canvas(root, width = 700, height = 500 , bg = "beige", highlightbackground= "gold2")
canvas.pack()

label = Label(root, text = "StartX", bg = "#b7410e", fg = "#30D5C8")
label.place(relx=0.03,rely=0.88,anchor=CENTER)

startx_get=StringVar()
startx=ttk.Combobox(root,textvariable=startx_get,state="readonly",values=[0,100,200,300,400,500,600,700,800])

starx=startx_get.get()
starty_get=StringVar()
starty=ttk.Combobox(root,textvariable=starty_get,state="readonly",values=[0,100,200,300,400,500])

label2 = Label(root, text = "StartY", bg = "#b7410e", fg = "#30D5C8")
label2.place(relx=0.27,rely=0.88,anchor=CENTER)

stary=starty_get.get()

endx_get=StringVar()
endx=ttk.Combobox(root,textvariable=endx_get,state="readonly",values=[0,100,200,300,400,500,600,700,800])

label3 = Label(root, text = "EndX", bg = "#b7410e", fg = "#30D5C8")
label3.place(relx=0.49,rely=0.88,anchor=CENTER)

enx=endx_get.get()
endy_get=StringVar()
endy=ttk.Combobox(root,textvariable=endy_get,state="readonly",values=[0,100,200,300,400,500])

label4 = Label(root, text = "EndY", bg = "#b7410e", fg = "#30D5C8")
label4.place(relx=0.72,rely=0.88,anchor=CENTER)

eny=endy_get.get()

fillcolour = ["red", "orange", "yellow", "green", "blue"]


colour_get=StringVar()
colour=ttk.Combobox(root,textvariable=colour_get,values=fillcolour)

label5 = Label(root, text = "Choose Colour", bg = "#b7410e", fg = "#30D5C8")
label5.place(relx=0.68,rely=0.94,anchor=CENTER)

color=colour_get.get()









startx.place(relx=0.16,rely=0.88,anchor=CENTER)
starty.place(relx=0.38,rely=0.88,anchor=CENTER)
endx.place(relx=0.6,rely=0.88,anchor=CENTER)
endy.place(relx=0.83,rely=0.88,anchor=CENTER)
colour.place(relx=0.83,rely=0.94,anchor=CENTER)

root.mainloop()