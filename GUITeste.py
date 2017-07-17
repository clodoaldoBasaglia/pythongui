from tkinter import *


def inicializar():
    root = Tk()
    w = Label(root, text="teste")
    w.pack(side=LEFT)
    entry = Entry(root, bd=5)
    entry.pack(side=LEFT)
    bu = Button(root, text="teste")
    bu.pack(side=RIGHT)
    root.mainloop()

def main():
    print("teste")
    inicializar()


main()