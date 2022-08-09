
L1S=input(" Enter a list ")
L1=L1S.split()                  #split the string to make a list
dict1 = {}

 #loop through the list item by item and check 
 # if it's already in the dictionary then add 1
 #  to its value, otherwise keep the value 1
for item in L1:                
    if item in dict1:
      dict1[item] +=1
    else:
      dict1[item] =1

print(dict1)