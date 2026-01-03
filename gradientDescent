import numpy as np

# Sample house sizes in square feet, standardized
house_sizes = np.array([[1000], [1500], [2000]])
house_sizes = (house_sizes - np.mean(house_sizes)) / np.std(house_sizes)
# Sample house prices in 1000s of dollars
house_prices = np.array([[300], [450], [600]])
# We initialize our parameters: slope (a) and intercept (b)
theta_real_estate = np.random.rand(2, 1)
# Learning rate and iterations for gradient descent, adjusted learning rate
alpha_real_estate = 0.01
iterations = 500
# Add a column of ones to the house sizes to accommodate the intercept (b)
X_b_real_estate = np.c_[np.ones((len(house_sizes), 1)), house_sizes]

def gradient_descent(X, y, theta, alpha, iterations):
    m = len(y)
    i = 0
    cost_history = []
    while(True):
        prediction = np.dot(X, theta)  # Matrix multiplication between X and theta
        # Gradient update rule with correct cost function calculation
        theta = theta - (1/m) * alpha * (X.T.dot(prediction - y))
        cost_history.append((1/(2*m)) * np.sum(np.square(prediction - y)))
        if(i>0):
            if(abs(cost_history[i] - cost_history[i-1]) < .01):
                break
        i += 1
    return theta, cost_history

# Run gradient descent
theta_real_estate, cost_history = gradient_descent(X_b_real_estate, house_prices, theta_real_estate, alpha_real_estate, iterations)
for i, cost in enumerate(cost_history[::10]):
    print(f'Iteration {i * 10}: Cost = {cost}')
