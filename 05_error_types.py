### Errar Type ###

# syntaxError

#print "¡Hola comunidad!" # Descomentar para Error
print("¡Hola comunidad!")

# NameError
lenguage = "Spanish" # Comentar para Error
print(lenguage)

# IndexError
my_list = ["Python", "Swift", "Kotlin", "Dart", "JavaScript",]
print(my_list[0])
print(my_list[4])
print(my_list[-1])
#print(my_list[5]) # Descomentar para Error

# ModuleNotFoundError
#import maths # Descomentar para Error
import math

# AttrubuteError
#print(math.PI) # Descomentar para Error
print(math.pi)

# KeyError
my_dict = {"Nombre":"Mario", "Apellido":"Celis","Edad":38, 1:"Python"}
print(my_dict["Edad"])
#print(my_dict["Apelido"]) # Descomentar para Error
print(my_dict["Apellido"])

# TypeError
#print(my_list["0"]) # Descomentar para Error
print(my_list[0])
print(my_list[False])

# ImportError
#from math import PI # Descomentar para Error
from math import pi
print(pi)
 
# ValueError
#my_int = int("10 Años") # Descomentar para Error
my_int = int("10")
print(type(my_int))

# ZeroDivisionError
print(4/2)
print(0/2)
# print(4/0) # Descomentar para Error