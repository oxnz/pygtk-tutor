#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk

class Note(object):
	def __init__(self):
		print "Init ..."
		window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		window.set_title("Note v 0.1")
		window.set_default_size(400, 200)
		window.connect("destroy", lambda w: gtk.main_quit())

		content = gtk.TextView()
		window.add(content)
		content.show()
		window.show()
	def run(self):
		print "run"
		gtk.main()
		return 0

if __name__ == "__main__":
	note = Note()
	note.run()
