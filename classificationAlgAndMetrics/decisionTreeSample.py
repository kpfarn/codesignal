# Select the best split point for a dataset
def get_split(dataset):
    class_values = list(set(row[-1] for row in dataset))
    b_index, b_value, b_score, b_groups = float('inf'), float('inf'), float('inf'), None
    for index in range(len(dataset[0])-1):
        for row in dataset:
            groups = test_split(index, row[index], dataset)
            gini = gini_index(groups, class_values)
            if gini < b_score:
                b_index, b_value, b_score, b_groups = index, row[index], gini, groups
    return {'index':b_index, 'value':b_value, 'groups':b_groups}

# Split a dataset based on an attribute and attribute value
def test_split(index, value, dataset):
    left, right = list(), list()
    for row in dataset:
        if row[index] < value:
            left.append(row)
        else:
            right.append(row)
    return left, right

# Calculate the Gini index for a split dataset
def gini_index(groups, classes):
    n_instances = float(sum([len(group) for group in groups]))
    gini = 0.0
    for group in groups:
        size = float(len(group))
        if size == 0:
            continue
        score = 0.0
        for class_val in classes:
            p = [row[-1] for row in group].count(class_val) / size
            score += p * p
        gini += (1.0 - score) * (size / n_instances)
    return gini


def create_terminal(group):
    #TODO : Fill in this function to find the most common
    outcomes = [row[-1] for row in group]
    return max(set(outcomes), key=outcomes.count)

def build_tree(train, max_depth, min_size):
    root = get_split(train)
    recurse_split(root, max_depth, min_size, 1)
    return root

def recurse_split(node, max_depth, min_size, depth):
    left, right = node['groups']
    del(node['groups'])
    
    # TODO: Handle the case if either left or right group is empty.
    if not left or not right:
        node['left'] = node['right'] = create_terminal(left + right)
        return
    # TODO: Handle the case if the current depth has reached or exceeded the maximum depth.
    if depth >= max_depth:
        node['left'], node['right'] = create_terminal(left), create_terminal(right)
    # TODO: Process the left group, call `create_terminal` or `get_split` method based on group size. Implement recursion if necessary.
    if len(left) <= min_size:
        node['left'] = create_terminal(left)
    else:
        node['left'] = get_split(left)
        recurse_split(node['left'], max_depth, min_size, depth+1)
    # TODO: Process the right group, call `create_terminal` or `get_split` method based on group size. Implement recursion if necessary.
    if len(right) <= min_size:
        node['right'] = create_terminal(right)
    else:
        node['right'] = get_split(right)
        recurse_split(node['right'], max_depth, min_size, depth+1)
        
def print_tree(node, depth=0):
    if isinstance(node, dict):
        print('%s[X%d < %.3f]' % ((depth*' ', (node['index']+1), node['value'])))
        print_tree(node['left'], depth+1)
        print_tree(node['right'], depth+1)
    else:
        print('%s[%s]' % ((depth*' ', node)))

# Sample dataset
dataset = [
    [5, 3, 0], [6, 3, 0], [6, 4, 0], [10, 3, 1],
    [11, 4, 1], [12, 8, 0], [5, 5, 0], [12, 4, 1]
]
max_depth = 2
min_size = 1
tree = build_tree(dataset, max_depth, min_size)
print_tree(tree)
