import mysql.connector as mysql

mysqlpass = input("Enter your mySQL password (if there is no password type clear) : ")
mysqlpass = "" if mysqlpass == "clear" else mysqlpass

mydb = mysql.connect(host="localhost", user="root", passwd=mysqlpass)
temp_cur = mydb.cursor()

try:
    temp_cur.execute("create database msms")
    temp_cur.execute("create database userdata")
except:
    temp_cur.execute("drop database msms")
    temp_cur.execute("drop database userdata")
    temp_cur.execute("create database msms")
    temp_cur.execute("create database userdata")

mydb.close()

db = mysql.connect(host="localhost", user="root", passwd=mysqlpass, database="msms")
cur = db.cursor()

q1 = """
create table creds(
    userid int primary key,
    userpass varchar(20) not null
)"""
q2 = """
create table items(
    itemid varchar(5) primary key,
    company varchar(20) not null,
    model varchar(20) not null,
    ram int,
    storage int,
    scrsize float,
    resolution varchar(10),
    scrtype varchar(20),
    pro varchar(20),
    battery int,
    rcamera varchar(20),
    fcamera varchar(20),
    price int not null,
    review varchar(200))"""
q3 = """
create table loginhistory(
    userid int,
    username varchar(20),
    date varchar(20)
)
"""
q4 = """
create table stocks(
    itemid varchar(5) primary key,
    stock int
)
"""
q5 = """
create table purchasehistory(
    itemid varchar(5),
    itemname varchar(40),
    userid int,
    usold int,
    date varchar(20)
)"""
q6 = "insert into creds values(1000,'admin')"
q7 = "create table users(userid int,username varchar(20))"
q8 = "insert into users values(1000,'admin')"
q9 = "create table revenue(revenue int(20))"
q10 = "insert into revenue values(0)"

for i in q1, q2, q3, q4, q5, q6, q7, q8, q9, q10:
    cur.execute(i)

db.commit()
db.close()
