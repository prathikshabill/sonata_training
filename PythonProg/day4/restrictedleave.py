class RestrictedLeave:
    def __init__(self, employeeid, name, leavebalance, Reasonforapplyingleave, DateOfBirth):
        self.eid = employeeid
        self.name = name
        self.lbalance = leavebalance
        self.rfal = Reasonforapplyingleave
        self.DOB = DateOfBirth

    def date(self):
        return self.eid + " " + self.name + " " + self.lbalance + " " + self.rfal + " " + self.DOB


emp = RestrictedLeave("123", "Prat", "20", "Sick", "18/04/2000")
print(emp.date())