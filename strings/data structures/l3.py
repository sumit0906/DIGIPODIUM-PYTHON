x = [1,2,3,4,5,6,7,8,9,192,3,2,1,1,2]

print(x.count(3))
print(x.count(2))
print(x.count(22))

print(x.index(3))
print(x.index(2))
#print(x.index(22))
z=x  #copy address
y =x.copy()  #copy values only not address
print(x is z)
print(x is y)
z.append(10)
y.append(20)
print(x)
print(y)
print(z)