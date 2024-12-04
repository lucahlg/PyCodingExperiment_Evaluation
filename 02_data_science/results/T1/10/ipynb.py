import pandas as pd

# Load the data
data_path = 'wiki4he_data/wiki4HE.csv'
data = pd.read_csv(data_path)

# Display the first few rows of the dataset
data.head()

# Load the data with the correct delimiter
data = pd.read_csv(data_path, delimiter=';')

# Display the first few rows of the dataset
data.head()

import matplotlib.pyplot as plt
import seaborn as sns

# Set the style for the plots
sns.set(style="whitegrid")

# Overview of demographics
demographics_summary = {
    'Age': data['AGE'].describe(),
    'Years of Experience': data['YEARSEXP'].describe(),
    'Domain': data['DOMAIN'].value_counts(),
    'Job Position': data['UOC_POSITION'].value_counts()
}

# Plotting Age distribution
plt.figure(figsize=(12, 6))
sns.histplot(data['AGE'], bins=10, kde=True)
plt.title('Age Distribution of Respondents')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid()
plt.show()

# Plotting Years of Experience distribution
plt.figure(figsize=(12, 6))
sns.histplot(data['YEARSEXP'], bins=10, kde=True)
plt.title('Years of Experience Distribution of Respondents')
plt.xlabel('Years of Experience')
plt.ylabel('Frequency')
plt.grid()
plt.show()

demographics_summary

# Identify the columns that correspond to survey questions
survey_columns = data.columns[10:]  # Assuming the first 10 columns are demographic data

# Count extreme responses (1 and 5) for each question
extreme_responses = data[survey_columns].apply(lambda x: (x == 1).sum() + (x == 5).sum())

# Filter questions with a majority of extreme responses (more than 50%)
majority_extreme_responses = extreme_responses[extreme_responses > (len(data) / 2)]

majority_extreme_responses

# Check the relevant columns for Wikipedia usage and domain
# Assuming 'Use1' to 'Use5' columns represent the usage of Wikipedia in their field
wikipedia_usage_columns = ['Use1', 'Use2', 'Use3', 'Use4', 'Use5']
domain_column = 'DOMAIN'

# Calculate the average Wikipedia usage per domain
wikipedia_usage_per_domain = data.groupby(domain_column)[wikipedia_usage_columns].mean()

# Calculate the average citation of Wikipedia in academic papers (assuming 'Pf1', 'Pf2', 'Pf3' are relevant)
citation_columns = ['Pf1', 'Pf2', 'Pf3']
citation_per_domain = data.groupby(domain_column)[citation_columns].mean()

# Combine the results into a single DataFrame for comparison
comparison_df = pd.DataFrame({
    'Average Wikipedia Usage': wikipedia_usage_per_domain.mean(axis=1),
    'Average Citation': citation_per_domain.mean(axis=1)
})

comparison_df = comparison_df.sort_values(by='Average Wikipedia Usage', ascending=False)
comparison_df

# Check the data types of the relevant columns
data[wikipedia_usage_columns + citation_columns].dtypes

# Redefine the relevant columns for Wikipedia usage and citations
wikipedia_usage_columns = ['Use1', 'Use2', 'Use3', 'Use4', 'Use5']
citation_columns = ['Pf1', 'Pf2', 'Pf3']

# Check the data types of the relevant columns
data[wikipedia_usage_columns + citation_columns].dtypes

# Convert the relevant columns to numeric, coercing errors to NaN
data[wikipedia_usage_columns] = data[wikipedia_usage_columns].apply(pd.to_numeric, errors='coerce')
data[citation_columns] = data[citation_columns].apply(pd.to_numeric, errors='coerce')

# Calculate the average Wikipedia usage per domain
wikipedia_usage_per_domain = data.groupby(domain_column)[wikipedia_usage_columns].mean()

# Calculate the average citation of Wikipedia in academic papers
citation_per_domain = data.groupby(domain_column)[citation_columns].mean()

# Combine the results into a single DataFrame for comparison
comparison_df = pd.DataFrame({
    'Average Wikipedia Usage': wikipedia_usage_per_domain.mean(axis=1),
    'Average Citation': citation_per_domain.mean(axis=1)
})

comparison_df = comparison_df.sort_values(by='Average Wikipedia Usage', ascending=False)
comparison_df

