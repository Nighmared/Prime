# coding= UTF-8
try:
	from Tkinter import *
except:
	from tkinter import *
import prime as pr

BG_COL = 'white'
master = Tk()
master.title("Primes")
master.minsize(width=500,height=100)
master['bg'] = BG_COL
GenList = []

def importold():
	global l
	global GenList
	l.delete(0,END)
	f = open('genlist.txt').read().split(',')
	for e in f:
		GenList.append(e)
		e += '.csv'
		l.insert(END,e)
def exportold():
	global GenList
	if GenList:
		GenList = [int(e) for e in GenList]
		GenList.sort()
		f = open('genlist.txt','w')
		for e in GenList:
			if e != GenList[-1]:
				f.write(str(e)+',')
			else:
				f.write(str(e))

def quitt(event=0):
	global master
	master.destroy()
	exportold()
def quittl(event):
	global TL
	e.focus_set()
	TL.destroy()


def getinput():
	t2['text'] = ""
	try:
		if int(e.get())>50000000:
			t2['text'] = "Range zu hoch, das Maximum beträgt 50'000'000"
		else:
			return int(e.get())
	except ValueError:
		t2['text'] = "Ungültige Eingabe"
		e.delete(0,END)
		return(False)
def passon(event):
	run()
def run():
	global l
	global GenList
	l.select_clear(0,END)
	resT['text'] = ''
	RNG = getinput()
	e.delete(0,END)
	if not RNG == False:
		fname = str(RNG)+'.csv'
		if not fname in l.get(0,END):
			pr.goforit(RNG,False)
			resT['text']= 'Datei als {} exportiert'.format(fname)
			l.insert(END,fname)
			l.see(END)
			GenList.append(RNG)
		else:
			for x in range(0,len(l.get(0,END))+1):
				resT['text']= 'Datei existiert schon'
				if l.get(x) == fname:
					l.select_set(x)
					l.see(x)

def giveit(event):
	index = (l.nearest(event.y))
	try: openup(l.get(0,END)[index])
	except IndexError: None

def openup(file):
	global TL
	numlist = getfile(file)
	Wx,Wy = master.winfo_x(),master.winfo_y()
	Ww = master.winfo_width()
	TL = Toplevel(bg='LightGreen')
	TL.geometry("%dx%d+%d+%d" % (200, 500, Wx+Ww+30, Wy))
	TL.title("ListViewer - {}".format(file))
	TL.focus_force()
	TL.bind('<Escape>',quittl)
	scroll1 = Scrollbar(TL,orient=VERTICAL)
	scroll1.pack(side=RIGHT,fill=Y)
	l2 = Listbox(TL,bg='LightGreen',width=100,height=40,selectbackground='LightGreen',selectforeground='black',activestyle='none',yscrollcommand=scroll1.set)
	l2.pack(fill=Y,ipadx=20,ipady=25)
	l2.delete(0,END)
	l2.focus_set()
	scroll1.config(command=l2.yview)
	for e in numlist:
		l2.insert(END,'  '+e)

def getfile(file):
	f = open(file).read().split()
	return f


wt = Label(master,text="Bei sehr hohen Range Werten kann die Berechnung einige Minuten in Anspruch nehmen.\n Das Programm hat sich aber, auch wenn Windows das anders sieht, nicht aufgehangen!", fg="green",bg="yellow")
wt.pack()
t = Label(master,text="Range eingeben",bg=BG_COL)
t.pack()

t2 = Label(master,text="",fg='red',bg=BG_COL)
t2.pack()

e = Entry(master,bg=BG_COL)
e.bind('<Return>',passon)
e.pack()
e.focus_set()

b = Button(master,text="Run",width=10, command=run)
b.pack()

resT = Label(master,text="",fg="blue",bg=BG_COL)
resT.pack()

t3 = Label(master,text="Schon berechnete Listen",bg=BG_COL,fg='black')
t3.pack()


l = Listbox(master,bg='lightgrey',selectbackground='white',activestyle='none',selectforeground="black")
l.pack()
l.bind('<Double-Button-1>',giveit)

importold()

master.bind('<Escape>',quitt)
master.protocol("WM_DELETE_WINDOW", quitt)

mainloop()
