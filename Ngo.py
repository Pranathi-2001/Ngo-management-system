from tkinter import*
from PIL import ImageTk,Image
import loginCred
import os
import source
import FramesSource
import FramesVol
import tkinter.messagebox

path = "/Users/haasitapinnepu/Desktop/NMS/loginCred" #Replace with path to loginCred folder in your system

#DonorList = []
#VolList = []
#StuList = []

indP = path + "/IdIndex"

file = open(indP, "r")
DonorIndex = int(file.readline())
VolIndex = int(file.readline())
StuIndex = int(file.readline())
file.close()

class TopFrame(Frame):
    def __init__(self, master=NONE):
        Frame.__init__(self, master)
        Frame.__init__(self, master)
        self.master = master
        self.master.title("NGO Management System")
        self.master.geometry("450x275")
        self.master.configure(bg ='thistle3')
        self.configure(bg = 'LightGoldenrod2')
        self.pack()
        #self.grid(row=0,rowspan=2,columnspan=2,sticky=S+N+E+W)
        self.lab1 = Label(self,text="    LOGIN PAGE   ",padx=10,pady=5, bg = 'LightGoldenrod2')
        self.lab1.grid(row=0,column=1)  
        self.lab2 = Label(self,text="User id",padx=10,pady=5, bg = 'LightGoldenrod2')
        self.lab2.grid(row=1,column=0,padx=10,pady=5)
        self.text1 = Entry(self,width=15, bg = 'LightGoldenrod2')
        self.text1.grid(row=1,column=1)
        #self.canvas = Canvas(root, width = 300, height = 300)
        
        self.lab1 = Label(self,text="Password ",padx=10,pady=5, bg = 'LightGoldenrod2')
        self.lab1.grid(row=2,column=0,padx=10,pady=5)
        self.text2 = Entry(self,width=15,show="*", bg = 'LightGoldenrod2')
        self.text2.grid(row=2,column=1)  
        self.lab3 = Label(self,text="Login as",padx=10,pady=5, bg = 'LightGoldenrod2')
        self.lab3.grid(row=4,column=1,padx=10,pady=5)
      
        self.button3 =Button(self,text="Donor",width=12,height=1,command = self.login_verify_Donor, highlightbackground = 'LightGoldenrod2')
        self.button3.grid(row=5,column=0)
        
        self.button2 =Button(self,text="volunteer",width=12,height=1, command = self.login_verify_Volunteer, highlightbackground = 'LightGoldenrod2')
        self.button2.grid(row=5,column=1)
        
        self.button1 =Button(self,text="Manager",width=12,height=1, command = self.login_verify_Manager, highlightbackground = 'LightGoldenrod2')
        self.button1.grid(row=5,column=2)

        self.button =Button(self,text="Register as Donor",width=15,height=1, command = self.RegiDonor, highlightbackground = 'LightGoldenrod2')
        self.button.grid(row=6,column=1)

    def login_verify_Manager(self):
        if(self.text1.get()==''):
            return tkinter.messagebox.showwarning('Message','Invalid Input')
        
        if(self.text2.get()==''):
            return tkinter.messagebox.showwarning('Message','Invalid Input')
        self.username1 = self.text1.get()
        self.password1 = self.text2.get()

        self.text1.delete(0,END)
        self.text2.delete(0,END)
        '''
        self.username1 = self.text1.get("1.0", "end-1c")
        self.password1 = self.text2.get()

        self.text1.delete("1.0", "end-1c")
        self.text2.delete(0, 'end')
        #print(self.username1)
        '''

        list_of_files = os.listdir(path)
        if self.username1 in list_of_files:
            pathFile = path + "/" + self.username1
            file1 = open(pathFile, "r")
            verify = file1.read().splitlines()
            if self.password1 in verify:
                root2 = Tk()
                app1 = Manager(root2)
                root2.mainloop()
 
            else:
                self.password_not_recognised()
 
        else:
            self.user_not_found()

    def login_verify_Donor(self):
        if(self.text1.get()==''):
            return tkinter.messagebox.showwarning('Message','Invalid Input')
        
        if(self.text2.get()==''):
            return tkinter.messagebox.showwarning('Message','Invalid Input')
        self.username2 = self.text1.get()
        self.password2 = self.text2.get()

        self.text1.delete(0,END)
        self.text2.delete(0,END)
        '''
        self.username2 = self.text1.get("1.0", "end-1c")
        self.password2 = self.text2.get("1.0", "end-1c")

        self.text1.delete("1.0", "end-1c")
        self.text2.delete("1.0", "end-1c")
        #print(self.username1)
        '''

        path2 = path + "/Donors"
        list_of_files = os.listdir(path2)
        #print(list_of_files)
        if self.username2 in list_of_files:
            pathFile = path2 + "/" + self.username2
            file1 = open(pathFile, "r")
            verify = file1.read().splitlines()
            if self.password2 in verify:
                root4 = Tk()
                app4 = PledgeDonor(root4, self.username2)
                root4.mainloop()
 
            else:
                self.password_not_recognised()
 
        else:
            self.user_not_found()

    def login_verify_Volunteer(self):
        if(self.text1.get()==''):
            return tkinter.messagebox.showwarning('Message','Invalid Input')
        
        if(self.text2.get()==''):
            return tkinter.messagebox.showwarning('Message','Invalid Input')
        self.username3 = self.text1.get()
        self.password3 = self.text2.get()

        self.text1.delete(0,END)
        self.text2.delete(0,END)
        '''
        self.username3 = self.text1.get("1.0", "end-1c")
        self.password3 = self.text2.get("1.0", "end-1c")

        self.text1.delete("1.0", "end-1c")
        self.text2.delete("1.0", "end-1c")
        #print(self.username1)
        '''

        path3 = path + "/volunteers"
        list_of_files = os.listdir(path3)
        #print(list_of_files)
        if self.username3 in list_of_files:
            pathFile = path3 + "/" + self.username3
            file1 = open(pathFile, "r")
            verify = file1.read().splitlines()
            if self.password3 in verify:
                root5 = Tk()
                app5 = Volunteer(root5)
                root5.mainloop()
 
            else:
                self.password_not_recognised()
 
        else:
            self.user_not_found()
    
    def RegiDonor(self):
        root3 = Tk()
        app2 = RegDonor(root3)
        root3.mainloop()

    def login_sucess(self):
        self.login_success_screen = Tk()
        self.login_success_screen.title("Success")
        self.login_success_screen.geometry("150x100")
        Label(self.login_success_screen, text="Login Success").pack()
        Button(self.login_success_screen, text="OK", command = self.login_success_screen.destroy).pack()
        self.login_success_screen.mainloop()
    
    def password_not_recognised(self):
        self.password_not_recog_screen = Tk()
        self.password_not_recog_screen.title("Error")
        self.password_not_recog_screen.geometry("150x100")
        Label(self.password_not_recog_screen, text="Invalid Password ").pack()
        Button(self.password_not_recog_screen, text="OK", command=self.password_not_recog_screen.destroy).pack()
        self.password_not_recog_screen.mainloop()

    def user_not_found(self):
        self.user_not_found_screen = Tk()
        self.user_not_found_screen.title("Error")
        self.user_not_found_screen.geometry("150x100")
        Label(self.user_not_found_screen, text="User Not Found").pack()
        Button(self.user_not_found_screen, text="OK", command=self.user_not_found_screen.destroy).pack()
        self.user_not_found_screen.mainloop()


