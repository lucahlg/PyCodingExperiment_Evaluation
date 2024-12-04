import pandas as pd

# Load the dataset
data_path = 'parkinsons_data/parkinsons.data'
df = pd.read_csv(data_path)

# Display the first few rows of the dataset
df.head()

# Check for missing values and get a summary of the dataset
missing_values = df.isnull().sum()
summary = df.describe()

missing_values, summary

from sklearn.preprocessing import MinMaxScaler

# Drop the 'name' column and separate features and target variable
X = df.drop(columns=['name', 'status'])
y = df['status']

# Normalize the feature columns
scaler = MinMaxScaler()
X_normalized = scaler.fit_transform(X)

# Create a new DataFrame for the normalized features
df_normalized = pd.DataFrame(X_normalized, columns=X.columns)

# Display the first few rows of the normalized dataset
df_normalized.head(), y.head()



# Drop the 'name' column and separate features and target variable
X = df.drop(columns=['name', 'status'])
y = df['status']

# Normalize the feature columns
scaler = MinMaxScaler()
X_normalized = scaler.fit_transform(X)

# Create a new DataFrame for the normalized features
df_normalized = pd.DataFrame(X_normalized, columns=X.columns)

# Display the first few rows of the normalized dataset
df_normalized.head(), y.head()

import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Load the dataset again
data_path = 'parkinsons_data/parkinsons.data'
df = pd.read_csv(data_path)

# Drop the 'name' column and separate features and target variable
X = df.drop(columns=['name', 'status'])
y = df['status']

# Normalize the feature columns
scaler = MinMaxScaler()
X_normalized = scaler.fit_transform(X)

# Create a new DataFrame for the normalized features
df_normalized = pd.DataFrame(X_normalized, columns=X.columns)

# Display the first few rows of the normalized dataset
df_normalized.head(), y.head()

from sklearn.preprocessing import StandardScaler

# Standardize the features (compute z-scores)
scaler_z = StandardScaler()
X_standardized = scaler_z.fit_transform(X_normalized)

# Create a new DataFrame for the standardized features
df_standardized = pd.DataFrame(X_standardized, columns=X.columns)

# Display the first few rows of the standardized dataset
df_standardized.head()

from sklearn.model_selection import train_test_split

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_standardized, y, test_size=0.2, random_state=42, stratify=y)

# Display the shapes of the resulting datasets
X_train.shape, X_test.shape, y_train.shape, y_test.shape

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV

# Set up the logistic regression model with L2 regularization
log_reg = LogisticRegression(penalty='l2', solver='liblinear')

# Define the parameter grid for cross-validation
param_grid = {'C': [0.001, 0.01, 0.1, 1, 10, 100]}

# Set up GridSearchCV to optimize for F1 score
grid_search = GridSearchCV(log_reg, param_grid, scoring='f1', cv=5)
grid_search.fit(X_train, y_train)

# Get the best parameters and the best score
best_params = grid_search.best_params_
best_score = grid_search.best_score_

best_params, best_score

from sklearn.neighbors import KNeighborsClassifier

# Set up the KNN model
knn = KNeighborsClassifier()

# Define the parameter grid for cross-validation
param_grid_knn = {'n_neighbors': range(1, 21)}  # Testing K from 1 to 20

# Set up GridSearchCV to optimize for F1 score
grid_search_knn = GridSearchCV(knn, param_grid_knn, scoring='f1', cv=5)
grid_search_knn.fit(X_train, y_train)

# Get the best parameters and the best score
best_params_knn = grid_search_knn.best_params_
best_score_knn = grid_search_knn.best_score_

best_params_knn, best_score_knn

from sklearn.neural_network import MLPClassifier

# Set up the neural network model
mlp = MLPClassifier(max_iter=1000, random_state=42)

# Define the parameter grid for cross-validation (testing hidden layer sizes from 1 to 20)
param_grid_mlp = {'hidden_layer_sizes': [(i,) for i in range(1, 21)]}

# Set up GridSearchCV to optimize for F1 score
grid_search_mlp = GridSearchCV(mlp, param_grid_mlp, scoring='f1', cv=5)
grid_search_mlp.fit(X_train, y_train)

# Get the best parameters and the best score
best_params_mlp = grid_search_mlp.best_params_
best_score_mlp = grid_search_mlp.best_score_

best_params_mlp, best_score_mlp

from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score

# Logistic Regression
log_reg_best = LogisticRegression(penalty='l2', C=best_params['C'], solver='liblinear')
log_reg_best.fit(X_train, y_train)
y_pred_log_reg = log_reg_best.predict(X_test)

# KNN
knn_best = KNeighborsClassifier(n_neighbors=best_params_knn['n_neighbors'])
knn_best.fit(X_train, y_train)
y_pred_knn = knn_best.predict(X_test)

# Neural Network
mlp_best = MLPClassifier(hidden_layer_sizes=best_params_mlp['hidden_layer_sizes'], max_iter=1000, random_state=42)
mlp_best.fit(X_train, y_train)
y_pred_mlp = mlp_best.predict(X_test)

# Calculate metrics for each classifier
results = {
    'Logistic Regression': {
        'Precision': precision_score(y_test, y_pred_log_reg),
        'Recall': recall_score(y_test, y_pred_log_reg),
        'F1 Score': f1_score(y_test, y_pred_log_reg),
        'Accuracy': accuracy_score(y_test, y_pred_log_reg),
        'Best Hyperparameters': best_params
    },
    'KNN': {
        'Precision': precision_score(y_test, y_pred_knn),
        'Recall': recall_score(y_test, y_pred_knn),
        'F1 Score': f1_score(y_test, y_pred_knn),
        'Accuracy': accuracy_score(y_test, y_pred_knn),
        'Best Hyperparameters': best_params_knn
    },
    'Neural Network': {
        'Precision': precision_score(y_test, y_pred_mlp),
        'Recall': recall_score(y_test, y_pred_mlp),
        'F1 Score': f1_score(y_test, y_pred_mlp),
        'Accuracy': accuracy_score(y_test, y_pred_mlp),
        'Best Hyperparameters': best_params_mlp
    }
}

results

# Calculate the baseline performance (majority class assignment)
majority_class = y.value_counts().idxmax()
y_pred_majority = [majority_class] * len(y_test)

# Calculate metrics for the baseline
baseline_results = {
    'Precision': precision_score(y_test, y_pred_majority),
    'Recall': recall_score(y_test, y_pred_majority),
    'F1 Score': f1_score(y_test, y_pred_majority),
    'Accuracy': accuracy_score(y_test, y_pred_majority),
    'Majority Class': majority_class
}

baseline_results

