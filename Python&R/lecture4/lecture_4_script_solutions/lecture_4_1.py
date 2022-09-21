

# Warm or cold?

# Print a message to wear a coat if it is cold,
# else print a message that no coat is needed.

is_it_cold = input("Is it cold outside? Yes or No: ").lower()

if is_it_cold == "yes":
    print("Wear a coat!")

else:
    print("No coat needed!")


# Warm or cold... maybe..?

# Print a message to wear a coat if it is cold,
# else print a message that no coat is needed.
# But also account for if it will maybe be cold,
# and ask to wear a coat just in case. 
is_it_cold = input("Is it cold outside? Yes, No or Maybe: ").lower()

if is_it_cold == "yes":
    print("Wear a coat!")

elif is_it_cold == "no":
    print("No coat needed!")

else:
    print("Err... perhaps you should bring the coat anyways..")
