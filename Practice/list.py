# List:- Python lists are containers to store a set of values of any datatypes.

food=['Apple','Mango',10,20,'Panner',True,23.23]
l1=[56,45,1,12,57,32,23]
print(food)
print(food[0],food[2])
(food[0])='Pomigranet'  # List are mutable.
print(food[0])
print(food[1:5])
print(type(food))
food.append('Orange') #append add valua in last.
print(food)
l1.sort() #sort the list
#l1.reverse() # Reverse the list.
#l1.insert(3,2) # Insert value at index.
print(l1.pop(3))
print(l1)
