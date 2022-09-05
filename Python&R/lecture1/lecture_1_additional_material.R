
# R programming Lecture 1 Additional material

# Use Alt + O (letter) to collapse code
# Use Alt + Shift + O (letter) to uncollapse code

# install packages ----
install.packages("car")
library(car)

# Dates and time ----

# What date is it now?
Sys.Date()

# I want more specifics!
Sys.time()

# What date is it tomorrow and yesterday?
Sys.Date() + 1
Sys.Date() - 1

# What is the time 1 minute from now and 1 minute ago?
Sys.time() + 60
Sys.time() - 60

# What timezone is currently used?
Sys.timezone()

# Make R "Sleep" for 5 seconds... zzz -_-
# Useful for loops and functions,
# especially for web scraping.
Sys.sleep(5)

# Sequences ----

# Display some sequences of numbers
seq(30, 90)
mean(30:90)
sum(30:90)

# Find the maximum and minimum value of the sequence 30 to 90
min(seq(30, 90))
max(30:90)

# Combine two sequences
c(1:5, 10:15)

# Repeat a number 5 times
rep(2, 5)

# Combine two sequences and the repeated number
c(1:5, 10:15, rep(2, 5))

# Objects and memory ----

# Create some objects in the R environment
# The addition of L after the number 5 creates a integer value
a <- 5L
b <- 1.25
c <- "Steve"
d <- TRUE

# Check the classes and types
class(a)
typeof(a)

class(b)
typeof(b)

class(c)
typeof(c)

class(d)
typeof(d)

# Note the difference for b which is class numeric and typeof double.
# Numeric classes are of multiple types, whereby double and integer are two.
# Below is shown that actually a is also numeric!

# Both are numeric, even the one of class integer.
is.numeric(a)
is.numeric(b)

# Only b is double, however.
is.double(a)
is.double(b)

# I can show that the size is less for integers.
# It is, however, not possible with only one number.
one_integer <- 5L
one_double <- 5
object.size(one_integer)
object.size(one_double)

# But with some more numbers it can easily be shown
# that the eqvivalent vectors are of different size
multiple_integers <- c(5L, 4L, 3L, 2L, 1L)
multiple_doubles <- c(5, 4, 3, 2, 1)
is.double(multiple_integers)
is.double(multiple_doubles)
object.size(multiple_integers)
object.size(multiple_doubles)

# Return a vector of the objects in the environment
ls()

# Use help to learn about the function ls
? ls

# Let us remove the object given by the symbol c from environment
# Notice how it does not exist in environment anymore!
rm(c)

# Use help to learn about rm
# Take special note of the "list" argument in the help function
? rm

# We remove some more objects
rm(a, b)

# Maybe it feels tedious to remove each object one by one...
# Let us remove ALL OF THEM!
# Remember that ls() gives the entire vector of objects in
# the environment, and the list argument of rm
rm(list = ls())

# Now the environment is nice and clean :)

# There is also a function called gc() which refers to "garbage collection".
# It clears the memory, and should therefore give access to more RAM memory.
# R, however, usually deals with this by itself quite efficiently anyways.
gc()

# I am tired of all the mess that has built up in the console...
# Felt it is distracting. Let's clear it!
# Ctrl + L on Windows Rstudio accomplishes this.

# Functions ----

# I use the Rstudio environment and simply type "fun" and
# press ENTER to get a prepared function defintion

# Type "fun" below, wait half a second or so, and press ENTER

# I can show easily that we are actually using functions quite
# extensively in R. Run the code below and check console
abs
mean
sd

# Lets create a simple function
fahrenheit_to_celsius <- function(temp_F) {
  temp_C <- (temp_F - 32) * 5 / 9
  return(temp_C)
}

# freezing point of water
fahrenheit_to_celsius(32)

# boiling point of water
fahrenheit_to_celsius(212)

# We can also show the inner workings of the functions,
# by omitting the () parentheses
fahrenheit_to_celsius

# The bytecode implies that the function has been compiled
# by the compiler package and as is thus faster.

# Clean up code!
# Ctrl + A
# Ctrl + Shift + A
#
# or highlight code and use
# Ctrl + Shift + A

# Lets try another function
mySum <- function(arg_1, arg_2 = 10) {
  output <- arg_1 + arg_2
  return(output)
}

# Lets have a look at the function
mySum

# The function is not compiled.
# But we can do this ourselves, if we so please.
# The package compiler already comes with R since version 2.13.0.
library(compiler)

# Lets compile it using function cmpfun
mySum_compiled <- cmpfun(mySum)
mySum_compiled

# We can even compare the speed
# For these particular functions, it's quite close.
# install.packages("microbenchmark")
# install.packages("ggplot2")
install.packages("microbenchmark")
library(microbenchmark)
library(ggplot2)
x = rnorm(100)
autoplot(microbenchmark(
  times = 10,
  unit = "ms",
  # milliseconds
  mySum(x),
  mySum_compiled(x)
))

# If we try run it without the first argument it will fail.
# The first argument has no default value.
mySum()

# Now we use a value in the first argument.
mySum(10)

# We can also override the second argument default value.
mySum(5, 5)

# To be clear, all the code below are equivalent in the output it produces
# despite the variation in syntax.
mySum(5, 5)
mySum(arg_1 = 5, 5)
mySum(5, arg_2 = 5)
mySum(arg_1 = 5, arg_2 = 5)

