# while loops


i = 0

while i < 3:
    print("Meow.")
    i += 1


# For loops


for i in [0, 1, 2]:
    print("Meow. Meow.")


for _ in range(3):
    print("Meow. Meow. Meow.")


# Print function for loops
    
print("Meow. Meow. Meow. Meow.\n" * 3, end="")


while True:
    n = int(input("What's n ? "))
    if n > 0:
    #     continue
    # else:
        break

for _ in range(n):
    print("Meow. Meow. Meow. Meow. Meow.")