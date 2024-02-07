import random, statistics, sys

x = random.choice(["head", "tails"])

print(f"You got {x}")

y = random.randint(1, 2)

print(f"Your random integer is {y}")

z = ["one", "two", "three", "four"]
random.shuffle(z)
for zz in z:
    print(zz)


i = statistics.mean([100, 0])
print(i)


try:
    print("Hello my dear system", sys.argv[1])
except IndexError:
    print("Input value Error.")


# if len(sys.argv) < 2:
#     sys.exit("Too few arguments.")
# elif len(sys.argv) > 2:
#     sys.exit("Too many arguments")
# else:
#     print("Hello my dear system", sys.argv[1])
print("Hello my dear system", sys.argv[1])

for arg in sys.argv[1:]:
    print("hello", arg)
