from ut_calculator import square

def main():
    test_square()

def test_square():

    # if square(2) == 4:
    #     print("The square of 2 is True")
    # if square(3) == 9:
    #     print("The square of 3 is True")
    try:
        assert square(2) == 4
    except AssertionError:
        print("Two square is not 4")

    try:
        assert square(3) == 9
    except AssertionError:
        print("Three square is not 9")
    
    try:
        assert square(-2) == 4
    except AssertionError:
        print("-2 square is not 4") 

    try:
        assert square(-3) == 9
    except AssertionError:
        print("-3 square is not 9")

    try:
        assert square(0) == 0
    except AssertionError:
        print("0 square is not 0")

if __name__ == "__main__":
    main()