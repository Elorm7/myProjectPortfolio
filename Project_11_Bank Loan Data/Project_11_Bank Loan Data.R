install.packages("gmodels")
library("gmodels")
library("tidyr")
library("dplyr")

# Part 1 (Independent Chi square)
# Does the term of the loan influence loan status? If so, how?

CrossTable(loans$term, loans$loan_status, fisher=TRUE, chisq = TRUE, expected = TRUE, sresid=TRUE, format="SPSS")

# CONCLUSION
# All cells have expected value greater than 5, therefore the assumption has been met
#  The p-value is less than 0.05, hence the Loan term significantly influences Loan status.
#   The 36 months loan term was charged-off less than expected and paid fully more than expected
#   The 60 months loan term was charged-off more than expected and paid fully less than expected


# Part 2 (McNemar)
# How has the ability to own a home changed after 2009?

loans$DateR <- as.Date(paste(loans$Date), "%m/%d/%Y")

loans1 <- separate(loans, DateR, c("Year", "Month", "Day"), sep="-")

loans1$YearR <- NA
loans1$YearR[loans1$Year <= 2009] <- 0
loans1$YearR[loans1$Year > 2009] <- 1

loans1$RentvOwn <- NA
loans1$RentvOwn[loans1$home_ownership == "RENT"] <- 0
loans1$RentvOwn[loans1$home_ownership == "OWN"] <- 1

CrossTable(loans1$RentvOwn, loans1$YearR, fisher=TRUE, chisq = TRUE, mcnemar = TRUE, expected = TRUE, sresid=TRUE, format="SPSS") 

# CONCLUSION
# All cells have expected value greater than 5, therefore the assumption has been met
#  A p-value of 0 indicates a significant difference in the ability to own homes before and after 2009.
#   However,since  none of the standard residuals have an absolute value of 2 or above, this test can be considered as is insignificant. 
#    Therefore, the ability to own homes has not been significantly change after 2009 


# Part 3
# Goodness of Fit Chi squares

loans %>% group_by(loan_status) %>% summarize(count=n())
observed = c(18173, 3282, 502)
expected = c(0.15, 0.10, 0.75)

chisq.test(x = observed, p = expected)

# CONCLUSION
# Since the p-value is less than 0.05, the there is a significant difference between the observed and expected values.
# Hence, the claim that 15% of homes are paid for fully paid for, and 10% charged of is not likely to have been based off the larger population of America.







