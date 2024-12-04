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

# Display the missing values
missing_values

from sklearn.preprocessing import MinMaxScaler

# Separate features and target variable
X = df.drop(columns=['status'])
y = df['status']

# Initialize the MinMaxScaler
scaler = MinMaxScaler()

# Normalize the features
X_normalized = scaler.fit_transform(X)

# Convert the normalized features back to a DataFrame
X_normalized = pd.DataFrame(X_normalized, columns=X.columns)

# Display the first few rows of the normalized features
X_normalized.head()



from sklearn.preprocessing import MinMaxScaler

# Separate features and target variable
X = df.drop(columns=['status'])
y = df['status']

# Initialize the MinMaxScaler
scaler = MinMaxScaler()

# Normalize the features
X_normalized = scaler.fit_transform(X)

# Convert the normalized features back to a DataFrame
X_normalized = pd.DataFrame(X_normalized, columns=X.columns)

# Display the first few rows of the normalized features
X_normalized.head()

from sklearn.preprocessing import StandardScaler

# Initialize the StandardScaler
scaler = StandardScaler()

# Standardize the features
X_standardized = scaler.fit_transform(X_normalized)

# Convert the standardized features back to a DataFrame
X_standardized = pd.DataFrame(X_standardized, columns=X.columns)

# Display the first few rows of the standardized features
X_standardized.head()

from sklearn.model_selection import train_test_split

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_standardized, y, test_size=0.2, random_state=42)

# Display the shapes of the training and testing sets
(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import f1_score

# Initialize the logistic regression model with L2 regularization
log_reg = LogisticRegression(penalty='l2', solver='liblinear')

# Define the parameter grid for cross-validation
param_grid = {'C': [0.01, 0.1, 1, 10, 100]}

# Initialize the GridSearchCV object
grid_search = GridSearchCV(log_reg, param_grid, cv=5, scoring='f1')

# Fit the model to the training data
grid_search.fit(X_train, y_train)

# Get the best model and its parameters
best_log_reg = grid_search.best_estimator_
best_params = grid_search.best_params_

# Predict on the test set
y_pred = best_log_reg.predict(X_test)

# Calculate the F1 score
f1 = f1_score(y_test, y_pred)

(best_params, f1)

from sklearn.neighbors import KNeighborsClassifier

# Initialize the KNN classifier
knn = KNeighborsClassifier()

# Define the parameter grid for cross-validation
param_grid = {'n_neighbors': [1, 3, 5, 7, 9, 11, 13, 15]}

# Initialize the GridSearchCV object
grid_search_knn = GridSearchCV(knn, param_grid, cv=5, scoring='f1')

# Fit the model to the training data
grid_search_knn.fit(X_train, y_train)

# Get the best model and its parameters
best_knn = grid_search_knn.best_estimator_
best_params_knn = grid_search_knn.best_params_

# Predict on the test set
y_pred_knn = best_knn.predict(X_test)

# Calculate the F1 score
f1_knn = f1_score(y_test, y_pred_knn)

(best_params_knn, f1_knn)

from sklearn.neural_network import MLPClassifier

# Initialize the neural network classifier
mlp = MLPClassifier(max_iter=1000, random_state=42)

# Define the parameter grid for cross-validation
param_grid = {'hidden_layer_sizes': [(5,), (10,), (15,), (20,), (25,), (30,)]}

# Initialize the GridSearchCV object
grid_search_mlp = GridSearchCV(mlp, param_grid, cv=5, scoring='f1')

# Fit the model to the training data
grid_search_mlp.fit(X_train, y_train)

# Get the best model and its parameters
best_mlp = grid_search_mlp.best_estimator_
best_params_mlp = grid_search_mlp.best_params_

# Predict on the test set
y_pred_mlp = best_mlp.predict(X_test)

# Calculate the F1 score
f1_mlp = f1_score(y_test, y_pred_mlp)

(best_params_mlp, f1_mlp)

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

{
    "Logistic Regression": {
        "Best Params": best_params,
        "Precision": precision_log_reg,
        "Recall": recall_log_reg,
        "F1 Score": f1_log_reg,
        "Accuracy": accuracy_log_reg
    },
    "K-Nearest Neighbors": {
        "Best Params": best_params_knn,
        "Precision": precision_knn,
        "Recall": recall_knn,
        "F1 Score": f1_knn,
        "Accuracy": accuracy_knn
    },
    "Neural Network": {
        "Best Params": best_params_mlp,
        "Precision": precision_mlp,
        "Recall": recall_mlp,
        "F1 Score": f1_mlp,
        "Accuracy": accuracy_mlp
    }
}

# Determine the majority class
majority_class = y_train.mode()[0]

# Predict the majority class for all test samples
y_pred_majority = [majority_class] * len(y_test)

# Calculate the precision, recall, F1 score, and accuracy for the majority class assignment
precision_majority = precision_score(y_test, y_pred_majority)
recall_majority = recall_score(y_test, y_pred_majority)
accuracy_majority = accuracy_score(y_test, y_pred_majority)
f1_majority = f1_score(y_test, y_pred_majority)

{
    "Majority Class Assignment": {
        "Precision": precision_majority,
        "Recall": recall_majority,
        "F1 Score": f1_majority,
        "Accuracy": accuracy_majority
    }
}

