import tkinter

test = tkinter.Tk()

label1 = tkinter.Label(test, text = 'label1')
label2 = tkinter.Button(test, text = 'label2')

label1.pack()
label2.pack()

test.mainloop()