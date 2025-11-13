#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd

# Function to calculate Gini Index
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

# Split a dataset based on an attribute and an attribute value
def test_split(index, value, dataset):
    left, right = list(), list()
    for row in dataset:
        if row[index] < value:
            left.append(row)
        else:
            right.append(row)
    return left, right

# Select the best split point for a dataset
def get_split(dataset):
    class_values = list(set(row[-1] for row in dataset))
    best_index, best_value, best_score, best_groups = 999, 999, 999, None
    for index in range(len(dataset[0]) - 1):
        for row in dataset:
            groups = test_split(index, row[index], dataset)
            gini = gini_index(groups, class_values)
            if gini < best_score:
                best_index, best_value, best_score, best_groups = index, row[index], gini, groups
    return {'index': best_index, 'value': best_value, 'groups': best_groups}

# Create a terminal node value
def to_terminal(group):
    outcomes = [row[-1] for row in group]
    return max(set(outcomes), key=outcomes.count)

# Create child splits for a node or make terminal
def split(node, max_depth, min_size, depth):
    left, right = node['groups']
    del(node['groups'])
    if not left or not right:
        node['left'] = node['right'] = to_terminal(left + right)
        return
    if depth >= max_depth:
        node['left'], node['right'] = to_terminal(left), to_terminal(right)
        return
    if len(left) <= min_size:
        node['left'] = to_terminal(left)
    else:
        node['left'] = get_split(left)
        split(node['left'], max_depth, min_size, depth + 1)
    if len(right) <= min_size:
        node['right'] = to_terminal(right)
    else:
        node['right'] = get_split(right)
        split(node['right'], max_depth, min_size, depth + 1)

# Build a decision tree
def build_tree(train, max_depth, min_size):
    root = get_split(train)
    split(root, max_depth, min_size, 1)
    return root

# Make a prediction with a decision tree
def predict(node, row):
    if row[node['index']] < node['value']:
        if isinstance(node['left'], dict):
            return predict(node['left'], row)
        else:
            return node['left']
    else:
        if isinstance(node['right'], dict):
            return predict(node['right'], row)
        else:
            return node['right']

# Function to print the tree
def print_tree(node, depth=0):
    if isinstance(node, dict):
        print('%s[X%d < %.3f]' % ((depth*'  ', node['index'], node['value'])))
        print_tree(node['left'], depth+1)
        print_tree(node['right'], depth+1)
    else:
        print('%s[%s]' % ((depth*'  ', node)))

# CART Algorithm
def decision_tree(train, test, max_depth, min_size):
    tree = build_tree(train, max_depth, min_size)
    print("Decision Tree:")
    print_tree(tree)
    predictions = []
    for row in test:
        prediction = predict(tree, row)
        predictions.append(prediction)
    return predictions

# --- Example dataset ---
dataset = [
    [2.771, 1.784, 0],
    [1.728, 1.169, 0],
    [3.678, 2.812, 0],
    [3.961, 2.619, 0],
    [2.999, 2.209, 0],
    [7.497, 3.162, 1],
    [9.002, 3.339, 1],
    [7.444, 0.476, 1],
    [10.124, 3.234, 1],
    [6.642, 3.319, 1]
]

# Split dataset into training and testing
train = dataset[:8]
test = dataset[8:]

# Run CART decision tree
predictions = decision_tree(train, test, max_depth=3, min_size=1)
print("\nPredictions:", predictions)
print("Actual:", [row[-1] for row in test])


# In[1]:


# 2. Implement rule-based classification using OneR algorithm. 
import pandas as pd

# Sample dataset
data = {
    'Outlook': ['Sunny', 'Sunny', 'Overcast', 'Rainy', 'Rainy', 'Rainy', 'Overcast', 'Sunny'],
    'Temperature': ['Hot', 'Hot', 'Hot', 'Mild', 'Cool', 'Cool', 'Cool', 'Mild'],
    'Humidity': ['High', 'High', 'High', 'High', 'Normal', 'Normal', 'Normal', 'High'],
    'Windy': [False, True, False, False, False, True, True, False],
    'Play': ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No']
}

df = pd.DataFrame(data)

# Function to implement OneR
def oneR(df, target):
    features = df.columns.drop(target)
    best_feature = None
    min_error = float('inf')
    best_rule = {}

    for feature in features:
        # Create rule for this feature
        rule = {}
        for value, subset in df.groupby(feature):
            # Most common class for this feature value
            most_common = subset[target].mode()[0]
            rule[value] = most_common
        
        # Calculate error for this feature
        predictions = df[feature].map(rule)
        error = sum(predictions != df[target])
        
        print(f"\nFeature: {feature}")
        print("Rule:", rule)
        print("Errors:", error)
        
        # Check if this feature is better
        if error < min_error:
            min_error = error
            best_feature = feature
            best_rule = rule

    print("\n Best Feature:", best_feature)
    print(" Final Rule:", best_rule)
    print("Total Errors:", min_error)
    return best_feature, best_rule

# Run OneR Algorithm
best_feature, best_rule = oneR(df, 'Play')

# Predicting using the rule
def predict(row):
    value = row[best_feature]
    return best_rule.get(value, 'Unknown')

df['Predicted'] = df.apply(predict, axis=1)
print("\nFinal Predictions:")
print(df[['Outlook', 'Temperature', 'Humidity', 'Windy', 'Play', 'Predicted']])

