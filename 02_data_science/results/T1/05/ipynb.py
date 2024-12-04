

import pandas as pd

# Load the dataset
file_path = 'wiki4he/wiki4HE.csv'
data = pd.read_csv(file_path)

# Display the first few rows of the dataset
data.head()

# Load the dataset with the correct delimiter
data = pd.read_csv(file_path, delimiter=';')

# Display the first few rows of the dataset
data.head()

import matplotlib.pyplot as plt

# Summary statistics for age and years of experience
age_summary = data['AGE'].describe()
years_exp_summary = data['YEARSEXP'].describe()

# Count of respondents by domain
domain_counts = data['DOMAIN'].value_counts()

# Count of respondents by job position
job_position_counts = data['UOC_POSITION'].value_counts()

# Plotting the demographic information
fig, axs = plt.subplots(2, 2, figsize=(15, 10))

# Age distribution
axs[0, 0].hist(data['AGE'], bins=10, color='skyblue', edgecolor='black')
axs[0, 0].set_title('Age Distribution')
axs[0, 0].set_xlabel('Age')
axs[0, 0].set_ylabel('Frequency')

# Years of experience distribution
axs[0, 1].hist(data['YEARSEXP'], bins=10, color='lightgreen', edgecolor='black')
axs[0, 1].set_title('Years of Experience Distribution')
axs[0, 1].set_xlabel('Years of Experience')
axs[0, 1].set_ylabel('Frequency')

# Domain distribution
domain_counts.plot(kind='bar', ax=axs[1, 0], color='salmon', edgecolor='black')
axs[1, 0].set_title('Domain Distribution')
axs[1, 0].set_xlabel('Domain')
axs[1, 0].set_ylabel('Frequency')

# Job position distribution
job_position_counts.plot(kind='bar', ax=axs[1, 1], color='lightcoral', edgecolor='black')
axs[1, 1].set_title('Job Position Distribution')
axs[1, 1].set_xlabel('Job Position')
axs[1, 1].set_ylabel('Frequency')

plt.tight_layout()
plt.show()

age_summary, years_exp_summary, domain_counts, job_position_counts

# Identify columns corresponding to survey questions
survey_columns = data.columns[10:]  # Survey questions start from the 11th column

# Calculate the proportion of extreme responses (1 or 5) for each question
extreme_responses = {}
for col in survey_columns:
    extreme_count = data[col].value_counts().get(1, 0) + data[col].value_counts().get(5, 0)
    extreme_proportion = extreme_count / len(data)
    extreme_responses[col] = extreme_proportion

# Sort the questions by the proportion of extreme responses
sorted_extreme_responses = sorted(extreme_responses.items(), key=lambda x: x[1], reverse=True)
sorted_extreme_responses

# List all column names to identify relevant columns
data.columns.tolist()

# Calculate the average response for consulting Wikipedia (Use1) and citing Wikipedia (Use2) by domain
consult_wikipedia_by_domain = data.groupby('DOMAIN')['Use1'].mean()
cite_wikipedia_by_domain = data.groupby('DOMAIN')['Use2'].mean()

consult_wikipedia_by_domain, cite_wikipedia_by_domain

# Check unique values in Use1 and Use2 columns
use1_unique_values = data['Use1'].unique()
use2_unique_values = data['Use2'].unique()

use1_unique_values, use2_unique_values

import numpy as np

# Replace '?' with NaN
data['Use1'] = data['Use1'].replace('?', np.nan).astype(float)
data['Use2'] = data['Use2'].replace('?', np.nan).astype(float)

# Calculate the average response for consulting Wikipedia (Use1) and citing Wikipedia (Use2) by domain
consult_wikipedia_by_domain = data.groupby('DOMAIN')['Use1'].mean()
cite_wikipedia_by_domain = data.groupby('DOMAIN')['Use2'].mean()

consult_wikipedia_by_domain, cite_wikipedia_by_domain

fig, axs = plt.subplots(1, 2, figsize=(15, 5))

# Plotting the average response for consulting Wikipedia by domain
consult_wikipedia_by_domain.plot(kind='bar', ax=axs[0], color='skyblue', edgecolor='black')
axs[0].set_title('Average Response for Consulting Wikipedia by Domain')
axs[0].set_xlabel('Domain')
axs[0].set_ylabel('Average Response')
axs[0].set_ylim(0, 5)

# Plotting the average response for citing Wikipedia by domain
cite_wikipedia_by_domain.plot(kind='bar', ax=axs[1], color='lightgreen', edgecolor='black')
axs[1].set_title('Average Response for Citing Wikipedia by Domain')
axs[1].set_xlabel('Domain')
axs[1].set_ylabel('Average Response')
axs[1].set_ylim(0, 5)

plt.tight_layout()
plt.show()

