import pandas as pd

# Load the dataset
data_path = 'parkinsons_data/parkinsons.data'
df = pd.read_csv(data_path)

# Display the first few rows and summary information
df_info = df.info()
df_head = df.head()

df_info, df_head

from sklearn.preprocessing import MinMaxScaler

# Separate features and target variable
X = df.drop(columns=['name', 'status'])
y = df['status']

# Normalize the features
scaler = MinMaxScaler()
X_normalized = scaler.fit_transform(X)

# Create a new DataFrame with normalized features
df_normalized = pd.DataFrame(X_normalized, columns=X.columns)

df_normalized.head()  # Display the first few rows of the normalized data



from sklearn.preprocessing import MinMaxScaler

# Separate features and target variable
X = df.drop(columns=['name', 'status'])
y = df['status']

# Normalize the features
scaler = MinMaxScaler()
X_normalized = scaler.fit_transform(X)

# Create a new DataFrame with normalized features
df_normalized = pd.DataFrame(X_normalized, columns=X.columns)

df_normalized.head()  # Display the first few rows of the normalized data

from sklearn.preprocessing import StandardScaler

# Standardize the features
scaler = StandardScaler()
X_standardized = scaler.fit_transform(X_normalized)

# Create a new DataFrame with standardized features
df_standardized = pd.DataFrame(X_standardized, columns=X.columns)

df_standardized.head()  # Display the first few rows of the standardized data

from sklearn.model_selection import train_test_split

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_standardized, y, test_size=0.2, random_state=42)

# Display the shapes of the resulting datasets
(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import f1_score

# Set up the logistic regression model with L2 regularization
log_reg = LogisticRegression(solver='liblinear')

# Define the parameter grid for cross-validation
param_grid = {'C': [0.001, 0.01, 0.1, 1, 10, 100]}

# Set up GridSearchCV to find the best regularization parameter
grid_search = GridSearchCV(log_reg, param_grid, scoring='f1', cv=5)
grid_search.fit(X_train, y_train)

# Get the best parameters and the best score
best_params = grid_search.best_params_
best_f1_score = grid_search.best_score_

best_params, best_f1_score

from sklearn.neighbors import KNeighborsClassifier

# Set up the KNN model
knn = KNeighborsClassifier()

# Define the parameter grid for K
param_grid_knn = {'n_neighbors': range(1, 21)}  # Testing K values from 1 to 20

# Set up GridSearchCV to find the best K
grid_search_knn = GridSearchCV(knn, param_grid_knn, scoring='f1', cv=5)
grid_search_knn.fit(X_train, y_train)

# Get the best parameters and the best score
best_k = grid_search_knn.best_params_
best_knn_f1_score = grid_search_knn.best_score_

best_k, best_knn_f1_score

from sklearn.neural_network import MLPClassifier

# Set up the neural network model
mlp = MLPClassifier(max_iter=1000)

# Define the parameter grid for the width of the hidden layer
param_grid_mlp = {'hidden_layer_sizes': [(i,) for i in range(1, 21)]}  # Testing widths from 1 to 20

# Set up GridSearchCV to find the best hidden layer size
grid_search_mlp = GridSearchCV(mlp, param_grid_mlp, scoring='f1', cv=5)
grid_search_mlp.fit(X_train, y_train)

# Get the best parameters and the best score
best_hidden_layer_size = grid_search_mlp.best_params_
best_mlp_f1_score = grid_search_mlp.best_score_

best_hidden_layer_size, best_mlp_f1_score

from sklearn.metrics import precision_score, recall_score, accuracy_score

# Evaluate Logistic Regression
log_reg_best = LogisticRegression(C=best_params['C'], solver='liblinear')
log_reg_best.fit(X_train, y_train)
y_pred_log_reg = log_reg_best.predict(X_test)

# Calculate metrics for Logistic Regression
log_reg_precision = precision_score(y_test, y_pred_log_reg)
log_reg_recall = recall_score(y_test, y_pred_log_reg)
log_reg_f1 = f1_score(y_test, y_pred_log_reg)
log_reg_accuracy = accuracy_score(y_test, y_pred_log_reg)

# Store results
log_reg_results = {
    'Model': 'Logistic Regression',
    'Best Parameters': best_params,
    'Precision': log_reg_precision,
    'Recall': log_reg_recall,
    'F1 Score': log_reg_f1,
    'Accuracy': log_reg_accuracy
}

log_reg_results

# Evaluate KNN
knn_best = KNeighborsClassifier(n_neighbors=best_k['n_neighbors'])
knn_best.fit(X_train, y_train)
y_pred_knn = knn_best.predict(X_test)

# Calculate metrics for KNN
knn_precision = precision_score(y_test, y_pred_knn)
knn_recall = recall_score(y_test, y_pred_knn)
knn_f1 = f1_score(y_test, y_pred_knn)
knn_accuracy = accuracy_score(y_test, y_pred_knn)

# Store results
knn_results = {
    'Model': 'K-Nearest Neighbors',
    'Best Parameters': best_k,
    'Precision': knn_precision,
    'Recall': knn_recall,
    'F1 Score': knn_f1,
    'Accuracy': knn_accuracy
}

knn_results

# Evaluate Neural Network
mlp_best = MLPClassifier(hidden_layer_sizes=best_hidden_layer_size['hidden_layer_sizes'], max_iter=1000)
mlp_best.fit(X_train, y_train)
y_pred_mlp = mlp_best.predict(X_test)

# Calculate metrics for Neural Network
mlp_precision = precision_score(y_test, y_pred_mlp)
mlp_recall = recall_score(y_test, y_pred_mlp)
mlp_f1 = f1_score(y_test, y_pred_mlp)
mlp_accuracy = accuracy_score(y_test, y_pred_mlp)

# Store results
mlp_results = {
    'Model': 'Neural Network',
    'Best Parameters': best_hidden_layer_size,
    'Precision': mlp_precision,
    'Recall': mlp_recall,
    'F1 Score': mlp_f1,
    'Accuracy': mlp_accuracy
}

mlp_results

# Calculate the baseline accuracy (majority class)
majority_class = y.value_counts().idxmax()
baseline_accuracy = (y == majority_class).mean()

baseline_accuracy

