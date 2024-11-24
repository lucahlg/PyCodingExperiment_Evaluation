Let's start with Task 1, which involves loading the dataset and cleaning/normalizing the data if necessary. First, I will download the dataset from the provided URL and extract it.

The dataset has been successfully downloaded and extracted. Now, I will load the dataset using pandas and check for any necessary cleaning or normalization. Let's start by loading the main dataset file parkinsons.data.

The dataset has been successfully loaded, and it contains 195 entries with 24 columns. The columns include various voice measurements and a status column indicating whether the patient has Parkinson's disease (1) or not (0).


There are no missing values, so we can proceed to normalize the data. Normalization typically involves scaling the features to a standard range. In this case, I will use Min-Max scaling to normalize the features, excluding the name and status columns.


Let's perform the normalization now.

It seems that the scikit-learn library is not installed in the current environment. I will install it now.

scikit-learn has been successfully installed. Now, I will proceed with normalizing the dataset using Min-Max scaling. Let's do that now.

The dataset has been successfully normalized. The features are now scaled between 0 and 1, and the status column remains unchanged.


Now, let's move on to Task 2, which involves standardizing the features by computing the z-scores. I will standardize the features using the StandardScaler from scikit-learn. Let's proceed with that.

The features have been successfully standardized using z-scores. Now, let's move on to Task 3, which involves splitting the data into training and testing sets. I will use an 80-20 split for this purpose.


Let's proceed with splitting the dataset.

The dataset has been successfully split into training and testing sets, with 156 samples in the training set and 39 samples in the testing set.


Now, let's move on to Task 4, which involves training an L2-regularized logistic regression classifier to predict whether the voice recording comes from a patient with Parkinson's disease. We will determine the regularization parameter using cross-validation aimed at optimizing the F1 score.


Let's proceed with training the logistic regression classifier.

The L2-regularized logistic regression classifier has been trained successfully. The optimal regularization parameter ( C ) is 10, and the best F1 score achieved during cross-validation is approximately 0.905.


Now, let's move on to Task 5, which involves training a K-nearest neighbor (KNN) classifier for the same purpose, with ( K ) determined from cross-validation. Let's proceed with that.

The K-nearest neighbor (KNN) classifier has been trained successfully. The optimal number of neighbors ( K ) is 1, and the best F1 score achieved during cross-validation is approximately 0.953.


Now, let's move on to Task 6, which involves training a neural network with a single hidden layer, where the width of the hidden layer is determined from cross-validation. Let's proceed with that.

The neural network has been trained successfully. The optimal width of the hidden layer is 14 neurons, and the best F1 score achieved during cross-validation is approximately 0.954.


Now, let's move on to Task 7, which involves testing all three classifiers (logistic regression, KNN, and neural network) and printing the optimal hyperparameters, precision, recall, F1 score, and accuracy for each classifier. Let's proceed with that.

Here are the results for the three classifiers:


Logistic Regression

Precision: 0.912
Recall: 0.969
F1 Score: 0.939
Accuracy: 0.897
Best Params: ( C = 10 )
K-Nearest Neighbors (KNN)

Precision: 1.000
Recall: 0.969
F1 Score: 0.984
Accuracy: 0.974
Best Params: ( n_neighbors = 1 )
Neural Network

Precision: 0.939
Recall: 0.969
F1 Score: 0.954
Accuracy: 0.923
Best Params: ( \text{hidden_layer_sizes} = (14,) )

Now, let's move on to Task 8, which involves comparing the performance of the classifiers with class majority assignment as the baseline. I will calculate the baseline performance and compare it with the classifiers' performance. Let's proceed with that.

The baseline performance using class majority assignment is as follows:


Precision: 0.821
Recall: 1.000
F1 Score: 0.901
Accuracy: 0.821

Comparison of Classifier Performance with Baseline:

Logistic Regression:

Precision: 0.912
Recall: 0.969
F1 Score: 0.939
Accuracy: 0.897
K-Nearest Neighbors (KNN):

Precision: 1.000
Recall: 0.969
F1 Score: 0.984
Accuracy: 0.974
Neural Network:

Precision: 0.939
Recall: 0.969
F1 Score: 0.954
Accuracy: 0.923
Baseline:

Precision: 0.821
Recall: 1.000
F1 Score: 0.901
Accuracy: 0.821

Summary:

All classifiers outperformed the baseline in terms of precision, F1 score, and accuracy, with KNN achieving the highest performance across all metrics.


If you have any further questions or tasks, feel free to ask!