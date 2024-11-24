Let's start with Task 1, which involves loading the dataset and cleaning/normalizing the data if necessary. First, I will download the dataset from the provided URL and extract it.

The dataset has been successfully downloaded and extracted. Now, let's load the dataset using pandas and check for any necessary cleaning or normalization. I will start by loading the main data file, which is parkinsons.data.

The dataset has been successfully loaded, and it contains 195 entries with 24 columns. The columns include various voice measurements and a status column indicating whether the patient has Parkinson's disease (1 for positive, 0 for negative).


There are no missing values in the dataset, so no cleaning is necessary. However, we may want to normalize the data, especially since the features are on different scales.


Next, I will proceed to normalize the data. Let's apply Min-Max normalization to the feature columns (excluding the name and status columns).

It seems that the scikit-learn library is not installed in the current environment. I will install it now.

scikit-learn has been successfully installed. Now, I will proceed to normalize the data using Min-Max normalization as planned.

The data has been successfully normalized using Min-Max scaling. Now, we can proceed to Task 2, which involves standardizing the features by computing the z-scores.


I will standardize the features using the StandardScaler from scikit-learn. Let's do that now.

The features have been successfully standardized using z-scores. Now we can proceed to Task 3, which involves splitting the data into training and testing sets.


I will split the dataset into 80% training data and 20% testing data. Let's do that now.

The data has been successfully split into training and testing sets, with 156 samples in the training set and 39 samples in the testing set.


Now, let's move on to Task 4, which involves training an L2-regularized logistic regression classifier to predict whether the voice recording comes from a patient with Parkinson's disease. We will determine the regularization parameter using cross-validation aimed at optimizing the F1 score.


I'll proceed with this task now.

The L2-regularized logistic regression classifier has been trained successfully. The optimal regularization parameter ( C ) is 10, and the best F1 score achieved during cross-validation is approximately 0.905.


Now, let's proceed to Task 5, which involves training a K-nearest neighbor (KNN) classifier for the same purpose, with ( K ) determined from cross-validation. I'll perform this task now.

The K-nearest neighbor (KNN) classifier has been trained successfully. The optimal number of neighbors ( K ) is 1, and the best F1 score achieved during cross-validation is approximately 0.953.


Next, let's proceed to Task 6, which involves training a neural network with a single hidden layer. The width of the hidden layer will be determined from cross-validation. I'll perform this task now.

The neural network has been trained successfully. The optimal width of the hidden layer is 14 neurons, and the best F1 score achieved during cross-validation is approximately 0.954.


Now, let's proceed to Task 7, which involves testing all three classifiers (logistic regression, KNN, and neural network) and printing the optimal hyperparameters, precision, recall, F1 score, and accuracy for each classifier. I'll perform this task now.

Here are the performance metrics for each classifier:


Logistic Regression

Precision: 0.912
Recall: 0.969
F1 Score: 0.939
Accuracy: 0.897
Optimal Hyperparameters: ( C = 10 )
K-Nearest Neighbors (KNN)

Precision: 1.000
Recall: 0.969
F1 Score: 0.984
Accuracy: 0.974
Optimal Hyperparameters: ( n_neighbors = 1 )
Neural Network

Precision: 0.939
Recall: 0.969
F1 Score: 0.954
Accuracy: 0.923
Optimal Hyperparameters: ( \text{hidden_layer_sizes} = (14,) )

Now, let's proceed to Task 8, which involves comparing the performance of the classifiers with class majority assignment as the baseline. I will calculate the baseline performance and compare it with the classifiers' performance.

The baseline performance using class majority assignment is as follows:


Precision: 0.821
Recall: 1.000
F1 Score: 0.901
Accuracy: 0.821

Summary of Performance Comparison:

Logistic Regression:
F1 Score: 0.939
Accuracy: 0.897
K-Nearest Neighbors (KNN):
F1 Score: 0.984
Accuracy: 0.974
Neural Network:
F1 Score: 0.954
Accuracy: 0.923
Baseline:
F1 Score: 0.901
Accuracy: 0.821

The classifiers outperformed the baseline model in terms of F1 score and accuracy, with KNN achieving the highest performance.


If you have any further questions or tasks, let me know! Otherwise, I will conclude this task.