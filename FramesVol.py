from tkinter import*
from PIL import ImageTk,Image
import loginCred
import os
import source
import FramesSource
import tkinter.messagebox

path = "/Users/haasitapinnepu/Desktop/NMS/loginCred" #Replace with path to loginCred folder in your system

indP = path + "/IdIndex"

file = open(indP, "r")
DonorIndex = int(file.readline())
VolIndex = int(file.readline())
StuIndex = int(file.readline())
file.close()

class RegStudent(Frame):
    def __init__(self, master=NONE):
        Frame.__init__(self, master)
        self.master = master
        self.master.title("Register Student")
        self.master.geometry("450x800")
        self.master.configure(bg ='thistle3')
        self.configure(bg = 'LightGoldenrod2')
        self.pack()
        
        self.lab1 = Label(self, text="Enter Data",padx=10,pady=5, bg = 'LightGoldenrod2')
        self.lab1.grid(row=0,column=1)
        
        self.lab1 = Label(self,text="Name",padx=10,pady=5, bg = 'LightGoldenrod2')
        self.lab1.grid(row=1,column=0)
        
        self.text1 = Entry(self,width=10, bg = 'LightGoldenrod2')
        self.text1.grid(row=1,column=1,padx=10,pady=15)
        
        self.lab2 = Label(self,text="Date of Birth",padx=10,pady=5, bg = 'LightGoldenrod2')
        self.lab2.grid(row=2,column=0)
        
        self.text2 = Entry(self,width=10, bg = 'LightGoldenrod2')
        self.text2.grid(row=2,column=1,padx=10,pady=15)
        self.text2.insert(0, "YYYY-MM-DD")

        self.lab3 = Label(self,text="School",padx=10,pady=5, bg = 'LightGoldenrod2')
        self.lab3.grid(row=3,column=0)
        
        self.text3 = Entry(self,width=10, bg = 'LightGoldenrod2')
        self.text3.grid(row=3,column=1,padx=10,pady=15)
        
        self.lab6 = Label(self,text="Class Studying",padx=10,pady=5, bg = 'LightGoldenrod2')
        self.lab6.grid(row=6,column=0)
        
        self.text6 = Entry(self,width=10, bg = 'LightGoldenrod2')
        self.text6.grid(row=6,column=1,padx=10,pady=15)

        self.lab = Label(self,text="Gender",padx=10,pady=5, bg = 'LightGoldenrod2')
        self.lab.grid(row=7,column=0)
        
        options = ["Male","Female"]
        self.clicked = StringVar()
        self.clicked.set( "Male" )
        
        self.drop = OptionMenu( self , self.clicked , *options )
        self.drop.config(bg = 'LightGoldenrod2')
        self.drop.grid(row=7,column=1)
        
        self.lab7 = Label(self,text="Parental Income",padx=10,pady=5, bg = 'LightGoldenrod2')
        self.lab7.grid(row=8,column=0,padx=10)
        
        self.text7 = Entry(self,width=10, bg = 'LightGoldenrod2')
        self.text7.grid(row=8,column=1,padx=10,pady=15)
        
        self.lab8 = Label(self,text="Percentage",padx=10,pady=5, bg = 'LightGoldenrod2')
        self.lab8.grid(row=9,column=0)
        
        self.text8 = Entry(self,width=10, bg = 'LightGoldenrod2')
        self.text8.grid(row=9,column=1,padx=10,pady=15)

        self.lab9 = Label(self,text="BOOKS",padx=10,pady=5, bg = 'LightGoldenrod2')
        self.lab9.grid(row=10,column=0)
        
        self.text9 = Entry(self,width=10, bg = 'LightGoldenrod2')
        self.text9.grid(row=10,column=1,padx=10,pady=15)

        self.lab10 = Label(self,text="BAGS",padx=10,pady=5, bg = 'LightGoldenrod2')
        self.lab10.grid(row=11,column=0)
        
        self.text10 = Entry(self,width=10, bg = 'LightGoldenrod2')
        self.text10.grid(row=11,column=1,padx=10,pady=15)

        self.lab11 = Label(self,text="SHOES",padx=10,pady=5, bg = 'LightGoldenrod2')
        self.lab11.grid(row=12,column=0)
        
        self.text11 = Entry(self,width=10, bg = 'LightGoldenrod2')
        self.text11.grid(row=12,column=1,padx=10,pady=15)

        self.lab12 = Label(self,text="DRESS",padx=10,pady=5, bg = 'LightGoldenrod2')
        self.lab12.grid(row=13,column=0)
        
        self.text12 = Entry(self,width=10, bg = 'LightGoldenrod2')
        self.text12.grid(row=13,column=1,padx=10,pady=15)

        self.lab13 = Label(self,text="FEES",padx=10,pady=5, bg = 'LightGoldenrod2')
        self.lab13.grid(row=14,column=0)
        
        self.text13 = Entry(self,width=10, bg = 'LightGoldenrod2')
        self.text13.grid(row=14,column=1,padx=10,pady=15)

        self.button=Button(self,text="Register",width=7,height=1, command = self.RegStudent, highlightbackground = 'LightGoldenrod2')
        self.button.grid(row=15 ,column=1,ipadx=5,padx=5,pady=10)
    
    def RegStudent(self):

        '''
        if (self.text1.get("1.0","end-1c")=='' or self.text2.get("1.0","end-1c")==''or 
        self.text3.get("1.0","end-1c")==''or self.text6.get("1.0","end-1c")==''or 
        self.text7.get("1.0","end-1c")==''or self.text8.get("1.0","end-1c")=='' or 
        self.text9.get("1.0","end-1c")=='' or self.text10.get("1.0","end-1c")=='' or
         self.text11.get("1.0","end-1c")=='' or self.text12.get("1.0","end-1c")=='' or self.text13.get("1.0","end-1c")==''):
           return self.FailScreen()

        self.StudMan = source.Student()
        self.StudMan.name = self.text1.get("1.0", "end-1c")
        self.StudMan.dob = self.text2.get("1.0", "end-1c")
        self.StudMan.school = self.text3.get("1.0", "end-1c")
        self.StudMan.standard = int(self.text6.get("1.0", "end-1c"))
        self.StudMan.gender = self.clicked.get()
        self.StudMan.parentalIncome = int(self.text7.get("1.0", "end-1c"))
        self.StudMan.percentage = int(self.text8.get("1.0", "end-1c"))
        self.StudMan.help.books = int(self.text9.get("1.0", "end-1c"))
        self.StudMan.help.bags = int(self.text10.get("1.0", "end-1c"))
        self.StudMan.help.shoes = int(self.text11.get("1.0", "end-1c"))
        self.StudMan.help.dress = int(self.text12.get("1.0", "end-1c"))
        self.StudMan.help.fees = int(self.text13.get("1.0", "end-1c"))
        '''
        pattern = r'(19|20)\d\d[- /.](0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])'
        match = re.search(pattern,self.text2.get())
        if match==None:
            return tkinter.messagebox.showwarning('Message','Invalid Input')
    
        if((self.text1.get().isalpha())==False or self.text1.get()==''):
            return tkinter.messagebox.showwarning('Message','Invalid Input')
        
        if((self.text3.get().isalpha())==False or self.text3.get()==''):
            return tkinter.messagebox.showwarning('Message','Invalid Input')
        if((self.text6.get().isdigit())==False or self.text6.get()==''):
            return tkinter.messagebox.showwarning('Message','Invalid Input')
        if((self.text7.get().isdigit())==False or self.text7.get()==''):
            return tkinter.messagebox.showwarning('Message','Invalid Input')
        if((self.text8.get().isdigit())==False or self.text8.get()==''):
            return tkinter.messagebox.showwarning('Message','Invalid Input')
        if((self.text9.get().isdigit())==False or self.text9.get()==''):
            return tkinter.messagebox.showwarning('Message','Invalid Input')
        if((self.text10.get().isdigit())==False or self.text10.get()==''):
            return tkinter.messagebox.showwarning('Message','Invalid Input')
        if((self.text11.get().isdigit())==False or self.text11.get()==''):
            return tkinter.messagebox.showwarning('Message','Invalid Input')
        if((self.text12.get().isdigit())==False or self.text12.get()==''):
            return tkinter.messagebox.showwarning('Message','Invalid Input')
        if((self.text13.get().isdigit())==False or self.text13.get()==''):
            return tkinter.messagebox.showwarning('Message','Invalid Input')
        
      
        self.StudMan = source.Student()
        self.StudMan.name = self.text1.get()
        self.StudMan.dob = self.text2.get()
        self.StudMan.school = self.text3.get()
        self.StudMan.standard = int(self.text6.get())
        self.StudMan.gender = self.clicked.get()
        self.StudMan.parentalIncome = int(self.text7.get())
        self.StudMan.percentage = int(self.text8.get())
        self.StudMan.help.books = int(self.text9.get())
        self.StudMan.help.bags = int(self.text10.get())
        self.StudMan.help.shoes = int(self.text11.get())
        self.StudMan.help.dress = int(self.text12.get())
        self.StudMan.help.fees = int(self.text13.get())

        global StuIndex
        StuIndex = StuIndex + 1
        ID = "S0" + str(StuIndex)

        self.StudMan.id = ID

        pathFS = path + "/students/" + ID

        self.StudMan.UpdateFile(pathFS)
        self.RegSucess()

    def RegSucess(self):
        self.success_screen = Tk()
        self.success_screen.title("Success")
        self.success_screen.geometry("150x100")
        Label(self.success_screen, text="Student Registration Success").pack()
        Label(self.success_screen, text="ID: " + self.StudMan.id).pack()
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

