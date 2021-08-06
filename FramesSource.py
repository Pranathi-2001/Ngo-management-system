from tkinter import*
from PIL import ImageTk, Image
import loginCred
import os
import source
#import FramesVol
import operator
import tkinter.messagebox

# Replace with path to loginCred folder in your system
path = "/User/D G Pranathi/Desktop/NMS/loginCred"
#StudList = []
indP = path + "/IdIndex"

file = open(indP, "r")
DonorIndex = int(file.readline())
VolIndex = int(file.readline())
StuIndex = int(file.readline())
file.close()


class RegVolunteer(Frame):
    # add scroll bar make two frames (left and right)
    '''
    def __init__(self, master=NONE):
        Frame.__init__(self, master)
        self.master = master
        self.master.title("Register volunteer")
        self.master.geometry("450x550")
        self.master.configure(bg ='thistle3')
        self.configure(bg = 'LightGoldenrod2')
        self.pack()
        #self.grid(row=0, rowspan=2, columnspan=2, sticky=S+N+E+W)

        #self.lab0 = Label(self, text="Register volunteer", padx=10, pady=5, bg = 'LightGoldenrod2')
        #self.lab0.grid(row=1, column=1)

        self.lab = Label(self, text="Basic info", padx=10, pady=5, bg = 'LightGoldenrod2')
        self.lab.grid(row=2, column=1)

        self.lab1 = Label(self, text="Name", padx=10, pady=5, bg = 'LightGoldenrod2')
        self.lab1.grid(row=3, column=0)

        self.text1 = Text(self, width=10, height=1, padx=10, pady=5, bg = 'LightGoldenrod2')
        self.text1.grid(row=3, column=1, padx=10, pady=15)

        self.lab2 = Label(self, text="Date of Birth", padx=10, pady=5, bg = 'LightGoldenrod2')
        self.lab2.grid(row=4, column=0)

        self.text2 = Text(self, width=10, height=1, padx=10, pady=5, bg = 'LightGoldenrod2')
        self.text2.grid(row=4, column=1, padx=10, pady=15)

        self.lab4 = Label(self, text="Email id", padx=10, pady=5, bg = 'LightGoldenrod2')
        self.lab4.grid(row=6, column=0)

        self.text4 = Text(self, width=10, height=1, padx=10, pady=5, bg = 'LightGoldenrod2')
        self.text4.grid(row=6, column=1, padx=10, pady=15)

        self.lab5 = Label(self, text="Password", padx=10, pady=5, bg = 'LightGoldenrod2')
        self.lab5.grid(row=7, column=0)

        self.text5 = Text(self, width=10, height=1, padx=10, pady=5, bg = 'LightGoldenrod2')
        self.text5.grid(row=7, column=1)

        self.lab6 = Label(self, text="Confirm Password", padx=10, pady=5, bg = 'LightGoldenrod2')
        self.lab6.grid(row=8, column=0)

        self.text6 = Text(self, width=10, height=1, padx=10, pady=5, bg = 'LightGoldenrod2')
        self.text6.grid(row=8, column=1, padx=10, pady=15)

        self.lab7 = Label(self, text="Address", padx=10, pady=5, bg = 'LightGoldenrod2')
        self.lab7.grid(row=9, column=0, padx=10)

        self.text7 = Text(self, width=20, height=3, padx=10, pady=5, bg = 'LightGoldenrod2')
        self.text7.grid(row=9, column=1, padx=10, pady=15)

        self.lab9 = Label(self, text="Phone no", padx=10, pady=5, bg = 'LightGoldenrod2')
        self.lab9.grid(row=12, column=0)

        self.text9 = Text(self, width=10, height=1, padx=10, pady=5, bg = 'LightGoldenrod2')
        self.text9.grid(row=12, column=1, padx=10, pady=15)

        self.button = Button(self, text="Register", width=7,
                             height=1, command=self.RegVol, highlightbackground = 'LightGoldenrod2')
        self.button.grid(row=18, column=1, ipadx=5, padx=5, pady=10)

        self.lab14 = Label(self, text="*min time is 10 hrs per week*", bg = 'LightGoldenrod2')
        self.lab14.grid(row=19, column=0)
    '''

    def __init__(self, master=NONE):
        Frame.__init__(self, master)
        self.master = master
        self.master.title("Register volunteer")
        self.master.geometry("450x550")
        self.master.configure(bg ='thistle3')
        self.configure(bg = 'LightGoldenrod2')
        self.pack()
        
        #self.lab0 = Label(self,text="Register volunteer",padx=10,pady=5, bg = 'LightGoldenrod2')
        #self.lab0.grid(row=1,column=1)
        
        self.lab = Label(self,text="Basic info",padx=10,pady=5, bg = 'LightGoldenrod2')
        self.lab.grid(row=2,column=1)
        
        self.lab1 = Label(self,text="Name",padx=10,pady=5, bg = 'LightGoldenrod2')
        self.lab1.grid(row=3,column=0)
        
        self.text1 = Entry(self,width=10, bg = 'LightGoldenrod2')
        self.text1.grid(row=3,column=1,padx=10,pady=15)
        
        '''
        self.lab2 = Label(self,text="Date of Birth",padx=10,pady=5)
        self.lab2.grid(row=4,column=0)
        
        self.text2 =  Entry(self,width=10)
        self.text2.grid(row=4,column=1,padx=10,pady=15)
        '''
        
        self.lab4 = Label(self,text="Email id",padx=10,pady=5, bg = 'LightGoldenrod2')
        self.lab4.grid(row=6,column=0)
        
        self.text4 =  Entry(self,width=10, bg = 'LightGoldenrod2')
        self.text4.grid(row=6,column=1,padx=10,pady=15)
        
        self.lab5 = Label(self,text="Password",padx=10,pady=5, bg = 'LightGoldenrod2')
        self.lab5.grid(row=7,column=0)
        
        self.text5 =  Entry(self,width=10,show="*", bg = 'LightGoldenrod2')
        self.text5.grid(row=7,column=1,padx=10,pady=15)
        
        self.lab6 = Label(self,text="Confirm Password",padx=10,pady=5, bg = 'LightGoldenrod2')
        self.lab6.grid(row=8,column=0)
        
        self.text6 =  Entry(self,width=10,show="*", bg = 'LightGoldenrod2')
        self.text6.grid(row=8,column=1,padx=10,pady=15)
        
        self.lab7 = Label(self,text="Address",padx=10,pady=5, bg = 'LightGoldenrod2')
        self.lab7.grid(row=9,column=0,padx=10)
        
        self.text7 = Text(self,width=20,height=3,padx=10,pady=5, bg = 'LightGoldenrod2')
        self.text7.grid(row=9,column=1,padx=10,pady=15)
        
        self.lab9 = Label(self,text="Phone no",padx=10,pady=5, bg = 'LightGoldenrod2')
        self.lab9.grid(row=12,column=0)
        
        self.text9 = Entry(self,width=10, bg = 'LightGoldenrod2')
        self.text9.grid(row=12,column=1,padx=10,pady=15)
        
        self.button=Button(self,text="Register",width=7,height=1, command = self.RegVol, highlightbackground = 'LightGoldenrod2')
        self.button.grid(row=18,column=1,ipadx=5,padx=5,pady=10)
        
        self.lab14=Label(self,text="*min time is 10 hrs per week", bg = 'LightGoldenrod2')
        self.lab14.grid(row=19,column=0)

    def RegVol(self):

        #pattern = r'(19|20)\d\d[- /.](0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])'
        #match = re.search(pattern,self.text2.get())
        #if match==None:
            #return self.FailScreen()
        '''
        if((self.text1.get().isalpha())==False or self.text1.get()==''):
            return self.FailScreen()
        
        if((self.text4.get().isalpha())==False or self.text4.get()==''):
            return self.FailScreen()

        if((self.text5.get().isalpha())==False or self.text5.get()==''):
            return self.FailScreen()

        if((self.text6.get().isalpha())==False or self.text6.get()==''):
            return self.FailScreen()

        if((self.text9.get().isdigit())==False or self.text9.get()==''):
            return self.FailScreen()
        

        if (self.text1.get()=='' or 
        self.text4.get()==''or self.text6.get()==''or 
        self.text5.get()==''or self.text7.get("1.0","end-1c")=='' or 
        self.text9.get()==''):
           return self.FailScreen()
        
       
        pattern = r'(19|20)\d\d[- /.](0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])'
        match = re.search(pattern,self.text2.get())
        if match==None:
            return messagebox.showwarning('Message','Invalid Input')
        '''
        
        if(self.text1.get()==''):
            return tkinter.messagebox.showwarning('Message','Invalid Input')
        
        if(self.text4.get()==''):
            return tkinter.messagebox.showwarning('Message','Invalid Input')
        if(self.text5.get()==''):
            return tkinter.messagebox.showwarning('Message','Invalid Input')
        if(self.text6.get()==''):
            return tkinter.messagebox.showwarning('Message','Invalid Input')
        if((self.text9.get().isdigit())==False or self.text9.get()==''):
            return tkinter.messagebox.showwarning('Message','Invalid Input')
        
         
        password1 = self.text5.get()
        passwordConfirm1 = self.text6.get()

        if(password1 == passwordConfirm1):
            self.VolSon = source.Volunteer()
            self.VolSon.name = self.text1.get()

            self.conc1 = source.Contact()
            self.conc1.email = self.text4.get()
            self.conc1.phone = self.text9.get()
            self.conc1.address = self.text7.get("1.0", "end-1c")
            self.VolSon.contact = self.conc1
            self.VolSon.password = password1


            global VolIndex
            VolIndex = VolIndex + 1
            ID = "V0" + str(VolIndex)
            print(ID)
            self.VolSon.id = ID

            #VolList.insert(VolIndex, self.VolSon)

            pathFile = path + "/volunteers/" + ID

            self.VolSon.UpdateFileV(pathFile)
            self.RegSucess()

        else:
            self.password_not_recog_screen = Tk()
            self.password_not_recog_screen.title("Error")
            self.password_not_recog_screen.geometry("150x100")
            Label(self.password_not_recog_screen,
                text="Confirm Password not same").pack()
            Button(self.password_not_recog_screen, text="OK",
                command=self.password_not_recog_screen.destroy).pack()
            self.password_not_recog_screen.mainloop()
        

    def RegSucess(self):
        self.success_screen = Tk()
        self.success_screen.title("Success")
        self.success_screen.geometry("150x100")
        Label(self.success_screen, text="Volunteer Registration Success").pack()
        Label(self.success_screen, text="ID: " + self.VolSon.id).pack()
        Button(self.success_screen, text="OK",
               command=self.success_screen.destroy).pack()
        self.success_screen.mainloop()

    def FailScreen(self):
        self.success_screen = Tk()
        self.success_screen.title("ERROR")
        self.success_screen.geometry("150x100")
        Label(self.success_screen, text="INVALID INPUT").pack()
        #Label(self.success_screen, text="ID: " + self.StudMan.id).pack()
        Button(self.success_screen, text="OK", command = self.success_screen.destroy).pack()
        self.success_screen.mainloop()


