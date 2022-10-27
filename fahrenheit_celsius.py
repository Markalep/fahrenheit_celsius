from cProfile import label
from tkinter import *

#°C = (°F - 32) ÷ 1,8
#-------------------------------------------------------------
# GUI

root = Tk()
root.title('App')

final = StringVar()

#-------------------------------------------------------------
# funções

def calcular():
    F = float(textbox1.get())
    C = (F - 32)* 5/9
    final.set(str(round(C, 1)) + ' graus Celsius')

#-------------------------------------------------------------
# widgets

label1 = Label(root, text = 'Fahrenheit:')
textbox1 = Entry(root)
btn = Button(root, text = 'Calcular:', command=calcular)
label_resultado = Label(root, textvariable=final)

#-------------------------------------------------------------
# layout

label1.grid()
textbox1.grid()
btn.grid(sticky='E')
label_resultado.grid()
root.geometry('500x300+400+300')

root.mainloop()