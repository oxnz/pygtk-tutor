#!/usr/bin/env python

# example checkbutton.py

import pygtk
pygtk.require('2.0')
import gtk

class RadioButtons:
	# Our callback.
	# The data passed to this method is printed to stdout
	def callback(self, widget, data=None):
		print "%s was toggled %s" % (data, ("OFF", "ON")[widget.get_active()])
	def close_application(self, widget, event, data=None):
		gtk.main_quit()
		return False

	def __init__(self):
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.connect("delete_event", self.close_application)
		# Set the window title
		self.window.set_title("Radio Button")
		# Sets the border width of the window
		self.window.set_border_width(0)

		# Create a vertical box
		box1 = gtk.VBox(False, 0)
		self.window.add(box1)
		box1.show()

		box2 = gtk.VBox(False, 10)
		box2.set_border_width(10)
		box1.pack_start(box2, True, True, 0)
		box2.show()

		button = gtk.RadioButton(None, "radio button1")
		button.connect("toggled", self.callback, "radio button 1")
		box2.pack_start(button, True, True, 0)
		button.show()

		button = gtk.RadioButton(button, "radio button2")
		button.connect("toggled", self.callback, "radio button 2")
		box2.pack_start(button, True, True, 0)
		button.show()

		button = gtk.RadioButton(button, "radio button3")
		button.connect("toggled", self.callback, "radio button 3")
		box2.pack_start(button, True, True, 0)
		button.show()

		separator = gtk.HSeparator()
		box1.pack_start(separator, False, True, 0)
		separator.show()

		box2 = gtk.VBox(False, 10)
		box2.set_border_width(10)
		box1.pack_start(box2, False, True, 0)
		box2.show()

		button = gtk.Button("Close")
		button.connect_object("clicked", self.close_application,
				self.window, None)
		box2.pack_start(button, True, True, 0)
		button.set_flags(gtk.CAN_DEFAULT)
		button.grab_default()
		button.show()
		self.window.show()

def main():
	gtk.main()
	return 0

if __name__ == "__main__":
	RadioButtons()
	main()
