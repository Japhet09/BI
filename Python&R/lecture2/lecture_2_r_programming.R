
# Lecture 2 R Programming

# See R script for lecture 1 for keyboard shortcuts.

# Slide 5 ----

# Use combine function to enter a numeric vector
x <- c(2, 3, 4, 4)
y <- c(1, 1, 1, 1)

# Instead use rep() to obtain y, since repeated values
# e.g., repeat the numerical value 1 as a vector of length 4
y <- rep(1, 4)

# Character data
Names <- c("John", "Danie", "Mary", "Oskar")

# Logical data
Male <- c(TRUE, TRUE, FALSE, TRUE)

# The numeric vector x
x <- c(2, 3, 4, 4)

# Slide 6 ----

# Construct a data frame with columns x, Names, and sex,
n <- data.frame()
# where the latter is a logical vector indicating
# the sex Male/Female.
# We construct this vector using characters as below.
indicator <- rep("Female", 4)
indicator[Male] <- "Male"
data <- data.frame(x, Names, sex = indicator)

# Slide 8 ----

# Let us investigate what we have created
# We use the functions class() and str()
class(data)
str(data)

# Slide 9 ----

# Enter YOUR OWN path here
my_path <- "C:/Downloads/"
path_to_save_space <- paste(my_path, "data_space.csv", sep = "")
path_to_save_comma <- paste(my_path, "data_comma.csv", sep = "")

# Save a space separated (delimited) version of the data 'data'
write.table(
  data,
  file = path_to_save_space,
  sep = " ",
  na = "NA",
  dec = ".",
  row.names  =  FALSE,
  col.names = TRUE
)

# Save a comma separated (delimited) version of the data 'data'
write.table(
  data,
  file = path_to_save_comma,
  sep = ",",
  na = "NA",
  dec = ".",
  row.names  = FALSE,
  col.names = TRUE
)

# Slide 12 ----

# Open a space separated (delimited) version of the data named 'data'
data_space <-
  read.table(
    file = path_to_save_space,
    header = TRUE,
    sep = " ",
    dec = ".",
    na.string = "NA"
  )

# Open a comma separated (delimited) version of the data named 'data'
data_comma <-
  read.table(
    file = path_to_save_comma,
    header = TRUE,
    sep = ",",
    dec = ".",
    na.string = "NA"
  )

# Try run this and see that we have the same data opened!
identical(data_space, data_comma)

# Slide 15 ----

# Create an object
test_object <- c(1, 2, 3)

# Saving the object to .rds extension file
saveRDS(test_object, file = "./path/name_of_file.rds")

# Read the object from .rds extension file
check_object <-
  readRDS(test_object, file = "./path/name_of_file.rds")

# Slide 17 ----

# Load data 'Prestige' from the R package 'car'
# Uncomment line below if have not installed yet:
# install.packages("car")
library(car)
data(Prestige)
? Prestige

# Slide 18 ----

# Debugging: Control that the imported Prestige data set
# looks like it should
summary(Prestige)
str(Prestige)

# Slide 21 ----

# Try to print the 'education' variable in 'Prestige'
# (This will fail with error message if not attached)
education

# Now attach the 'Prestige' data frame...
attach(Prestige)

# ...and try to print the 'education' variable in 'Prestige'
# (This should now succeed since attached)
education

# Detach Prestige
detach(Prestige)

# Slide 24 ----

# Attach Prestige
attach(Prestige)

# Change variable 'income' in attached copy of Prestige
income <- income / 1000

# Compute the average of income in the attached copy of Prestige
mean(income)

# Compute the average of income in the data frame Prestige
mean(Prestige$income)

# Detach Prestige
detach(Prestige)

# Slide 26 ----

# Create a vector with character data
y <- c(rep("yes", 2), rep("no", 3), rep("maybe", 4), "Don't know")
y

# Define it as a factor
y <- factor(y)
y

# Check the categories
levels(y)

# Check the number of categories
length(levels(y))

# Check the numbers in each category
summary(y)

# Slide 28 ----

# Some matrices and related functions

A <- matrix(c(1, 2, 3, 4), nrow = 3, ncol = 4)
A
dim(A)
ncol(A)
nrow(A)
length(A)

B <- matrix(c(1, 2, 3, 4), 3, 4, byrow = TRUE)
B
AB <- cbind(A, B)
AB
AB <- rbind(A, B)
AB

# Slide 29 ----

# A List
my_list <-
  list(
    A = A,
    B = B,
    C = matrix(c("a", "b", "c"), 3, 3),
    vec = c(0, 2, 3, 4)
  )

# Check str() of list
str(my_list)

# Print the whole list
my_list

# Only print the matrix A within the list
my_list$A

# Slide 31 ----

# NA values in data
y <- c(1, 3, 4, 5, NA, 5, NA)

# When you use the mean() function
# you now HAVE TO specify the na.rm option
# otherwise, no success in evaluating any mean
mean(y, na.rm = TRUE)

# With the summary function you don't have to do this.
summary(y)

# You can identify which elements are NA with is.na()
is.na(y)

# Slide 33 ----

# Recreate previous dataset
Names <- c("John", "Danie", "Mary", "Oskar")
Male <- c(TRUE, TRUE, FALSE, TRUE)

# Select Danie
Names[2]

# Or by a logical argument
Names[Names == "Danie"]

# "Danie" is actually "Daniel". Change this.
Names[Names == "Danie"] <- "Daniel"
Names

# Select the men
Names[Male]

# Select the only woman ('!' is negation)
Names[!Male]

# Slide 34 ----

# Make names as factor
f_names <- factor(Names)
f_names

# Select the first element
f_names[1]

# Select the boys
Male <- c(TRUE, TRUE, FALSE, TRUE)
f_names[Male]

# Slide 35 ----

# Create a matrix M
M <- matrix(c(1, 2, 3, 4), 4, 3)
M

# Select the first row of matrix M
M[1,]

# Select the second column
M[, 2]

# Remove row 2 and 3 ('-' is not)
M[-c(2, 3),]

# Select all value less than 3 from column 1
arg <- M[, 1] < 3
M[arg, 1]

# Slide 36 ----

# Check that Prestige is actually a data.frame
class(Prestige)

# Check the variable names of Prestige
names(Prestige)

# Compute the average of income using indexing
arg <- names(Prestige) == "income"
mean(Prestige[, arg])

# Select a sub-sample consisting of "prof" type of jobs
sub_Prestige <- subset(Prestige, type == "prof")
summary(sub_Prestige)

# Select without subset
summary(Prestige[Prestige$type == "prof", ])

# Slide 38 ----

# Create matrix
vec1 <- c(2, NA, 1, 3, 4, 6, NA)
vec2 <- c(NA, 2, 3, 4, 5, 4, NA)
Mat <- cbind(vec1, vec2)

# And
arg <- is.na(vec1) & is.na(vec2)
Mat[!arg, ]

# Or
arg <- is.na(vec1) | is.na(vec2)
Mat[!arg, ]

# Slide 40 ----

# Select the first object (matrix A) in my_list
my_list[[1]]

# Select the first row of matrix A in the my_list
my_list[[1]][1, ]
