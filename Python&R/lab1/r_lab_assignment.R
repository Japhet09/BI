# Lab assignment
# Basic R usage and data manipulation ----
#QUESTION 1 ----

vec1 <- c(0, 2, 3, 0, 2, 11, 0, 7, NA)

# a) Removing the NA value
vec1_remove_na <- vec1[!is.na(vec1)]
vec1_remove_na

# b) logical vector where  0 == TRUE, otherwise FALSE
vec1_logical <- vec1 == 0
vec1_logical

# c) nonzero values 

# d) length of non zero values

# QUESTION 2 ----

# a) Creating a csv from the table
WOMEN <- c(109, 112, 115, 121, 128, 132, 135, 140, 148)
MEN <- c(120, 122, 124, 130, 136, 140, 143, 150, 155)
GENDER <- c(rep("Female", 9), rep("Male", 9))
W <- c(WOMEN, MEN)
YEAR <- c(rep(2003:2011, 2))
question2 <- data.frame(W, GENDER, YEAR)
question2

# b) exporting the dataframe as a csv
write.table(question2, "/Users/mac/Desktop/BI/Python&R/lab1/question2.csv", sep =",", row.names = FALSE)

# QUESTION 3 ----
# a) Importing the data
freedman <- read.table("/Users/mac/Desktop/BI/Python&R/lab1/Freedman.csv", sep = ",", dec = ".", header = TRUE, na.strings = NA)

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
freedman[more_than30, ]

# QUESTION 4 ----
# a) installing the Prestige package
install.packages("car")
library(car)

# b)
sub_prestige_women <- Prestige[Prestige$women > 50, ]

# c) average prestige score
mean(sub_prestige_women$prestige, na.rm = TRUE)
# d) average prestige score women < 50%

# e)for loop
for (i in 2:ncol(Prestige)) {
  mean(Prestige$i, na.rm = TRUE)
  
}

