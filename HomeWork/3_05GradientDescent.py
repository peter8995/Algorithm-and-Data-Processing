import math
import matplotlib.pyplot as plt


def revenue_derivative_flipped(tax):
    return (0 - revenue_derivative(tax))

def revenue_derivative(tax):
    return(100 * (1 / (tax + 1) - 2 * (tax - 0.2)))

threshold = 0.0001
maximum_iterations = 10000
current_rate = 0.7
keep_going = True
iterations = 0
step_size = 0.001

while(keep_going):
    rate_change = step_size * revenue_derivative_flipped(current_rate)
    current_rate = current_rate - rate_change
    print(current_rate, rate_change)

    if(abs(rate_change) < threshold):
        keep_going = False
    if(iterations >= maximum_iterations):
        keep_going = False
    iterations = iterations + 1