<instructions>
You are a data science student. You will be given a data science related task that you need solve task by task.
</instructions>
<title> Customer segmentation </title>
<introduction>
The UC Irvine Machine Learning Repository includes a dataset of the annual spending of clients of a wholesale distributor on diverse product categories: https://archive.ics.uci.edu/static/public/292/wholesale+customers.zip
More information about the dataset and its attributes can be found at https://archive.ics.uci.edu/dataset/292/wholesale+customers
</introduction>
<task 1> load the dataset and drop the Region column </task 1>
<task 2> filter the data records for clients that are restaurants, hotels, and cafés (i.e., drop clients from retail) </task 2>
<task 3> normalize the data by computing the proportionate spending per product category (i.e., each row in the data table sums to one) </task 3>
<task 4> standardize the data </task 4>
<task 5> use K-means to cluster the distributor’s customers based on those data into K = 4 groups </task 5>
<task 6> print and visualize the cluster centroids </task 6>
<task 7> Offer a short description of each group of clients based on their annual spending across product categories </task 7>