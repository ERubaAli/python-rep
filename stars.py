def DTriangle ():
    NRows = int (input('enter the number: '))
    i=0
    for i in range (NRows):
        j=0
        while j < (NRows-i):
            print("* ", end="")
            j+=1
        print()
        i+=1

def DTri(NRows):
    #NRows = int (input('enter the number: '))
    for i in range (NRows-1,0,-1):          # changed NRows to NRows-1 to eleminate 1st row to make a diamond
        for j in range (0,NRows-i):
            print(end=" ")
        for j in range (0,i):
            print("*",end=" ")
        print()

def UTri():
    NRows = int (input('enter the number: '))
    for i in range (0,NRows):
        for j in range (0,NRows-i-1):
            print(end=" ")
        for j in range (0,i+1):
            print("*",end=" ")
        print()
    DTri(NRows)
UTri()
""" DTri()
"""
DTriangle() 