class RegDonor(Frame):
    def __init__(self, master=NONE):
        Frame.__init__(self, master)
        self.master = master
        self.master.title("Donor Registration")
        self.master.geometry("450x525")
        self.master.configure(bg ='thistle3')
        self.configure(bg = 'LightGoldenrod2')
        self.pack()
        #self.grid(row=0,rowspan=2,columnspan=2,sticky=S+N+E+W)
        
        self.lab1 = Label(self,text="Enter the Details",padx=10,pady=5, bg = 'LightGoldenrod2')
        self.lab1.grid(row=0,column=1)
        
        self.lab1 = Label(self,text="Name",padx=10,pady=5, bg = 'LightGoldenrod2')
        self.lab1.grid(row=1,column=0)
        
        self.text1 = Entry(self,width=10 ,bg = 'LightGoldenrod2')
        self.text1.grid(row=1,column=1,padx=10,pady=15)
        
        #self.lab2 = Label(self,text="Date of Birth",padx=10,pady=5)
        #self.lab2.grid(row=2,column=0)
        
        #self.text2 = Text(self,width=10,height=1,padx=10,pady=5)
        #self.text2.grid(row=2,column=1,padx=10,pady=15)
        
        self.lab3 = Label(self,text="Email",padx=10,pady=5, bg = 'LightGoldenrod2')
        self.lab3.grid(row=3,column=0)
        
        self.text3 = Entry(self,width=10 ,bg = 'LightGoldenrod2')
        self.text3.grid(row=3,column=1,padx=10,pady=15)
        
        self.lab4 = Label(self,text="Password",padx=10,pady=5, bg = 'LightGoldenrod2')
        self.lab4.grid(row=4,column=0)
        
        self.text4 = Entry(self,width=10,show="*" ,bg = 'LightGoldenrod2')
        self.text4.grid(row=4,column=1,padx=10,pady=15)
        
        self.lab5 = Label(self,text="Confirm Password",padx=10,pady=5, bg = 'LightGoldenrod2')
        self.lab5.grid(row=5,column=0)
        
        self.text5 = Entry(self,width=10,show="*" ,bg = 'LightGoldenrod2')
        self.text5.grid(row=5,column=1,padx=10,pady=15)
        
        self.lab6 = Label(self,text="Phone no",padx=10,pady=5, bg = 'LightGoldenrod2')
        self.lab6.grid(row=6,column=0)
        
        self.text6 = Entry(self,width=10 ,bg = 'LightGoldenrod2')
        self.text6.grid(row=6,column=1,padx=10,pady=15)
        
        self.lab7 = Label(self,text="Address",padx=10,pady=5, bg = 'LightGoldenrod2')
        self.lab7.grid(row=7,column=0,padx=10)
        
        self.text7 = Text(self,width=20,height=3,padx=10,pady=5, bg = 'LightGoldenrod2')
        self.text7.grid(row=7,column=1,padx=10,pady=15)
        
        self.lab8 = Label(self,text="Pledged amount",padx=10,pady=5, bg = 'LightGoldenrod2')
        self.lab8.grid(row=9,column=0)
        
        self.text8 = Entry(self,width=10 ,bg = 'LightGoldenrod2')
        self.text8.grid(row=9,column=1,padx=10,pady=15)
        
        self.lab9 = Label(self,text="Donation Plan",padx=10,pady=5, bg = 'LightGoldenrod2')
        self.lab9.grid(row=10,column=0)
        
        self.options = ["Semi_Annually", "Annually"]
        self.clicked = StringVar()
        self.clicked.set("Semi_Annually")
            
        self.drop = OptionMenu(self, self.clicked, *self.options)
        self.drop.config(bg = 'LightGoldenrod2')
        self.drop.grid(row=10,column=1)

        self.button1 =Button(self,text="Register",width=10,height=3,padx=5,pady=5, command = self.RegisterDonor, highlightbackground = 'LightGoldenrod2')
        self.button1.grid(row=5,column=2)

    def RegisterDonor(self):
        

        '''
        if (self.text1.get("1.0","end-1c")=='' or self.text3.get("1.0","end-1c")==''or 
        self.text4.get("1.0","end-1c")==''or self.text5.get("1.0","end-1c")==''or 
        self.text6.get("1.0","end-1c")==''or self.text7.get("1.0","end-1c")=='' or self.text8.get("1.0","end-1c")==''):
           return self.FailScreen()

        password1 = self.text4.get("1.0", "end-1c")
        passwordConfirm1 = self.text5.get("1.0", "end-1c")

        if(password1 == passwordConfirm1):
            self.DonorBabe = source.PledgedDonor()
            self.DonorBabe.name = self.text1.get("1.0", "end-1c")
            self.conc1 = source.Contact()
            self.conc1.email = self.text3.get("1.0", "end-1c")
            self.conc1.phone = self.text6.get("1.0", "end-1c")
            self.conc1.address = self.text7.get("1.0", "end-1c")
            self.DonorBabe.contact = self.conc1
            self.DonorBabe.amount = self.text8.get("1.0", "end-1c")
            self.DonorBabe.donationPlan = self.clicked.get()
            self.DonorBabe.password = password1
        '''
        if((self.text1.get().isalpha())==False or self.text1.get()==''):
            return tkinter.messagebox.showwarning('Message','Invalid Input')
        if(self.text3.get()==''):
            return tkinter.messagebox.showwarning('Message','Invalid Input')
        if(self.text4.get()==''):
            return tkinter.messagebox.showwarning('Message','Invalid Input')
        if(self.text5.get()==''):
            return tkinter.messagebox.showwarning('Message','Invalid Input')
        if((self.text6.get().isdigit())==False or self.text6.get()==''):
            return tkinter.messagebox.showwarning('Message','Invalid Input')
        if((self.text8.get().isdigit())==False or self.text8.get()==''):
            return tkinter.messagebox.showwarning('Message','Invalid Input')
       
        password1 = self.text4.get()
        passwordConfirm1 = self.text5.get()

        if(password1 == passwordConfirm1):
            self.DonorBabe = source.PledgedDonor()
            self.DonorBabe.name = self.text1.get()
            self.conc1 = source.Contact()
            self.conc1.email = self.text3.get()
            self.conc1.phone = self.text6.get()
            self.conc1.address = self.text7.get("1.0", "end-1c")
            self.DonorBabe.contact = self.conc1
            self.DonorBabe.amount = self.text8.get()
            self.DonorBabe.donationPlan = self.clicked.get()
            self.DonorBabe.password = password1

            global DonorIndex
            DonorIndex = DonorIndex + 1
            ID = "D0" + str(DonorIndex)
            print(ID)
            self.DonorBabe.id = ID

            #DonorList.insert(ID, self.DonorBabe)

            pathFile = path + "/Donors/" + ID

            self.DonorBabe.UpdateFile(pathFile)
            self.DonorRegSuccess()
        
        else:
            self.password_not_recog_screen = Tk()
            self.password_not_recog_screen.title("Error")
            self.password_not_recog_screen.geometry("150x100")
            Label(self.password_not_recog_screen, text="Confirm Password not same").pack()
            Button(self.password_not_recog_screen, text="OK", command=self.password_not_recog_screen.destroy).pack()
            self.password_not_recog_screen.mainloop()
    
    def DonorRegSuccess(self):
        self.success_screen = Tk()
        self.success_screen.title("Success")
        self.success_screen.geometry("150x100")
        Label(self.success_screen, text="Donor Registration Success").pack()
        Label(self.success_screen, text="ID: " + self.DonorBabe.id).pack()
        Button(self.success_screen, text="OK", command = self.success_screen.destroy).pack()
        self.success_screen.mainloop()
    
    def FailScreen(self):
        self.success_screen = Tk()
        self.success_screen.title("ERROR")
        self.success_screen.geometry("150x100")
        Label(self.success_screen, text="INVALID INPUT").pack()
        #Label(self.success_screen, text="ID: " + self.StudMan.id).pack()
        Button(self.success_screen, text="OK", command = self.success_screen.destroy).pack()
        self.success_screen.mainloop()

