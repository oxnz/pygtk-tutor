#!/usr/bin/env python

# example progressbar.py

import pygtk
pygtk.require('2.0')
import gtk

# Update the value of the progress bar so that we get some movement
def progress_timeout(pbobj):
	if pbobj.activity_check.get_active():
		pbobj.pbar.pulse()
	else:
		# Calculate the value of the progress bar using the
		# value range set in the adjustment object
		new_val = pbobj.pbar.get_fraction() + 0.01
		if new_val > 1.0:
			new_val = 0.0
		# Set the new value
		pbobj.pbar.set_fraction(new_val)
	
	# As this is a timeout function, return TRUE so that it coninues to
	# get called
	return True

class ProgressBar:
	# Callback that toggles the text display within the progress bar trough
	def toggle_show_text(self, widget, data=None):
		if widget.get_active():
			self.pbar.set_text("some text")
		else:
			self.pbar.set_text("")
	
	# Callback that toggles the activity mode of the progress bar
	def toggle_activity_mode(self, widget, data=None):
		if widget.get_active():
			self.pbar.pulse()
		else:
			self.pbar.set_fraction(0.0)
	
	# Callback that toggles the orientation of the progress bar

	def toggle_orientation(self, widget, data=None):
		if self.pbar.get_orientation() == gtk.PROGRESS_LEFT_TO_RIGHT:
			self.pbar.set_orientation(gtk.PROGRESS_RIGHT_TO_LEFT)
		elif self.pbar.get_orientation() == gtk.PROGRESS_RIGHT_TO_LEFT:
			self.pbar.set_orientation(gtk.PROGRESS_LEFT_TO_RIGHT)
			# Clean up allocated memory and remove the timer
		def destroy_progress(self, widget, data=None):
			gobject.source_remove(self.timer)
			self.timer = 0
			gtk.main_quit()
		def __init__(self):
			self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
			self.window.set_resizable(True)
			self.window.connect("destroy", self.destroy_progress)
			self.window.set_title("ProgressBar")
			self.window.set_border_width(0)
			vbox = gtk.VBox(False, 5)
			vbox.set_border_width(10)
			self.window.add(vbox)
			vbox.show()
			# Create a centering alignment object
			align = gtk.Alignment(0.5, 0.5, 0, 0)
			vbox.pack_start(align, False, False, 5)
			align.show()
			# Create the ProgressBar
			self.pbar = gtk.ProgressBar()
			align.add(self.pbar)
			self.pbar.show()
			# Add a timer callback to update the value of the progress bar
			self.timer = gobject.timeout_add (100, progress_timeout, self)
			separator = gtk.HSeparator()
			vbox.pack_start(separator, False, False, 0)

