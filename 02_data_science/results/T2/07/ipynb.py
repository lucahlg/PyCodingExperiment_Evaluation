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

# Convert back to DataFrame for easier handling
X_normalized_df = pd.DataFrame(X_normalized, columns=X.columns)

# Display the first few rows of the normalized data
X_normalized_df.head()



from sklearn.preprocessing import MinMaxScaler

# Separate features and target variable
X = df.drop(columns=['name', 'status'])
y = df['status']

# Normalize the features
scaler = MinMaxScaler()
X_normalized = scaler.fit_transform(X)

# Convert back to DataFrame for easier handling
X_normalized_df = pd.DataFrame(X_normalized, columns=X.columns)

# Display the first few rows of the normalized data
X_normalized_df.head()

from sklearn.preprocessing import StandardScaler

# Standardize the features
scaler_standard = StandardScaler()
X_standardized = scaler_standard.fit_transform(X_normalized_df)

# Convert back to DataFrame for easier handling
X_standardized_df = pd.DataFrame(X_standardized, columns=X_normalized_df.columns)

# Display the first few rows of the standardized data
X_standardized_df.head()

from sklearn.model_selection import train_test_split

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_standardized_df, y, test_size=0.2, random_state=42)

# Display the shapes of the resulting datasets
X_train.shape, X_test.shape, y_train.shape, y_test.shape

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV

# Set up the logistic regression model with L2 regularization
log_reg = LogisticRegression(solver='liblinear')

# Define the parameter grid for cross-validation
param_grid = {'C': [0.01, 0.1, 1, 10, 100]}

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

# Initialize classifiers with the best parameters
log_reg_best = LogisticRegression(C=best_params['C'], solver='liblinear')
knn_best = KNeighborsClassifier(n_neighbors=best_params_knn['n_neighbors'])
mlp_best = MLPClassifier(hidden_layer_sizes=best_params_mlp['hidden_layer_sizes'], max_iter=1000, random_state=42)

# Fit the classifiers on the training data
log_reg_best.fit(X_train, y_train)
knn_best.fit(X_train, y_train)
mlp_best.fit(X_train, y_train)

# Make predictions on the test set
y_pred_log_reg = log_reg_best.predict(X_test)
y_pred_knn = knn_best.predict(X_test)
y_pred_mlp = mlp_best.predict(X_test)

# Calculate metrics for each classifier
metrics = {
    'Logistic Regression': {
        'Precision': precision_score(y_test, y_pred_log_reg),
        'Recall': recall_score(y_test, y_pred_log_reg),
        'F1 Score': f1_score(y_test, y_pred_log_reg),
        'Accuracy': accuracy_score(y_test, y_pred_log_reg),
        'Optimal Hyperparameters': best_params
    },
    'KNN': {
        'Precision': precision_score(y_test, y_pred_knn),
        'Recall': recall_score(y_test, y_pred_knn),
        'F1 Score': f1_score(y_test, y_pred_knn),
        'Accuracy': accuracy_score(y_test, y_pred_knn),
        'Optimal Hyperparameters': best_params_knn
    },
    'Neural Network': {
        'Precision': precision_score(y_test, y_pred_mlp),
        'Recall': recall_score(y_test, y_pred_mlp),
        'F1 Score': f1_score(y_test, y_pred_mlp),
        'Accuracy': accuracy_score(y_test, y_pred_mlp),
        'Optimal Hyperparameters': best_params_mlp
    }
}

metrics

# Calculate the baseline performance (majority class assignment)
majority_class = y_train.mode()[0]
y_pred_baseline = [majority_class] * len(y_test)

# Calculate metrics for the baseline
baseline_metrics = {
    'Precision': precision_score(y_test, y_pred_baseline),
    'Recall': recall_score(y_test, y_pred_baseline),
    'F1 Score': f1_score(y_test, y_pred_baseline),
    'Accuracy': accuracy_score(y_test, y_pred_baseline),
}

baseline_metrics

