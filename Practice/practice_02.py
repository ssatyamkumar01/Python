''' a=input("What is your name : ")
print("Good Morning " + a)
'''

letter=''' Dear <|Name|>
You are selected !
<|Date|>'''
print(letter.replace('<|Name|>','Assassin').replace('<|Date|>','24-Jan-2027'))

# Find double space at which position.
name="Kya haal  hai Darling !"
print(name.find("  "))
print(name.find("D"))
print(name.find("a"))

# Replace double space with Single space.
name="Kya haal  hai Darling !"
print(name.replace("  "," "))

# Formate the program.
x=" Hey Assassin, \n \t Bgmi is the multiplayer game.\n Play !"
print(x)