# Reordering as below is also possible, but is kind of pointless and confusing.
mySum(arg_2 = 5, arg_1 = 5)

# We can return multiple objects from a function,
# but to do so we would have to
# create a list.
# This will be covered in Lecture 2.

# Vectors ----

# Let us create a vector of values
x <- c(9, 7, 5, 3, 2, 4, 2)
y <- c(1, 8, 3, 2, 5, 7, 6)

# We can perform arithmetics on these vectors.
# Remember that vectors are basically columns in R,
# even though they might appear to look like rows in the console.
# Operations are made element-wise.
x - y
x + y
x * y
x / y
# and so on...

# The length can be found as following
length(x)
length(y)
length(c(x, y))
length(c(x, y, x, y))

# Check the console for how longer vectors are given
# Especially with regards to the square brackets []
rnorm(1000)

# Indexing numerical vectors ----

# Let us create a vector of values
x <- c(9, 7, 5, 3, 2, 4, 2)
y <- c(1, 8, 3, 2, 5, 7, 6)

# Select element 3 of both vectors
x[3]
y[3]

# Select values larger than 4 in both vectors
x[x > 4]
y[y > 4]

# Logical vector for values of x that exist in y
x %in% y

# Logical vector for values of x that does not exist in y
# i.e., negate the logical vector!(x %in% y)

# Select values in x that exist in y
x[x %in% y]

# Select values in x that does not exist in y
# i.e., negate the logical vector when subsetting
x[!(x %in% y)]

# Do the same, but switch x and y position
y[y %in% x]
y[!(y %in% x)]

# Select values in x which are in y,
# but also are larger or equal to 5
x[x %in% y & x >= 5]

# Select values in x which are in y,
# are also larger or equal to 5, AND
# is less than 7
x[x %in% y & x >= 5 & x < 7]

# Select values in x which are in y,
# are also larger or equal to 5, OR
# is less than 7
x[x %in% y & x >= 5 | x < 7]

# Indexing character vectors and logical ----

# Create character vectors and logical vectors,
vip_names <-
  c(
    "Charlie",
    "Kenneth",
    "Mengjie",
    "Moudud",
    "Kristina",
    "Greta Thunberg",
    "Stefan L?fven",
    "Jultomten"
  )
male <- c(TRUE, TRUE, TRUE, TRUE, FALSE, FALSE, TRUE, TRUE)
work <- c(rep("Dalarna University", 5),
          "Unemployed",
          "Looking for job",
          "North Pole")

# Only select employees of Dalarna University
vip_names[work %in% "Dalarna University"]

# Only select females working in Dalarna University
vip_names[work %in% "Dalarna University" & !male]

# Only select males not working in Dalarna University
vip_names[!(work %in% "Dalarna University") & male]

# Only select people working in the North Pole
vip_names[work %in% "North Pole"]

# Conditionals and Loops ----

# Create character vectors and logical vectors,
vip_names <-
  c(
    "Charlie",
    "Kenneth",
    "Mengjie",
    "Moudud",
    "Kristina",
    "Greta Thunberg",
    "Stefan L?fven",
    "Jultomten"
  )
male <- c(TRUE, TRUE, TRUE, TRUE, FALSE, FALSE, TRUE, TRUE)
work <- c(rep("Dalarna University", 5),
          "Unemployed",
          "Looking for job",
          "North Pole")

# Loop over the vip names and print these names,
for (my_iteration in vip_names) {
  print(my_iteration)
  
}

# Show what seq_along function does
seq_along(vip_names)

# Loop over the vip names and print these names, 
# sex, and employment
for (i in seq_along(vip_names)) {
  if (male[i]) {
    sex <- "Male"
    
  } else {
    sex <- "Female"
    
  }
  
  result <- c(vip_names[i],
              sex,
              work[i])
  
  print(result)
  
}

# In R, %% gives the modular division. I.e., the remainder after a division.
# For instance:
75 / 4
# has remainder of 3
75 %% 4
# where hence
(75 - 3) %% 4
# Gives no remainder.
#
# Modular division is very useful in R.

# Create a function which loops over a given sequence of numbers,
# and print a message if the value is an odd number,
# but also print a message if the number is negative.
check_numbers <- function(x) {
  for (i in x) {
    print(i)
    
    if ((i %% 2) == 0 & i < 0) {
      print("number is even and negative")
      
    } else if ((i %% 2) != 0 & i < 0) {
      print("number is odd and negative")
      
    } else if ((i %% 2) != 0 & i > 0) {
      print("number is odd and positive")
      
    } else {
      print("number is even and positive")
      
    }
    
  }
  
}

# Let us try it out!
check_numbers(-5:5)

# Plotting a volcano with R! ----

# install package plotly
install.packages("plotly", dependencies = TRUE)
library(plotly)

# volcano is a numeric matrix that ships with R
volcano

# Plot the volcano interactively using plotly!
fig <- plot_ly(z = ~ volcano)
fig <- fig %>% add_surface()
fig

# Add contours to the volcano!
fig <- plot_ly(z = ~ volcano) %>% add_surface(contours = list(
  z = list(
    show = TRUE,
    usecolormap = TRUE,
    highlightcolor = "#ff0000",
    project = list(z = TRUE)
  )
))
fig <- fig %>% layout(scene = list(camera = list(eye = list(
  x = 1.87, y = 0.88, z = -0.64
))))
fig
