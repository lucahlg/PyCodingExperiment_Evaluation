import pandas as pd

# Load the dataset
data_path = 'parkinsons_data/parkinsons.data'
df = pd.read_csv(data_path)

# Display the first few rows of the dataset
df.head()

# Drop the 'name' column
df = df.drop(columns=['name'])

# Check for missing values
missing_values = df.isnull().sum()

# Normalize the feature columns (excluding the target column 'status')
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
features = df.drop(columns=['status'])
normalized_features = scaler.fit_transform(features)

# Create a new DataFrame with normalized features
normalized_df = pd.DataFrame(normalized_features, columns=features.columns)
normalized_df['status'] = df['status'].values

# Display the first few rows of the normalized DataFrame
normalized_df.head(), missing_values



import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Load the dataset
data_path = 'parkinsons_data/parkinsons.data'
df = pd.read_csv(data_path)

# Drop the 'name' column
df = df.drop(columns=['name'])

# Check for missing values
missing_values = df.isnull().sum()

# Normalize the feature columns (excluding the target column 'status')
scaler = MinMaxScaler()
features = df.drop(columns=['status'])
normalized_features = scaler.fit_transform(features)

# Create a new DataFrame with normalized features
normalized_df = pd.DataFrame(normalized_features, columns=features.columns)
normalized_df['status'] = df['status'].values

# Display the first few rows of the normalized DataFrame
normalized_df.head(), missing_values

from sklearn.preprocessing import StandardScaler

# Standardize the feature columns (excluding the target column 'status')
scaler = StandardScaler()
features = normalized_df.drop(columns=['status'])
standardized_features = scaler.fit_transform(features)

# Create a new DataFrame with standardized features
standardized_df = pd.DataFrame(standardized_features, columns=features.columns)
standardized_df['status'] = normalized_df['status'].values

# Display the first few rows of the standardized DataFrame
standardized_df.head()

from sklearn.model_selection import train_test_split

# Split the data into training and testing sets
X = standardized_df.drop(columns=['status'])
y = standardized_df['status']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Display the shapes of the training and testing sets
X_train.shape, X_test.shape, y_train.shape, y_test.shape

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import f1_score

# Define the logistic regression model with L2 regularization
log_reg = LogisticRegression(penalty='l2', solver='liblinear')

# Define the parameter grid for cross-validation
param_grid = {'C': [0.01, 0.1, 1, 10, 100]}

# Perform grid search with cross-validation to find the best regularization parameter
grid_search = GridSearchCV(log_reg, param_grid, cv=5, scoring='f1')
grid_search.fit(X_train, y_train)

# Get the best model and its parameters
best_log_reg = grid_search.best_estimator_
best_params = grid_search.best_params_

# Train the best model on the entire training set
best_log_reg.fit(X_train, y_train)

# Predict on the test set
y_pred = best_log_reg.predict(X_test)

# Calculate the F1 score
f1 = f1_score(y_test, y_pred)

best_params, f1

from sklearn.neighbors import KNeighborsClassifier

# Define the KNN model
knn = KNeighborsClassifier()

# Define the parameter grid for cross-validation
param_grid = {'n_neighbors': [1, 3, 5, 7, 9, 11, 13, 15]}

# Perform grid search with cross-validation to find the best number of neighbors
grid_search_knn = GridSearchCV(knn, param_grid, cv=5, scoring='f1')
grid_search_knn.fit(X_train, y_train)

# Get the best model and its parameters
best_knn = grid_search_knn.best_estimator_
best_params_knn = grid_search_knn.best_params_

# Train the best model on the entire training set
best_knn.fit(X_train, y_train)

# Predict on the test set
y_pred_knn = best_knn.predict(X_test)

# Calculate the F1 score
f1_knn = f1_score(y_test, y_pred_knn)

best_params_knn, f1_knn

from sklearn.neural_network import MLPClassifier

# Define the neural network model
mlp = MLPClassifier(max_iter=1000, random_state=42)

# Define the parameter grid for cross-validation
param_grid = {'hidden_layer_sizes': [(5,), (10,), (15,), (20,), (25,), (30,)]}

# Perform grid search with cross-validation to find the best hidden layer size
grid_search_mlp = GridSearchCV(mlp, param_grid, cv=5, scoring='f1')
grid_search_mlp.fit(X_train, y_train)

# Get the best model and its parameters
best_mlp = grid_search_mlp.best_estimator_
best_params_mlp = grid_search_mlp.best_params_

# Train the best model on the entire training set
best_mlp.fit(X_train, y_train)

# Predict on the test set
y_pred_mlp = best_mlp.predict(X_test)

# Calculate the F1 score
f1_mlp = f1_score(y_test, y_pred_mlp)

best_params_mlp, f1_mlp

from sklearn.metrics import precision_score, recall_score, accuracy_score

# Logistic Regression
y_pred_log_reg = best_log_reg.predict(X_test)
precision_log_reg = precision_score(y_test, y_pred_log_reg)
recall_log_reg = recall_score(y_test, y_pred_log_reg)
accuracy_log_reg = accuracy_score(y_test, y_pred_log_reg)
f1_log_reg = f1_score(y_test, y_pred_log_reg)

# K-Nearest Neighbors
y_pred_knn = best_knn.predict(X_test)
precision_knn = precision_score(y_test, y_pred_knn)
recall_knn = recall_score(y_test, y_pred_knn)
accuracy_knn = accuracy_score(y_test, y_pred_knn)
f1_knn = f1_score(y_test, y_pred_knn)

# Neural Network
y_pred_mlp = best_mlp.predict(X_test)
precision_mlp = precision_score(y_test, y_pred_mlp)
recall_mlp = recall_score(y_test, y_pred_mlp)
accuracy_mlp = accuracy_score(y_test, y_pred_mlp)
f1_mlp = f1_score(y_test, y_pred_mlp)

results = {
    'Logistic Regression': {
        'Best Params': best_params,
        'Precision': precision_log_reg,
        'Recall': recall_log_reg,
        'F1 Score': f1_log_reg,
        'Accuracy': accuracy_log_reg
    },
    'K-Nearest Neighbors': {
        'Best Params': best_params_knn,
        'Precision': precision_knn,
        'Recall': recall_knn,
        'F1 Score': f1_knn,
        'Accuracy': accuracy_knn
    },
    'Neural Network': {
        'Best Params': best_params_mlp,
        'Precision': precision_mlp,
        'Recall': recall_mlp,
        'F1 Score': f1_mlp,
        'Accuracy': accuracy_mlp
    }
}

results

from sklearn.dummy import DummyClassifier

# Define the dummy classifier with the strategy of assigning the most frequent class
dummy_clf = DummyClassifier(strategy='most_frequent')

# Train the dummy classifier on the training set
dummy_clf.fit(X_train, y_train)

# Predict on the test set
y_pred_dummy = dummy_clf.predict(X_test)

# Calculate the performance metrics
precision_dummy = precision_score(y_test, y_pred_dummy)
recall_dummy = recall_score(y_test, y_pred_dummy)
accuracy_dummy = accuracy_score(y_test, y_pred_dummy)
f1_dummy = f1_score(y_test, y_pred_dummy)

baseline_results = {
    'Baseline (Class Majority Assignment)': {
        'Precision': precision_dummy,
        'Recall': recall_dummy,
        'F1 Score': f1_dummy,
        'Accuracy': accuracy_dummy
    }
}

baseline_results

