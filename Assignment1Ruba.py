from string import punctuation
import string

def LoopList(i=0):                                                      #funtion to loop through the list of strings
    for i in range(leng) :                                              #looping according to list's length
        x=L1[i]                                                         #assign x the string in L1[i]
        j=0                                                             
        c=0
        while j < leng :                                                #looping to compare the value stored -- 
            if x==L1[j]:                                                #--with all list items
                c+=1
            j+=1
        dict_1[x]=c
        i+=1

par = str(input('enter your text'))                                   # user enters text
Npar=par.casefold()                                                   #change to lower case
Npar=Npar.translate(str.maketrans(' ',' ', string.punctuation))       #change to no punctuation
L1 = Npar.split()                                                     #store string in a list
leng=len(L1)                                                          #list's length
dict_1=dict()                                                         #new dictionary
print(L1)



LoopList()                                                              #calling
print (dict_1)                                                          #print final dictionary
    
