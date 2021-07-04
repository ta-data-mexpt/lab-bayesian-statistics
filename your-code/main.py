# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Intro to Bayesian Statistics Lab
# 
# Complete the following set of exercises to solidify your knowledge of Bayesian statistics and Bayesian data analysis.

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# %% [markdown]
# ## 1. Cookie Problem
# 
# Suppose we have two bowls of cookies. Bowl 1 contains 30 vanilla cookies and 10 chocolate cookies. 
# Bowl 2 contains 20 of each. You randomly pick one cookie out of one of the bowls, and it is vanilla. 
# Use Bayes Theorem to calculate the probability that the vanilla cookie you picked came from Bowl 1?

# %%
priors = [3/4, 1/4]
likelihoods = [1/2, 1/2]

def bayes(priors, likelihoods):
    marginal = sum(np.multiply(priors, likelihoods))
    num = np.multiply(priors, likelihoods)
    posteriori = np.divide(num, marginal)
    return posteriori

bayes(priors, likelihoods)


# %% [markdown]
# What is the probability that it came from Bowl 2?

# %%


# %% [markdown]
# What if the cookie you had picked was chocolate? What are the probabilities that the chocolate cookie came from Bowl 1 and Bowl 2 respectively?

# %%


# %% [markdown]
# ## 2. Candy Problem
# 
# Suppose you have two bags of candies:
# 
# - In Bag 1, the mix of colors is:
#     - Brown - 30%
#     - Yellow - 20%
#     - Red - 20%
#     - Green - 10%
#     - Orange - 10%
#     - Tan - 10%
#     
# - In Bag 2, the mix of colors is:
#     - Blue - 24%
#     - Green - 20%
#     - Orange - 16%
#     - Yellow - 14%
#     - Red - 13%
#     - Brown - 13%
#     
# Not knowing which bag is which, you randomly draw one candy from each bag. One is yellow and one is green. What is the probability that the yellow one came from the Bag 1?
# 
# *Hint: For the likelihoods, you will need to multiply the probabilities of drawing yellow from one bag and green from the other bag and vice versa.*

# %%


# %% [markdown]
# What is the probability that the yellow candy came from Bag 2?

# %%


# %% [markdown]
# What are the probabilities that the green one came from Bag 1 and Bag 2 respectively?

# %%


# %% [markdown]
# ## 3. Monty Hall Problem
# 
# Suppose you are a contestant on the popular game show *Let's Make a Deal*. The host of the show (Monty Hall) presents you with three doors - Door A, Door B, and Door C. He tells you that there is a sports car behind one of them and if you choose the correct one, you win the car!
# 
# You select Door A, but then Monty makes things a little more interesting. He opens Door B to reveal that there is no sports car behind it and asks you if you would like to stick with your choice of Door A or switch your choice to Door C. Given this new information, what are the probabilities of you winning the car if you stick with Door A versus if you switch to Door C?

# %%


# %% [markdown]
# ## 4. Bayesian Analysis 
# 
# Suppose you work for a landscaping company, and they want to advertise their service online. They create an ad and sit back waiting for the money to roll in. On the first day, the ad sends 100 visitors to the site and 14 of them sign up for landscaping services. Create a generative model to come up with the posterior distribution and produce a visualization of what the posterior distribution would look like given the observed data.

# %%


# %% [markdown]
# Produce a set of descriptive statistics for the posterior distribution.

# %%


# %% [markdown]
# What is the 90% credible interval range?

# %%


# %% [markdown]
# What is the Maximum Likelihood Estimate?

# %%



