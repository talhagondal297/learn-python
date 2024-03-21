# Assuming there are 7.481 gallons in a cubic foot, write a program that asks the user to
# enter a number of gallons, and then displays the equivalent in cubic feet.


Gallons_Per_Cubic_Foot = 7.481 
gallons = float(input("Enter a number of gallons: "))

gallons_In_Cubic_Feet = gallons / Gallons_Per_Cubic_Foot

print(f"{gallons} gallons is equivalent to {gallons_In_Cubic_Feet} cubic feet.")
