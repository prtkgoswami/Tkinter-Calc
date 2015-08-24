from Tkinter import *
root = Tk()

#	
#	_________________________________
#	|_________Calculator______|O|-|x|
#	|===========DISPLAY=============| 
#	|_______________________________| 
#	|		C		|	X	|	Y	| 
#	| Poly+	| Poly-	| Poly*	| Poly/	| 
#	|	^	| sqrt	|	%	|	/	|
#	|	9	|	8	|	7	|	*	| 
#	|	6	|	5	|	4	|	-	| 
#	|	3	|	2	|	1	|	+	| 
#	|		0		|	.	|	=	| 
#	|_______________________________| 
#

# VARIABLES
disp = StringVar()
txt="0"

# FUNCTIONS
def clear():
	disp.set("0")

def calc():
	s=display.get()
	i=0
	op=""
	res=0
	operator=["+","-","*","/","%","^"]
	for o in operator:
		if o in s:
			i=s.find(o)
			op=o
	a=float(s[:i])
	b=float(s[i+1:])
	if op=="+":
		res=a+b
	elif op=="-":
		res=a-b
	elif op=="*":
		res=a*b
	elif op=="/":
		res=a/b
	elif op=="%":
		res=a%b
	elif op=="^":
		res=a**b
	disp.set("%.2f"%res)

def sqroot():
	s=float(display.get())
	disp.set("%.2f"%(s**0.5))

def enterDisp(n):
	s=display.get()
	if s=="0":
		disp.set(n)
	else:
		s+=n
		disp.set(s)

root.title("CALCULATOR")

# geometry(60,100)
frame = Frame(root)
frame.pack()
frame.configure(background="#2f2f2f")

# DISPLAY
disp.set(txt)
display=Entry(frame,font="Helvetica 30",justify="right",bg="#263238",fg="#f5f5f5",textvariable=disp,width=20)
display.grid(row=0,column=0,columnspan=4)

# BUTTONS
# OPERATORS
# ROW 1
clear=Button(frame,command=clear,text="C",font="Helvetica 18",bg="#b71c1c",fg="#f5f5f5",width=15).grid(row=1,column=0,columnspan=2)
x=Button(frame,text="x",font="Helvetica 18",bg="#FFC400",fg="#2f2f2f",width=7).grid(row=1,column=2,columnspan=1)
y=Button(frame,text="y",font="Helvetica 18",bg="#FFC400",fg="#2f2f2f",width=7).grid(row=1,column=3,columnspan=1)
# ROW 2
poly_add=Button(frame,text="Poly+",font="Helvetica 18",bg="#e65100",fg="#f5f5f5",width=7).grid(row=2,column=0,columnspan=1)
poly_minus=Button(frame,text="Poly-",font="Helvetica 18",bg="#e65100",fg="#f5f5f5",width=7).grid(row=2,column=1,columnspan=1)
poly_mult=Button(frame,text="Poly*",font="Helvetica 18",bg="#e65100",fg="#f5f5f5",width=7).grid(row=2,column=2,columnspan=1)
poly_div=Button(frame,text="Poly/",font="Helvetica 18",bg="#e65100",fg="#f5f5f5",width=7).grid(row=2,column=3,columnspan=1)
# ROW 3
power=Button(frame,command=lambda:enterDisp("^"),text="^",font="Helvetica 18",bg="#FFC400",fg="#2f2f2f",width=7).grid(row=3,column=0,columnspan=1)
sqroot=Button(frame,command=sqroot,text="sqrt",font="Helvetica 18",bg="#FFC400",fg="#2f2f2f",width=7).grid(row=3,column=1,columnspan=1)
mod=Button(frame,command=lambda:enterDisp("%"),text="%",font="Helvetica 18",bg="#FFC400",fg="#2f2f2f",width=7).grid(row=3,column=2,columnspan=1)
div=Button(frame,command=lambda:enterDisp("/"),text="/",font="Helvetica 18",bg="#FFC400",fg="#2f2f2f",width=7).grid(row=3,column=3,columnspan=1)
# ROW 4
mult=Button(frame,command=lambda:enterDisp("*"),text="*",font="Helvetica 18",bg="#FFC400",fg="#2f2f2f",width=7).grid(row=4,column=3,columnspan=1)
# ROW 5
minus=Button(frame,command=lambda:enterDisp("-"),text="-",font="Helvetica 18",bg="#FFC400",fg="#2f2f2f",width=7).grid(row=5,column=3,columnspan=1)
# ROW 6
plus=Button(frame,command=lambda:enterDisp("+"),text="+",font="Helvetica 18",bg="#FFC400",fg="#2f2f2f",width=7).grid(row=6,column=3,columnspan=1)
# ROW 7
equals=Button(frame,command=calc,text="=",font="Helvetica 18",bg="#FFC400",fg="#2f2f2f",width=7).grid(row=7,column=3,columnspan=1)
#NUMBERS
b9=Button(frame,command=lambda:enterDisp("9"),text="9",font="Helvetica 18",bg="#212121",fg="#f5f5f5",width=7).grid(row=4,column=0,columnspan=1)
b8=Button(frame,command=lambda:enterDisp("8"),text="8",font="Helvetica 18",bg="#212121",fg="#f5f5f5",width=7).grid(row=4,column=1,columnspan=1)
b7=Button(frame,command=lambda:enterDisp("7"),text="7",font="Helvetica 18",bg="#212121",fg="#f5f5f5",width=7).grid(row=4,column=2,columnspan=1)
b6=Button(frame,command=lambda:enterDisp("6"),text="6",font="Helvetica 18",bg="#212121",fg="#f5f5f5",width=7).grid(row=5,column=0,columnspan=1)
b5=Button(frame,command=lambda:enterDisp("5"),text="5",font="Helvetica 18",bg="#212121",fg="#f5f5f5",width=7).grid(row=5,column=1,columnspan=1)
b4=Button(frame,command=lambda:enterDisp("4"),text="4",font="Helvetica 18",bg="#212121",fg="#f5f5f5",width=7).grid(row=5,column=2,columnspan=1)
b3=Button(frame,command=lambda:enterDisp("3"),text="3",font="Helvetica 18",bg="#212121",fg="#f5f5f5",width=7).grid(row=6,column=0,columnspan=1)
b2=Button(frame,command=lambda:enterDisp("2"),text="2",font="Helvetica 18",bg="#212121",fg="#f5f5f5",width=7).grid(row=6,column=1,columnspan=1)
b1=Button(frame,command=lambda:enterDisp("1"),text="1",font="Helvetica 18",bg="#212121",fg="#f5f5f5",width=7).grid(row=6,column=2,columnspan=1)
b0=Button(frame,command=lambda:enterDisp("0"),text="0",font="Helvetica 18",bg="#212121",fg="#f5f5f5",width=15).grid(row=7,column=0,columnspan=2)
point=Button(frame,command=lambda:enterDisp("."),text=".",font="Helvetica 18",bg="#212121",fg="#f5f5f5",width=7).grid(row=7,column=2,columnspan=1)

root.mainloop()