class CheckFunds(Frame):
    def __init__(self, master=NONE):
        Frame.__init__(self, master)
        self.master = master
        self.master.title("Funds And Inventory")
        self.master.geometry("475x420")
        self.master.configure(bg ='thistle3')
        self.configure(bg = 'LightGoldenrod2')
        self.pack()
        #self.grid(sticky=S+N+E+W)

        self.lab1 = Label(self, text="Class", relief=FLAT, width=7, height=1, bg = 'LightGoldenrod2')
        self.lab1.grid(row=0, column=0, pady=10)

        self.lab2 = Label(self, text="Books", relief=FLAT, width=12, height=1, bg = 'LightGoldenrod2')
        self.lab2.grid(row=0, column=1, pady=10)

        self.lab3 = Label(self, text="Bags", relief=FLAT, width=9, height=1, bg = 'LightGoldenrod2')
        self.lab3.grid(row=0, column=2, pady=10)

        self.lab4 = Label(self, text="Shoes", relief=FLAT, width=10, height=1, bg = 'LightGoldenrod2')
        self.lab4.grid(row=0, column=3, pady=10)

        self.lab5 = Label(self, text="Dress", relief=FLAT, width=7, height=1, bg = 'LightGoldenrod2')
        self.lab5.grid(row=0, column=4, pady=10)

        InvenC = []

        for k in range(1, 13):
            pathN = path + "/Inventory/" + str(k)

            invNew = source.Inventory()
            invNew.ExtractData(pathN)
            InvenC.append(invNew)

        for i in range(12):
            for j in range(5):
                self.e = Text(self, width=10, height=1, bg = 'LightGoldenrod2')
                self.e.grid(row=i+1, column=j)

                if j == 0:
                    self.e.insert(END, str(InvenC[i].standard))

                if j == 1:
                    self.e.insert(END, str(InvenC[i].help.books))

                if j == 2:
                    self.e.insert(END, str(InvenC[i].help.bags))

                if j == 3:
                    self.e.insert(END, str(InvenC[i].help.shoes))

                if j == 4:
                    self.e.insert(END, str(InvenC[i].help.dress))

            # print(str(i))

        self.lab6 = Label(self, text="FUNDS", relief=FLAT, width=7, height=1, bg = 'LightGoldenrod2')
        self.lab6.grid(row=13, column=2, pady=10)

        self.text6 = Text(self, width=10, height=1, bg = 'LightGoldenrod2')
        self.text6.grid(row=14, column=2)

        pathF = path + "/Inventory/f"

        fnew = source.Funds()
        fnew.ExtractFunds(pathF)

        self.text6.insert(END, str(fnew.funds))


