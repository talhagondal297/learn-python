# On a certain day the British pound was equivalent to $1.487 U.S., the French franc was
# $0.172, the German deutschemark was $0.584, and the Japanese yen was $0.00955.
# Write a program that allows the user to enter an amount in dollars, and then displays this
# value converted to these four other monetary units.

British_pound = 1.487
French_franc = 0.172
German_deutschemark = 0.584
Japanese_yen = 0.00955

try:
    Amount_In_Dollar = float(input("Enter dollars: "))

    British_pound = Amount_In_Dollar / British_pound
    French_franc = Amount_In_Dollar / French_franc
    German_deutschemark = Amount_In_Dollar / German_deutschemark
    Japanese_yen = Amount_In_Dollar / Japanese_yen

    print(f"The {Amount_In_Dollar} Dollars are equivalent to {British_pound:.2f} British Pound")
    print(f"The {Amount_In_Dollar} Dollars are equivalent to {French_franc:.2f} French franc")
    print(f"The {Amount_In_Dollar} Dollars are equivalent to {German_deutschemark:.2f} German deutschemark")
    print(f"The {Amount_In_Dollar} Dollars are equivalent to {Japanese_yen:.2f} Japanese yen")

except ValueError:
    print("Invalid input. Please enter a valid amount in dollars.")
