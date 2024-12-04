import pandas as pd

# Load the dataset
data_path = 'parkinsons_data/parkinsons.data'
df = pd.read_csv(data_path)

# Display the first few rows and the summary of the dataset
df.head(), df.info()

# Drop the 'name' column
df_cleaned = df.drop(columns=['name'])

# Normalize the data (min-max normalization)
df_normalized = (df_cleaned - df_cleaned.min()) / (df_cleaned.max() - df_cleaned.min())

# Display the first few rows of the normalized dataset
df_normalized.head()

from sklearn.preprocessing import StandardScaler

# Standardize the features (compute z-scores)
scaler = StandardScaler()
features_standardized = scaler.fit_transform(df_normalized.drop(columns=['status']))

# Create a new DataFrame with standardized features and the status column
df_standardized = pd.DataFrame(features_standardized, columns=df_normalized.columns[:-1])
df_standardized['status'] = df_normalized['status']

# Display the first few rows of the standardized dataset
df_standardized.head()



from sklearn.preprocessing import StandardScaler

# Standardize the features (compute z-scores)
scaler = StandardScaler()
features_standardized = scaler.fit_transform(df_normalized.drop(columns=['status']))

# Create a new DataFrame with standardized features and the status column
df_standardized = pd.DataFrame(features_standardized, columns=df_normalized.columns[:-1])
df_standardized['status'] = df_normalized['status']

# Display the first few rows of the standardized dataset
df_standardized.head()

from sklearn.model_selection import train_test_split

# Split the data into features and target variable
X = df_standardized.drop(columns=['status'])
y = df_standardized['status']

# Split the dataset into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Display the shapes of the resulting datasets
X_train.shape, X_test.shape, y_train.shape, y_test.shape

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV

# Set up the logistic regression model with L2 regularization
log_reg = LogisticRegression(solver='liblinear')

# Define the parameter grid for cross-validation
param_grid = {'C': [0.01, 0.1, 1, 10, 100]}  # Inverse of regularization strength

# Set up GridSearchCV to optimize for F1 score
grid_search = GridSearchCV(log_reg, param_grid, scoring='f1', cv=5)
grid_search.fit(X_train, y_train)

# Get the best parameters and the best score
best_params = grid_search.best_params_
best_f1_score = grid_search.best_score_

best_params, best_f1_score

from sklearn.neighbors import KNeighborsClassifier

# Set up the KNN model
knn = KNeighborsClassifier()

# Define the parameter grid for cross-validation
param_grid_knn = {'n_neighbors': range(1, 21)}  # Testing K values from 1 to 20

# Set up GridSearchCV to optimize for F1 score
grid_search_knn = GridSearchCV(knn, param_grid_knn, scoring='f1', cv=5)
grid_search_knn.fit(X_train, y_train)

# Get the best parameters and the best score
best_params_knn = grid_search_knn.best_params_
best_f1_score_knn = grid_search_knn.best_score_

best_params_knn, best_f1_score_knn

from sklearn.neural_network import MLPClassifier

# Set up the neural network model
mlp = MLPClassifier(max_iter=1000)

# Define the parameter grid for cross-validation
param_grid_mlp = {'hidden_layer_sizes': [(i,) for i in range(1, 21)]}  # Testing hidden layer sizes from 1 to 20

# Set up GridSearchCV to optimize for F1 score
grid_search_mlp = GridSearchCV(mlp, param_grid_mlp, scoring='f1', cv=5)
grid_search_mlp.fit(X_train, y_train)

# Get the best parameters and the best score
best_params_mlp = grid_search_mlp.best_params_
best_f1_score_mlp = grid_search_mlp.best_score_

best_params_mlp, best_f1_score_mlp

from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score

# Test the logistic regression classifier
log_reg_best = LogisticRegression(C=best_params['C'], solver='liblinear')
log_reg_best.fit(X_train, y_train)
y_pred_log_reg = log_reg_best.predict(X_test)

# Test the KNN classifier
knn_best = KNeighborsClassifier(n_neighbors=best_params_knn['n_neighbors'])
knn_best.fit(X_train, y_train)
y_pred_knn = knn_best.predict(X_test)

# Test the neural network classifier
mlp_best = MLPClassifier(hidden_layer_sizes=best_params_mlp['hidden_layer_sizes'], max_iter=1000)
mlp_best.fit(X_train, y_train)
y_pred_mlp = mlp_best.predict(X_test)

# Calculate metrics for each classifier
results = {
    'Logistic Regression': {
        'Precision': precision_score(y_test, y_pred_log_reg),
        'Recall': recall_score(y_test, y_pred_log_reg),
        'F1 Score': f1_score(y_test, y_pred_log_reg),
        'Accuracy': accuracy_score(y_test, y_pred_log_reg),
        'Best Params': best_params
    },
    'KNN': {
        'Precision': precision_score(y_test, y_pred_knn),
        'Recall': recall_score(y_test, y_pred_knn),
        'F1 Score': f1_score(y_test, y_pred_knn),
        'Accuracy': accuracy_score(y_test, y_pred_knn),
        'Best Params': best_params_knn
    },
    'Neural Network': {
        'Precision': precision_score(y_test, y_pred_mlp),
        'Recall': recall_score(y_test, y_pred_mlp),
        'F1 Score': f1_score(y_test, y_pred_mlp),
        'Accuracy': accuracy_score(y_test, y_pred_mlp),
        'Best Params': best_params_mlp
    }
}

results

# Calculate the baseline performance (majority class assignment)
majority_class = y_train.mode()[0]
y_pred_baseline = [majority_class] * len(y_test)

# Calculate metrics for the baseline
baseline_results = {
    'Precision': precision_score(y_test, y_pred_baseline),
    'Recall': recall_score(y_test, y_pred_baseline),
    'F1 Score': f1_score(y_test, y_pred_baseline),
    'Accuracy': accuracy_score(y_test, y_pred_baseline)
}

baseline_results

