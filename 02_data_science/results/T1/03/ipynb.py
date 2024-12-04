

import pandas as pd

# Load the data
data_path = 'wiki4he/wiki4HE.csv'
df = pd.read_csv(data_path)

# Display the first few rows of the DataFrame
df.head()

# Load the data with the correct delimiter
df = pd.read_csv(data_path, delimiter=';')

# Display the first few rows of the DataFrame
df.head()

import matplotlib.pyplot as plt
import seaborn as sns

# Set the style for the plots
sns.set(style="whitegrid")

# Plot the distribution of age
plt.figure(figsize=(10, 6))
sns.histplot(df['AGE'], bins=10, kde=True)
plt.title('Distribution of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Plot the distribution of years of experience
plt.figure(figsize=(10, 6))
sns.histplot(df['YEARSEXP'], bins=10, kde=True)
plt.title('Distribution of Years of Experience')
plt.xlabel('Years of Experience')
plt.ylabel('Frequency')
plt.show()

# Plot the distribution of domain/field of expertise
plt.figure(figsize=(10, 6))
sns.countplot(x='DOMAIN', data=df)
plt.title('Distribution of Domain/Field of Expertise')
plt.xlabel('Domain')
plt.ylabel('Frequency')
plt.show()

# Plot the distribution of job position
plt.figure(figsize=(10, 6))
sns.countplot(x='UOC_POSITION', data=df)
plt.title('Distribution of Job Position')
plt.xlabel('Job Position')
plt.ylabel('Frequency')
plt.show()

# Extract the columns related to survey questions
survey_columns = df.columns[10:]

# Calculate the percentage of extreme responses (1 or 5) for each question
extreme_responses = df[survey_columns].apply(lambda x: (x == 1).sum() + (x == 5).sum()) / len(df) * 100

# Identify the questions with a majority of extreme responses (more than 50%)
extreme_responses_majority = extreme_responses[extreme_responses > 50]

extreme_responses_majority

# Extract relevant columns for consulting and citing Wikipedia
consult_wiki_columns = ['Use1', 'Use2', 'Use3', 'Use4', 'Use5']
cite_wiki_columns = ['Qu1', 'Qu2', 'Qu3', 'Qu4', 'Qu5']

# Calculate the mean response for consulting Wikipedia for each domain
consult_wiki_mean = df.groupby('DOMAIN')[consult_wiki_columns].mean().mean(axis=1)

# Calculate the mean response for citing Wikipedia for each domain
cite_wiki_mean = df.groupby('DOMAIN')[cite_wiki_columns].mean().mean(axis=1)

# Combine the results into a single DataFrame
wiki_usage = pd.DataFrame({
    'Consult Wikipedia': consult_wiki_mean,
    'Cite Wikipedia': cite_wiki_mean
}).reset_index()

wiki_usage

# Convert relevant columns to numeric, coercing errors to NaN
df[consult_wiki_columns + cite_wiki_columns] = df[consult_wiki_columns + cite_wiki_columns].apply(pd.to_numeric, errors='coerce')

# Calculate the mean response for consulting Wikipedia for each domain
consult_wiki_mean = df.groupby('DOMAIN')[consult_wiki_columns].mean().mean(axis=1)

# Calculate the mean response for citing Wikipedia for each domain
cite_wiki_mean = df.groupby('DOMAIN')[cite_wiki_columns].mean().mean(axis=1)

# Combine the results into a single DataFrame
wiki_usage = pd.DataFrame({
    'Consult Wikipedia': consult_wiki_mean,
    'Cite Wikipedia': cite_wiki_mean
}).reset_index()

wiki_usage

# Plot the mean responses for consulting and citing Wikipedia for each domain
plt.figure(figsize=(12, 6))
sns.barplot(x='DOMAIN', y='Consult Wikipedia', data=wiki_usage, color='blue', label='Consult Wikipedia')
sns.barplot(x='DOMAIN', y='Cite Wikipedia', data=wiki_usage, color='red', label='Cite Wikipedia', alpha=0.6)
plt.title('Consulting and Citing Wikipedia by Domain')
plt.xlabel('Domain')
plt.ylabel('Mean Response')
plt.legend()
plt.show()