class Manager(Frame):
    def __init__(self, master=NONE):
        Frame.__init__(self, master)
        self.master = master
        self.master.title("Manager Login")
        self.master.geometry("550x350")
        self.master.configure(bg ='thistle3')
        self.configure(bg = 'LightGoldenrod2')
        self.pack()
        #self.grid(sticky=S+N+E+W)
        
        self.button1=Button(self,text="Logout",relief=FLAT,width=7,height=1, command = self.master.destroy, highlightbackground = 'LightGoldenrod2')
        self.button1.grid(row=4,column=1,ipadx=5,padx=15,pady=10)
        
        self.button=Button(self,text="Register Volunteer",relief=FLAT,width=12,height=1, command = self.RegVol, highlightbackground = 'LightGoldenrod2')
        self.button.grid(row=1,column=0,ipadx=10,padx=15,pady=10)
        
        self.button=Button(self,text="Notify donors",relief=FLAT,width=9,height=1, command = self.notifyDonors, highlightbackground = 'LightGoldenrod2')
        self.button.grid(row=3,column=1,ipadx=5,padx=15,pady=10)
        
        self.button=Button(self,text="Initiate Help",relief=FLAT,width=9,height=1, command = self.initiateHelp, highlightbackground = 'LightGoldenrod2')
        self.button.grid(row=1,column=2,ipadx=5,padx=15,pady=10)
        
        self.button=Button(self,text="Check Records",relief=FLAT,width=10,height=1, command = self.CheckRecords, highlightbackground = 'LightGoldenrod2')
        self.button.grid(row=2,column=0,ipadx=5,padx=15,pady=10)
        
        self.button=Button(self,text="Remove Volunteer",relief=FLAT,width=12,height=1, command = self.remVol, highlightbackground = 'LightGoldenrod2')
        self.button.grid(row=2,column=2,ipadx=10,padx=15,pady=10)
    
    def RegVol(self):
        rootV = Tk()
        appV =FramesSource.RegVolunteer(rootV)
        rootV.mainloop()
    
    def remVol(self):
        root3 = Tk()
        app2 = FramesSource.RemoveVol(root3)
        root3.mainloop()
    
    def CheckRecords(self):
        self.button=Button(self,text="Check Funds",relief=FLAT,width=9,height=1, command = self.checkfunds, highlightbackground = 'LightGoldenrod2')
        self.button.grid(row=5,column=0,ipadx=5,padx=15,pady=10)

        self.button=Button(self,text="Students List",relief=FLAT,width=9,height=1, command = self.checkStudents, highlightbackground = 'LightGoldenrod2')
        self.button.grid(row=5,column=2,ipadx=5,padx=15,pady=10)

        self.button=Button(self,text="Volunteers List",relief=FLAT,width=9,height=1, command = self.checkvolunteers, highlightbackground = 'LightGoldenrod2')
        self.button.grid(row=6,column=0,ipadx=5,padx=15,pady=10)

        self.button=Button(self,text="Donors List",relief=FLAT,width=9,height=1, command= self.checkdonors, highlightbackground = 'LightGoldenrod2')
        self.button.grid(row=6,column=2,ipadx=5,padx=15,pady=10)

    def checkStudents(self):
        root5 = Tk()
        app6 = FramesSource.CheckStudents(root5)
        root5.mainloop()
    
    def checkfunds(self):
        root6 = Tk()
        app = FramesSource.CheckFunds(root6)
        root6.mainloop()
    
    def checkvolunteers(self):
        root2 = Tk()
        app4 = FramesSource.CheckVolunteer(root2)
        root2.mainloop()
    
    def checkdonors(self):
        root2 = Tk()
        app4 = FramesSource.CheckDonors(root2)
        root2.mainloop()
    
    def notifyDonors(self):
        root2 = Tk()
        app4 = FramesSource.CheckDonors(root2)
        root2.mainloop()
    
    def initiateHelp(self):
        root2 = Tk()
        app4 = FramesSource.Initiate_Help(root2)
        root2.mainloop()
                        

