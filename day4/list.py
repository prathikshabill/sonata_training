a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c=[]

for i in a:
    for j in b:
        if i==j:
            c.append(i)
print(set(c))

d = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
e=[]
def even(d):
    for i in d:
        if i%2==0:
            e.append(i)
    return e
print(even(d))

