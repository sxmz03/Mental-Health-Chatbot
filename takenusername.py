from tkinter import *
takenusername = Tk()

class takenusername:
	#initilising
	def __init__(self, start = TRUE):
		self.start = start
		global takenusername
		#creates window for GUI
		takenusername = Tk()
		#changes title for window
		takenusername.title("Therabuddy")


	def createacc(self):
	#checks if username is taken
		newusername = usernameentry.get()
		file1 = open("username.txt", "r")
		for line in file1:
			#saves username and password
			if newusername not in line:
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
				takenusername.destroy()
				import details


	def takenusernameGUI(self):
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
		#creates label for username take text
		taken1 = Label(text = "Username taken",
		fg = "red")
		taken1.pack()
		#creates label for try again text
		taken2 = Label(text = "Please enter another username",
		fg ="red")
		taken2.pack()

		takenusername.mainloop()
takenusername(TRUE).takenusernameGUI()