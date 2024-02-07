def main():

    value_1 = float(input("What is the first Value ? : "))
    print(f"Your Squared value is ", value(value_1))

def value(n):
    return pow(n, 2)

main()