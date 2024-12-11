# Python program to create a simple GUI calculator using tkinter
from tkinter import*
# create a GUI window
window = Tk()
# set the background colour of GUI window
window.configure(background="white")

# set the title of GUI window
window.title("Simple Calculator")

# set the configuration of GUI window
window.geometry("265x125")

# StringVar() is the variable class
# we create an instance of this class
equation = StringVar()
expression_field = Entry(window, textvariable=equation).grid(columnspan=4, ipadx=70)
# globally declare the expr variable
expr = ""


def update(num):
    global expr

    # concatenation of string
    expr = expr + str(num)

    # update the expr by using set method
    equation.set(expr)


# Function to evaluate the final expression
def equal():
    try:

        global expr

        # eval function evaluate the expression and str function convert the result into string

        total = str(eval(expr))

        equation.set(total)
        expr = total

    except:
        equation.set(" error ")
        expr = ""


# Function to clear the contents of text entry box
def clear():
    global expr
    expr = ""
    equation.set("")


Button(window, text=' 1 ', fg='white', bg='grey', command=lambda: update(1), height=1, width=7).grid(row=2, column=0)

Button(window, text=' 2 ', fg='white', bg='grey', command=lambda: update(2), height=1, width=7).grid(row=2, column=1)

Button(window, text=' 3 ', fg='white', bg='grey', command=lambda: update(3), height=1, width=7).grid(row=2, column=2)

Button(window, text=' 4 ', fg='white', bg='grey', command=lambda: update(4), height=1, width=7).grid(row=3, column=0)

Button(window, text=' 5 ', fg='white', bg='grey', command=lambda: update(5), height=1, width=7).grid(row=3, column=1)

Button(window, text=' 6 ', fg='white', bg='grey', command=lambda: update(6), height=1, width=7).grid(row=3, column=2)

Button(window, text=' 7 ', fg='white', bg='grey', command=lambda: update(7), height=1, width=7).grid(row=4, column=0)

Button(window, text=' 8 ', fg='white', bg='grey', command=lambda: update(8), height=1, width=7).grid(row=4, column=1)

Button(window, text=' 9 ', fg='white', bg='grey', command=lambda: update(9), height=1, width=7).grid(row=4, column=2)

Button(window, text=' 0 ', fg='white', bg='grey', command=lambda: update(0), height=1, width=7).grid(row=5, column=0)

Button(window, text=' + ', fg='white', bg='grey', command=lambda: update("+"), height=1, width=7).grid(row=2, column=3)

Button(window, text=' - ', fg='white', bg='grey', command=lambda: update("-"), height=1, width=7).grid(row=3, column=3)

Button(window, text=' * ', fg='white', bg='grey', command=lambda: update("*"), height=1, width=7).grid(row=4, column=3)

Button(window, text=' / ', fg='white', bg='grey', command=lambda: update("/"), height=1, width=7).grid(row=5, column=3)

Button(window, text='	=	', fg='white', bg='grey', command=equal, height=1, width=7).grid(row=5, column=2)

Button(window, text='Clear', fg='white', bg='grey', command=clear, height=1, width=7).grid(row=5, column=1)

window.mainloop()
