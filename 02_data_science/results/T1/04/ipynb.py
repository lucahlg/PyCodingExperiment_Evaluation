import pandas as pd

# Load the data
data_path = 'wiki4he/wiki4HE.csv'
df = pd.read_csv(data_path)

# Display the first few rows of the dataframe
df.head()

# Load the data with the correct delimiter
df = pd.read_csv(data_path, delimiter=';')

# Display the first few rows of the dataframe
df.head()

import matplotlib.pyplot as plt
import seaborn as sns

# Set up the plotting environment
sns.set(style="whitegrid")

# Age distribution
plt.figure(figsize=(10, 6))
sns.histplot(df['AGE'], bins=10, kde=True)
plt.title('Age Distribution of Respondents')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Years of experience distribution
plt.figure(figsize=(10, 6))
sns.histplot(df['YEARSEXP'], bins=10, kde=True)
plt.title('Years of Experience Distribution of Respondents')
plt.xlabel('Years of Experience')
plt.ylabel('Frequency')
plt.show()

# Domain/Field of expertise distribution
plt.figure(figsize=(10, 6))
sns.countplot(y='DOMAIN', data=df, order=df['DOMAIN'].value_counts().index)
plt.title('Domain/Field of Expertise Distribution of Respondents')
plt.xlabel('Count')
plt.ylabel('Domain')
plt.show()

# Job position distribution
plt.figure(figsize=(10, 6))
sns.countplot(y='UOC_POSITION', data=df, order=df['UOC_POSITION'].value_counts().index)
plt.title('Job Position Distribution of Respondents')
plt.xlabel('Count')
plt.ylabel('Job Position')
plt.show()

# Extract the columns related to survey questions
survey_columns = df.columns[10:]

# Calculate the percentage of extreme responses (1 or 5) for each question
extreme_responses = df[survey_columns].apply(lambda x: (x == 1).sum() + (x == 5).sum()) / len(df) * 100

# Filter questions with a majority of extreme responses (more than 50%)
majority_extreme_responses = extreme_responses[extreme_responses > 50]

majority_extreme_responses

# Calculate the mean response for consulting Wikipedia (USERWIKI) by domain
consult_wiki_by_domain = df.groupby('DOMAIN')['USERWIKI'].mean()

# Calculate the mean response for citing Wikipedia in academic papers (Qu5) by domain
cite_wiki_by_domain = df.groupby('DOMAIN')['Qu5'].mean()

consult_wiki_by_domain, cite_wiki_by_domain

# Inspect the data types of the columns
df[['USERWIKI', 'Qu5']].dtypes

# Convert USERWIKI and Qu5 columns to numeric values
df['USERWIKI'] = pd.to_numeric(df['USERWIKI'], errors='coerce')
df['Qu5'] = pd.to_numeric(df['Qu5'], errors='coerce')

# Calculate the mean response for consulting Wikipedia (USERWIKI) by domain
consult_wiki_by_domain = df.groupby('DOMAIN')['USERWIKI'].mean()

# Calculate the mean response for citing Wikipedia in academic papers (Qu5) by domain
cite_wiki_by_domain = df.groupby('DOMAIN')['Qu5'].mean()

consult_wiki_by_domain, cite_wiki_by_domain

