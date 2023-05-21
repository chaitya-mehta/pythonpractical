from tkinter import *

def buttonClear():
    e.delete(0, END)

#function
def buttonAdd(number):
    
    current = e.get()
    e.delete(0, END)
    e.insert(0, current + str(number))
    
def buttonAddition():
    first_num = int(e.get())
    global f_num
    global math
    math = "addition"
    f_num = int(first_num)
    e.delete(0, END)

def buttoneQUAL():
    second_num = int(e.get())
    e.delete(0, END)

    if math == 'addition':
        sum = f_num + second_num
        e.insert(0, sum)
    elif math == 'substraction':
        e.insert(0, f_num - second_num)
    elif math == 'multiplication':
        e.insert(0, f_num * second_num)
    elif math == 'division':
        e.insert(0, f_num / second_num)

def buttonMult():
    first_num = int(e.get())
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_num)
    e.delete(0, END)

def buttonSub():
    first_num = int(e.get())
    global f_num
    global math
    math = "substraction"
    f_num = int(first_num)
    e.delete(0, END)

def buttonDiv():
    first_num = int(e.get())
    global f_num
    global math
    math = "division"
    f_num = int(first_num)
    e.delete(0, END)

#main
root = Tk()
root.title("Calculator")

e = Entry(root, width=40, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Define button
btn_1 = Button(root, text='1', padx=40, pady=20, command=lambda: buttonAdd(1))
btn_2 = Button(root, text='2', padx=40, pady=20, command=lambda: buttonAdd(2))
btn_3 = Button(root, text='3', padx=40, pady=20, command=lambda: buttonAdd(3))
btn_4 = Button(root, text='4', padx=40, pady=20, command=lambda: buttonAdd(4))
btn_5 = Button(root, text='5', padx=40, pady=20, command=lambda: buttonAdd(5))
btn_6 = Button(root, text='6', padx=40, pady=20, command=lambda: buttonAdd(6))
btn_7 = Button(root, text='7', padx=40, pady=20, command=lambda: buttonAdd(7))
btn_8 = Button(root, text='8', padx=40, pady=20, command=lambda: buttonAdd(8))
btn_9 = Button(root, text='9', padx=40, pady=20, command=lambda: buttonAdd(9))
btn_0 = Button(root, text='0', padx=40, pady=20, command=lambda: buttonAdd(0))

btn_add = Button(root, text='+', padx=40, pady=20, command=lambda: buttonAddition())
btn_mult = Button(root, text='x', padx=40, pady=20, command=lambda: buttonMult())
btn_sub = Button(root, text='-', padx=40, pady=20, command=lambda: buttonSub())
btn_div = Button(root, text='/', padx=40, pady=20, command=lambda: buttonDiv())

btn_equal = Button(root, text='=', padx=89, pady=20, command=lambda: buttoneQUAL())
btn_clear = Button(root, text='Clear', padx=79, pady=20, command=lambda: buttonClear())

# put buttons on screen

btn_1.grid(row=3, column=0)
btn_2.grid(row=3, column=1)
btn_3.grid(row=3, column=2)
btn_4.grid(row=2, column=0)
btn_5.grid(row=2, column=1)
btn_6.grid(row=2, column=2)
btn_7.grid(row=1, column=0)
btn_8.grid(row=1, column=1)
btn_9.grid(row=1, column=2)
btn_0.grid(row=4, column=0)

btn_add.grid(row=5, column=0)
btn_mult.grid(row=1, column=3)
btn_sub.grid(row=2, column=3)
btn_div.grid(row=3, column=3)

btn_clear.grid(row=5, column=1, columnspan=2)
btn_equal.grid(row=4, column=1, columnspan=2)

root.mainloop()