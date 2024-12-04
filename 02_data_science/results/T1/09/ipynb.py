

import pandas as pd

# Load the dataset
data = pd.read_csv('wiki4HE.csv')

# Display the first few rows of the dataset
data.head()

# Load the dataset with the correct delimiter
data = pd.read_csv('wiki4HE.csv', delimiter=';')

# Display the first few rows of the dataset
data.head()

# Overview of respondents' demographics
demographics_summary = {
    'Age': data['AGE'].describe(),
    'Years of Experience': data['YEARSEXP'].describe(),
    'Domain': data['DOMAIN'].value_counts(),
    'Job Position': data['UOC_POSITION'].value_counts()
}

demographics_summary

# Identify columns that correspond to survey questions
# Assuming questions are labeled as Qu1, Qu2, Qu3, Qu4, Qu5, etc.
question_columns = [col for col in data.columns if col.startswith('Qu')]

# Count extreme responses (1 and 5) for each question
extreme_counts = {
    'Question': [],
    'Count of 1s': [],
    'Count of 5s': [],
    'Total Responses': [],
    'Percentage of Extremes': []
}

for question in question_columns:
    count_1 = (data[question] == 1).sum()
    count_5 = (data[question] == 5).sum()
    total_responses = count_1 + count_5
    if total_responses > 0:
        extreme_counts['Question'].append(question)
        extreme_counts['Count of 1s'].append(count_1)
        extreme_counts['Count of 5s'].append(count_5)
        extreme_counts['Total Responses'].append(total_responses)
        extreme_counts['Percentage of Extremes'].append((total_responses / len(data)) * 100)

# Convert to DataFrame for better visualization
extreme_counts_df = pd.DataFrame(extreme_counts)

# Filter for questions with a majority of extreme responses (more than 50%)
majority_extreme_responses = extreme_counts_df[extreme_counts_df['Percentage of Extremes'] > 50]

majority_extreme_responses

# Identify columns related to Wikipedia usage
usage_columns = [col for col in data.columns if col.startswith('Use')]

# Display the usage columns
usage_columns

# Group by domain and calculate the average usage of Wikipedia
domain_usage = data.groupby('DOMAIN')[usage_columns].mean()

# Calculate the average citation of Wikipedia in academic papers
domain_usage['Average UserWiki'] = data.groupby('DOMAIN')['USERWIKI'].mean()

# Display the results
domain_usage

# Convert usage columns to numeric, forcing errors to NaN
for col in usage_columns:
    data[col] = pd.to_numeric(data[col], errors='coerce')

# Group by domain and calculate the average usage of Wikipedia
domain_usage = data.groupby('DOMAIN')[usage_columns].mean()

# Calculate the average citation of Wikipedia in academic papers
domain_usage['Average UserWiki'] = data.groupby('DOMAIN')['USERWIKI'].mean()

# Display the results
domain_usage

# Convert USERWIKI column to numeric, forcing errors to NaN
data['USERWIKI'] = pd.to_numeric(data['USERWIKI'], errors='coerce')

# Group by domain and calculate the average usage of Wikipedia
domain_usage = data.groupby('DOMAIN')[usage_columns].mean()

# Calculate the average citation of Wikipedia in academic papers
domain_usage['Average UserWiki'] = data.groupby('DOMAIN')['USERWIKI'].mean()

# Display the results
domain_usage

