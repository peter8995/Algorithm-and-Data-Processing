import math
import matplotlib.pyplot as plt

def revenue_derivative(tax):
    return(100 * (1 / (tax + 1) - 2 * (tax - 0.2)))

current_rate = 0.7

print(revenue_derivative(current_rate))