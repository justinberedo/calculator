from tkinter import *

expression = ""

def press(num):
	global expression
	expression = expression + str(num)
	equation.set(expression)

def pressequal():
	try:
		global expression
		result = str(eval(expression))
		equation.set(result)
		expression = ""
	except:
		equation.set(" error ")
		expression = ""
def clear():
	global expression
	expression = ""
	equation.set("0")

if __name__ == "__main__":
	gui = Tk()
	gui.configure(background="black")
	gui.title("Calculator")
	gui.geometry("150x150")
	equation = StringVar()
	expression_field = Entry(gui, textvariable=equation)
	expression_field.grid(columnspan=4, ipadx=10)
	equation.set('0')

	button1 = Button(gui, text='1', bg='orange',
		command=lambda: press(1), height=1, width=3)
	button1.grid(row=5, column=0)

	button2 = Button(gui, text='2', bg='orange',
		command=lambda: press(2), height=1, width=3)
	button2.grid(row=5, column=1)

	button3 = Button(gui, text='3', bg='orange',
		command=lambda: press(3), height=1, width=3)
	button3.grid(row=5, column=2)

	button4 = Button(gui, text='4', bg='orange',
		command=lambda: press(4), height=1, width=3)
	button4.grid(row=4, column=0)

	button5 = Button(gui, text='5', bg='orange',
		command=lambda: press(5), height=1, width=3)
	button5.grid(row=4, column=1)

	button6 = Button(gui, text='6', bg='orange',
		command=lambda: press(6), height=1, width=3)
	button6.grid(row=4, column=2)

	button7 = Button(gui, text='7', bg='orange',
		command=lambda: press(7), height=1, width=3)
	button7.grid(row=3, column=0)

	button8 = Button(gui, text='8', bg='orange',
		command=lambda: press(8), height=1, width=3)
	button8.grid(row=3, column=1)

	button9 = Button(gui, text='9', bg='orange',
		command=lambda: press(9), height=1, width=3)
	button9.grid(row=3, column=2)

	button0 = Button(gui, text='0', bg='orange',
		command=lambda: press(0), height=1, width=3)
	button0.grid(row=6, column=0)

	Decimal = Button(gui, text='.', bg='orange',
		command=lambda: press('.'), height=1, width=3)
	Decimal.grid(row=7, column=0)

	plus = Button(gui, text='+', bg='orange',
		command=lambda: press('+'), height=1, width=3)
	plus.grid(row=3, column=3)

	minus = Button(gui, text='-', bg='orange',
		command=lambda: press('-'), height=1, width=3)
	minus.grid(row=4, column=3)

	multiply = Button(gui, text='*', bg='orange',
		command=lambda: press('*'), height=1, width=3)
	multiply.grid(row=5, column=3)

	divide = Button(gui, text='/', bg='orange',
		command=lambda: press('/'), height=1, width=3)
	divide.grid(row=6, column=3)

	clear = Button(gui, text='AC', bg='orange',
		command=clear, height=1, width=3)
	clear.grid(row=6, column=1)

	equal = Button(gui, text='=', bg='orange',
		command=pressequal, height=1, width=3)
	equal.grid(row=6, column=2)

	gui.mainloop()


