from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename="superhero")

#root = tk()
root.title("TTk Bootstrap!")
# root.iconbitmap('images/codemy.ico')
root.geometry('800x650')


my_button = tb.Button(text="Hello World!", bootstyle=)
my_button.pack(pady=40)


root.mainloop()