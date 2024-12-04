Let's start by loading the dataset and inspecting its contents. We will download the dataset from the provided URL, extract it, and load it into a pandas DataFrame.


First, let's download and extract the dataset.

Great! The dataset has been downloaded and extracted. Now, let's load the dataset into a pandas DataFrame and inspect its contents.


We will start by loading the parkinsons.data file, which contains the main dataset for Parkinson's disease detection.

The dataset has been successfully loaded into a pandas DataFrame. It contains 24 columns, including the target variable status, which indicates whether the patient has Parkinson's disease (1) or not (0).


Next, let's clean and normalize the data if necessary. We will:


Drop the name column as it is not useful for our analysis.
Check for any missing values and handle them if present.
Normalize the feature columns.

Let's proceed with these steps.

There are no missing values in the dataset. Now, let's normalize the feature columns. We will use the MinMaxScaler from scikit-learn to scale the features to a range of [0, 1].


Let's proceed with normalizing the data.

It seems that the scikit-learn library is not installed. Let's install it first.

The scikit-learn library has been successfully installed. Let's proceed with normalizing the data using the MinMaxScaler.

The features have been successfully normalized. Now, let's proceed to the next task: standardizing the features by computing the z-scores.


We will use the StandardScaler from scikit-learn to standardize the features.


Let's proceed with standardizing the data.

The features have been successfully standardized. Now, let's proceed to the next task: splitting the data into training and testing sets.


We will use the train_test_split function from scikit-learn to split the data. Let's proceed with this step.

The data has been successfully split into training and testing sets. The training set contains 156 samples, and the testing set contains 39 samples.


Next, let's train an L2-regularized logistic regression classifier to predict whether the voice recording comes from a patient who suffers from Parkinson’s disease. We will use cross-validation to determine the optimal regularization parameter aimed at optimizing the F1 score.


Let's proceed with this step.

The optimal regularization parameter for the logistic regression model is ( C = 10 ), and the F1 score on the test set is approximately 0.939.


Next, let's train a K-nearest neighbor (KNN) classifier for the same purpose, with ( K ) determined from cross-validation.


Let's proceed with this step.

The optimal number of neighbors for the KNN classifier is ( K = 1 ), and the F1 score on the test set is approximately 0.984.


Next, let's train a neural network with a single hidden layer, the width of which is determined from cross-validation.


Let's proceed with this step.

The optimal width for the hidden layer in the neural network is 10 neurons, and the F1 score on the test set is approximately 0.954.


Now, let's test all three classifiers and print the optimal hyperparameters, precision, recall, F1 score, and accuracy for each classifier.


Let's proceed with this step.

Here are the results for the three classifiers:


Logistic Regression

Best Params: {'C': 10}
Precision: 0.9118
Recall: 0.9688
F1 Score: 0.9394
Accuracy: 0.8974

K-Nearest Neighbors

Best Params: {'n_neighbors': 1}
Precision: 1.0
Recall: 0.9688
F1 Score: 0.9841
Accuracy: 0.9744

Neural Network

Best Params: {'hidden_layer_sizes': (10,)}
Precision: 0.9394
Recall: 0.9688
F1 Score: 0.9538
Accuracy: 0.9231

Next, let's compare the performance of these classifiers with class majority assignment as the baseline. We will calculate the precision, recall, F1 score, and accuracy for a model that assigns every data record the class that appears most frequently in the dataset.


Let's proceed with this step.

Here are the results for the majority class assignment:


Majority Class Assignment

Precision: 0.8205
Recall: 1.0
F1 Score: 0.9014
Accuracy: 0.8205

Comparison Summary

Logistic Regression:
F1 Score: 0.9394
Accuracy: 0.8974
K-Nearest Neighbors:
F1 Score: 0.9841
Accuracy: 0.9744
Neural Network:
F1 Score: 0.9538
Accuracy: 0.9231
Majority Class Assignment:
F1 Score: 0.9014
Accuracy: 0.8205

The K-Nearest Neighbors classifier performed the best among the three classifiers, achieving the highest F1 score and accuracy. All three classifiers outperformed the majority class assignment baseline.


If you have any further questions or tasks, please let me know! Otherwise, we can conclude this task.