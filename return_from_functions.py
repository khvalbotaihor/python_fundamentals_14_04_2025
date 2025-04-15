def sum(a,b):
    return a + b, a * b


a,p = sum(1, 2)
print(a,p)



def sum(a: int,b: int) -> int:
    return a + b

c= sum(1, 2)

print(c)

d = sum('hi', ' there')
print(d)