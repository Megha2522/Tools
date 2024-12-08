from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
import random
# making main window
window = Tk() 
window.title("HANG-MAN GAME")
window.config(background="teal")

##### SOME ADDITIONAL FUNCTIONS
def index_finder(lis,char):
    l=[]
    for k in range(len(lis)):
        if lis[k]==char: l.append(k)
    return l
def endgame():
	b.configure(state='disabled')
	c.configure(state='disabled')
	d.configure(state='disabled')
	f.configure(state='disabled')
	g.configure(state='disabled')
	h.configure(state='disabled')
	j.configure(state='disabled')
	k.configure(state='disabled')
	l.configure(state='disabled')
	m.configure(state='disabled')
	n.configure(state='disabled')
	p.configure(state='disabled')
	q.configure(state='disabled')
	r.configure(state='disabled')
	s.configure(state='disabled')
	t.configure(state='disabled')
	v.configure(state='disabled')
	w.configure(state='disabled')
	x.configure(state='disabled')
	y.configure(state='disabled')
	z.configure(state='disabled')
	a0.configure(state='disabled')
	a1.configure(state='disabled')
	a2.configure(state='disabled')
	a3.configure(state='disabled')
	a4.configure(state='disabled')
	a5.configure(state='disabled')
def play_again():
	messagebox.showinfo("PLAY AGAIN","To Play the GAME again:\nClose game window & restart HANG-MAN Game file OR Click on the HANG-MAN GAME Button...")
## HANGMAN IMAGE TEMPLATES
hman_full="_______\n|----------  \n|     O      \n|     /|\\      \n|     / \\      \n|_______"
hman_empty="_______\n              \n              \n              \n              \n_______"
hman_start="_______\n|----------- \n|              \n|              \n|              \n|_______"
hman_head="_______\n|----------  \n|     O      \n|              \n|              \n|_______"
hman_body="_______\n|---------- \n|     O      \n|     /|\\      \n|              \n|_______"
# movies data
movies=["V E N O M","I N T E R S T E L L A R","G O D Z I L L A","S P E C T R E","A V E N G E R S","X M E N","T R A N S F O R M E R S","S P I D E R M A N","T H O R","T I T A N I C"]
select_movie=movies.pop(random.randint(0,len(movies)-1))
dplct_slct=select_movie.split()
coded=select_movie.split()
display_var=""
lis=['A','E','I','O','U']
for i in range(len(coded)):
	if coded[i] not in ['A','E','I','O','U']: coded[i]=" _ "  
