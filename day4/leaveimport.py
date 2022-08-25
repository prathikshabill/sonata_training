from day4.leave import Leave
from basketofleave import BasketOfLeave
from restrictedleave import RestrictedLeave

l1=Leave(827,"Prat","20")
print(l1.ApplyLeave())
l2=BasketOfLeave(827,"Prat","20","Medical Emergency")
l3=RestrictedLeave(827,"Prat","20","18-04-2000")



#l2.ApplyLeave()
#l3.ApplyLeave()

