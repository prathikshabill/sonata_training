import MySQLdb

mydb = MySQLdb.connect(host="localhost",user="root",password="root@123",database="python")

mycursor=mydb.cursor()



mycursor.execute("SELECT *,basic+hra FROM employee")
myresult = mycursor.fetchall()

for x in myresult:
  print(x[0] , x[1] , x[2],x[3] ,x[4])

