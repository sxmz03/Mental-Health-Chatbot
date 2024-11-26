from tkinter import *


class phonenumber:
    #initilising
    def __init__(self, start = TRUE):
        self.start = start
        #creates window for GUI
        phonenumberpage = Tk()
        #changes title for window
        phonenumberpage.title("Therabuddy")

    def savenumber(self):
        #takes in phonenumber and gets rid of page and calls chatbot page
        global number
        number = phonenumberentry.get()
        phonenumberpage.destroy()
        import chatbot


    def phonenumberGUI(self):
        # creates banner at top of screen for name and logo
        banner = Label(text="Therabuddy",
                       width=50,
                       height=1,
                       bg="lightblue",
                       font="arial"
                       )
        banner.pack()

        # creates label that indicates to users what box to put phonenumber in
        phonenumbertxt = Label(text="Enter Carers Phonenumber:",
                               font="arial",
                               width=30
                               )
        phonenumbertxt.pack()

        # creates box for users to input their username into
        global phonenumberentry
        phonenumberentry = Entry(width=50,
                                 bg="ivory",
                                 )
        phonenumberentry.pack()

        # create button to enter in details
        enter = Button(text="Enter",
                       width=10,
                       bg="silver",
                       command= self.savenumber)
        enter.pack()

        phonenumberpage.mainloop()
phonenumber(TRUE).phonenumberGUI()