class CheckStudents(Frame):
    def __init__(self, master=NONE):
        Frame.__init__(self, master)
        self.master = master
        self.master.title("Students List")
        self.master.geometry("700x150")
        self.master.configure(bg ='thistle3')
        self.configure(bg = 'LightGoldenrod2')
        self.pack()
        #self.grid(sticky=S+N+E+W)

        self.lab = Label(self, text="ID", relief=FLAT, width=7, height=1, bg = 'LightGoldenrod2')
        self.lab.grid(row=0, column=0, pady=10)

        self.lab0 = Label(self, text="Name", relief=FLAT, width=7, height=1, bg = 'LightGoldenrod2')
        self.lab0.grid(row=0, column=1, pady=10)

        self.lab1 = Label(self, text="Class", relief=FLAT, width=7, height=1, bg = 'LightGoldenrod2')
        self.lab1.grid(row=0, column=2, pady=10)

        self.lab2 = Label(self, text="Books", relief=FLAT, width=12, height=1, bg = 'LightGoldenrod2')
        self.lab2.grid(row=0, column=3, pady=10)

        self.lab3 = Label(self, text="Bags", relief=FLAT, width=9, height=1, bg = 'LightGoldenrod2')
        self.lab3.grid(row=0, column=4, pady=10)

        self.lab4 = Label(self, text="Shoes", relief=FLAT, width=10, height=1, bg = 'LightGoldenrod2')
        self.lab4.grid(row=0, column=5, pady=10)

        self.lab5 = Label(self, text="Dress", relief=FLAT, width=7, height=1, bg = 'LightGoldenrod2')
        self.lab5.grid(row=0, column=6, pady=10)

        self.lab6 = Label(self, text="Fee", relief=FLAT, width=7, height=1, bg = 'LightGoldenrod2')
        self.lab6.grid(row=0, column=7, pady=10)

        StudList = []

        pathNS = path + "/students"
        list_of_files = os.listdir(pathNS)

        for Nfile in list_of_files:
            pathNF = pathNS + "/" + Nfile

            StudNew = source.Student()
            StudNew.ExtractData(pathNF)
            StudList.append(StudNew)

        for i in range(len(StudList)):
            for j in range(8):

                self.e = Text(self, width=10, height=1, bg = 'LightGoldenrod2')
                self.e.grid(row=i+1, column=j)

                if j == 0:
                    self.e.insert(END, str(StudList[i].id))

                if j == 1:
                    self.e.insert(END, str(StudList[i].name))

                if j == 2:
                    self.e.insert(END, str(StudList[i].standard))

                if j == 3:
                    self.e.insert(END, str(StudList[i].help.books))

                if j == 4:
                    self.e.insert(END, str(StudList[i].help.bags))

                if j == 5:
                    self.e.insert(END, str(StudList[i].help.shoes))

                if j == 6:
                    self.e.insert(END, str(StudList[i].help.dress))

                if j == 7:
                    self.e.insert(END, str(StudList[i].help.fees))


