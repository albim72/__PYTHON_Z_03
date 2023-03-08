from enum import Enum
import time


PizzaProgress = Enum('PizzaProgress','queued preparation baking ready')
PizzaDough = Enum('PizzaDough','thin thick')
PizzaSauce= Enum('PizzaSauce','totmato creme_fraiche')
PizzaTopping = Enum('PizzaTopping','mozarella double_mozarella bacon ham mushrooms red_onion oregano')
STEP_DELAY = 3

class Pizza:
    def __init__(self,name):
        self.name=name
        self.dough=None
        self.sauce = None
        self.topping = []

    def __str__(self):
        return self.name

    def prepare_dough(self,dough):
        self.dough = dough
        print(f'preparing the {self.dough.name} dough of your {self} ...')
        time.sleep(STEP_DELAY)
        print(f'done with the {self.dough.name} dough')


class MargaritaBuilder:
    def __init__(self):
        self.pizza = Pizza('margarita')
        self.progress = PizzaProgress.queued
        self.baking_time = 5

    def prepare_dough(self):
        self.progress = PizzaProgress.preparation
        self.pizza.prepare_dough(PizzaDough.thin)

    def add_sauce(self):
        print("adding the tomato sauce to your margarita...")
        self.pizza.sauce = PizzaSauce.tomato
        time.sleep(STEP_DELAY)
        print('done with the tomato sauce')

    def add_topping(self):
        topping_desc = 'double_mozarella oregano'
        topping_items = (PizzaTopping.double_mozarella, PizzaTopping.oregano)
        print(f'adding the toping({topping_desc} to your margarita)')
        self.pizza.topping.append([t for t in topping_items])
        time.sleep(STEP_DELAY)
        print(f'done with the topping ({topping_desc}')

    def bake(self):
        self.progress = PizzaProgress.baking
        print(f'baking your margarita for {self.baking_time} s')
        time.sleep(self.baking_time)
        self.progress = PizzaProgress.ready
        print('maragrita is ready!!!')


class CreamyBaconBuilder:
    def __init__(self):
        self.pizza = Pizza('creamy bacon')
        self.progress = PizzaProgress.queued
        self.baking_time = 7

    def prepare_dough(self):
        self.progress = PizzaProgress.preparation
        self.pizza.prepare_dough(PizzaDough.thin)

    def add_sauce(self):
        print("adding the tomato sauce to your creamy bacon...")
        self.pizza.sauce = PizzaSauce.creme_fraiche
        time.sleep(STEP_DELAY)
        print('done with the creme_fraiche sauce')

    def add_topping(self):
        topping_desc = 'double_mozarella, bacon, ham, mushrooms, red onion, oregano'
        topping_items = (PizzaTopping.mozarella,
                         PizzaTopping.bacon,
                         PizzaTopping.ham,
                         PizzaTopping.mushrooms,
                         PizzaTopping.red_onion,
                         PizzaTopping.oregano)
        print(f'adding the toping({topping_desc} to your creamy bacon)')
        self.pizza.topping.append([t for t in topping_items])
        time.sleep(STEP_DELAY)
        print(f'done with the topping ({topping_desc}')

    def bake(self):
        self.progress = PizzaProgress.baking
        print(f'baking your creamy bacon for {self.baking_time} s')
        time.sleep(self.baking_time)
        self.progress = PizzaProgress.ready
        print('creamy bacon is ready!!!')
        
        
class Waiter:
    def __init__(self):
        self.builder = None
        
    def construct_pizza(self,builder):
        self.builder = builder
        steps = (builder.prepare_dough,
                 builder.add_sauce,
                 builder.add_topping,
                 builder.bake)
        [step() for step in steps]
        
    @property
    def pizza(self):
        return self.builder.pizza
