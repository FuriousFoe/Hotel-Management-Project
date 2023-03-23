import tkinter
from tkinter import *
import sqlite3 as sql
import datetime
from time import strftime
import random
from PIL import ImageTk,Image

# Data base connectivity :-
con = sql.connect('Hotel Data.db')
cur = con.cursor()

# Funtions
# random number generation :-
def custno():
    customers = ['1123' ,'1456' ,'5967' , '1978' ,'8766', '3897' , '4564' , '3459']
    r = random.randint(0 , 7)
    cust = tkinter.Label(frameBill, bd=5, text=customers[r] , height= 1, width=10)
    cust.grid(row=1, column=1)


def billno():
    cu = ['1234', '1463', '5788', '6878', '3008', '3845', '6764', '7839' ,
                 '4444' , '5353' ,'3332' ,'4343']
    r = random.randint(0, 8)
    cust = tkinter.Label(frameBill, bd=5, text=cu[r], height=1, width=10)
    cust.grid(row=3, column=1)


def clear():
    totalcost.delete(0 , "end")
    display.delete("1.0", "end")
    entry_Bill.delete(0 , "end")
    entry_table.delete(0 ,"end")
    entry_customer.delete(0 ,"end")
    lbstat.delete("1.0", "end")


def Set():
    clear()
    display.insert(END, "\n------------------------------\n")
    display.insert(END, " Sodhi Da Dhaba , Nagar Road ,By pass NH-03, Nashik.")
    display.insert(END, "\n------------------------------\n")


def displayitem(Menu):
    item = Menu.split("-")
    display.insert(END, "{} {}\n".format(item[0], item[1]))
    c = item[1].split()

    global total
    total = total + int(c[1])
    print(total)


def totalbill():
    totalcost.insert(0,"Rs {}/-".format(total))


def selectTable(click):
    item = click.split("-")
    lbstat.insert(END, "{} {}\n".format(item[0], item[1]))
    k = item[1].split()
    global j
    j = int(k[0])


def delete():
    root.destroy()


def addToDataBase():
    insert()


def insert():
    customer = int(entry_customer.get())
    bill = int(entry_Bill.get())
    table = int(entry_table.get())
    totalvalue = int(total)

    cur.execute('INSERT INTO data VALUES(?,?,?,?)' , (customer , table ,bill , totalvalue))
    con.commit()

# The Interface
root = tkinter.Tk()
root.title("Hotel Management Template")
# root.geometry("550x415")
root.geometry("600x500")
root.resizable()

#Image section
img = Image.open('menuimg.jpg')
img = img.resize((300, 200))
img = ImageTk.PhotoImage(img)

img1 = Image.open('billbg.jpeg')
img1 = img1.resize((480, 480))
img1 = ImageTk.PhotoImage(img1)

img2 = Image.open('stats.jpeg')
img2 = img2.resize((300, 500))
img2 = ImageTk.PhotoImage(img2)

#Panels
panel1 = tkinter.PanedWindow(bd=4, relief="raised", bg="Grey")
panel1.pack(fill=BOTH, expan=1)

panel2 = tkinter.PanedWindow(panel1, orient=VERTICAL, bd=4, bg="grey", relief="raised" ,width=100 )
panel1.add(panel2)

left_label = tkinter.Label(panel1, text="Left" , image=img1)
panel1.add(left_label)

top = tkinter.Label(panel2, text="Top" , image=img)
panel2.add(top)

bottom = tkinter.Label(panel2, text="Bottom" ,image=img2)
panel2.add(bottom)

frame = tkinter.Frame(top)
frame.pack()

frameBill = tkinter.Frame(left_label )
frameBill.pack()

frameStat = tkinter.Frame(bottom)
frameStat.pack()

# Dropdown  menu

label = Label(top, text=" "  , bg='lightyellow')
label.pack()
label = Label(frame , text="Place Order :-" , font=('Helvetica' ,'10' , 'bold') , bg='lightyellow').grid()

