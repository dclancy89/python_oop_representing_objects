import Animal
#def __init__(self, name, health):

import Bike
#def __init__(self, price, max_speed):

import Car
#def __init__(self, price, speed, fuel, mileage):

import call_center
#def __init__(self):

import hospital
#def __init__(self, name, capacity):

import math_dojo
#def __init__(self):

import product
#def __init__(self, price, item_name, weight, brand):



animal = Animal.Animal('zebra', 100)
print animal

bike = Bike.Bike(100, '10mph')
print bike

car = Car.Car(1000, '50mph', 'full', '10mpg')
print car

center = call_center.CallCenter()
print center

hospital1 = hospital.Hospital('RP', 200)
print hospital1

mathdojo = math_dojo.MathDojo()
print mathdojo

product = product.Product(200, 'ipod', '6oz', 'apple')
print product