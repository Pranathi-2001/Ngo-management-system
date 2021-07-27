class Contact:
    def __init__(self):
        self.address = " "
        self.phone = 0
        self.email = " "

class Help:
    def __init__(self):
        self.books = 0
        self.bags = 0
        self.shoes = 0
        self.dress = 0
        self.fees = 0


class Funds:
    def __init__(self):
        self.funds = 0
        self.Requiredfunds = 0
    
    def UpdateFunds(self, pathF):
        file = open(pathF, "w")
        if self.funds == 0:
            file.write("0" + "\n")
        else:
            file.write(str(self.funds) + "\n")
        if self.Requiredfunds == 0:
            file.write("0")
        else: 
            file.write(str(self.Requiredfunds))
        file.close()

    def ExtractFunds(self, pathF):
        file = open(pathF, "r")
        self.funds = int(file.readline())
        self.Requiredfunds = int(file.readline())
        file.close()
    

class Inventory:

    def __init__(self):
        self.standard = 0
        self.help = Help()
        self.prices = Help()
        self.path = ""
    
    def UpdateFile(self, pathI):
        file = open(pathI, "w")
        file.write(str(self.standard) + "\n\n")
        file.write(str(self.help.books) + "\n") #Books
        file.write(str(self.help.bags) + "\n") #Bags
        file.write(str(self.help.shoes) + "\n") #Shoes
        file.write(str(self.help.dress) + "\n\n") #Dresses
        #file.write(str(self.help.fees)) #Fee

        file.write(str(self.prices.books) + "\n") #Books
        file.write(str(self.prices.bags) + "\n") #Bags
        file.write(str(self.prices.shoes) + "\n") #Shoes
        file.write(str(self.prices.dress)) #Dresses
        file.close()
    
    def ExtractData(self, pathIe):
        self.path = pathIe
        file = open(pathIe, "r")

        self.standard = int(file.readline())
        file.readline()
        self.help.books = int(file.readline())
        self.help.bags = int(file.readline())
        self.help.shoes = int(file.readline())
        self.help.dress = int(file.readline())
        #self.help.fees = int(file.readline())
        file.readline()
        self.prices.books = int(file.readline())
        self.prices.bags = int(file.readline())
        self.prices.shoes = int(file.readline())
        self.prices.dress = int(file.readline())

        file.close()



class Donor:
    def __init__(self):
        self.name
        self.contact

class Volunteer:
    def __init__(self):
        self.name = " "
        self.contact = Contact()
        self.id = " "
        self.password = " "
    
    def UpdateFileV(self, pathF):
        self.pathF = pathF
        file = open(pathF, "w")
        file.write(self.id + "\n")
        file.write(self.password + "\n\n")
        file.write(self.name + "\n")
        file.write(self.contact.address + "\n")
        file.write(str(self.contact.phone) + "\n")
        file.write(self.contact.email + "\n")
        file.close()
    
    def ExtractData(self, PathV):
        file = open(PathV, "r")

        self.id = file.readline().rstrip()
        self.password = file.readline().rstrip()
        file.readline()
        self.name = file.readline().rstrip()
        self.contact.address = file.readline().rstrip()
        self.contact.phone = int(file.readline())
        self.contact.email = file.readline().rstrip()

        file.close()
    '''
    def printV(self):
        print(self.id)
        print(self.password + "\n")
        print(self.name)
        print(self.contact.address)
        print(self.contact.phone)
        print(self.contact.email)
    '''


