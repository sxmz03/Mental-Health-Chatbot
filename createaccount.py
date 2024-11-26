from tkinter import *


class createaccountpage:
	#initilising
	def __init__(self, start = TRUE):
		self.start = start
		global createaccount
		#creates window for GUI
		createaccount = Tk()
		#changes title of window
		createaccount.title("Therabuddy")
	def createacc(self):
	#checks if username is already taken
		newusername = usernameentry.get()
		file1 = open("username.txt", "r")
		for line in file1:
			#calls takenusername page which tells the user the username is taken
			if newusername in line:
				createaccount.destroy()
				import takenusername

			else:
				#saves username and password
				file1 = open("username.txt", "a")
				file1.write(newusername)
				file1.write(",")
				file1.close
				newpassword = passwordentry.get()
				details = newusername+newpassword
				file2= open("usernameandpassword.txt","a")
				file2.write(details)
				file2.write(",")
				file2.close
				createaccount.destroy()
				import details



	def createaccountGUI(self):
			#creates banner at top of screen for name and logo
		banner= Label(text="Therabuddy",
		width =50,
		height = 1,
		bg = "lightblue",
		font = "arial" )
		banner.pack()

			#creates label that indicates to users what box to put username in
		usernametxt = Label(text = "Create Username:",
				font = "arial",
				width = 30
		)
		usernametxt.pack()
		#creates box for users to input their username into
		global usernameentry
		usernameentry = Entry(width = 50 ,
		bg = "ivory",
		)
		usernameentry.pack()


			#creates label that indicates to users what box to put password in
		passwordtxt = Label(text = "Create Password:",
					font = "arial",                  )
		passwordtxt.pack()


		#creates box for users to input their password into
		global passwordentry
		passwordentry = Entry(width = 50,
													bg = "ivory")
		passwordentry.pack()



			#create button to enter in details
		enter = Button(text = "Enter",
									width = 10,
									bg = "silver",
									command = self.createacc)
		enter.pack()
		createaccount.mainloop()
createaccountpage(TRUE).createaccountGUI()