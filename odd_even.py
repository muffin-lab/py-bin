# option - 1

# x = int(input("What is x ? "))

# if x % 2 == 0:
#     print("Even")
# else:
#     print("Odd")



# option - 2 

def main():
    
    x = int(input("What's X ? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")


def is_even(n):
    # if n % 2 == 0:
    #     return True
    # else:
    #     return False



    # return True if n % 2 == 0 else False


    return n % 2 == 0

main()

