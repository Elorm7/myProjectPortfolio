install.packages("Ecdat")
library("Ecdat")
library("ggplot2")
library("dplyr")
library("tidyr")
library("tidyverse")

View(Cigarette)

#Boxplot of the average number of packs per capita by state.

ggplot(Cigarette, aes(x= state, y= packpc)) + geom_boxplot()

#States which have the highest & lowest number of packs

Extremes <- Cigarette %>% group_by(state) %>% summarise(Mean = mean(packpc)) %>% arrange(Mean)
head(Extremes) # UT has the lowest number of packs
tail(Extremes) # KY hast the highest number of packs

#Finding the median over all the states of the number of packs per capita for each year.

packpc_median <- Cigarette %>% group_by(year) %>% summarise(Medpackpc = median(packpc))

#Plotting median value for the years from 1985 to 1995

ggplot(packpc_median, aes(x= year, y= Medpackpc)) + geom_point()
# From the graph, cigarette usage has gradually decreased over the years


# Creating a scatter plot of price per pack vs number of packs per capita for all states and years.

ggplot(Cigarette, aes(x = avgprs, y = packpc)) + geom_point() + geom_smooth(method = lm) + xlab("Price per pack") + ylab("Packs per capita")

# Are the price and the per capita packs positively correlated, negatively correlated, or uncorrelated? 

cor.test(Cigarette$avgprs, Cigarette$packpc, method = "pearson", use = "complete.obs")
# There is  negative moderate correlation between price & packs per capita


#Changing scatter plot to show the points for each year in a different color.

ggplot(Cigarette, aes(x = avgprs, y = packpc, color = year)) + geom_point() + geom_smooth(method = lm) + xlab("Price per pack") + ylab("Packs per capita")

#From the graph, 1980s saw higher cigarette consumption at lower prices. However, into the 1990s, as prices increased packs per capita decreased


#Linear regression for pack per capita & average price per pack

regression <- lm(packpc~avgprs, Cigarette)
summary(regression)
# The line explains 34% of variability

# Adjusting avgprs for inflation

infladjusted <- Cigarette %>% mutate(inflprs = avgprs / cpi)

#Plotting scatter plot with inflation adjusted price & packs per capita

ggplot(infladjusted, aes(x = inflprs, y = packpc, color = year)) + geom_point() + geom_smooth(method = lm) + xlab("Inflation-adjusted price per pack") + ylab("Packs per capita")

#Performing regression analysis with inflation adjusted price & packs per capita
regression <- lm(packpc~inflprs, Cigarette)
summary(regression)  #The line explains 34% of variability

#Creating data frames with rows from 1985
Cigarette1985 <- Cigarette %>% filter(year == 1985)

#Creating data frames with rows from 1995
Cigarette1995 <- Cigarette %>% filter(year == 1995)

#Use a paired t-test to see if the number of packs per capita in 1995.. 
#..was significantly different than the number of packs per capita in 1985.

t.test(Cigarette1985$packpc, Cigarette1995$packpc, paired = TRUE)

Mean1985 <- mean(Cigarette1985$packpc)
Mean1985

Mean1995 <- mean(Cigarette1995$packpc)
Mean1995

#There was significant change in the number of packs per capita, decreasing from 122.04 packs per capita in 1985, to 96.33 in 1995





