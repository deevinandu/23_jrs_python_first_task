num = input("Enter something: ")

try:
    x = int(num)
    if str(x) != num:
        print("Invalid input")
    else:
        fact = 1
        for i in range(1, x+1):
            fact *= i

        print("factorial = ",fact)

except ValueError:
    print("Invalid input")
