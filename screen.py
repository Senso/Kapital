import pygtk 
pygtk.require("2.0")
import gtk

class Screen:
	def __init__(self):
		self.vbox = gtk.VBox() 
		self.hbox = gtk.HBox()
		win = gtk.Window()
		win.add(self.vbox)
		
		self.top_menu()
		self.main_label()
		
		win.show_all()
		gtk.main()
		
	def top_menu(self):
		self.menubar = gtk.MenuBar()
		file_item = gtk.MenuItem("_File")
		help_item = gtk.MenuItem("_Help")
		
		file_item_sub = gtk.Menu()
		save = gtk.MenuItem("_Save")
		quit = gtk.MenuItem("_Quit")
		file_item_sub.append(save)
		file_item_sub.append(quit)
		
		help_item_sub = gtk.Menu()
		about = gtk.MenuItem("_About")
		help_item_sub.append(about)
		
		file_item.set_submenu(file_item_sub)
		help_item.set_submenu(help_item_sub)
		self.menubar.append(file_item)
		self.menubar.append(help_item)
		
		save.connect("activate", self.save_callback)
		quit.connect("activate", self.quit_callback)
		about.connect("activate", self.about_callback)
		self.vbox.pack_start(self.menubar, True, True, 2)
		
	def main_label(self):
		self.label = gtk.Label()
		self.label.selectable = 1
		self.vbox.pack_start(self.label, True, True, 2)
		
	def save_callback(self, widget=None):
		print "Save menu item was pressed"

	def quit_callback(self, widget=None):
		print "Quit menu item was pressed"
		gtk.main_quit()

	def about_callback(widget=None):
		print "About menu item was pressed"













