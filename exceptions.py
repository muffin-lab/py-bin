
def main():

    x = num()

    y = num2("What is y : ")
    
def num():
    
    while True:
        try:
            x = int(input("What is the value of x :  "))
            print(f"The value of x is {x}")
        except ValueError:
           print("This value is not an integer")
        else:
            break
    return x

    
def num2(prompt):

    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass
main()