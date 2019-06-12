import tkinter
from tkinter.constants import *
tk = tkinter.Tk()
frame = tkinter.Frame(tk, relief=GROOVE, borderwidth=100)
frame.pack(fill=BOTH,expand=7)
label = tkinter.Label(frame, text="Buttons")
label.pack(fill=X, expand=1)
button = tkinter.Button(frame,text="hey!")
button.pack(side=BOTTOM)
tk.mainloop()
