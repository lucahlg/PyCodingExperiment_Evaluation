You are a data scientist tasked with analyzing and performing different operations on a dataset. 

<Project>
The UC Irvine Machine Learning Repository includes a dataset [Cardoso 2014] of the annual spending of clients of a wholesale distributor on diverse product categories. The dataset is available at https://archive.ics.uci.edu/static/public/292/wholesale+customers.zip.
</Project>
<Tasks>
Write a computer program that will:
- load the dataset and drop the Region column,
- filter the data records for clients that are restaurants, hotels, and cafés (i.e., drop clients from retail),
- normalize the data by computing the proportionate spending per product category (i.e., each row in the data table sums to one),
- standardize the data,
- use K-means to cluster the distributor’s customers based on those data into K = 4 groups,
- print the cluster centroids.
Offer a short description of each group of clients based on their annual spending across product categories.
</Tasks>
