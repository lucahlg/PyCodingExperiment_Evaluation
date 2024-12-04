

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

# Summary of demographics
demographics_summary = {
    'Age': data['AGE'].describe(),
    'Years of Experience': data['YEARSEXP'].describe(),
    'Domain': data['DOMAIN'].value_counts(),
    'Job Position': data['UOC_POSITION'].value_counts()
}

demographics_summary

import matplotlib.pyplot as plt
import seaborn as sns

# Set the style for the plots
sns.set(style="whitegrid")

# Create a figure with subplots
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Histogram for Age
sns.histplot(data['AGE'], bins=20, ax=axes[0, 0], kde=True)
axes[0, 0].set_title('Age Distribution')
axes[0, 0].set_xlabel('Age')
axes[0, 0].set_ylabel('Frequency')

# Bar chart for Domain
sns.barplot(x=demographics_summary['Domain'].index, y=demographics_summary['Domain'].values, ax=axes[0, 1])
axes[0, 1].set_title('Number of Respondents by Domain')
axes[0, 1].set_xlabel('Domain')
axes[0, 1].set_ylabel('Number of Respondents')

# Bar chart for Job Position
sns.barplot(x=demographics_summary['Job Position'].index, y=demographics_summary['Job Position'].values, ax=axes[1, 0])
axes[1, 0].set_title('Number of Respondents by Job Position')
axes[1, 0].set_xlabel('Job Position')
axes[1, 0].set_ylabel('Number of Respondents')

# Hide the last subplot (not used)
axes[1, 1].axis('off')

# Adjust layout
plt.tight_layout()
plt.show()

# Display the columns to identify survey questions
data.columns.tolist()

# Define a function to calculate extreme response percentages
def extreme_response_percentage(column):
    return (column.isin([1, 5]).sum() / column.count()) * 100

# Calculate extreme response percentages for relevant columns
extreme_responses = {
    col: extreme_response_percentage(data[col]) for col in data.columns if col.startswith(('PU', 'PEU', 'ENJ', 'Qu', 'Vis', 'Im', 'SA', 'Use', 'Pf', 'JR', 'BI', 'Inc', 'Exp'))
}

# Convert to DataFrame for easier visualization
extreme_responses_df = pd.DataFrame(extreme_responses.items(), columns=['Question', 'Extreme Response Percentage'])
extreme_responses_df = extreme_responses_df.sort_values(by='Extreme Response Percentage', ascending=False)

extreme_responses_df

# Check the columns related to Wikipedia usage
wikipedia_usage_columns = ['Use1', 'Use2', 'Use3', 'Use4', 'Use5']
domain_usage = data.groupby('DOMAIN')[wikipedia_usage_columns].mean()

# Calculate the average usage of Wikipedia for each domain
domain_usage['Average Usage'] = domain_usage.mean(axis=1)

# Sort by average usage
domain_usage_sorted = domain_usage[['Average Usage']].sort_values(by='Average Usage', ascending=False)

domain_usage_sorted

# Check the data types of the Wikipedia usage columns
data[wikipedia_usage_columns].dtypes

# Convert the Wikipedia usage columns to numeric, coercing errors to NaN
data[wikipedia_usage_columns] = data[wikipedia_usage_columns].apply(pd.to_numeric, errors='coerce')

# Now, calculate the average usage of Wikipedia for each domain again
domain_usage = data.groupby('DOMAIN')[wikipedia_usage_columns].mean()

# Calculate the average usage across the usage columns
domain_usage['Average Usage'] = domain_usage.mean(axis=1)

# Sort by average usage
domain_usage_sorted = domain_usage[['Average Usage']].sort_values(by='Average Usage', ascending=False)

domain_usage_sorted

