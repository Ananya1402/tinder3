'''
DATING APP PROJECT
MADE BY: ANANYA ROY
COLLEGE: GOVT. COLLEGE OF ENGINEERING AND TEXTILE TECHNOLOGY, SERAMPORE
MYWBUT REGISTRATION ID: TECHLWT190179
PROJECT SUBMITTED ON:30/01/2020
'''
import dbhelper
import guihelper
from tkinter import messagebox

class Tinder(guihelper.GUI):    #this class inherits class GUI
    '''A private constructor of class DBHelper'''
    def __init__(self):
        self._dbObject = dbhelper.DBHelper()
        super().__init__(self.loginHandler, self.regHandler, self.updateHandler)

    '''This method updates the profile by sending the updated values to the database'''
    def updateHandler(self, name, email, password, age, gender, city, bio,menu):
        flag = self._dbObject.update("fname",name,"email",email,"password",password,"age",age,"gender",gender,"city",city,"bio",bio,"users",self._user_id)
        if flag==1:
            messagebox.showinfo("User info!","Updated successfully!")
        else:
            messagebox.showerror("Error!!","Cannot update!")
        menu.delete(0, guihelper.END)
        self.clearScreen()
        self.loginWindow(self.loginHandler,self.regHandler)

    '''This method sends the entered email id and password to the database to verify if the user is a registered user'''
    def loginHandler(self, email, password):
        self.login_response = self._dbObject.search("email",email,"password",password,"users")
        print(self.login_response)
        self.setResponse(self.login_response)
        if len(self.login_response)==0:
            messagebox.showerror("Invalid login!","You have entered wrong email id or password")
        else:
            print("Welcome user")
            self._user_id = self.login_response[0][0]
            self.doLogin(self.login_response)

    '''This method searches the database for the users whom you have proposed'''
    def proposalHandler(self,num):
        response = self._dbObject.search2("proposals", "romeo_id", self._user_id, "LIKE")
        if len(response)==0:
            messagebox.showinfo("User alert!","No proposals yet")
        else:
            if num < 0:
                messagebox.showinfo("User alert!", "No proposals before this")
            elif num >= len(response):
                messagebox.showinfo("User alert!", "No proposals after this")
            else:
                data = []
                x = response[num]
                data.append(x)
                print(data)
                response2 = self._dbObject.search2("users", "user_id", data[0][2], "LIKE")
                print(response2)
                self.profileDetails(self, response2, 3, num)

    '''This method searches the database for the users who have proposed you'''
    def requestHandler(self,num):
        response = self._dbObject.search2("proposals", "juliet_id", self._user_id, "LIKE")
        if len(response)==0:
            messagebox.showinfo("User alert!","No requests yet")
        else:
            if num < 0:
                messagebox.showinfo("User alert!", "No requests before this")
            elif num >= len(response):
                messagebox.showinfo("User alert!", "No requests after this")
            else:
                data = []
                x = response[num]
                data.append(x)
                print(data)
                response2 = self._dbObject.search2("users", "user_id", data[0][1], "LIKE")
                print(response2)
                self.profileDetails(self, response2, 4, num)

    '''This method searches the database for the users who have proposed you and whom you have proposed as well'''
    def matchHandler(self,num):
        response1 = self._dbObject.search2("proposals", "romeo_id", self._user_id, "LIKE")
        response2 = self._dbObject.search2("proposals", "juliet_id", self._user_id, "LIKE")
        #print(response1)
        #print(response2)
        response3=[]
        for i in response1:
            for j in response2:
                if i[2]==j[1] and i[1]==j[2]:
                    response3.append(j)
        #print(response3)
        if len(response3)==0:
            messagebox.showinfo("User alert!","No matches yet")
        else:
            if num < 0:
                messagebox.showinfo("User alert!", "No matches before this")
            elif num >= len(response3):
                messagebox.showinfo("User alert!", "No matches after this")
            else:
                data = []
                x = response3[num]
                data.append(x)
                print(data)
                response4 = self._dbObject.search2("users", "user_id", data[0][1], "LIKE")
                print(response4)
                self.profileDetails(self, response4, 5, num)

    '''A method which takes you to your profile window'''
    def doLogin(self,response):
        self.mainWindow(self, response, mode=1)

    '''A method which returns all the other users existing in Tinder'''
    def viewUsers(self,num):
        response = self._dbObject.search2("users","user_id",self._user_id,"NOT LIKE")
        if num<0:
            messagebox.showinfo("User alert!","No users before this")
        elif num>=len(response):
            messagebox.showinfo("User alert!","No users after this")
        else:
            data = []
            x = response[num]
            data.append(x)
            self.mainWindow(self, data, mode=2, num=num)

    '''Inserts a new row in the proposals table'''
    def propose(self,juliet_id):
        response = self._dbObject.search("romeo_id",self._user_id,"juliet_id",juliet_id,"proposals")
        if len(response) == 0:
            proposeDict = {"proposal_id":"NULL", "romeo_id":self._user_id, "juliet_id":juliet_id}
            flag = self._dbObject.insert(proposeDict, "proposals")
            if flag==1:
                messagebox.showinfo("User info","Your proposal has been sent successfully!")
            else:
                messagebox.showerror("Error!!","Your proposal cannot be sent")
        else:
            messagebox.showinfo("User alert!","You have already sent proposal to this user!")

    '''All the registration details that you have entered are stored in the users table by this method'''
    def regHandler(self, name, email, password, age, gender, city, bio):
        myDict = {"user_id":"NULL","fname":name,"email":email,"password":password,"age":age,"gender":gender,"bg":"Avatar.jpg","city":city,"bio":bio}
        flag = self._dbObject.insert(myDict,"users")
        if flag==1:
            messagebox.showinfo("User info!","Registered successfully!")
        else:
            messagebox.showerror("Error!!","Cannot register!")
        self._root1.destroy()

objTinder = Tinder()  #an object of class Tinder
