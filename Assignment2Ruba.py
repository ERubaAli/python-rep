class Location :
    def __init__(self,city,street,BldngNo) :
        self.city=city
        self.street=street
        self.BldngNo=BldngNo


class Residence :
    #two lists to categorize luxury houses and normal ones
    LuxList=[]
    NormList=[]

    def __init__(self,ownerName,area,price,rooms,city,street,BldngNo) :
        self.__ownerName=ownerName
        self.__area=area
        self.__price=price
        self.__rooms=rooms
        self.location=Location(city,street,BldngNo)

    def getOwner(self):
        return self.__ownerName
    
    def getArea(self):
        return self.__area
    
    def getPrice(self):
        return self.__price
    
    def getRooms(self):
        return self.__rooms

    def getLocation(self):
        return self.location.city, self.location.city, self.location.BldngNo

    def setPrice(self,newPrice):
        self.__price=newPrice

    def setRooms(self,newRooms):
        self.__rooms=newRooms

#categorize houses based on price
    def checkLuxury(self):
        if self.__price >200000:
            Residence.LuxList.append(self.__ownerName)
        else : Residence.NormList.append(self.__ownerName)
        return Residence.LuxList , Residence.NormList

#if the house is in Amman then add a tax to the price
    def CapitalTax(self):
        capital1=self.location.city
        capital2='AMMAN'
        if capital1.casefold()==capital2.casefold():            #manage the upper and lower case entries
            self.__price= self.__price*1.02
        return self.__price


class Villa(Residence):
    def __init__(self, ownerName, area, price, rooms, city, street, BldngNo,TerraceArea):
        super().__init__(ownerName, area, price, rooms, city, street, BldngNo)
        self.TerraceArea=TerraceArea

    def getTerraceArea(self):
        return self.TerraceArea

#calculate inner and outer area
    def TotalArea(self):                        
        TotalArea=Residence.getArea(self)+self.getTerraceArea()
        return TotalArea

    def checkLuxury(self):                              #OVERRIDING
        if Residence.getPrice(self) >300000:
            Residence.LuxList.append(self.getOwner())
        else : Residence.NormList.append(self.getOwner())
        return Residence.LuxList , Residence.NormList


class Apartment(Residence):
    def __init__(self, ownerName, area, price, rooms, city, street, BldngNo, floorNo,serFees):
        super().__init__(ownerName, area, price, rooms, city, street, BldngNo)
        self.floorNo=floorNo
        self.serFees=serFees

    def getFloor(self):
        return self.floorNo


    def CapitalTax(self):                                       #OVERRIDING
        capital1=self.location.city
        capital2='AMMAN'
        if capital1.casefold()==capital2.casefold():            #manage the upper and lower case entries
            self.price= self.getPrice()*1.01
        return self.price

    def serviceFees(self):
        if self.floorNo ==0:
            return self.serFees
        else:
            return self.serFees*1.1


# Res1=Residence('Mohammad',250,250000,5,'Amman','Huriya','15C')
# Res1.checkLuxury()
# Res1.CapitalTax()
# Res2=Residence('Gaith',300,270000,5,'Amman','Der Ghbar','14B')
# Res2.checkLuxury()
# Res2.CapitalTax()
# Res3=Residence('Salim',200,100000,5,'ALSalt','Sbehi','10B')
# Res3.checkLuxury()
# Res3.CapitalTax()

# V1=Villa('Kamal',350,350000,5,'Amman','Huriya','15C',50)
# print ("\nTotal area with terrace is : " , V1.TotalArea(),"\n")
# V1.checkLuxury()

# AP1=Apartment('Samir',150,70000,5,'Amman','Huriya','15C',0,10)
# AP1.CapitalTax()
# AP1.checkLuxury()
# AP1.serviceFees()
# print("the new price is : ", AP1.CapitalTax())
# print("your service fee is : " , AP1.serviceFees(),"\n")

# AP2=Apartment('Tariq',150,60000,4,'Amman','Huriya','15C',2,10)
# AP2.CapitalTax()
# AP2.checkLuxury()
# AP2.serviceFees()
# print("the new price is : ", AP2.CapitalTax())
# print("your service fee is : " , AP2.serviceFees(),"\n")

# print("Luxurous house owners are : ", Residence.LuxList)
# print("Normal house owners are : ",Residence.NormList,"\n")

# print (Res1.getOwner() , " , price is :  ", Res1.getPrice())
# print (Res2.getOwner() , " , price is :  ", Res2.getPrice())
# print (Res3.getOwner() , " , price is :  ", Res3.getPrice(),"\n")



