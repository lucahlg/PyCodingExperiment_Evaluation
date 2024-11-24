Let's start with Task 1, which involves loading the dataset and cleaning/normalizing the data if necessary. First, I will download the dataset from the provided URL and extract it.

The dataset has been successfully downloaded and extracted. Now, let's load the dataset using pandas and check for any necessary cleaning or normalization. I'll start by loading the main data file parkinsons.data.

The dataset has been successfully loaded, and it contains 195 entries with 24 columns. The columns include various voice measurements and a status column indicating whether the patient has Parkinson's disease (1) or not (0).


There are no missing values in the dataset, so we can proceed to normalize the data. Normalization typically involves scaling the features to a standard range. In this case, we can use Min-Max scaling to normalize the features.


Let's normalize the features (excluding the name and status columns) and prepare the dataset for further analysis.

It seems that the scikit-learn library is not installed in the current environment. I will install it now.

scikit-learn has been successfully installed. Now, let's proceed with normalizing the features of the dataset.

The features have been successfully normalized. Now we can proceed to Task 2, which involves standardizing the features by computing the z-scores. This will help in ensuring that the features have a mean of 0 and a standard deviation of 1.


Let's standardize the features using the StandardScaler from scikit-learn.

The features have been successfully standardized. Now we can proceed to Task 3, which involves splitting the data into training and testing sets. We'll use an 80-20 split for this purpose.


Let's perform the split using train_test_split from scikit-learn.

The data has been successfully split into training and testing sets, with 156 samples in the training set and 39 samples in the testing set.


Now, let's move on to Task 4, which involves training an L2-regularized logistic regression classifier to predict whether the voice recording comes from a patient who suffers from Parkinson’s disease. We will use cross-validation to determine the optimal regularization parameter aimed at optimizing the F1 score.


Let's proceed with this task.

The optimal regularization parameter for the L2-regularized logistic regression classifier is ( C = 10 ), with a best F1 score of approximately 0.905.


Now, let's proceed to Task 5, which involves training a K-nearest neighbor (KNN) classifier for the same purpose, with ( K ) determined from cross-validation. I'll set up the KNN model and perform the cross-validation to find the best ( K ) value.

The optimal number of neighbors for the K-nearest neighbor classifier is ( K = 1 ), with a best F1 score of approximately 0.953.


Now, let's proceed to Task 6, which involves training a neural network with a single hidden layer. The width of the hidden layer will be determined from cross-validation. I'll set up the neural network model and perform the cross-validation to find the best width for the hidden layer.

The optimal width for the hidden layer in the neural network is 11 neurons, with a best F1 score of approximately 0.954.


Now, let's proceed to Task 7, which involves testing all three classifiers (logistic regression, KNN, and neural network) and printing the optimal hyperparameters, precision, recall, F1 score, and accuracy for each classifier.


I'll start by evaluating the logistic regression classifier.

The evaluation results for the Logistic Regression classifier are as follows:


Model: Logistic Regression
Best Parameters: ( C = 10 )
Precision: 0.912
Recall: 0.969
F1 Score: 0.939
Accuracy: 0.897

Next, let's evaluate the K-nearest neighbor (KNN) classifier.

The evaluation results for the K-nearest neighbor (KNN) classifier are as follows:


Model: K-Nearest Neighbors
Best Parameters: ( K = 1 )
Precision: 1.000
Recall: 0.969
F1 Score: 0.984
Accuracy: 0.974

Now, let's evaluate the neural network classifier.

The evaluation results for the Neural Network classifier are as follows:


Model: Neural Network
Best Parameters: 11 neurons in the hidden layer
Precision: 0.939
Recall: 0.969
F1 Score: 0.954
Accuracy: 0.923

Now that we have evaluated all three classifiers, let's summarize the results:


Logistic Regression

Best Parameters: ( C = 10 )
Precision: 0.912
Recall: 0.969
F1 Score: 0.939
Accuracy: 0.897
K-Nearest Neighbors

Best Parameters: ( K = 1 )
Precision: 1.000
Recall: 0.969
F1 Score: 0.984
Accuracy: 0.974
Neural Network

Best Parameters: 11 neurons in the hidden layer
Precision: 0.939
Recall: 0.969
F1 Score: 0.954
Accuracy: 0.923

Next, let's proceed to Task 8, which involves comparing the performance of the classifiers with class majority assignment as the baseline. I'll calculate the baseline performance and compare it with the classifiers' performances. The baseline will be the accuracy of a model that predicts the majority class for all instances.

The baseline accuracy, which represents the performance of a model that predicts the majority class for all instances, is approximately 0.754.


Now, let's summarize the comparison of the classifiers' performances against the baseline:


Classifier Performance Summary

Baseline (Majority Class)

Accuracy: 0.754
Logistic Regression

Accuracy: 0.897
K-Nearest Neighbors

Accuracy: 0.974
Neural Network

Accuracy: 0.923

Conclusion

All three classifiers significantly outperform the baseline accuracy of 0.754, with the K-nearest neighbors classifier achieving the highest accuracy of 0.974.


If you have any further questions or tasks, feel free to ask!