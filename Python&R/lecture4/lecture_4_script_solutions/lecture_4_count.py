
# Let's try and write a count loop
# with an accumulator.

count = 0

for i in range(1,6):
    count = count + i
    print(count)

print("The final count is", count)

# with shorthand notation

count = 0

for i in range(1,6):
    count += i
    print(count)

print("The final count is", count)
