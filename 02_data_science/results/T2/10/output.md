Let's start with Task 1, which involves loading the dataset and cleaning/normalizing the data if necessary. First, I will download the dataset from the provided URL and extract it.

The dataset has been successfully downloaded and extracted. Now, let's load the dataset using pandas and check its structure to see if any cleaning or normalization is necessary. I'll start by loading the parkinsons.data file, which contains the relevant data for our analysis.

The dataset has been successfully loaded, and it contains 195 entries with 24 columns. The columns include various voice measurements and a status column indicating whether the patient has Parkinson's disease (1) or not (0).


There are no missing values, so we can proceed to normalize the data. The name column is not needed for our analysis, so we will drop it. Let's clean the dataset by removing the name column and normalizing the feature columns.


I'll perform the following steps:


Drop the name column.
Normalize the feature columns.

Let's proceed with these steps.

The dataset has been cleaned by dropping the name column and normalized using min-max normalization. The normalized dataset is ready for further analysis.


Now, let's move on to Task 2, which involves standardizing the features by computing the z-scores. This will help in ensuring that each feature contributes equally to the analysis. I'll proceed with standardizing the features.

It seems that the scikit-learn library is not installed in the current environment. I will install it now so that we can proceed with standardizing the features.

scikit-learn has been successfully installed. Now, I will proceed to standardize the features by computing the z-scores.

The features have been successfully standardized using z-scores. The standardized dataset is now ready for further analysis.


Next, let's move on to Task 3, which involves splitting the data into training and testing sets. I'll use an 80-20 split for this purpose. Let's proceed with the split.

The dataset has been successfully split into training and testing sets, with 156 samples in the training set and 39 samples in the testing set.


Now, let's move on to Task 4, which involves training an L2-regularized logistic regression classifier to predict whether the voice recording comes from a patient who suffers from Parkinson’s disease. We will determine the regularization parameter using cross-validation aimed at optimizing the F1 score.


I'll proceed with this task now.

The L2-regularized logistic regression classifier has been trained successfully. The optimal regularization parameter ( C ) is 100, and the best F1 score achieved during cross-validation is approximately 0.908.


Now, let's move on to Task 5, which involves training a K-nearest neighbor (KNN) classifier for the same purpose, with ( K ) determined from cross-validation. I'll proceed with this task now.

The K-nearest neighbor (KNN) classifier has been trained successfully. The optimal number of neighbors ( K ) is 1, and the best F1 score achieved during cross-validation is approximately 0.948.


Next, let's move on to Task 6, which involves training a neural network with a single hidden layer. The width of the hidden layer will be determined from cross-validation. I'll proceed with this task now.

The neural network has been trained successfully. The optimal width of the hidden layer is 18 neurons, and the best F1 score achieved during cross-validation is approximately 0.944.


Now, let's move on to Task 7, which involves testing all three classifiers (logistic regression, KNN, and neural network) and printing the optimal hyperparameters, precision, recall, F1 score, and accuracy for each classifier. I'll proceed with this task now.

Here are the results for the three classifiers:


Logistic Regression

Precision: 0.914
Recall: 1.0
F1 Score: 0.955
Accuracy: 0.923
Best Params: ( C = 100 )
K-Nearest Neighbors (KNN)

Precision: 1.0
Recall: 1.0
F1 Score: 1.0
Accuracy: 1.0
Best Params: ( n_neighbors = 1 )
Neural Network

Precision: 0.939
Recall: 0.969
F1 Score: 0.954
Accuracy: 0.923
Best Params: ( \text{hidden_layer_sizes} = (18,) )

Now, let's move on to Task 8, which involves comparing the performance of the classifiers with class majority assignment as the baseline. I'll calculate the baseline performance and compare it with the classifiers' performances.

The baseline performance using class majority assignment is as follows:


Precision: 0.821
Recall: 1.0
F1 Score: 0.901
Accuracy: 0.821

Summary of Results:

Logistic Regression:

Precision: 0.914
Recall: 1.0
F1 Score: 0.955
Accuracy: 0.923
K-Nearest Neighbors (KNN):

Precision: 1.0
Recall: 1.0
F1 Score: 1.0
Accuracy: 1.0
Neural Network:

Precision: 0.939
Recall: 0.969
F1 Score: 0.954
Accuracy: 0.923
Baseline:

Precision: 0.821
Recall: 1.0
F1 Score: 0.901
Accuracy: 0.821

Conclusion:

The KNN classifier outperformed the others, achieving perfect precision, recall, and F1 score. All classifiers performed better than the baseline, indicating that they are effective in predicting Parkinson's disease based on the voice recordings.


If you have any further questions or tasks, let me know! Otherwise, I will conclude this session.