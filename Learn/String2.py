# Strings are immutable.
a='Assassin'
b='!!! Assassin !!!'
print(len(a))
print(a.upper())
print(a.lower())
print(a.lower())
print(b.rstrip('!')) # Remove ! from back.
print(a.replace('Assassin','Bgmi Name'))
print(b.split(" "))
moviename='mirzapur the moviE'
moviename2='toxic'
print(moviename.capitalize()) # Make first letter capital.
print(moviename2.capitalize())
print(len(a))
print(len(a.center(20))) 
print(a.count('s')) # How many time this word or letter occures.

c='welcome to the jungle.'
print(c.endswith('.'))
print(c.endswith('to',4,10)) # we can check through that that using slicing.

d='What is your name Mr.'
print(d.find('is'))
print(d.find('ill')) # Return -1 when given string is not found.
#print(d.index('ill')) # Return error when given string is not found.

e="Iloveindia1"
print(e.isalnum()) # If not take number output will be false.

f='India12'
print(f.isalpha()) # If take number output will be false.

g="saala"
print(g.islower()) # It check in this every thing is written in small or not.
print(g.isspace()) # It check is any space or not if found return true else false.
print(g.startswith('s'))
print(f.swapcase()) # It convert capital latter into small latter viseversa.