class CheckDonors(Frame):
    def __init__(self, master=NONE):
        Frame.__init__(self, master)
        self.master = master
        self.master.title("Donors List")
        self.master.geometry("750x200")
        self.master.configure(bg ='thistle3')
        self.configure(bg = 'LightGoldenrod2')
        self.pack()

        self.lab = Label(self, text="ID", relief=FLAT, width=7, height=1, bg = 'LightGoldenrod2')
        self.lab.grid(row=0, column=0, pady=10)

        self.lab0 = Label(self, text="Name", relief=FLAT, width=7, height=1, bg = 'LightGoldenrod2')
        self.lab0.grid(row=0, column=1, pady=10)

        self.lab1 = Label(self, text="Phone", relief=FLAT, width=7, height=1, bg = 'LightGoldenrod2')
        self.lab1.grid(row=0, column=2, pady=10)

        self.lab2 = Label(self, text="Amount", relief=FLAT, width=12, height=1, bg = 'LightGoldenrod2')
        self.lab2.grid(row=0, column=3, pady=10)

        self.lab3 = Label(self, text="Plan", relief=FLAT, width=9, height=1, bg = 'LightGoldenrod2')
        self.lab3.grid(row=0, column=4, pady=10)

        self.lab4 = Label(self, text="Notified",
                          relief=FLAT, width=10, height=1, bg = 'LightGoldenrod2')
        self.lab4.grid(row=0, column=5, pady=10)

        self.lab4 = Label(self, text="Donated",
                          relief=FLAT, width=10, height=1, bg = 'LightGoldenrod2')
        self.lab4.grid(row=0, column=6, pady=10)

        self.DonorList = []

        pathNS = path + "/Donors"
        list_of_files = os.listdir(pathNS)

        for Nfile in list_of_files:
            if Nfile != '.DS_Store':
                pathNF = pathNS + "/" + Nfile
                # print(Nfile)
                DonorNew = source.PledgedDonor()
                DonorNew.ExtractData(pathNF)
                self.DonorList.append(DonorNew)

        self.DonorList.sort(key=lambda x: x.amount, reverse=True)

        for i in range(len(self.DonorList)):
            for j in range(7):

                self.e = Text(self, width=10, height=1, bg = 'LightGoldenrod2')
                self.e.grid(row=i+1, column=j)

                if j == 0:
                    self.e.insert(END, str(self.DonorList[i].id))

                if j == 1:
                    self.e.insert(END, str(self.DonorList[i].name))

                if j == 2:
                    self.e.insert(END, str(self.DonorList[i].contact.phone))

                if j == 3:
                    self.e.insert(END, str(self.DonorList[i].amount))

                if j == 4:
                    self.e.insert(END, str(self.DonorList[i].donationPlan))

                if j == 5:
                    if self.DonorList[i].notified == 0:
                        self.e.insert(END, "NO")

                    else:
                        self.e.insert(END, "YES")

                if j == 6:
                    if self.DonorList[i].donated == 0:
                        self.e.insert(END, "NO")

                    elif self.DonorList[i].donationPlan == "Semi_Annually":
                        if self.DonorList[i].donated == 1:
                            self.e.insert(END, "ONCE")

                        if self.DonorList[i].donated == 2:
                            self.e.insert(END, "YES, TWICE")

        self.button2 = Button(self, text="Notify Donors",
                              width=12, height=1, command=self.NotifyDonors, highlightbackground = 'LightGoldenrod2')
        self.button2.grid(row=len(self.DonorList)+1,
                          column=3, ipadx=5, padx=5, pady=10)

    def NotifyDonors(self):
        NF = source.Funds()
        pathF = path + "/Inventory/f"
        NF.ExtractFunds(pathF)

        amm = NF.Requiredfunds

        for i in range(len(self.DonorList)):

            if amm <= 0:
                break

            if self.DonorList[i].donated == 0:
                self.DonorList[i].ToBeNotified = 1
                amm = amm - self.DonorList[i].amount

            elif self.DonorList[i].donationPlan == "Semi_Annually":
                if self.DonorList[i].donated == 1:
                    self.DonorList[i].ToBeNotified = 1
                    amm = amm - self.DonorList[i].amount

            if amm <= 0:
                break

        self.lab4 = Label(self, text="To Be Notified",
                          relief=FLAT, width=10, height=1)
        self.lab4.grid(row=0, column=7, pady=10)

        for i in range(len(self.DonorList)):
            self.e = Text(self, width=10, height=1, bg = 'LightGoldenrod2')
            self.e.grid(row=i+1, column=7)

            if self.DonorList[i].ToBeNotified == 0:
                self.e.insert(END, "NO")

            else:
                self.e.insert(END, "YES")

        self.button = Button(self, text="CONFIRM", width=12,
                             height=1, command=self.ConfirmButton, highlightbackground = 'LightGoldenrod2')
        self.button.grid(row=len(self.DonorList)+2,
                         column=3, ipadx=5, padx=5, pady=10)

        if amm <= 0:
            NF.Requiredfunds = 0
            NF.UpdateFunds(pathF)

        else:
            NF.Requiredfunds = amm
            NF.UpdateFunds(pathF)

    def ConfirmButton(self):
        for i in range(len(self.DonorList)):
            if self.DonorList[i].ToBeNotified == 1:
                self.DonorList[i].notified = 1
                newDon = source.PledgedDonor()
                pathNew = path + "/Donors/" + self.DonorList[i].id
                newDon.ExtractData(pathNew)
                newDon.notified = 1
                newDon.UpdateFile(pathNew)
        self.RegSucess()

    def RegSucess(self):
        self.success_screen = Tk()
        self.success_screen.title("Success")
        self.success_screen.geometry("150x100")
        Label(self.success_screen, text="Notified Donors (If Any)").pack()
        Button(self.success_screen, text="OK",
               command=self.success_screen.destroy).pack()
        self.success_screen.mainloop()


