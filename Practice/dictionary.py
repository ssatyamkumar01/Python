# Dictionary is mutable.

marks={
    'satyam':95,
    'satyam':99,
    'Shubham':98,
    'Raju':55
}
d={'name':'Babu'}
print(marks,type(marks))
marks['Shubham']=100   #update
print(marks['satyam'])
print(marks['Shubham'])
d["age"] = 21          # update
d["country"] = "India" # add new
print(d["name"])   # John
print(d.get("age"))  # 20
d.pop("age")     # remove specific key
#d.clear()        # remove all items
d = {"a": 1, "b": 2}

print(marks.keys())    # dict_keys(['a', 'b'])
print(marks.values())  # dict_values([1, 2])
print(marks.items())   # dict_items([('a',1), ('b',2)])