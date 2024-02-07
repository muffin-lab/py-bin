def main():

    x = getz("whats x ? ")
    
    y = getz("whats y ?")

    print(f"Your Total Value is: ", x + y)


def getz(n):
        while True: 
            try:
                return int(input(n))        
            except ValueError:
                pass


# def getx():
#     while True:

#         try:
#             return int(input("what is the first value ? : "))        
#         except ValueError:
#             pass

# def gety():
#     while True:

#         try:
#             return int(input("what is the second value ? : "))        
#         except ValueError:
#             pass

main()