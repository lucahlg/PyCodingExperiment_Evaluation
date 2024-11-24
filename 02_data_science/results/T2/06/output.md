Let's start with Task 1, which involves loading the dataset and cleaning/normalizing the data if necessary. First, I will download the dataset from the provided URL and extract it.

The dataset has been successfully downloaded and extracted. Now, let's load the dataset using pandas and check for any necessary cleaning or normalization. The main data file we will focus on is parkinsons.data.


I'll load the dataset and display the first few rows to understand its structure.

The dataset has been loaded successfully, and it contains 24 columns, including various voice measurements and a status column indicating whether the patient has Parkinson's disease (1 for positive, 0 for negative).


Next, let's check for any missing values and normalize the data if necessary. I'll display the summary of the dataset and check for null values.

The dataset has no missing values, which is great. The summary statistics show a range of values for the various features, indicating that normalization may be beneficial for some of the features, especially those with different scales.


Next, let's proceed to normalize the data. We will drop the name column (as it is not useful for our analysis) and normalize the feature columns using Min-Max scaling. The status column will be retained as it is our target variable.


I'll perform these steps now.

It seems that the scikit-learn library is not installed in the current environment. Let me install it first before proceeding with the normalization of the dataset.

scikit-learn has been successfully installed. Now, let's proceed with normalizing the dataset by dropping the name column and applying Min-Max scaling to the feature columns. I'll perform these steps now.

It seems that the kernel needs to be restarted to recognize the newly installed scikit-learn package. Let me restart the kernel and then re-import the necessary libraries to proceed with the normalization of the dataset.


I'll do that now.

The dataset has been successfully normalized, and the first few rows of the normalized features and the target variable (status) are displayed.


Now we can move on to Task 2, which involves standardizing the features by computing the z-scores. I'll perform this step next.

The features have been successfully standardized using z-scores. Now we can move on to Task 3, which involves splitting the data into training and testing sets.


I'll split the dataset into training and testing sets, using 80% of the data for training and 20% for testing. Let's proceed with this step.

The dataset has been successfully split into training and testing sets, with 156 samples for training and 39 samples for testing.


Now we can proceed to Task 4, which involves training an L2-regularized logistic regression classifier to predict whether the voice recording comes from a patient who suffers from Parkinson’s disease. We will use cross-validation to determine the optimal regularization parameter aimed at optimizing the F1 score.


Let's implement this now.

The optimal regularization parameter ( C ) for the L2-regularized logistic regression classifier is 10, with a best F1 score of approximately 0.908.


Now, let's proceed to Task 5, which involves training a K-nearest neighbor (KNN) classifier for the same purpose, with ( K ) determined from cross-validation. I'll implement this next.

The optimal number of neighbors ( K ) for the K-nearest neighbor classifier is 1, with a best F1 score of approximately 0.958.


Now, let's proceed to Task 6, which involves training a neural network with a single hidden layer. The width of the hidden layer will be determined from cross-validation. I'll implement this next.

The optimal width of the hidden layer for the neural network is 17, with a best F1 score of approximately 0.958.


Now, let's proceed to Task 7, where we will test all three classifiers (logistic regression, KNN, and neural network) and print the optimal hyperparameters, precision, recall, F1 score, and accuracy for each classifier. I'll implement this next.

Here are the results for the three classifiers:


Logistic Regression

Precision: 0.931
Recall: 0.931
F1 Score: 0.931
Accuracy: 0.897
Best Hyperparameters: ( C = 10 )
K-Nearest Neighbors (KNN)

Precision: 0.967
Recall: 1.000
F1 Score: 0.983
Accuracy: 0.974
Best Hyperparameters: ( n_neighbors = 1 )
Neural Network

Precision: 0.963
Recall: 0.897
F1 Score: 0.929
Accuracy: 0.897
Best Hyperparameters: ( \text{hidden_layer_sizes} = (17,) )

Now, let's proceed to Task 8, where we will compare the performance of the classifiers with class majority assignment as the baseline. I'll implement this next.

The baseline performance using class majority assignment is as follows:


Precision: 0.744
Recall: 1.000
F1 Score: 0.853
Accuracy: 0.744
Majority Class: 1

Summary of Results:

The classifiers significantly outperformed the baseline:
KNN achieved the highest F1 score (0.983) and accuracy (0.974).
Logistic Regression and Neural Network also performed well, but KNN was the best among them.

If you have any further questions or tasks, feel free to ask! Otherwise, I will conclude this task.