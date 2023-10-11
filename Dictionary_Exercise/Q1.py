a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
c = a + b
d = sorted(set(c))
e = ''.join(d)
# a1 = sorted(set(a))
# b1 = sorted(set(b))

print(e)
# print(a1,b1)