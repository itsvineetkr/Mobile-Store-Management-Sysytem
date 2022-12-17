from tabulate import tabulate
import mysql.connector as mysql
from datetime import datetime


def add_item():
    """
    This method will add an item in items table

    Args = None
    Return = None
    """
    itemid = input("Enter item id: ")
    comp = input("Enter company name: ")
    model = input("Enter model name: ")
    ram = input("Enter RAM: ")
    storage = input("Enter storage: ")
    scrsize = input("Enter screen size: ")
    resolution = input("Enter resolution :")
    scrtype = input("Enter screen type: ")
    pro = input("Enter processor info: ")
    battery = input("Enter battery capacity: ")
    rcamera = input("Enter rear camera info: ")
    fcamera = input("Enter front camera info: ")
    price = input("Enter price: ")
    info = input("Any additional info: ")
    stock = input("Enter stock: ")
    q1 = "insert into items values('{}','{}','{}',{},{},{},'{}','{}','{}',{},'{}','{}',{},'{}')".format(
        itemid,
        comp,
        model,
        ram,
        storage,
        scrsize,
        resolution,
        scrtype,
        pro,
        battery,
        rcamera,
        fcamera,
        price,
        info,
    )
    cur.execute(q1)
    q2 = "insert into stocks values('{}',{})".format(itemid, stock)
    cur.execute(q2)
    db.commit()


def see_item():
    """
    This method will show items table

    Args = None
    Return = None
    """
    cur.execute("select * from items")
    d = cur.fetchall()
    header = [
        "item id",
        "company",
        "model",
        "ram",
        "storage",
        "screen size",
        "resolution",
        "screen type",
        "processor",
        "battery",
        "rcamera",
        "fcamera",
        "price",
        "additional info",
    ]
    print(tabulate(d, headers=header, tablefmt="pretty"))


def see_stocks():
    """
    This method will show stocks table

    Args = None
    Return = None
    """
    cur.execute("select * from stocks")
    d = cur.fetchall()
    header = ["item id", "stocks"]
    print(tabulate(d, headers=header, tablefmt="pretty"))


def see_login_history():
    """
    This method will show login history table

    Args = None
    Return = None
    """
    cur.execute("select * from loginhistory")
    d = cur.fetchall()
    header = ["User id", "Username", "Date and Time"]
    print(tabulate(d, headers=header, tablefmt="pretty"))


def update_spec():
    """
    This method will update details of an item in items table

    Args = None
    Return = None
    """
    itemid = input("Enter item id you want to update: ")
    s = "Enter coloumn name (itemid,company,model,ram,storage,scrsize,resolution,\
    scrtype,pro,battery,rcamera,fcamera,price,info)\n"
    col = input(s)
    n = input("Enter new data: ")
    if col in [
        "itemid",
        "company",
        "model",
        "resolution",
        "scrtype",
        "pro",
        "rcamera",
        "fcamera",
        "review",
    ]:
        q = "update items set {}='{}' where itemid='{}'".format(col, n, itemid)
        cur.execute(q)
    elif col in ["ram", "storage", "scrsize", "battery", "price"]:
        q = "update items set {}={} where itemid='{}'".format(col, n, itemid)
        cur.execute(q)
    db.commit()


def update_stocks():
    """
    This method will update stock of an item in stocks table

    Args = None
    Return = None
    """
    itemid = input("Enter itemid whose stock has to be updated: ")
    stock = input("Enter new stock: ")
    q = "update stocks set stock={} where itemid='{}'".format(stock, itemid)
    cur.execute(q)
    db.commit()


def delete_items():
    """
    This method will delete details of an item in items table and stocks table

    Args = None
    Return = None
    """
    itemid = input("Enter itemid whose data has to be deleted: ")
    q1 = "delete from items where itemid='{}'".format(itemid)
    cur.execute(q1)
    q2 = "delete from stocks where itemid='{}'".format(itemid)
    cur.execute(q2)
    db.commit()


