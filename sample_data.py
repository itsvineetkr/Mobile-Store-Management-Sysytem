import mysql.connector as mysql

mysqlpass = input("Enter your mySQL password (if there is no password type clear): ")
mysqlpass = "" if mysqlpass == "clear" else mysqlpass

db = mysql.connect(host="localhost", user="root", passwd=mysqlpass, database="msms")
cur = db.cursor()

d1 = "delete from items"
d2 = "delete from stocks"
q1 = "insert into items values('0001','Samsung','GS22 Ultra',6,128,6.8,'FHD+',\
'Super Amoled','Exynos 2200',5000,'12MP+12MP+48MP','10MP',138000,'A great flagship phone')"
q2 = "insert into stocks values('0001',25)"
q3 = "insert into items values('0002','Mi','A1',4,64,6.1,'FHD','LCD Panel',\
'Snapdragon 625',3500,'12MP+12MP','5MP',13999,'Evergreen phone with best camera')"
q4 = "insert into stocks values('0002',18)"
q5 = "insert into items values('0003','iPhone','14 Pro',6,128,6.5,'FHD+','Amoled',\
'Bionic Chip 15',4500,'12MP+12MP+48MP','10MP',125000,'It is Apple')"
q6 = "insert into stocks values('0003',23)"
q7 = "insert into items values('0004','Realme','X7 Max',6,128,6.1,'FHD+','Amoled',\
'Snapdragon 720G',4500,'12MP+48MP+8MP','10MP',24999,'Nice phone for everyday use')"
q8 = "insert into stocks values('0004',34)"

for i in d1, d2, q1, q2, q3, q4, q5, q6, q7, q8:
    cur.execute(i)

db.commit()
db.close()
