from singleaddress import *
class AddressBook(SingleAddress):
    def __init__(self, lastname, firstname, streetaddress, city, state, country, postalcode):
       super().__init__(self, lastname, firstname, streetaddress, city, state, country, postalcode)

    def data(self):
        dict = {"Rhea":"KR Road", "Risha":"Church street"}


address3=SingleAddress("B","Vaish","KR Road","Bengaluru","Karnataka","India","560004")

