class Employee:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
       #self.address=address

    def getFullname(self):
        return self.firstname + " "+ self.lastname

class address:
    def __init__(self,*address):
        self.addr=address
    def add(self):
        return self.addr

emp1 = Employee("prathiksha","billava")
fullname=emp1.getFullname()
print(fullname)
print(emp1.firstname[0],emp1.lastname[0])
add1=address("udupi","mangalore","kumta")
