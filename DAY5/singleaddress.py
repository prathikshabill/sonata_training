class SingleAddress:
    def __init__(self,lastname,firstname,streetaddress,city,state,country,postalcode):
        self.lname = lastname
        self.fname = firstname
        self.streetaddress = streetaddress
        self.city = city
        self.state= state
        self.country=country
        self.postal = postalcode
        SingleAddress.lname=lastname

    def FetchAddress(self):
        return self.lname + " " + self.fname + " " + self.streetaddress + " " + self.city + " " + self.state +" " + self.country +" " + self.postal


address1 = SingleAddress("B","Rhea","KR Road","Bengaluru","Karnataka","India","560004")
address2 = SingleAddress("c","Risha","Church street","Bengaluru","Karnataka","India","560008")
#print(address1.FetchAddress())
