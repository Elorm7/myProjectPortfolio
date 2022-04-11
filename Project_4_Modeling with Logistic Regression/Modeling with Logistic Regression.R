library("caret")
library("magrittr")
library("dplyr")
library("tidyr")
library("lmtest")
library("popbio")
library("e1071")

#Testing assumptions

mylogit <- glm(Gold ~ Antimony, data=minerals, family="binomial")

#Predicting presence or absence of gold

probabilities <- predict(mylogit, type = "response")
minerals$Predicted <- ifelse(probabilities > .5, "present", "absent")

#Recoding predicted variables
minerals$PredictedR <- NA
minerals$PredictedR[minerals$Predicted=='present'] <- 1
minerals$PredictedR[minerals$Predicted=='absent'] <- 0

#Converting Gold and PredictedR variables to factors

minerals$PredictedR <- as.factor(minerals$PredictedR)
minerals$Gold <- as.factor(minerals$Gold)

#Creating Confusion Matrix
conf_mat <- caret::confusionMatrix(minerals$PredictedR, minerals$Gold)
conf_mat

#Note: Since one of the cells in the confusion matrix has a value less than 5, 
#this dataset does not meet the minimum sample size for binary logistic regression


#Logit Linearity
minerals1 <- minerals %>% 
dplyr::select_if(is.numeric)

predictors <- colnames(minerals1)

minerals1 <- minerals1 %>%
mutate(logit=log(probabilities/(1-probabilities))) %>%
gather(key= "predictors", value="predictor.value", -logit)

#Graphing
ggplot(minerals1, aes(logit, predictor.value))+
  geom_point(size=.5, alpha=.5)+
  geom_smooth(method= "loess")+
  theme_bw()+
  facet_wrap(~predictors, scales="free_y")

#From the graph, the predictor variable shows a strong linear relationship, hence passes this assumption.