for j in range(len(coded)): display_var=display_var+coded[j]
#widgets
topFrame=Frame(window)
topFrame.pack()
leftFrame=Frame(window)
leftFrame.pack(side=LEFT)
rightFrame=Frame(window)
rightFrame.pack(side=RIGHT)
heading=Label(topFrame,text="STICKMAN HANG-MAN GAME", bg="black", fg="white",font=("Arial Bold", 30))
heading.pack(fill=X)
############################### FUNCTIONING STARTS ###############################
wrong=0
def ins(arg):
	global wrong
	###### DISABLING RESPECTIVE BUTTONS ON CLICK | STARTS  ######
	if arg=='B': b.configure(state='disabled')
	elif arg=='C': c.configure(state='disabled')
	elif arg=='D': d.configure(state='disabled')
	elif arg=='F': f.configure(state='disabled')
	elif arg=='G': g.configure(state='disabled')
	elif arg=='H': h.configure(state='disabled')
	elif arg=='J': j.configure(state='disabled')
	elif arg=='K': k.configure(state='disabled')
	elif arg=='L': l.configure(state='disabled')
	elif arg=='M': m.configure(state='disabled')
	elif arg=='N': n.configure(state='disabled')
	elif arg=='P': p.configure(state='disabled')
	elif arg=='Q': q.configure(state='disabled')
	elif arg=='R': r.configure(state='disabled')
	elif arg=='S': s.configure(state='disabled')
	elif arg=='T': t.configure(state='disabled')
	elif arg=='V': v.configure(state='disabled')
	elif arg=='W': w.configure(state='disabled')
	elif arg=='X': x.configure(state='disabled')
	elif arg=='Y': y.configure(state='disabled')
	elif arg=='Z': z.configure(state='disabled')
	elif arg=='0': a0.configure(state='disabled')
	elif arg=='1': a1.configure(state='disabled')
	elif arg=='2': a2.configure(state='disabled')
	elif arg=='3': a3.configure(state='disabled')
	elif arg=='4': a4.configure(state='disabled')
	elif arg=='5': a5.configure(state='disabled')
	###### DISABLING RESPECTIVE BUTTONS ON CLICK | ENDS  ######
	if arg in select_movie:
		indexes=index_finder(dplct_slct,arg)
		for i in indexes: coded[i]=arg
		string=""
		for a in range(len(coded)): string=string+coded[a]
		display.configure(text=string)
		if " _ " not in coded: 
			endgame()
			messagebox.showinfo("YOU WON!!!","\n\t| > > > > > YOU WON  < < < < < |\t\t\n\n")
			play_again()
	else:
		wrong+=1
		if wrong==1: hangman_img.configure(text=hman_start)
		elif wrong==2: hangman_img.configure(text=hman_head)
		elif wrong==3: hangman_img.configure(text=hman_body)
		elif wrong==4: 
			hangman_img.configure(text=hman_full)
			display.configure(text=select_movie)
			endgame()
			messagebox.showerror("YOU LOST !!!","\n\n\t\t|~~~ YOU LOST ~~~|\t\t\n\t\tBetter LUCK next Time !!!\t\t\n")
			play_again()