class SetPrice(Frame):
    def __init__(self, master=NONE):
            Frame.__init__(self, master)
            self.master = master
            self.master.title("Set Price")
            self.master.geometry("475x400")
            self.master.configure(bg ='thistle3')
            self.configure(bg = 'LightGoldenrod2')
            self.pack()  
            
            self.lab1=Label(self,text="Class",relief=FLAT,width=7,height=1, bg = 'LightGoldenrod2')
            self.lab1.grid(row=0,column=0,pady=10)
            
            self.lab2=Label(self,text="Books",relief=FLAT,width=12,height=1, bg = 'LightGoldenrod2')
            self.lab2.grid(row=0,column=1,pady=10)
            
            self.lab3=Label(self,text="Bags",relief=FLAT,width=9,height=1, bg = 'LightGoldenrod2')
            self.lab3.grid(row=0,column=2,pady=10)
            
            self.lab4=Label(self,text="Shoes",relief=FLAT,width=10,height=1, bg = 'LightGoldenrod2')
            self.lab4.grid(row=0,column=3,pady=10)

            self.lab5=Label(self,text="Dress",relief=FLAT,width=7,height=1, bg = 'LightGoldenrod2')
            self.lab5.grid(row=0,column=4,pady=10)

            self.button=Button(self,text="Update",height=1, command = self.UpdatePrice, highlightbackground = 'LightGoldenrod2')
            self.button.grid(row=13,column=2,pady=15,ipadx=3)
            
            self.InvenC = []

            for k in range(1, 13):
                pathN = path + "/Inventory/" + str(k)

                invNew = source.Inventory()
                invNew.ExtractData(pathN)
                self.InvenC.append(invNew)

            self.textBoxR = []
            
            for i in range(12):
                self.textBoxC = []
                for j in range(5):   
                    self.e = Text(self, width=10,height=1, bg = 'LightGoldenrod2')
                    self.e.grid(row=i+1, column=j)

                    self.textBoxC.append(self.e)

                    if j == 0:
                        self.e.insert(END, str(self.InvenC[i].standard))
                    
                    if j == 1:
                        self.e.insert(END, str(self.InvenC[i].prices.books))
                    
                    if j == 2:
                        self.e.insert(END, str(self.InvenC[i].prices.bags))
                    
                    if j == 3:
                        self.e.insert(END, str(self.InvenC[i].prices.shoes))
                    
                    if j == 4:
                        self.e.insert(END, str(self.InvenC[i].prices.dress))
                self.textBoxR.append(self.textBoxC)
    
    def UpdatePrice(self):
        for i in range(12):
            for j in range(1, 5):

                if j == 1:
                    self.InvenC[i].prices.books = int(self.textBoxR[i][j].get("1.0", "end-1c"))
                    
                if j == 2:
                    self.InvenC[i].prices.bags = int(self.textBoxR[i][j].get("1.0", "end-1c"))
                    
                if j == 3:
                    self.InvenC[i].prices.shoes = int(self.textBoxR[i][j].get("1.0", "end-1c"))
                    
                if j == 4:
                    self.InvenC[i].prices.dress = int(self.textBoxR[i][j].get("1.0", "end-1c"))

            #pathN = path + "/Inventory/" + str(i+1)
            self.InvenC[i].UpdateFile(self.InvenC[i].path)
        self.UpSucess()

    def UpSucess(self):
        self.success_screen = Tk()
        self.success_screen.title("Success")
        self.success_screen.geometry("150x100")
        Label(self.success_screen, text="Update Success").pack()
        Button(self.success_screen, text="OK", command = self.success_screen.destroy).pack()
        self.success_screen.mainloop()    

