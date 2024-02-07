name = input("What is your name ? ")

# option - 1 

'''if name == "Harry":
    print("Gryphendor")
elif name == "Hermoine":
    print("Gryphendor")
elif name == "Ron":
    print("Gryphendor")
elif name == "Malfoy":
    print("Slytherin")
else:
    print("You are no one my Dear.")'''


# option - 2 

'''if name == "Harry" or name == "Hermoine" or name == "Ron":
    print("Gryphendor")
elif name == "Malfoy":
    print("Slytherin")
else:
    print("You are no one my Dear.")'''


'''match name:
    case "Harry":
        print("Gryphendor")
    case "Hermoine":
        print("Gryphendor")
    case "Ron":
        print("Gryphendor")
    case "Malfoy":
        print("Slytherin")
    case _:
        print("You are Dead.")'''

match name:
    case "Harry" | "Hermoine" | "Ron":
        print("Gryphendor")
    case "Malfoy":
        print("Slytherin")
    case _:
        print("You are probably Dead.")