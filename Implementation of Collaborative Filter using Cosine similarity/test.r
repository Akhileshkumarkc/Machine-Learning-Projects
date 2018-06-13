cosine <- read.table("predictions_cosine.txt",header = T, sep = ",")
pearson <- read.table("predictions_pearson.txt",header = T, sep = ",")
names(cosine) <- c("movieid","userid","givenrating","predictedrating")
names(pearson) <- c("movieid","userid","givenrating","predictedrating")

summary(cosine)
summary(pearson)
par(mfrow = c(1, 2))
plot(cosine$givenrating,cosine$predictedrating)
plot(pearson$givenrating,pearson$predictedrating)
par(mfrow = c(1, 1))


par(mfrow = c(1, 3))
hist(cosine$givenrating, xlab = "Given Rating" )
hist(cosine$predictedrating, xlab = " cosine Predicted Rating")
par(mfrow = c(1, 1))

hist(cosine$predictedrating, xlab = " cosine Predicted Rating")
hist(pearson$predictedrating,xlab = "Pearson Predicted Rating")
