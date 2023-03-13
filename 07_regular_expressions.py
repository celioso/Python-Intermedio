### Regular Expressions ###

import re 

# match
print("\nmatch\n")

my_string = "Esta es la lección número 7: lección llamada Expresiones Regulares"
my_otrer_string = "Esta no es la leccion número 6: Manejo de ficheros"

match = re.match("Esta es la lección", my_string)
print(match)
start, end = match.span()
print(my_string[start:end])

match = re.match("Esta es la lección", my_otrer_string)
#if not (match == None): # Otra forma de comprobar el None
#if not (match != None):
if match is not None:
    print(match)
    start, end = match.span()
    print(my_string[start:end])

#print(re.match("Expresiones Regulares", my_string))

# search
print("\nsearch\n")

search = re.search("lección", my_string, re.I)
print(search)
start , end = search.span()
print(my_string[start:end])

# findall
print("\nfindall\n")

findall = re.findall("lección", my_string, re.I)
print(findall)

# split

print("\nsplit\n")
print(re.split(":", my_string))

# sub

print("\nsub\n")
print(re.sub("[l | L]ección", " LECCIÓN", my_string))
print(re.sub("lección | lección", " LECCIÓN", my_string))
print(re.sub("Expresiones Regulares","Regex", my_string))

# Patterns
print("\nPattern\n")

pattern = r"[lL]ección"
print(re.findall(pattern, my_string))

pattern = r"[lL]ección | Expresiones"
print(re.findall(pattern, my_string))
print(re.match(pattern, my_string))

pattern = r"[0-9]"
print(re.findall(pattern, my_string))
print(re.match(pattern, my_string))
print(re.search(pattern, my_string))

pattern = r"\d"
print(re.findall(pattern, my_string))

pattern = r"\D"
print(re.findall(pattern, my_string))

pattern = r"[l].*"
print(re.findall(pattern, my_string))

email = "celioso@hotmail.com"

pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
print(re.match(pattern, email))
print(re.search(pattern, email))
print(re.findall(pattern, email))

email = "celioso12@hotmail.es"
print(re.findall(pattern, email))