class MinorDonation(Frame):
    def __init__(self, master=NONE):
            Frame.__init__(self, master)
            self.master = master
            self.master.title("Minor Donation")
            self.master.geometry("525x375")
            self.master.configure(bg ='thistle3')
            self.configure(bg = 'LightGoldenrod2')
            self.pack()  
            
            #self.lab1=Label(self,text="WELCOME",relief=FLAT,width=12,height=1, bg = 'LightGoldenrod2')
            #self.lab1.grid(row=0,column=1,ipadx=5,padx=15,pady=10)
            
            self.lab2=Label(self,text="Frequency",relief=FLAT,width=12,height=1, bg = 'LightGoldenrod2')
            self.lab2.grid(row=1,column=1,ipadx=10,padx=15,pady=10)

            self.lab3=Label(self,text="Class",relief=FLAT,width=12,height=1, bg = 'LightGoldenrod2')
            self.lab3.grid(row=4,column=2,ipadx=10,padx=15,pady=10)

            self.text1 = Text(self,width=5,height=1,padx=10,pady=5, bg = 'LightGoldenrod2')
            self.text1.grid(row=5,column=2,padx=10,pady=15)
            
            self.lab4=Label(self,text="Books",relief=FLAT,width=10,height=1, bg = 'LightGoldenrod2')
            self.lab4.grid(row=3,column=0,ipadx=5,padx=15,pady=10)
            
            self.text = Text(self,width=5,height=1,padx=10,pady=5, bg = 'LightGoldenrod2')
            self.text.grid(row=3,column=1,padx=10,pady=15)
            
            self.lab5=Label(self,text="Bags",relief=FLAT,width=7,height=1, bg = 'LightGoldenrod2')
            self.lab5.grid(row=4,column=0,ipadx=5,padx=15,pady=10)
            
            self.text2 = Text(self,width=5,height=1,padx=10,pady=5, bg = 'LightGoldenrod2')
            self.text2.grid(row=4,column=1,padx=10,pady=15)

            self.lab6=Label(self,text="Shoes",relief=FLAT,width=7,height=1, bg = 'LightGoldenrod2')
            self.lab6.grid(row=5,column=0,ipadx=5,padx=15,pady=10)
            
            self.text4 = Text(self,width=5,height=1,padx=10,pady=5, bg = 'LightGoldenrod2')
            self.text4.grid(row=5,column=1,padx=10,pady=15)
            
            self.lab7=Label(self,text="Dresses",relief=FLAT,width=9,height=1, bg = 'LightGoldenrod2')
            self.lab7.grid(row=6,column=0,ipadx=5,padx=15,pady=10)
            
            self.text6 = Text(self,width=5,height=1,padx=10,pady=5, bg = 'LightGoldenrod2')
            self.text6.grid(row=6,column=1,padx=10,pady=15)
        
            self.lab6=Label(self,text="Money",relief=FLAT,width=12,height=1, bg = 'LightGoldenrod2')
            self.lab6.grid(row=7,column=0,ipadx=10,padx=15,pady=10)
            
            self.text9 = Text(self,width=5,height=1,padx=10,pady=5, bg = 'LightGoldenrod2')
            self.text9.grid(row=7,column=1,padx=10,pady=15)

            self.button=Button(self,text="Accept",width=12,height=1, command = self.AcceptDonation, highlightbackground = 'LightGoldenrod2')
            self.button.grid(row=6,column=2,ipadx=10,padx=15,pady=10)
            
    def AcceptDonation(self):
        self.Inv = source.Inventory()
        self.Inv.standard = self.text1.get("1.0", "end-1c")
        BooksN = int(self.text.get("1.0", "end-1c"))
        BagsN = int(self.text2.get("1.0", "end-1c"))
        ShoesN = int(self.text4.get("1.0", "end-1c"))
        DressN = int(self.text6.get("1.0", "end-1c"))
        FundN = int(self.text9.get("1.0", "end-1c"))

        pathN = path + "/Inventory/" + str(self.Inv.standard)

        self.Inv.ExtractData(pathN)
        self.Inv.help.books = self.Inv.help.books + BooksN
        self.Inv.help.bags = self.Inv.help.bags + BagsN
        self.Inv.help.shoes = self.Inv.help.shoes + ShoesN
        self.Inv.help.dress = self.Inv.help.dress + DressN

        self.Inv.UpdateFile(pathN)
        
        pathF = path + "/Inventory/f"

        self.f = source.Funds()
        self.f.ExtractFunds(pathF)
        self.f.funds = self.f.funds + FundN
        self.f.UpdateFunds(pathF)

        self.AccSucess()

    def AccSucess(self):
        self.success_screen = Tk()
        self.success_screen.title("Success")
        self.success_screen.geometry("150x100")
        Label(self.success_screen, text="Donation Accepted").pack()
        Button(self.success_screen, text="OK", command = self.success_screen.destroy).pack()
        self.success_screen.mainloop() 

