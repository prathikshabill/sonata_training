class Leave:
    def __init__(self,Employeeid,name,LeaveBalance):
        self.Employeeid=Employeeid
        self.name=name
        self.LeaveBalance=LeaveBalance
    def applyleave(self):
        return self.Employeeid + " " + self.name + " " + self.LeaveBalance

employee = Leave("123","Prat","20")
print(employee.applyleave())
