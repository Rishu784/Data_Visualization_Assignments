#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris


iris = load_iris()
X = iris.data   
y = iris.target 


X_meaned = X - np.mean(X, axis=0)

cov_matrix = np.cov(X_meaned, rowvar=False)

print("Covariance Matrix:\n", cov_matrix)



# In[4]:


eigen_values, eigen_vectors = np.linalg.eigh(cov_matrix)

print("\nEigenvalues:\n", eigen_values)
print("\nEigenvectors:\n", eigen_vectors)


# In[7]:


sorted_index = np.argsort(eigen_values)[::-1]
eigen_values = eigen_values[sorted_index]
eigen_vectors = eigen_vectors[:, sorted_index]

eigenvector_subset = eigen_vectors[:, 0:2]

X_reduced = np.dot(X_meaned, eigenvector_subset)

df_pca = pd.DataFrame(data=X_reduced, columns=['PC1', 'PC2'])
df_pca['Target'] = y

plt.figure(figsize=(8,6))
colors = ['red', 'green', 'blue']
labels = iris.target_names

for i, color, label in zip([0,1,2], colors, labels):
    plt.scatter(
        df_pca[df_pca['Target'] == i]['PC1'],
        df_pca[df_pca['Target'] == i]['PC2'],
        color=color,
        label=label,
        alpha=0.7
    )

plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("PCA of Iris Dataset (Manual Implementation)")
plt.legend()
plt.grid(True)
plt.show()

