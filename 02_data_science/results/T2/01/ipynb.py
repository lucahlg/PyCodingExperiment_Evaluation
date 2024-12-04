import pandas as pd

# Load the dataset
data_path = 'parkinsons_data/parkinsons.data'
df = pd.read_csv(data_path)

# Display the first few rows of the dataset
df.head()

# Drop the 'name' column
df.drop(columns=['name'], inplace=True)

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
X_normalized_df = pd.DataFrame(X_normalized, columns=X.columns)

# Display the first few rows of the normalized features
X_normalized_df.head()



from sklearn.preprocessing import MinMaxScaler

# Separate features and target variable
X = df.drop(columns=['status'])
y = df['status']

# Initialize the MinMaxScaler
scaler = MinMaxScaler()

# Normalize the features
X_normalized = scaler.fit_transform(X)

# Convert the normalized features back to a DataFrame
X_normalized_df = pd.DataFrame(X_normalized, columns=X.columns)

# Display the first few rows of the normalized features
X_normalized_df.head()

from sklearn.preprocessing import StandardScaler

# Initialize the StandardScaler
scaler = StandardScaler()

# Standardize the features
X_standardized = scaler.fit_transform(X_normalized_df)

# Convert the standardized features back to a DataFrame
X_standardized_df = pd.DataFrame(X_standardized, columns=X.columns)

# Display the first few rows of the standardized features
X_standardized_df.head()

from sklearn.model_selection import train_test_split

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_standardized_df, y, test_size=0.2, random_state=42)

# Display the shapes of the training and testing sets
(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import make_scorer, f1_score

# Initialize the logistic regression model
log_reg = LogisticRegression(penalty='l2', solver='liblinear')

# Define the parameter grid for cross-validation
param_grid = {'C': [0.01, 0.1, 1, 10, 100]}

# Define the F1 score as the scoring metric
f1_scorer = make_scorer(f1_score)

# Initialize the GridSearchCV object
grid_search = GridSearchCV(log_reg, param_grid, scoring=f1_scorer, cv=5)

# Fit the model to the training data
grid_search.fit(X_train, y_train)

# Get the best parameters and the best F1 score
best_params = grid_search.best_params_
best_f1_score = grid_search.best_score_

(best_params, best_f1_score)

from sklearn.neighbors import KNeighborsClassifier

# Initialize the KNN classifier
knn = KNeighborsClassifier()

# Define the parameter grid for cross-validation
param_grid = {'n_neighbors': [1, 3, 5, 7, 9, 11, 13, 15]}

# Initialize the GridSearchCV object
grid_search_knn = GridSearchCV(knn, param_grid, scoring=f1_scorer, cv=5)

# Fit the model to the training data
grid_search_knn.fit(X_train, y_train)

# Get the best parameters and the best F1 score
best_params_knn = grid_search_knn.best_params_
best_f1_score_knn = grid_search_knn.best_score_

(best_params_knn, best_f1_score_knn)

from sklearn.neural_network import MLPClassifier

# Initialize the neural network classifier
mlp = MLPClassifier(max_iter=1000, random_state=42)

# Define the parameter grid for cross-validation
param_grid = {'hidden_layer_sizes': [(5,), (10,), (15,), (20,), (25,), (30,)]}

# Initialize the GridSearchCV object
grid_search_mlp = GridSearchCV(mlp, param_grid, scoring=f1_scorer, cv=5)

# Fit the model to the training data
grid_search_mlp.fit(X_train, y_train)

# Get the best parameters and the best F1 score
best_params_mlp = grid_search_mlp.best_params_
best_f1_score_mlp = grid_search_mlp.best_score_

(best_params_mlp, best_f1_score_mlp)

from sklearn.metrics import precision_score, recall_score, accuracy_score

# Initialize the classifiers with the best parameters
log_reg_best = LogisticRegression(penalty='l2', C=10, solver='liblinear')
knn_best = KNeighborsClassifier(n_neighbors=1)
mlp_best = MLPClassifier(hidden_layer_sizes=(10,), max_iter=1000, random_state=42)

# Train the classifiers on the training data
log_reg_best.fit(X_train, y_train)
knn_best.fit(X_train, y_train)
mlp_best.fit(X_train, y_train)

# Make predictions on the test data
y_pred_log_reg = log_reg_best.predict(X_test)
y_pred_knn = knn_best.predict(X_test)
y_pred_mlp = mlp_best.predict(X_test)

# Calculate the performance metrics for each classifier
metrics = {
    'Logistic Regression': {
        'Precision': precision_score(y_test, y_pred_log_reg),
        'Recall': recall_score(y_test, y_pred_log_reg),
        'F1 Score': f1_score(y_test, y_pred_log_reg),
        'Accuracy': accuracy_score(y_test, y_pred_log_reg)
    },
    'K-Nearest Neighbors': {
        'Precision': precision_score(y_test, y_pred_knn),
        'Recall': recall_score(y_test, y_pred_knn),
        'F1 Score': f1_score(y_test, y_pred_knn),
        'Accuracy': accuracy_score(y_test, y_pred_knn)
    },
    'Neural Network': {
        'Precision': precision_score(y_test, y_pred_mlp),
        'Recall': recall_score(y_test, y_pred_mlp),
        'F1 Score': f1_score(y_test, y_pred_mlp),
        'Accuracy': accuracy_score(y_test, y_pred_mlp)
    }
}

metrics

# Determine the majority class in the training set
majority_class = y_train.mode()[0]

# Make predictions using the majority class
y_pred_majority = [majority_class] * len(y_test)

# Calculate the performance metrics for the majority class classifier
majority_metrics = {
    'Precision': precision_score(y_test, y_pred_majority),
    'Recall': recall_score(y_test, y_pred_majority),
    'F1 Score': f1_score(y_test, y_pred_majority),
    'Accuracy': accuracy_score(y_test, y_pred_majority)
}

majority_metrics

