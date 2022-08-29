class BasketOfLeave:
    def __init__(self, employeeid, name, leavebalance, Reasonforapplyingleave):
        self.eid = employeeid
        self.name = name
        self.lbalance = leavebalance
        self.reasonfor = Reasonforapplyingleave

    def reason(self):
        return self.eid + " " + self.name + " " + self.lbalance + " " + self.reasonfor


employee = BasketOfLeave("123", "Prat", "20", "Sick")
print(employee.reason())