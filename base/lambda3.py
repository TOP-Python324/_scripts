from tkinter import Tk, Button

root = Tk()
root.geometry('300x200')
root.title('Демонстратор')

btn = Button(
    text='НАЖМИ МЕНЯ!',
    command=lambda: print('НАЖАТИЕ')
)
btn.grid(
    row=0, column=0, 
    sticky='nsew',
    padx=20, pady=20
)

root.mainloop()
