# 2. Write a program that generates the following table:
# 1990 135
# 1991 7290
# 1992 11300
# 1993 16200
# Use a single cout statement for all output.


data = [
    (1990 , 135),
    (1991 , 7290),
    (1992 , 11300),
    (1993 , 16200)
]

ans = "\n".join([f"{year}  {value}" for year, value in data])

print(ans)