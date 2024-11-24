Let's start by loading the dataset and inspecting its contents. We will download the dataset from the provided URL, extract it, and load it into a pandas DataFrame.


First, let's download and extract the dataset.

The dataset has been successfully downloaded and extracted. Let's load the main dataset (parkinsons_data/parkinsons.data) into a pandas DataFrame and inspect its contents.

The dataset has been successfully loaded into a pandas DataFrame. The dataset contains 24 columns, including the target variable status, which indicates whether the patient has Parkinson's disease (1) or not (0).


Next, let's clean and normalize the data if necessary. We will:


Drop the name column as it is not useful for our analysis.
Check for any missing values and handle them if present.
Normalize the features.

Let's proceed with these steps.

There are no missing values in the dataset. Now, let's normalize the features. We will use the Min-Max scaling technique to normalize the features to a range of [0, 1].


Let's proceed with the normalization.

It seems that the scikit-learn library is not installed. Let's install it first.

The scikit-learn library has been successfully installed. Let's proceed with normalizing the features using the Min-Max scaling technique.

The features have been successfully normalized. Now, let's proceed to the next task: standardizing the features by computing the z-scores.


We will use the StandardScaler from scikit-learn to standardize the features.

The features have been successfully standardized. Now, let's proceed to the next task: splitting the data into training and testing sets.


We will use the train_test_split function from scikit-learn to split the data. Let's proceed with this step.

The data has been successfully split into training and testing sets. The training set contains 156 samples, and the testing set contains 39 samples.


Next, let's proceed to train an L2-regularized logistic regression classifier to predict whether the voice recording comes from a patient who suffers from Parkinson’s disease. We will use cross-validation to determine the optimal regularization parameter aimed at optimizing the F1 score.


Let's proceed with this step.

The optimal regularization parameter for the L2-regularized logistic regression classifier is ( C = 10 ), and the best F1 score from cross-validation is approximately 0.905.


Next, let's train a K-nearest neighbor (KNN) classifier for the same purpose, with ( K ) determined from cross-validation. We will use the same approach to optimize the F1 score.


Let's proceed with this step.

The optimal number of neighbors for the K-nearest neighbor classifier is ( K = 1 ), and the best F1 score from cross-validation is approximately 0.953.


Next, let's train a neural network with a single hidden layer, the width of which is determined from cross-validation. We will use the same approach to optimize the F1 score.


Let's proceed with this step.

The optimal width for the hidden layer of the neural network is 10 neurons, and the best F1 score from cross-validation is approximately 0.945.


Now, let's test all three classifiers (logistic regression, KNN, and neural network) on the test set and print the optimal hyperparameters, precision, recall, F1 score, and accuracy for each classifier.


Let's proceed with this step.

Here are the performance metrics for each classifier on the test set:


Logistic Regression:


Precision: 0.912
Recall: 0.969
F1 Score: 0.939
Accuracy: 0.897

K-Nearest Neighbors:


Precision: 1.000
Recall: 0.969
F1 Score: 0.984
Accuracy: 0.974

Neural Network:


Precision: 0.939
Recall: 0.969
F1 Score: 0.954
Accuracy: 0.923

Next, let's compare the performance of these classifiers with class majority assignment as the baseline. We will calculate the performance metrics for a classifier that assigns every data record the class that appears most frequently in the dataset.


Let's proceed with this step.

Here are the performance metrics for the majority class classifier:


Majority Class Classifier:


Precision: 0.821
Recall: 1.000
F1 Score: 0.901
Accuracy: 0.821

Comparison:


Metric	Logistic Regression	K-Nearest Neighbors	Neural Network	Majority Class
Precision	0.912	1.000	0.939	0.821
Recall	0.969	0.969	0.969	1.000
F1 Score	0.939	0.984	0.954	0.901
Accuracy	0.897	0.974	0.923	0.821

From the comparison, we can see that all three classifiers (Logistic Regression, K-Nearest Neighbors, and Neural Network) outperform the majority class classifier in terms of precision, F1 score, and accuracy. The K-Nearest Neighbors classifier achieves the highest F1 score and accuracy among the three classifiers.


If you have any further questions or need additional analysis, feel free to ask. Otherwise, we can conclude this task.