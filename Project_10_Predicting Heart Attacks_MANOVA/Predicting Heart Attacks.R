library("mvnormtest")
library("car")
library("IDPmisc")

# How does gender (sex) influence some of the heart attack predictors like resting blood pressure (trestbps) and cholesterol (chol)?

# DATA WRANGLING

str(heartAttacks$trestbps) #variable is numeric
str(heartAttacks$chol)     #variable is numeric
str(heartAttacks$sex)      #variable is numeric, convert to string/character

heartAttacks$sex <- as.character(heartAttacks$sex)

# Remove missing data

heartAttacks1 <- NaRV.omit(heartAttacks)

# Subsetting

keeps <- c("trestbps", "chol")
heartAttacks2 <- heartAttacks1[keeps]

# Format as matrix

heartAttacks3 <- as.matrix(heartAttacks2)

# TESTING ASSUMPTIONS

# Multivariate Normality
mshapiro.test(t(heartAttacks3))  #Assumption violated

# Homogeneity of variance

leveneTest(chol ~ sex, data=heartAttacks) #Assumption violated

leveneTest(trestbps ~ sex, data=heartAttacks) #Assumption met

# Absence of Multi-collinearity

cor.test(heartAttacks$trestbps, heartAttacks$chol, method="pearson", use="complete.obs")
# correlation is less than 0.7 Hence, assumption met


# RUN MANOVA ANALYIS

MANOVA <- manova(cbind(trestbps, chol) ~ sex, data = heartAttacks)
summary(MANOVA)      #Significant! Gender influences heart attack predictors

# Post Hoc
summary.aov(MANOVA, test = "wilks")   #Gender is a significant predictor cholesterol levels (but not resting blood pressure)