class CheckVolunteer(Frame):
    def __init__(self, master=NONE):
        Frame.__init__(self, master)
        self.master = master
        self.master.title("Volunteers List")
        self.master.geometry("300x200")
        self.master.configure(bg ='thistle3')
        self.configure(bg = 'LightGoldenrod2')
        self.pack()

        self.lab = Label(self, text="ID", relief=FLAT, width=7, height=1, bg = 'LightGoldenrod2')
        self.lab.grid(row=0, column=0, pady=10)

        self.lab0 = Label(self, text="Name", relief=FLAT, width=7, height=1, bg = 'LightGoldenrod2')
        self.lab0.grid(row=0, column=1, pady=10)

        self.lab1 = Label(self, text="Phone", relief=FLAT, width=7, height=1, bg = 'LightGoldenrod2')
        self.lab1.grid(row=0, column=2, pady=10)

        VolList = []

        pathNS = path + "/volunteers"
        list_of_files = os.listdir(pathNS)

        for Nfile in list_of_files:
            if Nfile != '.DS_Store':
                pathNF = pathNS + "/" + Nfile
                # print(Nfile)
                VolNew = source.Volunteer()
                VolNew.ExtractData(pathNF)
                VolList.append(VolNew)

            for i in range(len(VolList)):
                for j in range(3):

                    self.e = Text(self, width=10, height=1, bg = 'LightGoldenrod2')
                    self.e.grid(row=i+1, column=j)

                    if j == 0:
                        self.e.insert(END, str(VolList[i].id))

                    if j == 1:
                        self.e.insert(END, str(VolList[i].name))

                    if j == 2:
                        self.e.insert(END, str(VolList[i].contact.phone))


