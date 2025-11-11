#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report

iris = load_iris()
X = iris.data        
y = iris.target      # target classes (0, 1, 2)

# 3️⃣ Split dataset into training (70%) and testing (30%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 4️⃣ Create a Gaussian Naive Bayes model
model = GaussianNB()

# 5️⃣ Train the model
model.fit(X_train, y_train)

# 6️⃣ Predict on test data
y_pred = model.predict(X_test)

# 7️⃣ Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"✅ Accuracy of Naive Bayes model: {accuracy * 100:.2f}%\n")

# (Optional) Detailed performance report
print("Classification Report:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))

