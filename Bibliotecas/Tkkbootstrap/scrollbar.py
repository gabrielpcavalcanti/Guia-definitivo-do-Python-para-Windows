import ttkbootstrap as tb
from tkinter import *

root = tb.Window(themename="solar")
root.title("Scrollbars")
root.geometry("500x350")

frame = tb.Frame(root)
frame.pack(pady=20)

scroll = tb.Scrollbar(frame, orient='vertical', bootstyle='success round')
scroll.pack(side="right", fill="y")

text = Text(frame, width=30, height=25, yscrollcommand=scroll.set, wrap="none", font=("helvetica", 18))
text.pack()

scroll.config(command=text.yview)

root.mainloop()