def change_pass(userid, password):
    """
    This method will change password detail in creds table

    Args = userid, password
    Return = None
    """
    oldpass = input("Enter old password: ")
    if oldpass == password:
        newpass = input("Enter new password: ")
        repass = input("Confirm password: ")
        while True:
            if newpass == repass:
                q = "update creds set userpass='{}' where userid={};".format(
                    newpass, userid
                )
                cur.execute(q)
                db.commit()
                break
            else:
                print("Password doesn't match!")
                repass = input("Retry your password: ")
    else:
        print("You entered wrong password!")
        return None


def login_history(userid, username):
    """
    This method will update login history in loginhistory table

    Args = userid
    Return = None
    """
    date = str(datetime.now())[:19]
    q = "insert into loginhistory values({},'{}','{}');".format(userid, username, date)
    cur.execute(q)
    db.commit()


def purchase_history(username, userid=1000):
    """
    This method can be used see purchase history of users by admin
    or a user can use to see his own purchase history.

    Args = username, userid {in case of user only}
    Returns = None
    """

    if username == "admin":
        cur.execute("select * from purchasehistory")
        d = cur.fetchall()
        header = ["Item id", "Item name", "User id", "Unit Sold", "Date and Time"]
        print(tabulate(d, headers=header, tablefmt="pretty"))
    else:
        cur.execute(
            "select itemname,usold,date from purchasehistory where userid={}".format(
                userid
            )
        )
        d = cur.fetchall()
        header = ["Item name", "Unit Purchased", "Date and Time"]
        print(tabulate(d, headers=header, tablefmt="pretty"))


def menu():
    """
    This method will show login page and take input of user's choice

    Args = None
    Return = str {choice: admin, user, new, exit}
    """
    print()
    p1 = [[" Mobile Store Management System "]]
    p2 = [
        [],
        ["How would you like login?"],
        [],
        ['To enter as Admin type "admin"'],
        ['To enter as User type "user"'],
        ['To create a new user type "new"'],
        ['To exit type "exit"'],
    ]

    print(tabulate(p1, tablefmt="double_outline"))
    print(tabulate(p2, tablefmt="double_outline", headers=["Login page"]))
    print()
    choice = input("Enter your choice: ")
    return choice


def append_wishlist(username, itemid):
    """
    This method will add user's choice item into his wishlist in userdata database

    Args = username, itemid
    Returns = None
    """
    cur.execute("select * from items where itemid='{}'".format(itemid))
    d = cur.fetchall()[0]
    cur2.execute(
        "insert into {} values('{}','{}','{}')".format(username, d[0], d[1], d[2])
    )
    db2.commit()


def see_wishlist(username):
    """
    This method will show wishlist table from userdata database

    Args = username
    Return = None
    """
    cur2.execute("select * from {}".format(username))
    d = cur2.fetchall()
    header = ["Item id", "Company", "Model"]
    print(tabulate(d, headers=header, tablefmt="pretty"))


def purchase(username, userid, itemid, units):
    """
    This method will update:
    1. stocks table from msms
    2. purchasehistory table from msms
    3. following user's wishlist in userdata

    Args = username, userid, itemid, units
    Return = None
    """
    cur.execute("select * from stocks where itemid='{}'".format(itemid))
    d = cur.fetchall()
    if int(units) <= int(d[0][1]):
        date = str(datetime.now())[:19]
        cur.execute("select * from items where itemid='{}'".format(itemid))
        d = cur.fetchall()[0]
        q1 = "insert into purchasehistory values('{}','{}',{},{},'{}')".format(
            itemid, d[1] + " " + d[2], userid, units, date
        )
        cur.execute(q1)
        q2 = "update stocks set stock=stock-{} where itemid='{}'".format(units, itemid)
        cur.execute(q2)
        q3 = "delete from {} where itemid='{}'".format(username, itemid)
        cur2.execute(q3)
        db.commit()
        db2.commit()
        price = int(units) * int(d[-2])
        l = [
            [
                "You have successfully purchased {} {} on date {}".format(
                    d[1], d[2], date
                )
            ],
            ["You have to pay {} Rupees in the reception.".format(price)],
            ["Thank you {} for shopping from our store!".format(username.capitalize())],
        ]
        print(tabulate(l, tablefmt="double_outline"))
        cur.execute("update revenue set revenue=revenue+{}".format(price))
        db.commit()

    else:
        print("This much stock isn't available {}".format(username))


