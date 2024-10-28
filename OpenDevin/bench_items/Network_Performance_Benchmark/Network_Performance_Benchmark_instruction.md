# Analyze and Modify Benchmark Results

## Objective:

The goal of this exercise is to analyze a benchmark JSON object representing image classification performance and modify it according to given instructions. 

## Exercise Instructions:

You are provided with a JSON file containing benchmark data for an image classification model. Your tasks are as follows:

1. **Extract Accuracy:** Retrieve the accuracy value (percentage) achieved by the model and store it in a separate variable named `accuracy`.

2. **Dataset Size:**  Determine the number of images used in the dataset and save it to a variable called `datasetSize`.

3. **Convert Training Time:** Convert the training time from seconds to minutes and store the result in a variable named `trainingTimeMinutes`.

4. **Add New Result:** Append a new result object to the "results" array with the following information:
    -  `benchmarkId`: "bench_00001" 
    -  `timestamp`: Set the timestamp to the current date and time using your programming language's built-in datetime functionality.

5. **New Parameter Value:** In the newly added result, include a new parameter called `"Inference Time"` with a value of `200` milliseconds (`ms`) as its unit.


