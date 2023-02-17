# bias-variance tradeoff example plots

# generate fake quadratic trend data
set.seed(8675309)

# x is randomly sampled from a normal distribution
n <- 100
x <- rnorm(n=n, mean = 0, sd = 1)
# y is x squared, plus random noise
y <- x^2 + rnorm(n=n, mean = 0, sd = 2)

# trend lines
linear <- predict(lm(y ~ x))
quadratic <- predict(lm(y ~ poly(x, 2, raw = TRUE)))
nthpoly <- predict(lm(y ~ poly(x, n-2, raw = TRUE)))

# put it into a data frame for plotting
df <- data.frame(x=x, 
                 y=y,
                 l = linear,
                 q = quadratic, 
                 n = nthpoly)

# plots
library(ggplot2)

base_plot <- ggplot(df, aes(x=x, y=y)) + 
  geom_point() + 
  labs(x="BMI Z-scores", y="Depressive Symptoms") + 
  scale_x_continuous(breaks = NULL) + 
  scale_y_continuous(breaks = NULL) + 
  theme_classic()

underfit <- base_plot + 
  geom_line(aes(y=l)) 
ggsave(filename = file.path("media", "underfit.png"), underfit, width = 5, height = 5, units = "in")

overfit <- base_plot + 
  geom_line(aes(y=n)) 
ggsave(filename = file.path("media", "overfit.png"), overfit, width = 5, height = 5, units = "in")

goodfit <- base_plot + 
  geom_line(aes(y=q)) 
ggsave(filename = file.path("media", "goodfit.png"), goodfit, width = 5, height = 5, units = "in")