def alter_user(task):
    """
    This method can be used to see or delete data of a user.

    Args = task {see, delete}
    Returns = None
    """
    if task == "see":
        cur.execute("select * from users")
        d = cur.fetchall()
        header = ["User id", "Username"]
        print(tabulate(d, headers=header, tablefmt="rst"))
    elif task == "delete":
        username = input("Enter username: ")
        cur.execute("select userid from users where username='{}'".format(username))
        userid = cur.fetchall()[0][0]
        cur.execute("delete from users where username='{}'".format(username))
        cur.execute("delete from creds where userid={}".format(userid))
        cur2.execute("drop table {}".format(username))
        db.commit()
        db2.commit()
        print("User {} has been deleted!".format(username.capitalize()))


def user_page(userid, username, password):
    """
    This method is for user interface
    There is a while loop which will run till user types "exit".
    It is a menu driven code which will ask for user's choice
    (numbers from 1 to 6 assigned for different things) and will perform various tasks.
    If user chooses option 6 (to return to login page) then this function will call login_page()
    If user enters exit then this function will end.

    Args = userid, username, password
    Return = None
    """
    print(
        tabulate(
            [["Hello {}!".format(username.capitalize())]], tablefmt="rounded_outline"
        )
    )
    login_history(userid, username)
    c = ""
    while c != "exit":
        print()
        t = [
            ["To see items details press 1"],
            ["To add any item into wishlist press 2"],
            ["To see wishlist press 3"],
            ["To purchase any item press 4"],
            ["To see your purchase history press 5"],
            ["To change password press 6"],
            ["To go back to login page press 7"],
            ['To exit type "exit"'],
        ]
        print(tabulate(t, tablefmt="double_outline"))
        print()
        c = input("Enter what you have choosen: ")
        if c == "1":
            see_item()
        elif c == "2":
            itemid = input("Enter item's id which is to be added in wishlist: ")
            append_wishlist(username, itemid)
        elif c == "3":
            see_wishlist(username)
        elif c == "4":
            itemid = input("Enter the item's id: ")
            units = input("Enter number of units you want to purchase: ")
            purchase(username, userid, itemid, units)
        elif c == "5":
            purchase_history(username, userid)
        elif c == "6":
            change_pass(userid, password)
        elif c == "7":
            login_page()
            return None
        elif c == "exit":
            break


def admin_page(password):
    """
    This method will generate:
    A while loop will start which will run till user types "exit".
    It is a menu driven code which will ask for user's choice
    (numbers from 1 to 9 assigned for different things) and will perform
    various tasks. If user chooses option 9 (to return to login page)
    then this function will call it self again if user enters exit
    then this function will end and will return None

    Args = password
    Returns = None
    """
    c = ""
    print(tabulate([["Hello your majesty!"]], tablefmt="rounded_outline"))
    login_history(1000, "admin")
    while c != "exit":
        print()
        t = [
            ["To add item details press 1"],
            ["To see items details press 2"],
            ["To update item details press 3"],
            ["To update item stocks press 4"],
            ["To delete item details press 5"],
            ["To change password press 6"],
            ["To see login history press 7"],
            ["To see stocks info press 8"],
            ["To see revenue generated press 9"],
            ["To see purchase history press 10"],
            ["To see users press 11"],
            ["To delete any user press 12"],
            ["To go back to login page press 13"],
            ['To exit type "exit"'],
        ]

        print(tabulate(t, tablefmt="double_outline"))
        print()
        c = input("Enter what you have choosen: ")

        switch = {
            "1": add_item,
            "2": see_item,
            "3": update_spec,
            "4": update_stocks,
            "5": delete_items,
            "7": see_login_history,
            "8": see_stocks,
        }

        if c == "6":
            change_pass(1000, password)
        elif c == "9":
            cur.execute("select * from revenue")
            d = cur.fetchall()[0][0]
            print(
                tabulate(
                    [["Revenue generated till now is: {} INR".format(d)]],
                    tablefmt="pretty",
                )
            )
        elif c == "10":
            purchase_history("admin")
        elif c == "11":
            alter_user("see")
        elif c == "12":
            alter_user("delete")
        elif c == "13":
            login_page()
            return None
        elif c == "exit":
            break
        else:
            switch.get(c)()


