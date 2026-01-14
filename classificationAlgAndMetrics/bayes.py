import pandas as pd

def calculate_likelihoods_with_smoothing(X, y):
    likelihoods = {}
    for column in X.columns:
        likelihoods[column] = {}
        for class_ in y.unique():
            # TODO: Write a line of code to select class_data from X where corresponding y values are equal to class_
            class_data = X[y == class_][column]
            counts = class_data.value_counts()
            total_count = len(class_data) + len(X[column].unique())  # total count with smoothing
            likelihoods[column][class_] = (counts + 1) / total_count  # add-1 smoothing
    return likelihoods

# Create the features (X) and target (y) DataFrames
weather_data = pd.DataFrame({
    'Temperature': ['Hot', 'Mild', 'Cold', 'Hot', 'Mild', 'Cold', 'Hot'],
    'Humidity': ['High', 'High', 'High', 'Normal', 'Normal', 'Normal', 'Low'],
    'Weather': ['Sunny', 'Cloudy', 'Rainy', 'Sunny', 'Cloudy', 'Rainy', 'Sunny']
})

X = weather_data[['Temperature', 'Humidity']]
y = weather_data['Weather']

# TODO: Call the calculate_likelihoods_with_smoothing function with X and y and print its return value.
print(calculate_likelihoods_with_smoothing(X,y))
