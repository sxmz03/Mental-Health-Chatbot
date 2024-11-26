from tkinter import *


class wrongusername:
    #initilising
    def __init__(self, start = TRUE):
        self.start = start
        global wrongusername
        #creates window for GUI
        wrongusername = Tk()
        #changes title for window
        wrongusername.title("Therabuddy")

    def login(self):
        #takes in username and password
        logusername = usernameentry.get()
        logpassword = passwordentry.get()
        check = logusername + logpassword
        # textfile is checked for the users username and password
        file = open("usernameandpassword.txt", "r")
        # allows user to go to the chatbot
        for line in file:
            if check in line:
                import phonenumber
    def createaccount(self):
        #gets rid of page and calls create account page
        wrongusername.destroy()
        import createaccount




    def wrongusernameGUI(self):
        # creates banner at top of screen for name and logo
        banner = Label(text="Welcome to Therabuddy",
                       width=50,
                       height=1,
                       bg="lightblue",
                       font="arial"
                       )
        banner.pack()
        # creates label that indicates to users what box to put username in
        usernametxt = Label(text="Username:",
                            font="arial",
                            width=30
                            )
        usernametxt.pack()

        # creates box for users to input their username into
        global usernameentry
        usernameentry = Entry(width=50,
                              bg="ivory",
                              )
        usernameentry.pack()

        # creates label that indicates to users what box to put password in
        passwordtxt = Label(text="Password:",
                            font="arial", )
        passwordtxt.pack()

        # creates box for users to input their password into
        global passwordentry
        passwordentry = Entry(width=50,
                              bg="ivory")
        passwordentry.pack()

        # create button to enter in details
        enter = Button(text="Enter",
                       width=10,
                       bg="silver",
                       command=self.login)
        enter.pack()
        # dividers

        # button that takes users to create account page
        createacc = Button(text="Not got an account? Create one",
                           bg="silver",
                           command=self.createaccount

                           )
        createacc.pack()
        #creates label to let users know their details are wrong
        wrong1 = Label(text="Wrong username or password",
                       fg="red")
        wrong1.pack()
        #creates label for try again text
        wrong2 = Label(text="Try again",
                       fg="red")
        wrong2.pack()

        wrongusername.mainloop()
wrongusername(TRUE).wrongusernameGUI()





