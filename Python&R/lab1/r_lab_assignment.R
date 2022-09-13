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
