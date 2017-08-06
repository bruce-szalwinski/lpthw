s = 0
a = 1
b = 1
limit = 4000000

while b < limit:
    if b % 2 == 0:
        s += b
    h = a + b
    a = b
    b = h

print s