class UpdateProfile(Frame):
    def __init__(self, master=NONE):
            Frame.__init__(self, master)
            self.master = master
            self.master.title("Update Student Profile")
            self.master.geometry("650x325")
            self.master.configure(bg ='thistle3')
            self.configure(bg = 'LightGoldenrod2')
            self.pack()  
            
            self.lab0=Label(self,text="ID",relief=FLAT,width=7,height=1, bg = 'LightGoldenrod2')
            self.lab0.grid(row=0,column=2,pady=10)

            self.text0 = Text(self,width=5,height=1,padx=10,pady=5, bg = 'LightGoldenrod2')
            self.text0.grid(row=1,column=2,padx=10,pady=5)
            
            self.lab1=Label(self,text="Class",relief=FLAT,width=7,height=1, bg = 'LightGoldenrod2')
            self.lab1.grid(row=2,column=0,pady=10)
            
            self.lab2=Label(self,text="Books",relief=FLAT,width=12,height=1, bg = 'LightGoldenrod2')
            self.lab2.grid(row=2,column=1,pady=10)
            
            self.lab3=Label(self,text="Bags",relief=FLAT,width=9,height=1, bg = 'LightGoldenrod2')
            self.lab3.grid(row=2,column=2,pady=10)
            
            self.lab4=Label(self,text="Shoes",relief=FLAT,width=10,height=1, bg = 'LightGoldenrod2')
            self.lab4.grid(row=2,column=3,pady=10)

            self.lab5=Label(self,text="Dress",relief=FLAT,width=7,height=1, bg = 'LightGoldenrod2')
            self.lab5.grid(row=2,column=4,pady=10)

            self.lab6=Label(self,text="Fee",relief=FLAT,width=7,height=1, bg = 'LightGoldenrod2')
            self.lab6.grid(row=4,column=2,pady=10)

            self.text1 = Text(self,width=5,height=1,padx=10,pady=5, bg = 'LightGoldenrod2')
            self.text1.grid(row=5,column=2,padx=10,pady=5)

            self.Klist = []

            for j in range(5):    
                self.e = Text(self, width=10,height=1,padx=10,pady=5, bg = 'LightGoldenrod2')
                self.e.grid(row=3, column=j,padx=10,pady=5)

                self.Klist.append(self.e)


                    
            self.button1=Button(self,text="Update",width=7,height=1, command = self.UpdateButton, highlightbackground = 'LightGoldenrod2')
            self.button1.grid(row=6,column=2,ipadx=5,padx=15,pady=10)
    
    def UpdateButton(self):
        self.stud = source.Student()
        ID = str(self.text0.get("1.0", "end-1c"))

        pathNew = path + "/students/" + ID

        self.stud.ExtractData(pathNew)

        for j in range(5):

            if j == 0:
                self.stud.standard = int(self.Klist[j].get("1.0", "end-1c"))

            if j == 1:
                self.stud.help.books = int(self.Klist[j].get("1.0", "end-1c"))
                    
            if j == 2:
                self.stud.help.bags = int(self.Klist[j].get("1.0", "end-1c"))
                    
            if j == 3:
                self.stud.help.shoes = int(self.Klist[j].get("1.0", "end-1c"))
                    
            if j == 4:
                self.stud.help.dress = int(self.Klist[j].get("1.0", "end-1c"))

        self.stud.help.fees = int(self.text1.get("1.0", "end-1c"))

        self.stud.UpdateFile(pathNew)
        self.AccSucess()
    
    def AccSucess(self):
        self.success_screen = Tk()
        self.success_screen.title("Success")
        self.success_screen.geometry("150x100")
        Label(self.success_screen, text="Updated Succesfully").pack()
        Button(self.success_screen, text="OK", command = self.success_screen.destroy).pack()
        self.success_screen.mainloop()    

'''
root = Tk()
app = RegStudent(root)
root.mainloop()
'''