# Change the label text
def show():
    label.config(text=Menu.get())

menu = [
    "Aloo Paratha           - RS. 50",
    "Schz Fried Rice        - Rs. 70",
    "Schz Noodle            - Rs. 80",
    "Veg Manchurian         - Rs. 60",
    "Thali                  - Rs. 70",
    "Masala Dosa            - Rs. 90",
    "Egg Rice               - Rs. 90"
]

Menu = StringVar()
Menu.set("Menu :")
drop = OptionMenu(frame, Menu, *menu , command=displayitem)
drop.grid()

label = Label(top, text=" "  , bg='lightyellow')
label.pack()

# Bill wali frame :-

a = tkinter.Label(frameBill, text="Customer Number :-")
a.grid(row=1, column=0)

entry_customer = tkinter.Entry(frameBill,bd=5 )
entry_customer.grid(row= 1, column=1)

a = tkinter.Label(frameBill, text=" Table Number :-")
a.grid(row=2, column=0)

entry_table = tkinter.Entry(frameBill ,bd=5)
entry_table.grid(row=2, column=1)

a = tkinter.Label(frameBill, text="Bill Number :-")
a.grid(row=3, column=0)

entry_Bill = tkinter.Entry(frameBill ,bd=5)
entry_Bill.grid(row =3 , column=1)

bill = tkinter.Label(frameBill, text="Bill to be paid :-")
bill.grid(row=4, column=0, columnspan=2)

display = tkinter.Text(frameBill, height=15, width=32, bg="white", bd=10, relief=GROOVE)
display.grid(row=5, column=0, rowspan=2, columnspan=2)

total = Button(frameBill , text="Total bill -", font="time 10" ,command=totalbill)
total.grid(row =9 , column=0 ,)
total = 0

totalcost = Entry(frameBill )
totalcost.grid(row= 9, column=1)

bt = tkinter.Button(frameBill, text="Add " , command=addToDataBase)
bt.grid(row=10, column=0)

bt = tkinter.Button(frameBill, text="Exit " ,command=delete)
bt.grid(row=10, column=1)

bt = tkinter.Button(frameBill, text="Refresh", command=Set)
bt.grid(row=11, column=0, columnspan=2)

# Bottom wali frame

'''
def stat():
    lbstat.config(j)
'''

def dude():
    Statistic()

#Stats wali Window :-
def Statistic():
    import matplotlib.pyplot as plt
    global j
    cur.execute(f'SELECT TOTAL FROM data WHERE Table_no="{j}"')
    a = cur.fetchall()
    y = a
    plt.plot(y, marker='o')
    plt.title("Analysis", fontdict={'family': 'serif', 'size': '20', 'color': 'r'})
    plt.xlabel("Days", fontdict={'family': 'serif', 'size': '10', 'color': 'r'})
    plt.ylabel("Earning of table ", fontdict={'family': 'serif', 'size': '10', 'color': 'r'})
    plt.grid(axis='y', ls='--', lw=2.0)
    plt.show()

tables = ["Table -1", "Table -2", "Table -3", "Table -4", "Table -5", "Table -6", "Table -7", "Table -8", "Table -9"
    , "Table -10", "Table -11", "Table -12"]
click = StringVar()
click.set("Select")

drop = OptionMenu(frameStat, click, *tables , command=selectTable)
drop.pack(side=BOTTOM )
but = Button(frameStat, text="Selected Table \n Statistics :-", command=dude).pack()

lbstat = Text(frameStat , height=1 ,width=9)
lbstat.pack()

# time
def time():
    string = strftime('%H:%M:%S')
    timelabel.config(text=string,  fg='black')
    timelabel.after(1000, time)

timelabel  =Label(frameBill )
timelabel.grid(row= 0, column=1 , padx=30)
time()
date= datetime.datetime.now()
datelabel = Label(frameBill, text=f"{date:%d %B, %Y}", fg='black')
datelabel.grid(row=0, column=0, padx=30)

#billno()
#custno()
root.mainloop()
