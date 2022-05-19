import random
import kivy
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, StringProperty,ListProperty
from kivy.uix.spinner import Spinner, SpinnerOption
from kivy.uix.dropdown import DropDown
from cbkBackend import *

class InventoryList(GridLayout):
    def __init__(self, **kwargs):
        super(InventoryList, self).__init__(**kwargs)
        self.cols = 1
        self.subgrid = GridLayout()
        self.subgrid.cols = 5
        self.subgrid.rows = 6
        self.subgrid.add_widget(Label(text='Item', font_size=22, color = (0,0,0,1)))
        self.subgrid.add_widget(Label(text='Category', font_size=22, color = (0,0,0,1)))
        self.subgrid.add_widget(Label(text='Price', font_size=22, color = (0,0,0,1)))
        self.subgrid.add_widget(Label(text='In-Stock', font_size=22, color = (0,0,0,1)))
        self.subgrid.add_widget(Label(text='Good-Until', font_size=22, color = (0,0,0,1)))
        self.subgrid.add_widget(Label(text=names[0], font_size=12, color = (0,0,0,1)))
        self.subgrid.add_widget(Label(text=category[0], font_size=12, color = (0,0,0,1)))
        self.subgrid.add_widget(Label(text=str(price[0]), font_size=12, color = (0,0,0,1)))
        self.subgrid.add_widget(Label(text='In-Stock', font_size=12, color = (0,0,0,1)))
        self.subgrid.add_widget(Label(text='Good-Until', font_size=12, color = (0,0,0,1)))
        self.subgrid.add_widget(Label(text=names[1], font_size=12, color = (0,0,0,1)))
        self.subgrid.add_widget(Label(text=category[1], font_size=12, color = (0,0,0,1)))
        self.subgrid.add_widget(Label(text=str(price[1]), font_size=12, color = (0,0,0,1)))
        self.subgrid.add_widget(Label(text='In-Stock', font_size=12, color = (0,0,0,1)))
        self.subgrid.add_widget(Label(text='Good-Until', font_size=12, color = (0,0,0,1)))
        self.subgrid.add_widget(Label(text=names[2], font_size=12, color = (0,0,0,1)))
        self.subgrid.add_widget(Label(text=category[2], font_size=12, color = (0,0,0,1)))
        self.subgrid.add_widget(Label(text=str(price[2]), font_size=12, color = (0,0,0,1)))
        self.subgrid.add_widget(Label(text='In-Stock', font_size=12, color = (0,0,0,1)))
        self.subgrid.add_widget(Label(text='Good-Until', font_size=12, color = (0,0,0,1)))
        self.subgrid.add_widget(Label(text=names[3], font_size=12, color = (0,0,0,1)))
        self.subgrid.add_widget(Label(text=category[3], font_size=12, color = (0,0,0,1)))
        self.subgrid.add_widget(Label(text=str(price[3]), font_size=12, color = (0,0,0,1)))
        self.subgrid.add_widget(Label(text='In-Stock', font_size=12, color = (0,0,0,1)))
        self.subgrid.add_widget(Label(text='Good-Until', font_size=12, color = (0,0,0,1)))
        self.subgrid.add_widget(Label(text=names[4], font_size=12, color = (0,0,0,1)))
        self.subgrid.add_widget(Label(text=category[4], font_size=12, color = (0,0,0,1)))
        self.subgrid.add_widget(Label(text=str(price[4]), font_size=12, color = (0,0,0,1)))
        self.subgrid.add_widget(Label(text='In-Stock', font_size=12, color = (0,0,0,1)))
        self.subgrid.add_widget(Label(text='Good-Until', font_size=12, color = (0,0,0,1)))
        self.add_widget(self.subgrid)

class BudgetDisplay(GridLayout):
    pass

class ExpensesDisplay(GridLayout):
    pass

class GroceryDisplay(GridLayout):
    pass

class GoalsDisplay(GridLayout):
    pass

class HomePage(Screen):
    pass

class Manager(ScreenManager):
    pass

class CabinetKingApp(App):

    def build(self):
        kv = Builder.load_file("cabinetkingz.kv")
        self.title = 'Cabinet Kingz'
        return kv

if __name__ == "__main__":
    CabinetKingApp().run()
