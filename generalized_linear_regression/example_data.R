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

# random sampling of 0 and 1 for trisomy_21_dx
# sample from a normal distribution for BPD/FL, but use a higher mean if trisomy_21_dx == 1
data <- data.frame(trisomy_21_dx = sample(x = c(0,0,0,1), 
                                          size = n, 
                                          replace = TRUE)) |> 
  mutate(`BPD/FL` = ifelse(trisomy_21_dx == 1, 
                           rnorm(n, mean = 1.6, sd = .2),
                           rnorm(n, mean = 1.5, sd = .2)))


base_plot <- ggplot(data, aes(y=trisomy_21_dx, x=`BPD/FL`)) + 
  geom_point() + 
  theme_bw() + 
  labs(y = "Trisomy 21 Dx")

# try plotting the data with just a linear model
base_plot + 
  stat_smooth(method = "lm")
ggsave("linear_prediction.png", width = 5, height = 5, units = "in")

base_plot + 
  stat_smooth(method = "glm", method.args = list(family = "binomial"))
ggsave("logit_prediction.png", width = 5, height = 5, units = "in")