def login_page():
    """
    This method is for login interface
    Here we are running menu function and saving its returned value
    in a variable named choice.
    Here choice can contain (admin, user or new).

    Then we are applying conditions.

    If choice is admin then we will ask for password and will
    match it with the fetched passwords from creds table and
    if password is right then it will call admin_page function

    If choice is user then we will take username as input
    and will check if it exists it it exists then we will
    take password and then match it with data in creds and
    if it is correct then userpage function will run.

    If choice is new then we will take new username and check
    if it already exists or not if it does then a message will
    display that user already exists and if not then we will
    generate a new userid and update users table, creds table
    and create a new table in userdata database and
    name it as user's name.

    Args = None
    Returns = None
    """
    choice = menu()

    if choice == "admin":
        input_password = input("Enter password: ")
        cur.execute("select * from creds")
        d = cur.fetchall()
        if input_password == d[0][1]:
            admin_page(d[0][1])
        else:
            print("Password is incorrect")
            return None

    elif choice == "new":
        username = input("Enter new user's name: ").lower()
        cur.execute("select * from users order by userid")
        d = cur.fetchall()
        l = []
        for i, j in d:
            l.append(j)
        if username in l:
            print()
            print(
                tabulate(
                    [["User name already exists! try again."]],
                    tablefmt="rounded_outline",
                )
            )
            print()
            login_page()
            return None
        else:
            userid = (d[-1][0]) + 1
            password = input("Enter password: ")
            rpass = input("Confirm your password: ")
            if rpass == password:
                cur.execute(
                    "insert into creds values({},'{}')".format(userid, password)
                )
                cur.execute(
                    "insert into users values({},'{}')".format(userid, username)
                )
                cur2.execute(
                    "create table {}(itemid varchar(5) primary key,company varchar(20),model varchar(20))".format(
                        username
                    )
                )
                db.commit()
                print(
                    tabulate(
                        [["User created successfully"]], tablefmt="rounded_outline"
                    )
                )
            else:
                print("Passwords do not match try again.")
                login_page()
        print(
            tabulate(
                [
                    ["If you want to go to login page then press 1"],
                    ["If you want to exit then press 2"],
                ],
                tablefmt="rounded_outline",
            )
        )
        x = int(input("Enter choice: "))
        if x == 1:
            login_page()
            return None
        elif x == 2:
            pass

    elif choice == "user":
        username = input("Enter your user name: ").lower()
        cur.execute("select * from users where username='{}'".format(username))
        d = cur.fetchall()
        if len(d) != 0:
            userid = d[0][0]
            cur.execute("select * from creds where userid={}".format(userid))
            password = cur.fetchall()[0][1]
            passwd = input("Enter your password: ")
            if password == passwd:
                user_page(userid, username, password)
            else:
                print()
                print(
                    tabulate(
                        [["You entered wrong password try again later!"]],
                        tablefmt="rounded_outline",
                    )
                )
                print()
                login_page()

        else:
            print("Such username doesn't exist!")
            login_page()

    elif choice == "exit":
        pass

    else:
        login_page()
        return None


if __name__ == "__main__":
    mysqlpass = input(
        "Enter your mySQL password (if there is no password type clear) : "
    )
    mysqlpass = "" if mysqlpass == "clear" else mysqlpass
    db = mysql.connect(host="localhost", user="root", passwd=mysqlpass, database="msms")
    db2 = mysql.connect(
        host="localhost", user="root", passwd=mysqlpass, database="userdata"
    )
    if db.is_connected() and db2.is_connected():
        print("Connections established")
        cur = db.cursor()
        cur2 = db2.cursor()
        login_page()
        print("Thanks for using our software!")
        db.commit()
        db2.commit()
        db.close()
        db2.close()
    else:
        print("Connections ain't established!")