############################### FUNCTIONING ENDS #################################
display=Label(leftFrame,text=display_var,fg="black",bg="white",font=("Arial Bold",20))
display.grid(column=0,row=0,columnspan=9)
b=Button(leftFrame,text="B",fg="white",bg="black",command=lambda: ins('B'),font=("Arial Bold",17), height=1, width=2)
c=Button(leftFrame,text="C",fg="white",bg="black",command=lambda: ins('C'),font=("Arial Bold",17), height=1, width=2)
d=Button(leftFrame,text="D",fg="white",bg="black",command=lambda: ins('D'),font=("Arial Bold",17), height=1, width=2)
f=Button(leftFrame,text="F",fg="white",bg="black",command=lambda: ins('F'),font=("Arial Bold",17), height=1, width=2)
g=Button(leftFrame,text="G",fg="white",bg="black",command=lambda: ins('G'),font=("Arial Bold",17), height=1, width=2)
h=Button(leftFrame,text="H",fg="white",bg="black",command=lambda: ins('H'),font=("Arial Bold",17), height=1, width=2)
j=Button(leftFrame,text="J",fg="white",bg="black",command=lambda: ins('J'),font=("Arial Bold",17), height=1, width=2)
k=Button(leftFrame,text="K",fg="white",bg="black",command=lambda: ins('K'),font=("Arial Bold",17), height=1, width=2)
l=Button(leftFrame,text="L",fg="white",bg="black",command=lambda: ins('L'),font=("Arial Bold",17), height=1, width=2)
##
m=Button(leftFrame,text="M",fg="white",bg="black",command=lambda: ins('M'),font=("Arial Bold",17), height=1, width=2)
n=Button(leftFrame,text="N",fg="white",bg="black",command=lambda: ins('N'),font=("Arial Bold",17), height=1, width=2)
p=Button(leftFrame,text="P",fg="white",bg="black",command=lambda: ins('P'),font=("Arial Bold",17), height=1, width=2)
q=Button(leftFrame,text="Q",fg="white",bg="black",command=lambda: ins('Q'),font=("Arial Bold",17), height=1, width=2)
r=Button(leftFrame,text="R",fg="white",bg="black",command=lambda: ins('R'),font=("Arial Bold",17), height=1, width=2)
s=Button(leftFrame,text="S",fg="white",bg="black",command=lambda: ins('S'),font=("Arial Bold",17), height=1, width=2)
t=Button(leftFrame,text="T",fg="white",bg="black",command=lambda: ins('T'),font=("Arial Bold",17), height=1, width=2)
v=Button(leftFrame,text="V",fg="white",bg="black",command=lambda: ins('V'),font=("Arial Bold",17), height=1, width=2)
w=Button(leftFrame,text="W",fg="white",bg="black",command=lambda: ins('W'),font=("Arial Bold",17), height=1, width=2)
##
x=Button(leftFrame,text="X",fg="white",bg="black",command=lambda: ins('X'),font=("Arial Bold",17), height=1, width=2)
y=Button(leftFrame,text="Y",fg="white",bg="black",command=lambda: ins('Y'),font=("Arial Bold",17), height=1, width=2)
z=Button(leftFrame,text="Z",fg="white",bg="black",command=lambda: ins('Z'),font=("Arial Bold",17), height=1, width=2)
a0=Button(leftFrame,text="0",fg="white",bg="black",command=lambda: ins('0'),font=("Arial Bold",17),height=1, width=2)
a1=Button(leftFrame,text="1",fg="white",bg="black",command=lambda: ins('1'),font=("Arial Bold",17),height=1, width=2)
a2=Button(leftFrame,text="2",fg="white",bg="black",command=lambda: ins('2'),font=("Arial Bold",17),height=1, width=2)
a3=Button(leftFrame,text="3",fg="white",bg="black",command=lambda: ins('3'),font=("Arial Bold",17),height=1, width=2)
a4=Button(leftFrame,text="4",fg="white",bg="black",command=lambda: ins('4'),font=("Arial Bold",17),height=1, width=2)
a5=Button(leftFrame,text="5",fg="white",bg="black",command=lambda: ins('5'),font=("Arial Bold",17),height=1, width=2)
##
b.grid(column=0,row=1,padx=2,pady=2)
c.grid(column=1,row=1,padx=2,pady=2)
d.grid(column=2,row=1,padx=2,pady=2)
f.grid(column=3,row=1,padx=2,pady=2)
g.grid(column=4,row=1,padx=2,pady=2)
h.grid(column=5,row=1,padx=2,pady=2)
j.grid(column=6,row=1,padx=2,pady=2)
k.grid(column=7,row=1,padx=2,pady=2)
l.grid(column=8,row=1,padx=2,pady=2)
##
m.grid(column=0,row=2,padx=2,pady=2)
n.grid(column=1,row=2,padx=2,pady=2)
p.grid(column=2,row=2,padx=2,pady=2)
q.grid(column=3,row=2,padx=2,pady=2)
r.grid(column=4,row=2,padx=2,pady=2)
s.grid(column=5,row=2,padx=2,pady=2)
t.grid(column=6,row=2,padx=2,pady=2)
v.grid(column=7,row=2,padx=2,pady=2)
w.grid(column=8,row=2,padx=2,pady=2)
##
x.grid(column=0,row=3,padx=2,pady=2)
y.grid(column=1,row=3,padx=2,pady=2)
z.grid(column=2,row=3,padx=2,pady=2)
a0.grid(column=3,row=3,padx=2,pady=2)
a1.grid(column=4,row=3,padx=2,pady=2)
a2.grid(column=5,row=3,padx=2,pady=2)
a3.grid(column=6,row=3,padx=2,pady=2)
a4.grid(column=7,row=3,padx=2,pady=2)
a5.grid(column=8,row=3,padx=2,pady=2)
##
hangman_img=Label(rightFrame,text=hman_empty,font=("Arial Bold",22))
hangman_img.grid(column=0,row=0)
##
# RULES TO PLAY THE GAME
messagebox.showinfo("INSTRUCTIONS","RULES TO PLAY THE GAME:\n\t1) Click a button to guess respective alphabet.\n\t2) 3 Wrong answers are allowed.\n\t3) On 4th wrong answer Game will get Over.\n\t4) Only popular HOLLYWOOD movies are asked.\n\t5) Buttons will get disabled after CLICK.")
##
##
# mainloop
window.mainloop()