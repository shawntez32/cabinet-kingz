import datetime as dt
import sqlite3 as sql


class FoodItem:
    measures = ['per-gram','per-ounce','per-pound','per-gallon','per-case','per-bag']

    def __init__(self,name,category,measure,id,price):
        self.name = name
        self.category = category
        self.measure = measure
        self.id = id
        self.price = price

    def addItem(self):
        conn = sql.connect('grocerylist.db')
        cur = conn.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS Items(Name TEXT,Category TEXT,Measure TEXT,ID INT,Price INT)')
        cur.execute('INSERT INTO Items(Name,Category,Measure,ID,Price) VALUES(?,?,?,?,?)',(self.name,self.category,self.measure,self.id,self.price))
        conn.commit()
        conn.close()

    def dbItems(self):
        conn = sql.connect('grocerylist.db')
        cur = conn.cursor()
        cur.execute('SELECT * FROM Items')
        items = cur.fetchall()
        conn.close()
        for item in items:
            x = FoodItem(item[0],item[1],item[2],item[3],item[4])

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
    def __init__(self,name,category,measure,id,price,inStock,suff,succ):
        self.name = name
        self.category = category
        self.measure = measure
        self.id = id
        self.price = price
        self.stock = inStock
        self.suff = suff
        self.succ = succ

class Recipe:
    def __init__(self,name,recipeDict):
        self.name = name
        self.recipe = recipeDict

class Paycheck:
    def __init__(self,date,source,amt,taxes):
        self.date = date
        self.source = source
        self.amt = amt
        self.taxes = taxes

class Budget:
    def __init__(self,income,budgetDict,timeframe):
        self.income = income
        self.budget = budgetDict
        self.tf = timeframe

class Goal:
    def __init__(self,price,importance,goalDate):
        self.price = price
        self.imp = importance
        self.gDate = goalDate
