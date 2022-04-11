#Part 1

FitAll = lm(IQ ~ ., data = IQ)
summary(FitAll)

step(FitAll, direction = 'backward')

fitbest = lm(IQ ~ Test1 + Test2 + Test4, data = IQ)
summary(fitbest)

#Part 2
#backward

FitAll1 = lm(Y ~ ., data = stepwiseRegression)
summary(FitAll1)


step(FitAll1, direction = 'backward', scope = formula(FitAll1))

#Forward Selection
fitstart = lm(Y ~ 1, data = stepwiseRegression)
summary(fitstart)

step(fitstart, direction = 'forward', scope = (formula(FitAll1)))

#StepWise 
step(fitstart, direction = 'both', scope = formula(FitAll1))

fitsome <- lm(formula = Y ~ X2 + X4 + X6 + X10 + X11 + X12, data = stepwiseRegression)
summary(fitsome)