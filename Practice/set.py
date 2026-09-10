z=set()
print(z)

s = {1, 2, 3}

s.add(4)
print(s)   # {1, 2, 3, 4}
s = {1, 2}

s.update([3, 4])
print(s)   # {1, 2, 3, 4}
s = {1, 2, 3}

s.remove(2)
print(s)
s.discard(5)   # no error
s.pop()
a = {1, 2}
b = {2, 3}

print(a.union(b))   # {1, 2, 3}
print(a.intersection(b))  # {2}
print(a.difference(b))  # {1}
a = {1, 2}
b = {1, 2, 3}

print(a.issubset(b))    # True
print(b.issuperset(a))  # True