class RemoveVol(Frame):
    def __init__(self, master=NONE):
        Frame.__init__(self, master)
        self.master = master
        self.master.title("Remove Volunteer")
        self.master.geometry("350x150")
        self.master.configure(bg ='thistle3')
        self.configure(bg = 'LightGoldenrod2')
        self.pack()

        #self.lab0 = Label(self, text="Please enter the ID below", bg = 'LightGoldenrod2')
        #self.lab0.grid(row=0, column=0, sticky=E+W, pady=15)

        self.lab1 = Label(self, text="ID", relief=FLAT, width=7, height=1, bg = 'LightGoldenrod2')
        self.lab1.grid(row=1, column=0, ipadx=5, padx=15, pady=10)

        self.text2 = Text(self, width=10, height=1, bg = 'LightGoldenrod2')
        self.text2.grid(row=1, column=2, ipadx=5, padx=15, pady=10)

        self.button = Button(self, text="Delete",
                             height=1, command=self.DeleteF, highlightbackground = 'LightGoldenrod2')
        self.button.grid(row=2, column=1, pady=15, ipadx=3)

    def DeleteF(self):
        self.ID = self.text2.get("1.0", "end-1c")

        self.text2.delete("1.0", "end-1c")

        pathN = path + "/volunteers"
        list_of_files = os.listdir(pathN)

        if self.ID in list_of_files:
            pathNF = pathN + "/" + self.ID
            os.remove(pathNF)
            self.DeleteSuccess()

        else:
            self.DeleteFail()

    def DeleteSuccess(self):
        self.login_success_screen = Tk()
        self.login_success_screen.title("Success")
        self.login_success_screen.geometry("150x100")
        Label(self.login_success_screen, text="Delete Success").pack()
        Button(self.login_success_screen, text="OK",
               command=self.login_success_screen.destroy).pack()
        self.login_success_screen.mainloop()

    def DeleteFail(self):
        self.login_success_screen = Tk()
        self.login_success_screen.title("Fail")
        self.login_success_screen.geometry("150x100")
        Label(self.login_success_screen, text="Invalid ID").pack()
        Button(self.login_success_screen, text="OK",
               command=self.login_success_screen.destroy).pack()
        self.login_success_screen.mainloop()