class Volunteer(Frame):
    #add scroll bar make two frames (left and right)
    def __init__(self, master=NONE):
        Frame.__init__(self, master)
        self.master = master
        self.master.title("Volunteer Login")
        self.master.geometry("500x200")
        self.master.configure(bg ='thistle3')
        self.configure(bg = 'LightGoldenrod2')
        self.pack()
        #self.grid(row=0,rowspan=2,columnspan=2,sticky=S+N+E+W)
        
        self.button1=Button(self,text="Logout",relief=FLAT,width=7,height=1, command = self.master.destroy, highlightbackground = 'LightGoldenrod2')
        self.button1.grid(row=2,column=1,ipadx=5,padx=15,pady=10)
        
        self.button=Button(self,text="Register Student",relief=FLAT,width=12,height=1, command = self.RegStud, highlightbackground = 'LightGoldenrod2')
        self.button.grid(row=1,column=0,ipadx=10,padx=15,pady=10)
        
        self.button=Button(self,text="Set Price",relief=FLAT,width=9,height=1, command = self.setPrices, highlightbackground = 'LightGoldenrod2')
        self.button.grid(row=0,column=2,ipadx=5,padx=15,pady=10)
        
        self.button=Button(self,text="Minor Donation",relief=FLAT,width=9,height=1, command = self.getMinor, highlightbackground = 'LightGoldenrod2')
        self.button.grid(row=0,column=0,ipadx=5,padx=15,pady=10)
        
        #self.button=Button(self,text="Give Help",relief=FLAT,width=10,height=1)
        #self.button.grid(row=0,column=4,ipadx=5,padx=15,pady=10)
        
        self.button=Button(self,text="Update Profile",relief=FLAT,width=12,height=1, command = self.updatepp, highlightbackground = 'LightGoldenrod2')
        self.button.grid(row=1,column=2,ipadx=10,padx=15,pady=10)

    def RegStud(self):
        rootS = Tk()
        appS = FramesVol.RegStudent(rootS)
        rootS.mainloop()

    def setPrices(self):
        rootS = Tk()
        appS = FramesVol.SetPrice(rootS)
        rootS.mainloop()
    
    def getMinor(self):
        rootS = Tk()
        appS = FramesVol.MinorDonation(rootS)
        rootS.mainloop()
    
    def updatepp(self):
        rootS = Tk()
        appS = FramesVol.UpdateProfile(rootS)
        rootS.mainloop()

