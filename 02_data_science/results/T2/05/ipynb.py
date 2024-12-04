import pandas as pd

# Load the dataset
data_path = 'parkinsons_data/parkinsons.data'
df = pd.read_csv(data_path)

# Display the first few rows of the dataset
df.head()

from sklearn.preprocessing import MinMaxScaler

# Drop the 'name' column
df = df.drop(columns=['name'])

# Check for missing values
missing_values = df.isnull().sum()

# Normalize the data using Min-Max scaling
scaler = MinMaxScaler()
df[df.columns] = scaler.fit_transform(df[df.columns])

# Display the first few rows of the cleaned and normalized dataset
df.head(), missing_values



from sklearn.preprocessing import MinMaxScaler

# Drop the 'name' column
df = df.drop(columns=['name'])

# Check for missing values
missing_values = df.isnull().sum()

# Normalize the data using Min-Max scaling
scaler = MinMaxScaler()
df[df.columns] = scaler.fit_transform(df[df.columns])

# Display the first few rows of the cleaned and normalized dataset
df.head(), missing_values

from sklearn.preprocessing import StandardScaler

# Separate features and target variable
X = df.drop(columns=['status'])
y = df['status']

# Standardize the features
scaler = StandardScaler()
X_standardized = scaler.fit_transform(X)

# Convert the standardized features back to a DataFrame
X_standardized_df = pd.DataFrame(X_standardized, columns=X.columns)

# Display the first few rows of the standardized features
X_standardized_df.head()

from sklearn.model_selection import train_test_split

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_standardized_df, y, test_size=0.2, random_state=42)

# Display the shapes of the training and testing sets
X_train.shape, X_test.shape, y_train.shape, y_test.shape

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import f1_score, make_scorer

# Define the logistic regression model
log_reg = LogisticRegression(penalty='l2', solver='liblinear')

# Define the parameter grid for cross-validation
param_grid = {'C': [0.01, 0.1, 1, 10, 100]}

# Define the F1 score as the scoring metric
f1_scorer = make_scorer(f1_score)

# Perform grid search with cross-validation
grid_search = GridSearchCV(log_reg, param_grid, scoring=f1_scorer, cv=5)
grid_search.fit(X_train, y_train)

# Get the best model and its parameters
best_log_reg = grid_search.best_estimator_
best_params = grid_search.best_params_

# Display the best parameters
best_params

from sklearn.neighbors import KNeighborsClassifier

# Define the KNN model
knn = KNeighborsClassifier()

# Define the parameter grid for cross-validation
param_grid = {'n_neighbors': [1, 3, 5, 7, 9, 11, 13, 15]}

# Perform grid search with cross-validation
grid_search_knn = GridSearchCV(knn, param_grid, scoring=f1_scorer, cv=5)
grid_search_knn.fit(X_train, y_train)

# Get the best model and its parameters
best_knn = grid_search_knn.best_estimator_
best_params_knn = grid_search_knn.best_params_

# Display the best parameters
best_params_knn

from sklearn.neural_network import MLPClassifier

# Define the neural network model
mlp = MLPClassifier(max_iter=1000, random_state=42)

# Define the parameter grid for cross-validation
param_grid = {'hidden_layer_sizes': [(5,), (10,), (15,), (20,), (25,), (30,)]}

# Perform grid search with cross-validation
grid_search_mlp = GridSearchCV(mlp, param_grid, scoring=f1_scorer, cv=5)
grid_search_mlp.fit(X_train, y_train)

# Get the best model and its parameters
best_mlp = grid_search_mlp.best_estimator_
best_params_mlp = grid_search_mlp.best_params_

# Display the best parameters
best_params_mlp

from sklearn.metrics import precision_score, recall_score, accuracy_score

# Function to evaluate a model
def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    accuracy = accuracy_score(y_test, y_pred)
    return precision, recall, f1, accuracy

# Evaluate the logistic regression model
log_reg_precision, log_reg_recall, log_reg_f1, log_reg_accuracy = evaluate_model(best_log_reg, X_test, y_test)

# Evaluate the KNN model
knn_precision, knn_recall, knn_f1, knn_accuracy = evaluate_model(best_knn, X_test, y_test)

# Evaluate the neural network model
mlp_precision, mlp_recall, mlp_f1, mlp_accuracy = evaluate_model(best_mlp, X_test, y_test)

# Display the results
{
    "Logistic Regression": {
        "Best Parameter": best_params,
        "Precision": log_reg_precision,
        "Recall": log_reg_recall,
        "F1 Score": log_reg_f1,
        "Accuracy": log_reg_accuracy
    },
    "KNN": {
        "Best Parameter": best_params_knn,
        "Precision": knn_precision,
        "Recall": knn_recall,
        "F1 Score": knn_f1,
        "Accuracy": knn_accuracy
    },
    "Neural Network": {
        "Best Parameter": best_params_mlp,
        "Precision": mlp_precision,
        "Recall": mlp_recall,
        "F1 Score": mlp_f1,
        "Accuracy": mlp_accuracy
    }
}

# Calculate the baseline performance
majority_class = y_train.mode()[0]
y_baseline = [majority_class] * len(y_test)

baseline_precision = precision_score(y_test, y_baseline)
baseline_recall = recall_score(y_test, y_baseline)
baseline_f1 = f1_score(y_test, y_baseline)
baseline_accuracy = accuracy_score(y_test, y_baseline)

# Display the baseline performance
{
    "Baseline": {
        "Precision": baseline_precision,
        "Recall": baseline_recall,
        "F1 Score": baseline_f1,
        "Accuracy": baseline_accuracy
    }
}

