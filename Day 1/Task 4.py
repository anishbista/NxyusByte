# Question 4: Develop a program that takes a sentence from the user and counts the number of vowels in it using a loop and conditional statement.

sentence = input("Enter a sentence: ")

vowels = ["a", "e", "i", "o", "u"]
count = 0

for x in sentence:
    if x.lower() in vowels:
        count += 1

print(f"Number of vowels in your sentence are {count}")