class PledgeDonor(Frame):
    def __init__(self, master=NONE, donorID = " "):
            Frame.__init__(self, master)
            self.master = master
            self.master.title("Donor Login")
            self.master.geometry("450x300")
            self.master.configure(bg ='thistle3')
            self.configure(bg = 'LightGoldenrod2')
            self.pack()
            #self.grid(row=0,rowspan=2,columnspan=2,sticky=S+N+E+W)
            self.donorId = donorID
            
            self.button=Button(self,text="Logout",width=7,height=1, command = self.master.destroy, highlightbackground = 'LightGoldenrod2')
            self.button.grid(row=0,column=0,ipadx=5,padx=5,pady=10)
            
            self.lab1 = Label(self,text="Update Donation",padx=10,pady=5, bg = 'LightGoldenrod2')
            self.lab1.grid(row=1,column=1)
            
            self.lab2 = Label(self,text="Donation Amount",padx=10,pady=5, bg = 'LightGoldenrod2')
            self.lab2.grid(row=2,column=0)
            
            self.text1 = Text(self,width=10,height=1,padx=10,pady=5, bg = 'LightGoldenrod2')
            self.text1.grid(row=2,column=1,padx=10,pady=15)
            
            '''
            self.lab3 = Label(self,text="Phone no:",padx=10,pady=5)
            self.lab3.grid(row=3,column=0)
            
            self.text2 = Text(self,width=10,height=1,padx=10,pady=5)
            self.text2.grid(row=3,column=1,padx=10,pady=15)
            '''
            
            self.lab4 = Label(self,text="Change Plan",padx=10,pady=5, bg = 'LightGoldenrod2')
            self.lab4.grid(row=4,column=0)
            
            self.options = ["Semi_Annually", "Annually"]
            self.clicked = StringVar()
            self.clicked.set("Semi_Annually")
            
            self.drop = OptionMenu(self, self.clicked, *self.options)
            self.drop.config(bg = 'LightGoldenrod2')
            self.drop.grid(row=4,column=1)
            
            self.button=Button(self,text="Update",width=7,height=1, command = self.UpdateButton, highlightbackground = 'LightGoldenrod2')
            self.button.grid(row=5,column=1,ipadx=5,padx=5,pady=10)

            self.pathNew = path + "/Donors/" + str(self.donorId)

            self.donBro = source.PledgedDonor()
            self.donBro.ExtractData(self.pathNew)

            if self.donBro.notified == 1:
                if self.donBro.donated == 0:
                    self.button2=Button(self,text="Donate",width=7,height=1, command = self.DonateButton, highlightbackground = 'LightGoldenrod2')
                    self.button2.grid(row=6,column=1,ipadx=5,padx=5,pady=10)
                
                elif self.donBro.donationPlan == "Semi_Annually":
                    if self.donBro.donated == 1:
                        self.button2=Button(self,text="Donate",width=7,height=1, command = self.DonateButton, highlightbackground = 'LightGoldenrod2')
                        self.button2.grid(row=6,column=1,ipadx=5,padx=5,pady=10)
                
                
    
    def UpdateButton(self):
        donAmountNew = self.text1.get("1.0", "end-1c")
        newPlan = self.clicked.get()

        self.donBro.amount = donAmountNew
        self.donBro.donationPlan = newPlan
        
        self.donBro.UpdateFile(self.pathNew)
        self.UpSucess()
    
    def UpSucess(self):
        self.success_screen = Tk()
        self.success_screen.title("Success")
        self.success_screen.geometry("150x100")
        Label(self.success_screen, text="Update Success").pack()
        Button(self.success_screen, text="OK", command = self.success_screen.destroy).pack()
        self.success_screen.mainloop()

    def DonateButton(self):
        fundsUp = source.Funds()
        pathF = path + "/Inventory/f"
        fundsUp.ExtractFunds(pathF)

        fundsUp.funds = fundsUp.funds + self.donBro.amount
        fundsUp.UpdateFunds(pathF)
        self.donBro.donated = self.donBro.donated + 1
        self.donBro.UpdateFile(self.pathNew)
        self.button2.destroy()
        self.DonSucess()

    def DonSucess(self):
        self.success_screen = Tk()
        self.success_screen.title("Success")
        self.success_screen.geometry("150x100")
        Label(self.success_screen, text="Donated Successfully").pack()
        Label(self.success_screen, text="Thank you " + self.donBro.name).pack()
        Button(self.success_screen, text="OK", command = self.success_screen.destroy).pack()
        self.success_screen.mainloop()


        
def UpdateIndexF():
    file1 = open(indP, "w")
    file1.write(str(DonorIndex) + "\n")
    file1.write(str(VolIndex) + "\n")
    file1.write(str(StuIndex) + "\n")
    file1.close()      
        
def main():
    root=Tk()
    app=  TopFrame(root)
    root.mainloop()

    UpdateIndexF()


if __name__ == '__main__':
    main()