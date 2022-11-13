from tkinter import *


def button_press(num):

    global equation_text

    equation_text = equation_text + str(num)
    equation_label.set(equation_text)


def equals():

    try:
        global equation_text

        total = str(eval(equation_text))

        equation_label.set(total)

        equation_text = total

    except ZeroDivisionError:
        equation_label.set("Zero Division Error!")
        equation_text = ""

    except SyntaxError:
        equation_label.set("Syntax Error!")
        equation_text = ""


def clear():

    global equation_text

    equation_label.set("")
    equation_text = ""


window = Tk()
window.title("Basic Calculator by TMazarov")
window.geometry("400x490")
window.resizable(width=False, height=False)
window.config(background="grey")

equation_text = ""
equation_label = StringVar()

label = Label(window,
              textvariable=equation_label,
              font=("arial", 20, 'bold'),
              fg="#00FF00", bg="black",
              width=23,
              height=2,
              relief=SUNKEN,
              bd=10)

label.pack()

frame = Frame(window)
frame.pack()

button1 = Button(frame,
                 text=1,
                 height=2,
                 width=6,
                 font=('arial', 18, 'bold'),
                 command=lambda: button_press(1))

button1.grid(row=0, column=0)

button2 = Button(frame,
                 text=2,
                 height=2,
                 width=6,
                 font=('arial', 18, 'bold'),
                 command=lambda: button_press(2))

button2.grid(row=0, column=1)

button3 = Button(frame,
                 text=3,
                 height=2,
                 width=6,
                 font=('arial', 18, 'bold'),
                 command=lambda: button_press(3))
button3.grid(row=0, column=2)

button4 = Button(frame,
                 text=4,
                 height=2,
                 width=6,
                 font=('arial', 18, 'bold'),
                 command=lambda: button_press(4))

button4.grid(row=1, column=0)

button5 = Button(frame,
                 text=5,
                 height=2,
                 width=6,
                 font=('arial', 18, 'bold'),
                 command=lambda: button_press(5))

button5.grid(row=1, column=1)

button6 = Button(frame,
                 text=6,
                 height=2,
                 width=6,
                 font=('arial', 18, 'bold'),
                 command=lambda: button_press(6))

button6.grid(row=1, column=2)

button7 = Button(frame,
                 text=7,
                 height=2,
                 width=6,
                 font=('arial', 18, 'bold'),
                 command=lambda: button_press(7))

button7.grid(row=2, column=0)

button8 = Button(frame,
                 text=8,
                 height=2,
                 width=6,
                 font=('arial', 18, 'bold'),
                 command=lambda: button_press(8))

button8.grid(row=2, column=1)

button9 = Button(frame,
                 text=9,
                 height=2,
                 width=6,
                 font=('arial', 18, 'bold'),
                 command=lambda: button_press(9))

button9.grid(row=2, column=2)

button0 = Button(frame,
                 text=0,
                 height=2,
                 width=6,
                 font=('arial', 18, 'bold'),
                 command=lambda: button_press(0))

button0.grid(row=3, column=0)

plus_button = Button(frame,
                     text="+",
                     height=2,
                     width=6,
                     font=('arial', 18, 'bold'),
                     command=lambda: button_press('+'))

plus_button.grid(row=0, column=3)

minus_button = Button(frame,
                      text="-",
                      height=2,
                      width=6,
                      font=('arial', 18, 'bold'),
                      command=lambda: button_press('-'))

minus_button.grid(row=1, column=3)

multiply_button = Button(frame,
                         text="*",
                         height=2,
                         width=6,
                         font=('arial', 18, 'bold'),
                         command=lambda: button_press('*'))

multiply_button.grid(row=2, column=3)

divide_button = Button(frame,
                       text="/",
                       height=2,
                       width=6,
                       font=('arial', 18, 'bold'),
                       command=lambda: button_press('/'))

divide_button.grid(row=3, column=3)

equal_button = Button(frame,
                      text="=",
                      height=2,
                      width=6,
                      font=('arial', 18, 'bold'),
                      command=equals)

equal_button.grid(row=3, column=2)

decimal_button = Button(frame,
                        text=".",
                        height=2,
                        width=6,
                        font=('arial', 18, 'bold'),
                        command=lambda: button_press('.'))

decimal_button.grid(row=3, column=1)

clear_button = Button(window,
                      text="Clear",
                      height=4, width=39,
                      font=('arial', 12, 'bold'),
                      command=clear)

clear_button.pack()

window.mainloop()