class Initiate_Help(Frame):
    def __init__(self, master=NONE):
        Frame.__init__(self, master)
        self.master = master
        self.master.title("Remove Volunteer")
        self.master.geometry("350x300")
        self.master.configure(bg ='thistle3')
        self.configure(bg = 'LightGoldenrod2')
        self.pack()

        self.lab1 = Label(self, text="Total Funds", height=1, bg = 'LightGoldenrod2')
        self.lab1.grid(row=0, column=0, sticky=E+W)

        self.text = Text(self, width=9, height=1, bg = 'LightGoldenrod2')
        self.text.grid(row=0, column=1, ipadx=10, padx=15, pady=10)

        self.lab3 = Label(self, text="Total Registered Students", height=1, bg = 'LightGoldenrod2')
        self.lab3.grid(row=1, column=0, sticky=E+W)

        self.text1 = Text(self, width=9, height=1, bg = 'LightGoldenrod2')
        self.text1.grid(row=1, column=1, ipadx=5, padx=15, pady=10)

        self.lab5 = Label(self, text="Students to be Helped", height=1, bg = 'LightGoldenrod2')
        self.lab5.grid(row=2, column=0, sticky=E+W)

        self.text2 = Text(self, width=9, height=1, bg = 'LightGoldenrod2')
        self.text2.grid(row=2, column=1, ipadx=5, padx=15, pady=10)

        self.button = Button(self, text="Send Funds",
                             command=self.initiate_help, height=1, highlightbackground  = 'LightGoldenrod2')
        self.button.grid(row=3, column=1, pady=15, ipadx=3)

        self.received_help = []

        self.Fun = source.Funds()
        pathF = path + "/Inventory/f"
        self.Fun.ExtractFunds(pathF)
        self.Inv = []

        for k in range(1, 13):
            pathN = path + "/Inventory/" + str(k)

            invNew = source.Inventory()
            invNew.ExtractData(pathN)
            self.Inv.append(invNew)

        self.text.insert(END, self.Fun.funds)
        count = 0

        self.StuList = []

        pathNS = path + "/students"
        list_of_files = os.listdir(pathNS)

        for Nfile in list_of_files:
            pathNF = pathNS + "/" + Nfile

            StudNew = source.Student()
            StudNew.ExtractData(pathNF)
            self.StuList.append(StudNew)

        for i in range(len(self.StuList)):
            if self.StuList[i].NeedHelp == 1:
                count = count+1

        self.text1.insert(END, len(self.StuList))
        self.text2.insert(END, count)

    def initiate_help(self):
        amt = 0
        for i in range(len(self.StuList)):

            if self.StuList[i].NeedHelp == 1:
                j = self.StuList[i].standard

                if self.Inv[j-1].help.books < self.StuList[i].help.books:
                    amt = amt+self.Inv[j-1].prices.books*self.StuList[i].help.books

                if self.Inv[j-1].help.bags < self.StuList[i].help.bags:
                    amt = amt+self.Inv[j-1].prices.bags*self.StuList[i].help.bags

                if self.Inv[j-1].help.shoes < self.StuList[i].help.shoes:
                    amt = amt+self.Inv[j-1].prices.shoes*self.StuList[i].help.shoes

                if self.Inv[j-1].help.dress < self.StuList[i].help.dress:
                    amt = amt+self.Inv[j-1].prices.dress*self.StuList[i].help.dress

                amt = amt+self.StuList[i].help.fees

        #self.Fun.reqiuredfunds = amt

        LowPI = []
        LowPI = sorted(self.StuList, key=operator.attrgetter('parentalIncome'))
        GenderP = []
        GenderP = sorted(LowPI, key=operator.attrgetter('gender'))
        Merit = []
        Merit = sorted(GenderP, key=operator.attrgetter('percentage'))
        
        if(self.Fun.funds > amt):
            for i in range(len(self.StuList)):
                if self.StuList[i].NeedHelp == 1:
                    j = self.StuList[i].standard

                    pathNew = path + "/students/" + self.StuList[i].id
                    StudNew = source.Student()
                    StudNew.ExtractData(pathNew)

                    pathF = path + "/Inventory/" + str(j)
                    InvT = source.Inventory()
                    InvT.ExtractData(pathF)

                    if self.Inv[j-1].help.books > self.StuList[i].help.books:
                        self.Inv[j-1].help.books = self.Inv[j-1].help.books - self.StuList[i].help.books
                        InvT.help.books = self.Inv[j-1].help.books 
                    
                    else:
                        self.Fun.funds = self.Fun.funds - self.Inv[j-1].prices.books*self.StuList[i].help.books
                    
                    StudNew.help.books = 0

                    if self.Inv[j-1].help.bags > self.StuList[i].help.bags:
                        self.Inv[j-1].help.bags = self.Inv[j-1].help.bags-self.StuList[i].help.bags
                        InvT.help.bags = self.Inv[j-1].help.bags 

                    else:
                        self.Fun.funds = self.Fun.funds - self.Inv[j-1].prices.bags*self.StuList[i].help.bags
                    
                    StudNew.help.bags = 0

                    if self.Inv[j-1].help.shoes > self.StuList[i].help.shoes:
                        self.Inv[j-1].help.shoes = self.Inv[j-1].help.shoes - self.StuList[i].help.shoes
                        InvT.help.shoes = self.Inv[j-1].help.shoes
                    
                    else:
                        self.Fun.funds = self.Fun.funds - self.Inv[j-1].prices.shoes*self.StuList[i].help.shoes
                    
                    StudNew.help.shoes = 0

                    if self.Inv[j-1].help.dress > self.StuList[i].help.dress:
                        self.Inv[j-1].help.dress = self.Inv[j-1].help.dress - self.StuList[i].help.dress
                        InvT.help.dress = self.Inv[j-1].help.dress 
                    
                    else:
                        self.Fun.funds = self.Fun.funds - self.Inv[j-1].prices.dress*self.StuList[i].help.dress
                    
                    StudNew.help.dress = 0

                    self.Fun.funds = self.Fun.funds - self.StuList[i].help.fees
                    StudNew.help.fees = 0

                    StudNew.HelpRecived = 1
                    StudNew.NeedHelp = 0
                    StudNew.UpdateFile(pathNew)
                    InvT.UpdateFile(pathF)

        elif(self.Fun.funds < amt):

            self.StuList.sort(lambda x: x.parentalIncome)
            self.StuList.sort(lambda x: x.gender, reverse = True)
            self.StuList.sort(lambda x: x.percentage, reverse = True)

            for i in range(len(self.StuList)) & self.Fun.funds > 0:
                if self.StuList[i].NeedHelp == 1:
                    j = self.StuList[i].standard

                    pathNew = path + "/students/" + self.StuList[i].id
                    StudNew = source.Student()
                    StudNew.ExtractData(pathNew)

                    pathF = path + "/Inventory/" + str(j)
                    InvT = source.Inventory()
                    InvT.ExtractData(pathF)

                    if self.Inv[j-1].help.books > self.StuList[i].help.books:
                        self.Inv[j-1].help.books = self.Inv[j-1].help.books - self.StuList[i].help.books
                        InvT.help.books = self.Inv[j-1].help.books 
                    
                    else:
                        self.Fun.funds = self.Fun.funds - self.Inv[j-1].prices.books*self.StuList[i].help.books
                    
                    StudNew.help.books = 0

                    if self.Inv[j-1].help.bags > self.StuList[i].help.bags:
                        self.Inv[j-1].help.bags = self.Inv[j-1].help.bags-self.StuList[i].help.bags
                        InvT.help.bags = self.Inv[j-1].help.bags 

                    else:
                        self.Fun.funds = self.Fun.funds - self.Inv[j-1].prices.bags*self.StuList[i].help.bags
                    
                    StudNew.help.bags = 0

                    if self.Inv[j-1].help.shoes > self.StuList[i].help.shoes:
                        self.Inv[j-1].help.shoes = self.Inv[j-1].help.shoes - self.StuList[i].help.shoes
                        InvT.help.shoes = self.Inv[j-1].help.shoes
                    
                    else:
                        self.Fun.funds = self.Fun.funds - self.Inv[j-1].prices.shoes*self.StuList[i].help.shoes
                    
                    StudNew.help.shoes = 0

                    if self.Inv[j-1].help.dress > self.StuList[i].help.dress:
                        self.Inv[j-1].help.dress = self.Inv[j-1].help.dress - self.StuList[i].help.dress
                        InvT.help.dress = self.Inv[j-1].help.dress 
                    
                    else:
                        self.Fun.funds = self.Fun.funds - self.Inv[j-1].prices.dress*self.StuList[i].help.dress
                    
                    StudNew.help.dress = 0

                    self.Fun.funds = self.Fun.funds - self.StuList[i].help.fees
                    StudNew.help.fees = 0

                    StudNew.HelpRecived = 1
                    StudNew.NeedHelp = 0
                    StudNew.UpdateFile(pathNew)
                    InvT.UpdateFile(pathF)
            
        if self.Fun.funds < 0:
            self.Fun.Requiredfunds = (-1)*self.Fun.funds
            self.Fun.funds = 0

        pathf = path + "/Inventory/f"
        self.Fun.UpdateFunds(pathf)
        self.button = Button(self, text="GIVE HELP",
                             command=self.GiveHelpButton, height=1, highlightbackground = 'LightGoldenrod2')
        self.button.grid(row=4, column=1, pady=15, ipadx=3)
    
    def GiveHelpButton(self):
        root4 = Tk()
        app4 = GiveHelp(root4)
        root4.mainloop()

