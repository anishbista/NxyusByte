# Write a program that prompts the user to enter two sets of numbers. Print the
# intersection and union of the two sets.
set1 = set()
set2 = set()

while True:
    try:
        set1_size = int(input("Enter the size of set 1: "))
        set2_size = int(input("Enter the size of set 2: "))

        for x in range(1, set1_size + 1):
            try:
                element = int(input(f"Enter the {x} element for set1: "))
                set1.add(element)
            except ValueError as e:
                print("You entered other characters. Enter number only")
        for x in range(1, set2_size + 1):
            try:
                element = int(input(f"Enter the {x} element for set2: "))
                set2.add(element)
            except ValueError as e:
                print("You entered other characters. Enter number only")

        intersection = set1.intersection(set2)
        union = set1.union(set2)

        print(f"Intersection of the two sets: {intersection}")
        print(f"Union of the two sets: {union}")
        break
    except ValueError:
        print("Invalid input for set size. Enter a valid number.")
