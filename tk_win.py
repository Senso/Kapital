
from Tkinter import *

class Tk_win:
	def __init__(self):
		self.root = Tk()
		self.main_txt = StringVar()
		self.opts_txt = StringVar()
		self.head_txt = StringVar()

	def init_screen(self):
		# Top buttons
		self.button_1 = Button(self.root, text='Derp', state=DISABLED,
			height=1, width=4, anchor=W, justify=LEFT)
		self.button_1.grid(row=0, sticky=W)
		
		# Header text
		self.head_win = Label(self.root, width=60, height=3,
			justify=LEFT, anchor=NW, bg='#000000',
			fg='#FFFFFF', wraplength=500, font=("courier", "10"), textvariable=self.head_txt)
		self.head_win.grid(row=1, rowspan=5)
		
		# Main text window
		self.main_win = Label(self.root, width=60, height=25,
		  justify=LEFT, anchor=NW, bg='#000000',
		  fg='#FFFFFF', wraplength=500, font=("courier", "10"), textvariable=self.main_txt)
		self.main_win.grid(row=6, rowspan=20)
		
		# Options window
		self.opts_win = Label(self.root, width=60, height=10,
			justify=LEFT, anchor=SW, bg='#000000',
			fg='#FFFFFF', wraplength=500, font=("courier", "10"), textvariable=self.opts_txt)
		self.opts_win.grid(row=26, rowspan=5)

		self.root.mainloop()
		
	def display_column_data(self, prefix, header, data, suffix=''):
		data.insert(0, header)
		
		cols = zip(*data)
		col_widths = [ max(len(str(value)) for value in col) for col in cols ]
		format = ' '.join(['%%%ss' % width for width in col_widths ]) + '\n'
		
		text = prefix
		for row in data:
			text += format % tuple(row)
		text += suffix
		
		self.update_main_win(text)

	def update_head_win(self, txt):
		self.head_txt.set(txt)
		
	def update_main_win(self, txt):
		self.main_txt.set(txt)
		
	def update_opts_win(self, txt):
		self.opts_txt.set(txt)
	