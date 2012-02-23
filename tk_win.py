
from Tkinter import *

class Tk_win:
	def __init__(self):
		self.root = Tk()
		self.main_txt = StringVar()
		self.opts_txt = StringVar()
		self.head_txt = StringVar()

	def init_screen(self):
		# Header text
		self.head_win = Label(self.root, width=60, height=3,
			justify=LEFT, anchor=NW, bg='#000000',
			fg='#FFFFFF', wraplength=500, font=("courier", "10"), textvariable=self.head_txt)
		self.head_win.pack(side=TOP)
		
		# Main text window
		self.main_win = Label(self.root, width=60, height=25,
		  justify=LEFT, anchor=NW, bg='#000000',
		  fg='#FFFFFF', wraplength=500, font=("courier", "10"), textvariable=self.main_txt)
		self.main_win.pack(side=TOP)
		
		# Options window
		self.opts_win = Label(self.root, width=60, height=10,
			justify=LEFT, anchor=SW, bg='#000000',
			fg='#FFFFFF', wraplength=500, font=("courier", "10"), textvariable=self.opts_txt)
		self.opts_win.pack(side=BOTTOM)
		
		self.root.mainloop()
		
	def display_column_data(self, prefix, header, data, suffix=''):
		hmax = max(len(w) for w in header) + 1
		dmax = max(len(str(w)) for w in [item for sublist in data for item in sublist])
		vmax = hmax if hmax > dmax else dmax
		
		head = "%s" * len(header) + '\n'
		head = head % tuple([x.ljust(vmax) for x in header])
		
		text = prefix
		text += head
		
		dat = "%s" * len(header) + '\n'
		for line in data:
			text += dat % tuple([str(x).ljust(vmax) for x in line])
		
		text += suffix
		
		self.update_main_win(text)

	def update_head_win(self, txt):
		self.head_txt.set(txt)
		
	def update_main_win(self, txt):
		self.main_txt.set(txt)
		
	def update_opts_win(self, txt):
		self.opts_txt.set(txt)
	