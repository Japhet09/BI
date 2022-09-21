
''' Let a user compare two letters and
evaluate whether one occurs before
the other in the english alphabet'''

first_letter = input("Input a letter: ")
second_letter = input("Input another letter: ")

if first_letter < second_letter:
    print("First letter comes before second")
elif first_letter > second_letter:
    print("Second letter comes before first")
else:
    print("The letters are in equal position")
