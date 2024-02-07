from calculator_001 import sqr


def main():

    test_square()

def test_square():
    if sqr(2) != 4:
        print("not square")
    if sqr(3) != 9:
        print("not square")

if __name__ == "__main__":
    main()