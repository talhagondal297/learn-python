# a=10
# b=5
# c= a if a>=b else b
# print(c)


# a=55
# b=51
# print( "both a and b are equal" if a==b else "a is greater than b" if a>b else "b is greater than a" )

# a, b = 10, 10
 
# if a != b:
#     if a > b:
#         print("a is greater than b")
#     else:
#         print("b is greater than a")
# else:
#     print("Both a and b are equal")

data = [3, 5, 2, 8, 4]

for i in data:
    result = 'even' if i % 2 == 0 else 'odd'
    print(f'The number {i} is {result}.')