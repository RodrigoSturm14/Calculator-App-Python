import tkinter as tk # importar modulo tkinter
from tkinter import ttk

root = tk.Tk() # crear objeto root, q es la ventana

root.title('Calculadora')
root.geometry('400x400+50+50') # dimensiones y posicion
root.resizable(False, False) # evitar ajustar dimensiones
root.iconbitmap('./assets/vector-calculator-icon.ico')

def button_pressed(in_num):
  global equation_text
  equation_text += str(in_num)
  equation_label.set(equation_text)

def equals_pressed():
  global equation_text
  global total
  total = str(eval(equation_text))
  equation_text = total
  equation_label.set(total)

def ans_pressed(in_total):
  global equation_text
  equation_text += in_total
  equation_label.set(equation_text)

def clear_pressed():
  global equation_text
  equation_text = ''
  equation_label.set(equation_text)

equation_text = ''
total = ''
equation_label = tk.StringVar()

label = tk.Label(root, textvariable=equation_label, width=24, height=2, bg='white', font=('calibri', 20))
label.pack()

frame = ttk.Frame()
frame.pack()

button_1 = ttk.Button(frame, text=1, command= lambda: button_pressed(1))
button_1.grid(row=0, column=0, ipadx=5, ipady=10)

button_2 = ttk.Button(frame, text=2, command= lambda: button_pressed(2))
button_2.grid(row=0, column=1, ipadx=5, ipady=10)

button_3 = ttk.Button(frame, text=3, command= lambda: button_pressed(3))
button_3.grid(row=0, column=2, ipadx=5, ipady=10)

button_4 = ttk.Button(frame, text=4, command= lambda: button_pressed(4))
button_4.grid(row=1, column=0, ipadx=5, ipady=10)

button_5 = ttk.Button(frame, text=5, command= lambda: button_pressed(5))
button_5.grid(row=1, column=1, ipadx=5, ipady=10)

button_6 = ttk.Button(frame, text=6, command= lambda: button_pressed(6))
button_6.grid(row=1, column=2, ipadx=5, ipady=10)

button_7 = ttk.Button(frame, text=7, command= lambda: button_pressed(7))
button_7.grid(row=2, column=0, ipadx=5, ipady=10)

button_8 = ttk.Button(frame, text=8, command= lambda: button_pressed(8))
button_8.grid(row=2, column=1, ipadx=5, ipady=10)

button_9 = ttk.Button(frame, text=9, command= lambda: button_pressed(9))
button_9.grid(row=2, column=2, ipadx=5, ipady=10)

button_0 = ttk.Button(frame, text=0, command= lambda: button_pressed(0))
button_0.grid(row=3, column=1, ipadx=5, ipady=10)

decimal = ttk.Button(frame, text='.', command= lambda: button_pressed('.'))
decimal.grid(row=3, column=0, ipadx=5, ipady=10)

plus = ttk.Button(frame, text='+', command= lambda: button_pressed(' + '))
plus.grid(row=0, column=3, ipadx=5, ipady=10)

minus = ttk.Button(frame, text='-', command= lambda: button_pressed(' - '))
minus.grid(row=1, column=3, ipadx=5, ipady=10)

multiply = ttk.Button(frame, text='*', command= lambda: button_pressed(' * '))
multiply.grid(row=2, column=3, ipadx=5, ipady=10)

divide = ttk.Button(frame, text='/', command= lambda: button_pressed(' / '))
divide.grid(row=3, column=3, ipadx=5, ipady=10)

open_parenthesis = ttk.Button(frame, text='(', command= lambda: button_pressed(' ( '))
open_parenthesis.grid(row=4, column=0, ipadx=5, ipady=10)

close_parenthesis = ttk.Button(frame, text=')', command= lambda: button_pressed(' ) '))
close_parenthesis.grid(row=4, column=1, ipadx=5, ipady=10)

equal = ttk.Button(frame, text='=', command= lambda: equals_pressed())
equal.grid(row=4, column=3, ipadx=5, ipady=10)

answer = ttk.Button(frame, text='Ans', command= lambda: ans_pressed(total))
answer.grid(row=3, column=2, ipadx=5, ipady=10)

clear = ttk.Button(frame, text='C', command= lambda: clear_pressed())
clear.grid(row=4, column=2, ipadx=5, ipady=10)

root.mainloop() # mantener la ventana abierta
