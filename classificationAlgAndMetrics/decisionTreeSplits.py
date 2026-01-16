def test_split(index, value, dataset):
    left, right = list(), list()
    for row in dataset:
        if row[index] < value:
            left.append(row)
        else:
            right.append(row)
    return left, right

def gini_index(groups, classes):
    total_instances = sum([len(group) for group in groups])
    gini = 0.0
    for group in groups:
        size = float(len(group))
        if size == 0:
            continue
        score = sum([(group.count(class_val) / size) ** 2 for class_val in classes])
        gini += (1 - score) * (size / total_instances)
    return gini

def get_split(dataset):
    class_values = list(set(row[-1] for row in dataset))
    b_index, b_value, b_score, b_groups = 999, 999, 999, None
    for index in range(len(dataset[0])-1):
        for row in dataset:
            # TODO: call the test_split function to get groups
            # TODO: calculate the gini index using the gini_index function
            if gini < b_score:
                # TODO: update best index, best value, best score and best groups
    return {'index': b_index, 'value': b_value, 'groups': b_groups}

# Dataset: Age, Preferred Genre, Likelihood to Watch
dataset = [[16, 'Comedy', 'Yes'], [21, 'Action', 'No'], [25, 'Comedy', 'Yes']]
split = get_split(dataset)
print('Best Split: Column Index:', split['index'], 'Value:', split['value'])
