from tkinter import *


class loginpage:
    #initilising
    def __init__(self, start = TRUE):
        self.start = start
        global loginpage
        #creates window for the GUI
        loginpage = Tk()
        #changes the title of the window
        loginpage.title("Therabuddy")



    def login(self):
        # takes in username and password
        logusername = usernameentry.get()
        logpassword = passwordentry.get()
        check = logusername + logpassword + ","
        # textfile is checked for the users username and password
        file = open("usernameandpassword.txt", "r")
        # allows user to go to the chatbot
        for line in file:
            if check in line:
                loginpage.destroy()
                import phonenumber
            else:
                loginpage.destroy()
                import wrongusername
    def createaccount(self):
        #gets rid of window and calls createaccount page
        loginpage.destroy()
        import createaccount

    def loginGUI(self):
        # creates banner at top of screen for name and logo
        banner = Label(loginpage,text="Welcome to Therabuddy",
                       width=50,
                       height=1,
                       bg="lightblue",
                       font="arial"
                       )
        banner.pack()

        # creates label that indicates to users what box to put username in
        usernametxt = Label(loginpage,text="Username:",
                            font="arial",
                            width=30
                            )
        usernametxt.pack()

        # creates box for users to input their username into
        global usernameentry
        usernameentry = Entry(loginpage,width=50,
                              bg="ivory",
                              )
        usernameentry.pack()

        # creates label that indicates to users what box to put password in
        passwordtxt = Label(loginpage,text="Password:",
                            font="arial", )
        passwordtxt.pack()

        # creates box for users to input their password into
        global passwordentry
        passwordentry = Entry(loginpage,width=50,
                              bg="ivory")
        passwordentry.pack()

        # create button to enter in details
        enter = Button(loginpage,text="Enter",
                       width=10,
                       bg="silver",
                       command = self.login)
        enter.pack()
        # dividers

        # button that takes users to create account page
        createacc = Button(loginpage,text="Not got an account? Create one",
                           bg="silver",
                           command=self.createaccount

                           )
        createacc.pack()
        loginpage.mainloop()


loginpage(TRUE).loginGUI()





