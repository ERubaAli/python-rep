from Assignment2Ruba import Residence
from Assignment2Ruba import Villa
from Assignment2Ruba import Apartment



Res1=Residence('Mohammad',250,250000,5,'Amman','Huriya','15C')
Res1.checkLuxury()
Res1.CapitalTax()
Res2=Residence('Gaith',300,270000,5,'Amman','Der Ghbar','14B')
Res2.checkLuxury()
Res2.CapitalTax()
Res3=Residence('Salim',200,100000,5,'ALSalt','Sbehi','10B')
Res3.checkLuxury()
Res3.CapitalTax()

V1=Villa('Kamal',350,350000,5,'Amman','Huriya','15C',50)
print ("\nTotal area with terrace is : " , V1.TotalArea(),"\n")
V1.checkLuxury()

AP1=Apartment('Samir',150,70000,5,'Amman','Huriya','15C',0,10)
AP1.CapitalTax()
AP1.checkLuxury()
AP1.serviceFees()
print("the new price is : ", AP1.CapitalTax())
print("your service fee is : " , AP1.serviceFees(),"\n")

AP2=Apartment('Tariq',150,60000,4,'Amman','Huriya','15C',2,10)
AP2.CapitalTax()
AP2.checkLuxury()
AP2.serviceFees()
print("the new price is : ", AP2.CapitalTax())
print("your service fee is : " , AP2.serviceFees(),"\n")

print("Luxurous house owners are : ", Residence.LuxList)
print("Normal house owners are : ",Residence.NormList,"\n")

print (Res1.getOwner() , " , price is :  ", Res1.getPrice())
print (Res2.getOwner() , " , price is :  ", Res2.getPrice())
print (Res3.getOwner() , " , price is :  ", Res3.getPrice(),"\n")
