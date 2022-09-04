
# R programming laboration 1 exercises

# Use Alt + O (letter) to collapse code
# Use Alt + Shift + O (letter) to uncollapse code

# Exercise solutions for lecture 1.

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
x <- c(1:20,30:70,80:100)

# Provide the mean, length and sum of this vector
mean(x)
length(x)
sum(x)

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
fahrenheit_to_celsius <- function(temp_F) {
  temp_C <- (temp_F - 32) * 5 / 9
  if (temp_C < 21) {
    
    print("Please turn on the stove!")
    
  } else if (temp_C > 100) {
    
    print("The water is too hot and the tea will be ruined!")
    
  } else {
    
    return(round(100 - temp_C, 0))
    
  }
}

# Test the function. If it works, that is.
fahrenheit_to_celsius(100)

# Create a function which loops over a range of tempratures,
# and gradually slows down until max temperature is reached
# where it should stop completely (i.e., when max temperature reached)
# The function should disregard any range of negative temperatures 
# being supplied. Also, time taken should be displayed for each iteration.
#
# Hint: syntax "break" can be used to stop a loop within a iteration.
# Hint: syntax "next" can be used to jump to the next iteration.

boiling_function <- function (x) {
  
  values <- x[x > 0]
  
  for (i in values) {
    
    condition_to_check <- fahrenheit_to_celsius(i)[1]
    
    start_time <- Sys.time()
    
    if (condition_to_check %in% "The water is too hot and the tea will be ruined!") {
      
      break
      
    } else if (condition_to_check %in% "Please turn on the stove!") {
      
      next
      
    } else if (i == 0) {
      
      result <- fahrenheit_to_celsius(i)
      print(result)
      
    } else {
      
      result <- fahrenheit_to_celsius(i)
      print(result)
      Sys.sleep(i/1000)
      
    }
    
    print(Sys.time() - start_time)
    
  }
  
}

# Test the function
boiling_function(1:214)

boiling_function(x)

# Compile these functions
library(compiler)
fahrenheit_to_celsius <- cmpfun(fahrenheit_to_celsius)
boiling_function <- cmpfun(boiling_function)
