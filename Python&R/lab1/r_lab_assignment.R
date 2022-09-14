# Lab 1 assignment ----
# Basic R usage and data manipulation
#QUESTION 1 ----

vec1 <- c(0, 2, 3, 0, 2, 11, 0, 7, NA)

# a) Removing the NA value
vec1 <- vec1[!is.na(vec1)]
vec1

# b) logical vector where  0 == TRUE, otherwise FALSE
vec1_logical <- vec1 == 0
vec1_logical

# c) nonzero values
non_zero <- vec1[!vec1_logical]
non_zero

# d) length of non zero values
length(non_zero)

# QUESTION 2 ----

# a) Creating a csv from the table
# first create vectors for each corresponding row
WOMEN <- c(109, 112, 115, 121, 128, 132, 135, 140, 148)
MEN <- c(120, 122, 124, 130, 136, 140, 143, 150, 155)
GENDER <- c(rep("Female", 9), rep("Male", 9))
W <- c(WOMEN, MEN)
YEAR <- c(rep(2003:2011, 2))

# then using the vectors to create the data frame
question2 <- data.frame(W, GENDER, YEAR)
question2

# b) exporting the data frame as a csv file
write.table(
  question2,
  "/Users/mac/Desktop/BI/Python&R/lab1/question2.csv",
  sep = ",",
  dec = ".",
  row.names = FALSE,
  col.names = TRUE
)

# QUESTION 3 ----
# a) Importing the data
freedman <-
  read.table(
    "/Users/mac/Desktop/BI/Python&R/lab1/Freedman.csv",
    sep = ",",
    dec = ".",
    header = TRUE,
    na.strings = NA
  )

# b)
summary(freedman)
str(freedman)

# c)
# change the variables  to numeric
freedman$population <- as.numeric(freedman$population)
freedman$nonwhite <- as.numeric(freedman$nonwhite)
freedman$density <- as.numeric(freedman$density)
freedman$crime <- as.numeric(freedman$crime)

# confirm that they are now  numeric
is.numeric(freedman$population)
is.numeric(freedman$nonwhite)
is.numeric(freedman$density)
is.numeric(freedman$crime)

# d) Mean for each numerical column, stripping the NA before computation
mean_population <- mean(freedman$population, na.rm = TRUE)
mean_nonwhite <- mean(freedman$nonwhite, na.rm = TRUE)
mean_density <- mean(freedman$density, na.rm = TRUE)
mean_crime <- mean(freedman$crime, na.rm = TRUE)

# e) non white larger than 30%
more_than30 <- freedman$nonwhite > 30
freedman[more_than30,]

# QUESTION 4 ----
# a) installing the Prestige package
install.packages("car")
# loading the library
library(car)

# b) data frame of occupations with more than 50% women
sub_prestige_women <- Prestige[Prestige$women > 50,]

# c) average prestige score for this sub group
mean(sub_prestige_women$prestige, na.rm = TRUE)

# d) average prestige score women less 50%
below_50_women <- Prestige[Prestige$women < 50,]
mean(below_50_women$prestige, na.rm = TRUE)

# e)Average prestige score using a for loop

# store all unique occupation in a vector dropping missing values
unique_occupation <- unique(Prestige$type)
unique_occupation <- unique_occupation[!is.na(unique_occupation)]

# initialize empty vector to store the averages
occu_type_average <- c()

# loop through the unique occupations type
for (i in unique_occupation) {
  x <- mean(Prestige[Prestige$type == i,]$prestige, na.rm = TRUE)
  occu_type_average <- c(occu_type_average, x)
}
occu_type_average
