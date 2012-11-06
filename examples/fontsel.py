#!/usr/bin/env python
# -*- encoding: UTF-8 -*-

import pygtk
pygtk.require('2.0')
import gtk

class FontSelector:
	def font_ok_sel(self, w):
		print "%s" % self.fontseldlg.get_font_name()
	
	def destroy(self, widget):
		gtk.main_quit()
	def __init__(self):
		self.fontseldlg = gtk.FontSelectionDialog("Font selection")
		self.fontseldlg.connect("destroy", self.destroy)
		self.fontseldlg.ok_button.connect("clicked", self.font_ok_sel)
		self.fontseldlg.cancel_button.connect("clicked", lambda w: self.fontseldlg.destroy())
		self.fontseldlg.set_preview_text("0123456789!@#$%^&我爱中国")
		self.fontseldlg.show()

def main():
	gtk.main()
	return 0

if __name__ == "__main__":
	FontSelector()
	main()
