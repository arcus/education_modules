# bias-variance tradeoff example plots

# generate fake quadratic trend data
n <- 100
set.seed(1234)

# x is randomly sampled from a normal distribution
x <- rnorm(n=n, mean = 0, sd = 1)
# y is x squared, plus random noise
y <- -1*x^2 + rnorm(n=n, mean = 0, sd = 1)

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
  geom_point(alpha = .7) + 
  labs(x="Blood Pressure", y="Cognitive Performance") + 
  scale_x_continuous(breaks = NULL) + 
  scale_y_continuous(breaks = NULL) + 
  theme_classic()

underfit <- base_plot + 
  geom_line(aes(y=l)) 
ggsave(filename = file.path("media", "underfit_1.png"), underfit, width = 5, height = 4, units = "in")

overfit <- base_plot + 
  geom_line(aes(y=n)) 
ggsave(filename = file.path("media", "overfit_1.png"), overfit, width = 5, height = 4, units = "in")

goodfit <- base_plot + 
  geom_line(aes(y=q)) 
ggsave(filename = file.path("media", "goodfit_1.png"), goodfit, width = 5, height = 4, units = "in")

# facet plots
data <- tibble(sample = rep(c("Sample 1", "Sample 2", "Sample 3"), n),
               x = seq(from = -2, to = 2, length.out = n*3),
               y = -1*x^2 + rnorm(n=n*3, mean = 0, sd = 1)) |> 
  group_by(sample) |> 
  mutate(linear = predict(lm(y ~ x)),
         quadratic = predict(lm(y ~ poly(x, 2, raw = TRUE))),
         nthpoly = predict(lm(y ~ poly(x, 16, raw = TRUE))))

base_plot <- ggplot(data, aes(x=x, y=y)) + 
  geom_point(alpha = .3, show.legend = FALSE) + 
  facet_wrap(~sample) + 
  labs(x="Blood Pressure", y="Cognitive Performance") + 
  scale_x_continuous(breaks = NULL) + 
  scale_y_continuous(breaks = NULL) + 
  theme_classic()

underfit_facet <- base_plot + 
  geom_line(aes(y=linear), size = 1.5) 
ggsave(filename = file.path("media", "underfit_2.png"), underfit_facet, width = 9, height = 4, units = "in")

overfit_facet <- base_plot + 
  geom_line(aes(y=nthpoly), size = 1.5) 
ggsave(filename = file.path("media", "overfit_2.png"), overfit_facet, width = 9, height = 4, units = "in")

goodfit_facet <- base_plot + 
  geom_line(aes(y=quadratic), size = 1.5) 
ggsave(filename = file.path("media", "goodfit_2.png"), goodfit_facet, width = 9, height = 4, units = "in")

