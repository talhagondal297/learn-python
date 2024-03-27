# 1. Assume that you want to generate a table of multiples of any given number. Write a program that allows 
# the user to enter the number and then generates the table, formatting it
# into 10 columns and 20 lines. Interaction with the program should look like this (only the
# first three lines are shown):
# Enter a number: 7
# 7 14 21 28 35 42 49 56 63 70
# 77 84 91 98 105 112 119 126 133 140
# 147 154 161 168 175 182 189 196 203 210


print("Table of multiples number given by user")
print("-" * 50)

num = int(input("Enter a number: "))

counter = 0

for i in range(1, 4):  
    for j in range(10): 
        multiple = num * (counter * 10 + j + 1)
        print(multiple, end=" ")

    print()
    counter += 1


print("-" * 50)
