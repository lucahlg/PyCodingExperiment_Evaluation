<instructions>
You are a data science student. You will be given a data science related task that you need solve task by task.
</instructions>
<title> Parkinson’s disease detection</title>
<introduction> 
For this exercise and the following exercises, use of the Python libraries pandas and scikit-learn is recommended.
Speech disorders can be an early sign of motor impairment in Parkinson’s. The Oxford Parkinson’s Disease Detection Dataset can be used to demonstrate that biomedical voice measurements are indicative of whether the patient suffers from Parkinson’s. The dataset is available at the UC Irvine Machine Learning Repository: https://archive.ics.uci.edu/static/public/174/parkinsons.zip
More information about the dataset and its attributes can be found at https://archive.ics.uci.edu/dataset/174/parkinsons
</introduction>
<task 1> load the dataset; clean/normalize the data if necessary </taks 1>
<task 2> standardize the features (i.e., compute the z-scores) </task 2>
<task 3> split the data into training and testing data </task 3>
<task 4> train an L2-regularized logistic regression classifier to predict whether the voice recording comes from a patient who suffers from Parkinson’s disease, with the regularization parameter determined from cross-validation aimed at optimizing the F1 score </task 4>
<task 5> train a K-nearest neighbor classifier for the same purpose with K determined from cross-validation </task 5>
<task 6> train a neural network with a single hidden layer, the width of which is determined from cross-validation </task 6>
<task 7> test all three classifiers and print the optimal hyperparameter, precision, recall, F1 score, and accuracy </task 7>
<task 8> Compare the performance of the classifiers with class majority assignment as the baseline, i.e., with the performance of a machine that would assign every data record the class that appears most frequently in the dataset. </task 8>