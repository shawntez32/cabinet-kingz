import datetime as dt
import sqlite3 as sql

measures = ['per-gram','per-ounce','per-pound','per-gallon','per-case','per-bag']
items = []

def dbItems():
    conn = sql.connect('dbs/grocerylist.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM Items')
    rows = cur.fetchall()
    conn.close()
    for item in rows:
        items.append(item)

class FoodItem:

    def __init__(self,name,category,measure,price):
        self.name = name
        self.category = category
        self.measure = measure
        self.id = id
        self.price = price

    def add_item(self):
        conn = sql.connect('dbs/grocerylist.db')
        cur = conn.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS Items(Name TEXT,Category TEXT,Measure TEXT,id AUTO INTERGER PRIMARY KEY,Price INT)')
        cur.execute('INSERT INTO Items(Name,Category,Measure,Price) VALUES(?,?,?,?)',(self.name,self.category,self.measure,self.price))
        conn.commit()
        conn.close()

class Expense:
    occurences = ['once','daily','weekly','monthly','custom']

    def __init__(self,price,dscr,occurence):
        self.price = price
        self.dscr = dscr
        self.o = occurence

    def addExpense(self):
        conn = sql.connect('expenses.db')
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS Expense(Price INT,Description TEXT, Occurence TEXT)")
        cur.execute("INSERT INTO Expense(Price,Description,Occurence) VALUES(?,?,?)",(self.price,self.dscr,self.o))
        conn.commit()

class CurInventory:
    def __init__(self,name,category,measure,id,price,inStock,suff,succ,stkFor):
        self.name = name
        self.category = category
        self.measure = measure
        self.id = id
        self.price = price
        self.stock = inStock
        self.suff = suff
        self.succ = succ
        self.stkFor = stkFor

class Recipe:
    def __init__(self,name,recipeDict):
        self.name = name
        self.recipe = recipeDict

class Paycheck:
    def __init__(self,date,source,amt,taxes,id):
        self.date = date
        self.source = source
        self.amt = amt
        self.taxes = taxes

class Budget:
    def __init__(self,income,budgetDict,timeframe,id):
        self.income = income
        self.budget = budgetDict
        self.tf = timeframe

class Goal:
    def __init__(self,price,importance,goalDate,id):
        self.price = price
        self.imp = importance
        self.gDate = goalDate

#measures = ['per-gram','per-ounce','per-pound','per-gallon','per-case','per-bag']

names = []
category = []
price = []

dbItems()

for e in items:
    names.append(e[0])
    category.append(e[1])
    price.append(e[4])


