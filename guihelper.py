'''
DATING APP PROJECT
MADE BY: ANANYA ROY
COLLEGE: GOVT. COLLEGE OF ENGINEERING AND TEXTILE TECHNOLOGY, SERAMPORE
MYWBUT REGISTRATION ID: TECHLWT190179
PROJECT SUBMITTED ON: 30/01/2020
'''


from tkinter import *
from tkinter import messagebox
from tkinter import PhotoImage


class GUI:
    '''A private constructor of class GUI'''
    def __init__(self, loginHandler, regHandler, updateHandler):
        self._lh = loginHandler
        self._rh = regHandler
        self._uh = updateHandler
        self._root = Tk()
        self._root.title("Tinder")
        self._root.configure(background="#FF315F")
        self._root.minsize(400, 600)
        self._root.maxsize(400, 600)
        self.loginWindow(loginHandler,regHandler)

        self._root.mainloop()

    '''A method to initialize instance variable self.loginResponse'''
    def setResponse(self,response):
        self.loginResponse = response

    '''A method which contains the GUI of Login Window'''
    def loginWindow(self,loginHandler, regHandler):
        self._label1 = Label(self._root, text="TINDER", font=("Copperplate", 30, "bold italic"), bg="#FF315F",
                             fg="#0B3572")
        self._label1.pack(pady=(20, 30),padx=(30,70))
        self._heartIcon = PhotoImage(file="images/heart1.png")
        self._labelHeart = Label(self._root,bg="#FF315F",image=self._heartIcon)
        self._labelHeart.place(x=270,y=25)

        self._label2 = Label(self._root, text="Email id", font=("Arial", 13), fg="#0B3572", bg="#FF315F")
        self._label2.pack(pady=(10, 10),padx=(18,82))
        self._emailIcon = PhotoImage(file="images/email.png")
        self._labelEmail = Label(self._root,bg="#FF315F",image=self._emailIcon)
        self._labelEmail.place(x=108,y=114)

        self._emailInput = Entry(self._root, font=("times", 11), fg="#1264DB")
        self._emailInput.pack(pady=(5, 20), ipady=3, ipadx=20)

        self._label3 = Label(self._root, text="Password", font=("Arial", 13), fg="#0B3572", bg="#FF315F")
        self._label3.pack(pady=(10, 10),padx=(20,80))
        self._passwordIcon = PhotoImage(file="images/password.png")
        self._labelPassword = Label(self._root,bg="#FF315F",image = self._passwordIcon)
        self._labelPassword.place(x=108,y=208)

        self._passwordInput = Entry(self._root, font=("times", 11), fg="#1264DB",show="*")
        self._passwordInput.pack(pady=(5, 20), ipady=3, ipadx=20)

        self._loginButton = Button(self._root, text="Login", font=("Copperplate", 13), bg="#0B3572", fg="white",
                                   command=lambda: loginHandler(self._emailInput.get(), self._passwordInput.get()))
        self._loginButton.pack(pady=(10, 10), ipadx=20, ipady=3)

        self._label4 = Label(self._root, text="Not a user?", font=("Arial", 11), fg="#0B3572", bg="#FF315F")
        self._label4.pack(pady=(30, 6))

        self._regButton = Button(self._root, text="Register", font=("Copperplate", 13), bg="#0B3572", fg="white",
                                 command=lambda: self.regWindow(regHandler))
        self._regButton.pack(pady=(10, 10), ipadx=20, ipady=3)

    '''A method which contains the GUI of Profile Window/Users Window'''
    def mainWindow(self,other, response, mode,num=0):
        self.clearScreen()
        self.createMenu(other,response)
        self.profileDetails(other,response,mode,num)
        if mode != 2:
            self._label0 = Label(self._root, text="MY PROFILE", font=("Copperplate", 25, "bold italic"), bg="#FF315F",
                                 fg="#0B3572")
            # self._label1.grid(row=0,column=0)
            self._label0.place(x=100, y=20)
        else:
            self._label0 = Label(self._root, text="USERS", font=("Copperplate", 25, "bold italic"), bg="#FF315F",
                                 fg="#0B3572")
            # self._label1.grid(row=0,column=0)
            self._label0.place(x=125, y=20)

    '''A method which displays profile details'''
    def profileDetails(self,other,response,mode,num):
        self.clearScreen()
        if mode == 0:
            self._label0 = Label(self._root, text="MY PROFILE", font=("Copperplate", 25, "bold italic"), bg="#FF315F",
                                 fg="#0B3572")
            # self._label1.grid(row=0,column=0)
            self._label0.place(x=100, y=20)
        elif mode==3:
            self._label0 = Label(self._root, text="MY PROPOSALS", font=("Copperplate", 25, "bold italic"), bg="#FF315F",
                                 fg="#0B3572")
            # self._label1.grid(row=0,column=0)
            self._label0.place(x=70, y=20)
        elif mode==4:
            self._label0 = Label(self._root, text="MY REQUESTS", font=("Copperplate", 25, "bold italic"), bg="#FF315F",
                                 fg="#0B3572")
            # self._label1.grid(row=0,column=0)
            self._label0.place(x=70, y=20)

        elif mode==5:
            self._label0 = Label(self._root, text="MY MATCHES", font=("Copperplate", 25, "bold italic"), bg="#FF315F",
                                 fg="#0B3572")
            # self._label1.grid(row=0,column=0)
            self._label0.place(x=90, y=20)

        self._label1 = Label(self._root, text="Name: ", font=("Arial", 13, "bold"), bg="#FF315F", fg="#0B3572")
        # self._label1.grid(row=0,column=0)
        self._label1.place(x=110, y=80)

        name = response[0][1]
        self._label2 = Label(self._root, text=name, font=("Arial", 13), fg="#0B3572", bg="#FF315F")
        self._label2.place(x=185, y=80)

        self._label3 = Label(self._root, text="Age: ", font=("Arial", 13, "bold"), bg="#FF315F", fg="#0B3572")
        self._label3.place(x=110, y=110)

        age = response[0][4]
        self._label4 = Label(self._root, text=str(age), font=("Arial", 13), fg="#0B3572", bg="#FF315F")
        self._label4.place(x=185, y=110)

        self._label5 = Label(self._root, text="Gender: ", font=("Arial", 13, "bold"), bg="#FF315F", fg="#0B3572")
        self._label5.place(x=110, y=140)

        gender = response[0][5]
        self._label6 = Label(self._root, text=gender, font=("Arial", 13), fg="#0B3572", bg="#FF315F")
        self._label6.place(x=185, y=140)

        self._label7 = Label(self._root, text="Lives in: ", font=("Arial", 13, "bold"), bg="#FF315F", fg="#0B3572")
        self._label7.place(x=110, y=170)

        lives_in = response[0][7]
        self._label8 = Label(self._root, text=lives_in, font=("Arial", 13), fg="#0B3572", bg="#FF315F")
        self._label8.place(x=185, y=170)

        self._label9 = Label(self._root, text="About: ", font=("Arial", 13, "bold"), bg="#FF315F", fg="#0B3572")
        self._label9.place(x=110, y=200)

        about = response[0][8]
        self._label10 = Label(self._root, text=about, font=("Arial", 13), fg="#0B3572", bg="#FF315F")
        self._label10.place(x=185, y=200)

        if mode == 2:
            btn1 = Button(self._root, text="Previous", bg="#0B3572", fg="white",
                          command=lambda: other.viewUsers(num - 1))
            # btn1.grid(row=3, column=0)
            btn1.place(x=110, y=240)
            btn2 = Button(self._root, text="Propose", bg="#0B3572", fg="white",
                          command=lambda: other.propose(response[0][0]))
            # btn2.grid(row=3, column=1)
            btn2.place(x=170, y=240)
            btn3 = Button(self._root, text="Next", bg="#0B3572", fg="white", command=lambda: other.viewUsers(num + 1))
            # btn3.grid(row=3, column=2)
            btn3.place(x=230, y=240)

        if mode==3:
            btn1 = Button(self._root, text="Previous", bg="#0B3572", fg="white",
                          command=lambda: other.proposalHandler(num - 1))
            # btn1.grid(row=3, column=0)
            btn1.place(x=110, y=240)

            btn3 = Button(self._root, text="Next", bg="#0B3572", fg="white", command=lambda: other.proposalHandler(num + 1))
            # btn3.grid(row=3, column=2)
            btn3.place(x=230, y=240)

        if mode==4:
            btn1 = Button(self._root, text="Previous", bg="#0B3572", fg="white",
                          command=lambda: other.requestHandler(num - 1))
            # btn1.grid(row=3, column=0)
            btn1.place(x=110, y=240)

            btn3 = Button(self._root, text="Next", bg="#0B3572", fg="white", command=lambda: other.requestHandler(num + 1))
            # btn3.grid(row=3, column=2)
            btn3.place(x=230, y=240)

        if mode==5:
            btn1 = Button(self._root, text="Previous", bg="#0B3572", fg="white",
                          command=lambda: other.matchHandler(num - 1))
            # btn1.grid(row=3, column=0)
            btn1.place(x=110, y=240)

            btn3 = Button(self._root, text="Next", bg="#0B3572", fg="white", command=lambda: other.matchHandler(num + 1))
            # btn3.grid(row=3, column=2)
            btn3.place(x=230, y=240)

    '''A method which displays a menu on top of the window'''
    def createMenu(self, other,response):
        menu = Menu(self._root)
        self._root.config(menu=menu)
        fileMenu = Menu(menu)
        menu.add_cascade(label="Home",menu=fileMenu)
        fileMenu.add_command(label="My Profile", command=lambda : self.profileDetails(other,self.loginResponse,0,0))
        fileMenu.add_command(label="Edit Profile", command=lambda :self.profileWindow(self._uh,menu,other))
        fileMenu.add_command(label="View Profile", command=lambda :other.viewUsers(0))
        fileMenu.add_command(label="LogOut", command=lambda :self.logout(menu))

        helpMenu = Menu(menu)
        menu.add_cascade(label="Proposals", menu=helpMenu)
        helpMenu.add_command(label="My Proposals", command=lambda : self.myProposals(other))
        helpMenu.add_command(label="My Requests", command=lambda : self.myRequests(other))
        helpMenu.add_command(label="My Matches", command=lambda : self.myMatches(other))

    '''A method which calls the requestHandler() method from tinder.py'''
    def myRequests(self,other):
        self.clearScreen()
        other.requestHandler(num=0)

    '''A method which calls the proposalHandler() method from tinder.py'''
    def myProposals(self,other):
        self.clearScreen()
        other.proposalHandler(num=0)

    '''A method which calls the matchHandler() method from tinder.py'''
    def myMatches(self,other):
        self.clearScreen()
        other.matchHandler(num=0)

    '''A method which takes you back to the login window'''
    def logout(self,menu):
        menu.delete(0,END)
        self.clearScreen()
        self.loginWindow(self._lh, self._rh)
        messagebox.showinfo("Logout Successful!", "You have successfully logged out")

    '''This method clears the screen'''
    def clearScreen(self):
        for i in self._root.pack_slaves():
            i.destroy()

        for i in self._root.grid_slaves():
            i.destroy()

        for i in self._root.place_slaves():
            i.destroy()

    '''This method contains the GUI for updating your profile'''
    def profileWindow(self, updateHandler,menu,other):
        self.clearScreen()
        self._label1 = Label(self._root, text="EDIT PROFILE", font=("Copperplate", 22, "bold italic"), bg="#FF315F", fg="#0B3572")
        self._label1.pack(pady=(14, 14))

        self._label2 = Label(self._root, text="Name: ")
        self._label2.configure(font=("Copperplate", 14, "bold"), bg="#FF315F", fg="#0B3572")
        # self._label2.place(x=110, y=135)
        self._label2.pack(pady=(24,1), padx=(20, 190))

        self._nameInput = Entry(self._root, font=("times", 10), fg="#1264DB")
        self._nameInput.insert(0,other.login_response[0][1])
        self._nameInput.place(x=190,y=95)

        self._label3 = Label(self._root, text="Email: ")
        self._label3.configure(font=("Copperplate", 14, "bold"), bg="#FF315F", fg="#0B3572")
        # self._label2.place(x=110, y=135)
        self._label3.pack(pady=(24,1), padx=(20, 190))

        self._emailInput = Entry(self._root, font=("times", 10), fg="#1264DB")
        self._emailInput.insert(0,other.login_response[0][2])
        self._emailInput.place(x=190,y=149)

        self._label4 = Label(self._root, text="Password: ")
        self._label4.configure(font=("Copperplate", 14, "bold"), bg="#FF315F", fg="#0B3572")
        # self._label2.place(x=110, y=135)
        self._label4.pack(pady=(24,1), padx=(45,174))

        self._passwordInput = Entry(self._root, font=("times", 10), fg="#1264DB")
        self._passwordInput.insert(0,other.login_response[0][3])
        self._passwordInput.place(x=190,y=202)

        self._label5 = Label(self._root, text="Age: ")
        self._label5.configure(font=("Copperplate", 14, "bold"), bg="#FF315F", fg="#0B3572")
        # self._label2.place(x=110, y=135)
        self._label5.pack(pady=(24,1), padx=(11, 194))

        self._ageInput = Entry(self._root, font=("times", 10), fg="#1264DB")
        self._ageInput.insert(0, other.login_response[0][4])
        self._ageInput.place(x=190,y=254)

        self._label6 = Label(self._root, text="Gender: ")
        self._label6.configure(font=("Copperplate", 14, "bold"), bg="#FF315F", fg="#0B3572")
        # self._label2.place(x=110, y=135)
        self._label6.pack(pady=(24, 1), padx=(30, 180))

        self._genderInput = Entry(self._root, font=("times", 10), fg="#1264DB")
        self._genderInput.insert(0, other.login_response[0][5])
        self._genderInput.place(x=190,y=308)

        self._label7 = Label(self._root, text="City: ")
        self._label7.configure(font=("Copperplate", 14, "bold"), bg="#FF315F", fg="#0B3572")
        # self._label2.place(x=110, y=135)
        self._label7.pack(pady=(24, 1), padx=(8, 190))

        self._cityInput = Entry(self._root, font=("times", 10), fg="#1264DB")
        self._cityInput.insert(0, other.login_response[0][7])
        self._cityInput.place(x=190,y=361)

        self._label8 = Label(self._root, text="About: ")
        self._label8.configure(font=("Copperplate", 14, "bold"), bg="#FF315F", fg="#0B3572")
        # self._label2.place(x=110, y=135)
        self._label8.pack(pady=(30, 6), padx=(20, 180))

        self._bioInput = Entry(self._root, font=("times", 10), fg="#1264DB")
        self._bioInput.insert(0, other.login_response[0][8])
        self._bioInput.place(x=190,y=421)

        self._updateButton = Button(self._root, text="Update", font=("times", 12, "bold"), width=15, bg="#0B3572", fg="white",
                                      command=lambda: updateHandler(self._nameInput.get(), self._emailInput.get(),
                                                                 self._passwordInput.get(), self._ageInput.get(),
                                                                 self._genderInput.get(), self._cityInput.get(),
                                                                 self._bioInput.get(),menu))
        self._updateButton.pack(pady=(40, 30))

    '''A method which contains the GUI for registration window'''
    def regWindow(self, regHandler):
        self._root1 = Tk()
        self._root1.minsize(400, 700)
        self._root1.maxsize(400, 700)
        self._root1.title("Register")
        self._root1.configure(background="#FF315F")

        self._label1 = Label(self._root1, text="TINDER")
        self._label1.configure(font=("Copperplate",30,"bold italic"), bg="#FF315F", fg="#0B3572")
        self._label1.pack(pady=(40, 40))

        self._label2 = Label(self._root1, text="Name ")
        self._label2.configure(font=("Copperplate", 14, "bold"), bg="#FF315F", fg="#0B3572")
        # self._label2.place(x=110, y=135)
        self._label2.pack(pady=(5, 5), padx=(0, 180))

        self._nameInput = Entry(self._root1, font=("times", 10),fg="#1264DB")
        self._nameInput.pack(pady=(10, 10), ipady=4, ipadx=50)

        self._label3 = Label(self._root1, text="Email ")
        self._label3.configure(font=("Copperplate", 14, "bold"), bg="#FF315F", fg="#0B3572")
        # self._label2.place(x=110, y=135)
        self._label3.pack(pady=(5, 5), padx=(0, 180))

        self.emailInput = Entry(self._root1, font=("times", 10),fg="#1264DB")
        self.emailInput.pack(pady=(10, 10), ipady=4, ipadx=50)

        self._label4 = Label(self._root1, text="Password ")
        self._label4.configure(font=("Copperplate", 14, "bold"), bg="#FF315F", fg="#0B3572")
        # self._label2.place(x=110, y=135)
        self._label4.pack(pady=(5, 5), padx=(30, 160))

        self.passwordInput = Entry(self._root1, font=("times", 10),fg="#1264DB")
        self.passwordInput.pack(pady=(10, 10), ipady=4, ipadx=50)

        self._ageInput = Entry(self._root1, font=("times", 10),fg="#1264DB")
        self._ageInput.insert(0, "Age")
        self._ageInput.pack(pady=(10, 25), ipady=4, ipadx=50)

        self._genderInput = Entry(self._root1, font=("times", 10),fg="#1264DB")
        self._genderInput.insert(0, "Gender")
        self._genderInput.pack(pady=(0, 25), ipady=4, ipadx=50)

        self._cityInput = Entry(self._root1, font=("times", 10),fg="#1264DB")
        self._cityInput.insert(0, "City")
        self._cityInput.pack(pady=(0, 25), ipady=4, ipadx=50)

        self._bioInput = Entry(self._root1, font=("times", 10),fg="#1264DB")
        self._bioInput.insert(0, "About")
        self._bioInput.pack(pady=(0, 20), ipady=4, ipadx=50)

        self._registerButton = Button(self._root1, text="Register", font=("times", 12, "bold"), width=15, bg="#0B3572", fg="white",
                                      command=lambda: regHandler(self._nameInput.get(), self.emailInput.get(),
                                                                 self.passwordInput.get(), self._ageInput.get(),
                                                                 self._genderInput.get(), self._cityInput.get(),
                                                                 self._bioInput.get()))
        self._registerButton.pack()
        self._root1.mainloop()
