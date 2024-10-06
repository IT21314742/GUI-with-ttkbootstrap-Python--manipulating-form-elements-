from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename="superhero")

#root = tk()
root.title("TTk Bootstrap!")
# root.iconbitmap('images/codemy.ico')
root.geometry('800x650')

#style
my_style = tb.Style()
my_style.configure('success.Outline.TButton', font=("Helvetica", 18))


my_button = tb.Button(text="Hello World!",
                      bootstyle="success",
                      style="success.Update.TButton")

my_button.pack(pady=40)





root.mainloop()