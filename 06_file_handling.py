### File Handling ###

# .txt file
import os

txt_file = open("./my_file.txt", "w+") # r+ Leer y Escribir y w+ sobreescribe el archivo
txt_file.write("Mi nombre es Mario\nMi apellido es Celis\n20 años\ny mi idioma faborito es Python")
#print(txt_file.read())
#print(txt_file.read(10))
#print(txt_file.readline())
#print(txt_file.readline())
#print(txt_file.readlines())
for line in txt_file.readlines():
    print(line)

txt_file.write("\nAunque también me gusta Kotlin")
print(txt_file.readline())

txt_file.close()

#os.remove("./my_file.txt") # para borrar el fichero ojo

# .json file

import json

json_file = open("./my_file_json.json", "w+")

json_text = {
    "name":"Mario",
    "surname":"Celis", 
    "age": 38, 
    "vehicle": "BMW X3 XDrive 30e hybrid",
    "cash":"In the United States I have USD $1,500,000 approximately and in Colombia $5,000,000 pesos, approximately, dated February 15, 2023",
    "language":["Python", "Swift",  "Kotlin", "PHP"],
    "website":"https://www.baloto.com/"

    }

json.dump(json_text, json_file, indent = 2) #indent coloca espacios segun el numero que le coloque 

json_file.close()

with open("./my_file_json.json") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

json_dict = json.load(open("./my_file_json.json"))
print(json_dict)
print(type(json_dict))
print(json_dict["name"])

# .csv file
import csv

csv_file = open("./my_file_csv.csv", "w+")

csv_write = csv.writer(csv_file)
csv_write.writerow(["name", "surname", "age", "language","website"])
csv_write.writerow(["Mario", "Celis", 38, "Python", "https://www.baloto.com/"])
csv_write.writerow(["camilo", "Restrepo", 28, "COBAL", ""])

csv_file.close()

with open("./my_file_csv.csv") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

# .xlsx file

#import xlrd # debe instalarse el modulo

# .xml file

import xml

