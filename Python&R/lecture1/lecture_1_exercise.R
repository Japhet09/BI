
# R programming laboration 1 exercises

# Use Alt + O (letter) to collapse code
# Use Alt + Shift + O (letter) to uncollapse code

# In the comments below there are exercises to complete.
# The solutions are found in a separate script.
# Take help from lecture 1, the additional material script
# as well as ask me questions when you get stuck! :)

# install packages ----

# install the package "fortunes"
install.packages("fortunes")

# Load the package "fortunes" from library
library(fortunes)

# Try the function fortune() from package "fortunes"
fortune()

# Sequences ----

# Give a sequence of number between 1 and 100 with 
# a gap between 20 and 30 as well as 70 and 80.
nums <- c(1:20,30:70,80:100)
nums

# Provide the mean, length and sum of this vector
mean(nums)
length(nums)
sum(nums)

# Functions ----

# Consider the function
fahrenheit_to_celsius <- function(temp_F) {
  temp_C <- (temp_F - 32) * 5 / 9
  return(temp_C)
}

# Adjust this function so that it:
#
# 1. Returns the number of degrees left until the temperature 
# has reached the boiling point. Round off the values to integers.
# 2. If water is below 21 degrees celsius, ask to turn on the stove
# using printed message.
# 3. If water is above 100 degrees celsius, give a warning message
# that the water is too hot and the tea will be ruined!

# Test the function. If it works, that is.

# Create a function which loops over a range of tempratures,
# and gradually slows down until max temperature is reached
# where it should stop completely (i.e., when max temperature reached)
# The function should disregard any range of negative temperatures 
# being supplied. Also, time taken should be displayed for each iteration.
#
# Hint: syntax "break" can be used to stop a loop within a iteration.
# Hint: syntax "next" can be used to jump to the next iteration.

# Test the function

# Compile these functions
