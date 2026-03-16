Arjun_list=[1,2,4,2,3,6,10,12,12,4]
Arjun_set=set(Arjun_list)

if 5 in Arjun_set:
    print("yes")
else:
    print("no")

if 12 in Arjun_set:
    print("yes")
else:
    print("no")

Arjun_set.add(5)
Arjun_set.add(2)

Arjun_set.remove(5)
Arjun_set.discard(14)

print(Arjun_set)

a={1,2,3,4,5,8,9,12}
b={2,4,6,7,10,13,1}

print(a.union(b))
print(a|b)

print(a.intersection(b))
print(a&b)

print(a.difference(b))
print(a-b)

print(a.symmetric_difference(b))
print(a^b)

b={1,3,5,8,6,9,12,15,18,19}
s={2,4,3,7,9,8,11,14,13,17,19}

print(b.intersection(s))
print(b&s)

print(b.symmetric_difference(s))
print(b^s)

print(b.difference(s))
print(b-s)