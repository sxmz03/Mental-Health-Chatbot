from tkinter import *


class detailspage:
	#initiliasing
	def __init__(self, start=TRUE):
		self.start = start
		#creates window for the GUI
		details = Tk()
		#changes title of window
		details.title("Therabuddy")
	def detailsave(self):
		#takes in name and address
		name = nameentry.get()
		address = addressentry.get()
		#saves name and address
		file = open("details.txt","a")
		file.write(name+""+address)
		file.write(",")
		details.destroy()
		import main


	def detailsGUI(self):
		#creates banner for the top of the page
		banner = Label(text="Therabuddy",
					   width=50,
					   height=1,
					   bg="lightblue",
					   font="arial"
					   )
		banner.pack()
		#creates label for name
		nametxt = Label(text = "Full Name:",
			font = "arial",
				width = 30)
		nametxt.pack()
		#creates entry box for name so users can type their name
		global nameentry
		nameentry = Entry(width = 50,
		bg = "ivory")
		nameentry.pack()

			#creates label that indicates to users what box to put address in
		addresstxt = Label(text = "Please input your address",
					font = "arial",                  )
		addresstxt.pack()


			#creates box for users to input their address into
		addressentry = Entry(width = 50,
													bg = "ivory")
		addressentry.pack()
		#creates button to enter name and address
		Enter = Button(text = "Enter",
		width = 10,
									bg = "silver",
									command = self.detailsave )
		Enter.pack()
		details.mainloop()

detailspage(TRUE).detailsGUI()