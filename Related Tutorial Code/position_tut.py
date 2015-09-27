'''
	Another Tkinter layout tutorial using grid manager

	Site:	http://zetcode.com/gui/tkinter/layout/

	Created: 9.27.15

'''

from Tkinter import Tk, Text, Entry, BOTH, W, N, E, S
from ttk import Frame, Button, Label, Style
import serial


class Example(Frame):

	def __init__(self, parent):
		Frame.__init__(self, parent)
		self.parent = parent

		self.initUI()

	def initUI(self):

		self.parent.title("Windows")
		self.style = Style()
		self.style.theme_use("default")
		self.pack(fill=BOTH, expand=1)

		#	Configures padding between items in application
		self.columnconfigure(1, weight=1)
		self.columnconfigure(3, pad=7)
		self.rowconfigure(3, weight=1)
		self.rowconfigure(5, pad=7)

		self.lbl = Label(self, text="Windows")
		self.lbl.grid(sticky=W, pady=4, padx=5)

		self.area = Label(self)
		#	Column and row span make box go to that column/row
		self.area.grid(row=1, column=0, columnspan=2, rowspan=4, padx=5, sticky=E+W+S+N)

		self.abtn = Button(self, text="Connect", command = self.connect)
		# self.abtn["command"] = update_box()
		self.abtn.grid(row=1, column=3)

		self.cbtn = Button(self, text="Close")
		self.cbtn.grid(row=2, column=3, pady=4)

		self.hbtn = Button(self, text="Help")
		self.hbtn.grid(row=5, column=0, padx=5)

		self.obtn = Button(self, text="Open")
		self.obtn.grid(row=5, column=3)

	def connect(self):
		# self.area["text"] = "Activated"
		
		port = '/dev/tty.OBDII-Port'
		ser = serial.Serial(port)

	# def quit(self):
		# self.destroy()


def main():

	root = Tk()
	root.geometry("350x300+300+300")
	app = Example(root)
	root.mainloop()


if __name__ == '__main__':
	main()