class GiveHelp(Frame):
    def __init__(self, master=NONE):
        Frame.__init__(self, master)
        self.master = master
        self.master.title("Updated Needs of Students")
        self.master.geometry("750x250")
        self.master.configure(bg ='thistle3')
        self.configure(bg = 'LightGoldenrod2')
        self.pack()
        
        self.lab1=Label(self,text="ID",relief=FLAT,width=7,height=1, bg = 'LightGoldenrod2')
        self.lab1.grid(row=0,column=0,pady=10)
        
        self.lab1=Label(self,text="Class",relief=FLAT,width=7,height=1, bg = 'LightGoldenrod2')
        self.lab1.grid(row=0,column=1,pady=10)
        
        self.lab2=Label(self,text="Books",relief=FLAT,width=12,height=1, bg = 'LightGoldenrod2')
        self.lab2.grid(row=0,column=2,pady=10)
        
        self.lab3=Label(self,text="Bags",relief=FLAT,width=9,height=1, bg = 'LightGoldenrod2')
        self.lab3.grid(row=0,column=3,pady=10)
        
        self.lab4=Label(self,text="Shoes",relief=FLAT,width=10,height=1, bg = 'LightGoldenrod2')
        self.lab4.grid(row=0,column=4,pady=10)

        self.lab5=Label(self,text="Dress",relief=FLAT,width=7,height=1, bg = 'LightGoldenrod2')
        self.lab5.grid(row=0,column=5,pady=10)
        
        self.button1=Button(self,text="OK",width=7,height=1, command = self.master.destroy, highlightbackground = 'LightGoldenrod2')
        self.button1.grid(row=6,column=2,ipadx=5,padx=15,pady=10)
       
        StudList = []

        pathNS = path + "/students"
        list_of_files = os.listdir(pathNS)

        for Nfile in list_of_files:
            pathNF = pathNS + "/" + Nfile

            StudNew = source.Student()
            StudNew.ExtractData(pathNF)
            StudList.append(StudNew)
        
        for i in range(len(StudList)):
         for j in range(6):
                if StudList[i].HelpRecived == 1: 
                    if j == 0:
                            self.e0 = Text(self, width=10,height=1, bg = 'LightGoldenrod2')
                            self.e0.grid(row=i+1, column=j)
                            self.e0.insert(END, StudList[i].id)
                        
                    if j == 1:
                            self.e1 = Text(self, width=10,height=1, bg = 'LightGoldenrod2')
                            self.e1.grid(row=i+1, column=j)
                            self.e1.insert(END, StudList[i].help.books)
                        
                    if j == 2:
                            self.e2= Text(self, width=10,height=1, bg = 'LightGoldenrod2')
                            self.e2.grid(row=i+1, column=j)
                            self.e2.insert(END, StudList[i].help.bags)
                        
                    if j == 3:
                            self.e3 = Text(self, width=10,height=1, bg = 'LightGoldenrod2')
                            self.e3.grid(row=i+1, column=j)
                            self.e3.insert(END, StudList[i].help.shoes)
                        
                    if j == 4:
                            self.e4 = Text(self, width=10,height=1, bg = 'LightGoldenrod2')
                            self.e4.grid(row=i+1, column=j)
                            self.e4.insert(END, StudList[i].help.dress)
                            
                    if j == 5:
                            self.e4 = Text(self, width=10,height=1, bg = 'LightGoldenrod2')
                            self.e4.grid(row=i+1, column=j)
                            self.e4.insert(END, StudList[i].help.fees)
'''
root = Tk()
app = RegVolunteer(root)
root.mainloop()
'''


