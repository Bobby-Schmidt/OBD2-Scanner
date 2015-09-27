'''
	Initial:	Set up interface using Tkinter library
	Date:		9.26.15

'''

from Tkinter import *

class Application(Frame):


	def __init__(self, master):
		#	Initiaizes the frame
		Frame.__init__(self, master)
		self.grid()
		self.button_clicks = 0	#	Count number of clicks
		self.create_widgets()

	def create_widgets(self):

		#	Create buttons
		self.button1 = Button(self, text = "Total Clicks: 0")

		self.button1["command"] = self.update_count
		self.button1.grid(row = 0, column = 0, sticky = W)

		self.button2 = Button(self, text = "Second Button")
		self.button2.grid(row = 2, column = 0, sticky = W)

		self.button3 = Button(self, text = "Third Button")
		self.button3.grid()

	def update_count(self):
		#	Increases click count and display total
		self.button_clicks += 1
		self.button1["text"] = "Total Clicks: " + str(self.button_clicks)

root = Tk()
root.title("Buttons")
root.geometry("200x100")


app = Application(root)
root.mainloop()
