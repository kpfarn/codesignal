import pandas as pd

# Function to calculate prior probabilities
def calculate_prior_probabilities(y):
    return y.value_counts(normalize=True)

# Function to calculate likelihoods with Laplace smoothing
def calculate_likelihoods_with_smoothing(X, y):
    likelihoods = {}
    for column in X.columns:
        likelihoods[column] = {}
        for class_ in y.unique():
            # Calculate normalized counts with smoothing
            class_data = X[y == class_][column]
            counts = class_data.value_counts()
            total_count = len(class_data) + len(X[column].unique())  # total count with smoothing
            likelihoods[column][class_] = (counts + 1) / total_count  # add-1 smoothing
    return likelihoods

# Naive Bayes classifier function
def naive_bayes_classifier(X_test, priors, likelihoods):
    predictions = []
    for _, data_point in X_test.iterrows():
        class_probabilities = {}
        for class_ in priors.index:
            class_probabilities[class_] = priors[class_]
            for feature in X_test.columns:
                # Use .get to safely retrieve probability and get a default of 1/total to handle unseen values
                # TODO: Retrieve feature_probs for the current class and feature
                feature_probs = likelihoods[feature][class_]
                # TODO: Safely retrieve the likelihood from feature_probs using .get(data_point[feature], default value)
                # TODO: Update the class_probabilities for the class using the retrieved likelihood
                class_probabilities[class_] *= feature_probs.get(data_point[feature], 1 / (len(feature_probs) + 1))
                
        # TODO: Append to predictions the class with the maximum posterior probability for this data point
        predictions.append(max(class_probabilities))
    return predictions

df = pd.DataFrame({
    'Temperature': ['Hot', 'Cold', 'Cold', 'Hot', 'Cold'],
    'Outlook': ['Sunny', 'Rainy', 'Rainy', 'Sunny', 'Sunny'],
    'Play': ['Yes', 'Yes', 'No', 'Yes', 'No']
})

# Calculate the prior probabilities
priors = calculate_prior_probabilities(df['Play'])

# Calculate the likelihoods with Laplace smoothing
likelihoods = calculate_likelihoods_with_smoothing(df[['Temperature', 'Outlook']], df['Play'])

# Predicting whether we can play or not on a new day
new_day = pd.DataFrame([{'Temperature': 'Hot', 'Outlook': 'Sunny'}])
predictions = naive_bayes_classifier(new_day, priors, likelihoods)
print("Can we play on a new day? ", predictions[0])
