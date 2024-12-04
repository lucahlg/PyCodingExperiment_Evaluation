import pandas as pd

# Load the data
file_path = 'wiki4he/wiki4HE.csv'
data = pd.read_csv(file_path)

# Display the first few rows of the dataset
data.head()

# Load the data with the correct delimiter
data = pd.read_csv(file_path, delimiter=';')

# Display the first few rows of the dataset
data.head()

import matplotlib.pyplot as plt
import seaborn as sns

# Set up the plotting environment
sns.set(style="whitegrid")

# Age distribution
plt.figure(figsize=(10, 6))
sns.histplot(data['AGE'], bins=10, kde=True)
plt.title('Age Distribution of Respondents')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Years of experience distribution
plt.figure(figsize=(10, 6))
sns.histplot(data['YEARSEXP'], bins=10, kde=True)
plt.title('Years of Experience Distribution of Respondents')
plt.xlabel('Years of Experience')
plt.ylabel('Frequency')
plt.show()

# Domain/Field of expertise distribution
plt.figure(figsize=(10, 6))
sns.countplot(y='DOMAIN', data=data, order=data['DOMAIN'].value_counts().index)
plt.title('Domain/Field of Expertise Distribution of Respondents')
plt.xlabel('Count')
plt.ylabel('Domain')
plt.show()

# Job position distribution
plt.figure(figsize=(10, 6))
sns.countplot(y='UOC_POSITION', data=data, order=data['UOC_POSITION'].value_counts().index)
plt.title('Job Position Distribution of Respondents')
plt.xlabel('Count')
plt.ylabel('Job Position')
plt.show()

# Extract columns related to survey questions
survey_columns = data.columns[10:]

# Calculate the percentage of extreme responses (1 or 5) for each question
extreme_responses = data[survey_columns].apply(lambda x: (x == 1).sum() + (x == 5).sum()) / len(data) * 100

# Identify questions with a majority of extreme responses
majority_extreme_responses = extreme_responses[extreme_responses > 50]

majority_extreme_responses

# Relevant columns for consulting Wikipedia and citing Wikipedia
consult_wikipedia_col = 'USERWIKI'
cite_wikipedia_cols = ['Qu1', 'Qu2', 'Qu3', 'Qu4', 'Qu5']

# Calculate the average consultation of Wikipedia by domain
consult_wikipedia_by_domain = data.groupby('DOMAIN')[consult_wikipedia_col].mean()

# Calculate the average citation of Wikipedia by domain
cite_wikipedia_by_domain = data.groupby('DOMAIN')[cite_wikipedia_cols].mean().mean(axis=1)

consult_wikipedia_by_domain, cite_wikipedia_by_domain

# Convert relevant columns to numeric, coercing errors to NaN
data[consult_wikipedia_col] = pd.to_numeric(data[consult_wikipedia_col], errors='coerce')
data[cite_wikipedia_cols] = data[cite_wikipedia_cols].apply(pd.to_numeric, errors='coerce')

# Calculate the average consultation of Wikipedia by domain
consult_wikipedia_by_domain = data.groupby('DOMAIN')[consult_wikipedia_col].mean()

# Calculate the average citation of Wikipedia by domain
cite_wikipedia_by_domain = data.groupby('DOMAIN')[cite_wikipedia_cols].mean().mean(axis=1)

consult_wikipedia_by_domain, cite_wikipedia_by_domain

