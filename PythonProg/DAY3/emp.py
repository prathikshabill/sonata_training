class Employee:
    def __init__(self,fname,lname,address):
        self.firstname=fname
        self.lastname=lname
        self.address=address

    def getFullname(self):
        return self.firstname + " "+ self.lastname

emp1 = Employee("prathiksha","billava","udupi")
fullname=emp1.getFullname()
print(fullname)