class Student:
    def __init__(self):
        self.name = " "
        self.school = " "
        self.id = " "
        self.dob = " "
        self.standard = 0
        self.gender = " "
        self.parentalIncome = 0
        self.percentage = 0
        self.help = Help()
        self.NeedHelp = 0
        self.HelpRecived = 0
    
    def UpdateFile(self, pathS):
        file = open(pathS, "w")
        file.write(self.id + "\n\n")
        
        file.write(self.name + "\n") #Name
        file.write(self.school + "\n") #School
        file.write(str(self.dob) + "\n")  #DOB
        file.write(str(self.standard) + "\n") #Class
        file.write(str(self.gender) + "\n") #Gender
        file.write(str(self.parentalIncome) + "\n") #Parental Income
        file.write(str(self.percentage) + "\n\n") #Percentage

        file.write("Help Needed: " + "\n")
        file.write(str(self.help.books) + "\n") #Books
        file.write(str(self.help.bags) + "\n") #Bags
        file.write(str(self.help.shoes) + "\n") #Shoes
        file.write(str(self.help.dress) + "\n") #Dresses
        file.write(str(self.help.fees) + "\n\n") #Fee
        file.write(str(self.HelpRecived))
        file.close()
    
    def ExtractData(self, GivenPath):
        file = open(GivenPath, "r")

        self.id = file.readline().rstrip()
        file.readline()
        self.name = file.readline().rstrip()
        self.school = file.readline().rstrip()
        self.dob = file.readline().rstrip()
        self.standard = int(file.readline())
        self.gender = file.readline().rstrip()
        self.parentalIncome = int(file.readline())
        self.percentage = int(file.readline())
        file.readline()
        file.readline()
        self.help.books = int(file.readline())
        self.help.bags = int(file.readline())
        self.help.shoes = int(file.readline())
        self.help.dress = int(file.readline())
        self.help.fees = int(file.readline())
        file.readline()
        self.HelpRecived = int(file.readline())
        file.close()

        self.Needshelp()

    def Needshelp(self):
        temp = self.help.books + self.help.bags + self.help.shoes + self.help.dress + self.help.fees

        if temp == 0:
            self.NeedHelp = 0
        
        else:
            self.NeedHelp = 1
    '''
    def PrintStud(self):
        print(self.id + "\n")
        print(self.name)
        print(self.school)
        print(str(self.dob))
        print(str(self.standard))
        print(str(self.gender))
        print(str(self.parentalIncome))
        print(str(self.percentage) + "\n")
        print("help: ")
        print(str(self.help.books))
        print(str(self.help.bags))
        print(str(self.help.shoes))
        print(str(self.help.dress))
        print(str(self.help.fees))
    '''


PlanOptions = ["Semi_Annually", "Annually"]

class PledgedDonor:
    def __init__(self):
        self.name = " "
        self.id = " "
        self.contact = Contact()
        self.password = " "
        self.amount = 0
        self.donationPlan = " "
        self.notified = 0
        self.donated = 0
        self.ToBeNotified = 0

    def UpdateFile(self, pathF):

        self.pathF = pathF
        file = open(pathF, "w")
        file.write(self.id + "\n")
        file.write(self.password + "\n\n")
        file.write(self.name + "\n")    #Name
        file.write(self.contact.address + "\n") #Address
        file.write(str(self.contact.phone) + "\n")  #Phone
        file.write(self.contact.email + "\n")   #Email 
        file.write(str(self.amount) + "\n") #Pledged Amount 
        file.write(self.donationPlan + "\n")    #Donation Plan 
        file.write(str(self.notified) + "\n")    #Notified
        file.write(str(self.donated) + "\n") #Donated
        file.close()
    
    def ExtractData(self, path3):
        self.pathF = path3
        file = open(path3, "r")

        self.id = file.readline().rstrip()
        self.password = file.readline().rstrip()
        file.readline()
        self.name = file.readline().rstrip()
        self.contact.address = file.readline().rstrip()
        self.contact.phone = int(file.readline())
        self.contact.email = file.readline().rstrip()
        self.amount = int(file.readline())
        self.donationPlan = file.readline().rstrip()
        self.notified = int(file.readline())
        self.donated = int(file.readline())
        file.close()
    '''
    def PrintDonor(self):
        print(self.id)
        print(self.password + "\n")
        print(self.name)
        print(self.contact.address)
        print(self.contact.phone)
        print(self.contact.email)
        print(self.amount)
        print(self.donationPlan)
        print(self.notified)
        print(self.donated)
    '''
