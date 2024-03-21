# show the relationship between probability, odds, and logits
logit_demo <- data.frame(Logit = c(-Inf, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, Inf)) |> 
  mutate(Odds = exp(Logit),
         Probability = ifelse(Odds < Inf, Odds / (1 + Odds), 1))
knitr::kable(logit_demo, digits = 3)

library(tidyverse)
# set the random seed so results replicate exactly with the random number generators
set.seed(24601)

# sample size
n <- 100

# random sampling of 0 and 1 for sepsis
# sample from a normal distribution for heart_rate and temp, but use a higher mean if sepsis == 1
data <- data.frame(sepsis = sample(x = c(0,0,0,1), 
                                          size = n, 
                                          replace = TRUE)) |> 
  mutate(heart_rate = ifelse(sepsis == 1, 
                           rnorm(n, mean = 100, sd = 10),
                           rnorm(n, mean = 95, sd = 10)),
         temp = ifelse(sepsis == 1, 
                           rnorm(n, mean = 102, sd = 1),
                           rnorm(n, mean = 101, sd = 1)))                           


base_plot <- ggplot(data, aes(y=sepsis, x=heart_rate)) + 
  geom_point() + 
  theme_bw() + 
  labs(y = "Sepsis", x="Heart Rate")

# try plotting the data with just a linear model
base_plot + 
  stat_smooth(method = "lm")
ggsave("linear_prediction.png", width = 5, height = 5, units = "in")

base_plot + 
  stat_smooth(method = "glm", method.args = list(family = "binomial"))
ggsave("logit_prediction.png", width = 5, height = 5, units = "in")
