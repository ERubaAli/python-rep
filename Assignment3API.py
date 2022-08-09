from flask import Flask,request
import sqlite3

app=Flask(__name__)

conn = sqlite3.connect('Employees.db',check_same_thread=False)
cur = conn.cursor()

@app.route("/Tcreate", methods=[ 'POST','GET'])       #create tables
def CreateT():
   TName=request.args.get('TName')
   colDat=request.args.get('colDat')
   query1=f"CREATE TABLE {TName} ({colDat});"
   cur.execute(query1)
   conn.commit()
  
   return "DONE"

     

#--------------------------------------------------

# @app.route("/inValues",methods=['POST','GET'])  #insert data to tables
# def insert():
#    myTable=request.args.get('myTable')
#    colm=request.args.get('colm')
#    val=request.args.get('val')
#    # myTable="employee"
#    # colm="(empID,first_name,last_name,phone,depID)"
#    # val="(2,'Ahmad','Anas',797353446,3)"
#    query3=f'INSERT INTO {myTable} {colm} VALUES {val};'
   
#    cur.execute(query3)
#    conn.commit()
   
#    return "DONE"
#-----------------------------------------------------

# @app.route("/showRes")        #showing results using select inner join
# def selectR():
#     table1=request.args.get('table1')
#     table2=request.args.get('table2')
#     FK=request.args.get('FK')

#     queryS=f'SELECT * FROM {table1} INNER JOIN {table2} ON {table1}.{FK}={table2}.{FK};'

#     cur.execute(queryS)
#     Result=cur.fetchall()
#     conn.commit()
#     print(Result)
#     return "DONE"

#------------------------------------------------------------------------

# @app.route("/Deleting", methods=['POST','GET'])           #deleting a record
# def DeleteR():

#     TBL=request.args.get('TBL')
#     CL=request.args.get('CL')
#     CLI=request.args.get('CLI')

#     queryD=f"DELETE FROM {TBL} WHERE {CL} = {CLI};"
    
#     cur.execute(queryD)
#     conn.commit()

#     return "DONE"

#-----------------------------------------------

# @app.route("/updating",  methods=['POST','GET'])            #updating a value on a condition
# def updateC():

#     TBL=request.args.get('TBL')
#     oldCol=request.args.get('oldCol')
#     oldVal=request.args.get('oldVal')
#     newCol=request.args.get('newCol')
#     newVal=request.args.get('newVal')
#     queryU=f'UPDATE {TBL} SET {newCol} = {newVal} WHERE {oldCol} = {oldVal} ;'

#     cur.execute(queryU)
#     conn.commit()
    
#     return "DONE"




if __name__=="__main__":
    app.run()

conn.close()