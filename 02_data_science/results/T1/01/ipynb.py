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

# Summary statistics for age and years of experience
age_summary = df['AGE'].describe()
yearsexp_summary = df['YEARSEXP'].describe()

# Plotting the distribution of age
plt.figure(figsize=(10, 5))
sns.histplot(df['AGE'], bins=10, kde=True)
plt.title('Distribution of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Plotting the distribution of years of experience
plt.figure(figsize=(10, 5))
sns.histplot(df['YEARSEXP'], bins=10, kde=True)
plt.title('Distribution of Years of Experience')
plt.xlabel('Years of Experience')
plt.ylabel('Frequency')
plt.show()

# Plotting the distribution of domain/field of expertise
plt.figure(figsize=(10, 5))
sns.countplot(x='DOMAIN', data=df)
plt.title('Distribution of Domain/Field of Expertise')
plt.xlabel('Domain')
plt.ylabel('Count')
plt.show()

# Plotting the distribution of job position
plt.figure(figsize=(10, 5))
sns.countplot(x='UOC_POSITION', data=df)
plt.title('Distribution of Job Position')
plt.xlabel('Job Position')
plt.ylabel('Count')
plt.show()

age_summary, yearsexp_summary

# Extracting the columns related to survey questions
survey_columns = df.columns[10:]

# Calculating the percentage of extreme responses (1 or 5) for each question
extreme_responses = df[survey_columns].apply(lambda x: (x == 1).sum() + (x == 5).sum()) / len(df) * 100

# Plotting the percentage of extreme responses for each question
plt.figure(figsize=(15, 8))
extreme_responses.sort_values(ascending=False).plot(kind='bar')
plt.title('Percentage of Extreme Responses (1 or 5) for Each Survey Question')
plt.xlabel('Survey Question')
plt.ylabel('Percentage of Extreme Responses')
plt.show()

extreme_responses

# Analyzing the usage of Wikipedia across different domains
domain_wiki_usage = df.groupby('DOMAIN')['USERWIKI'].mean() * 100

# Plotting the usage of Wikipedia across different domains
plt.figure(figsize=(15, 8))
domain_wiki_usage.sort_values(ascending=False).plot(kind='bar')
plt.title('Percentage of Respondents Using Wikipedia by Domain')
plt.xlabel('Domain')
plt.ylabel('Percentage of Respondents Using Wikipedia')
plt.show()

# Analyzing the practice of citing Wikipedia in academic papers
# Assuming 'Qu5' represents the practice of citing Wikipedia in academic papers
domain_wiki_citing = df.groupby('DOMAIN')['Qu5'].mean()

# Plotting the practice of citing Wikipedia in academic papers across different domains
plt.figure(figsize=(15, 8))
domain_wiki_citing.sort_values(ascending=False).plot(kind='bar')
plt.title('Average Likert Scale Response for Citing Wikipedia in Academic Papers by Domain')
plt.xlabel('Domain')
plt.ylabel('Average Likert Scale Response')
plt.show()

domain_wiki_usage, domain_wiki_citing

# Convert USERWIKI column to numeric
df['USERWIKI'] = pd.to_numeric(df['USERWIKI'], errors='coerce')

# Analyzing the usage of Wikipedia across different domains
domain_wiki_usage = df.groupby('DOMAIN')['USERWIKI'].mean() * 100

# Plotting the usage of Wikipedia across different domains
plt.figure(figsize=(15, 8))
domain_wiki_usage.sort_values(ascending=False).plot(kind='bar')
plt.title('Percentage of Respondents Using Wikipedia by Domain')
plt.xlabel('Domain')
plt.ylabel('Percentage of Respondents Using Wikipedia')
plt.show()

# Analyzing the practice of citing Wikipedia in academic papers
# Assuming 'Qu5' represents the practice of citing Wikipedia in academic papers
df['Qu5'] = pd.to_numeric(df['Qu5'], errors='coerce')
domain_wiki_citing = df.groupby('DOMAIN')['Qu5'].mean()

# Plotting the practice of citing Wikipedia in academic papers across different domains
plt.figure(figsize=(15, 8))
domain_wiki_citing.sort_values(ascending=False).plot(kind='bar')
plt.title('Average Likert Scale Response for Citing Wikipedia in Academic Papers by Domain')
plt.xlabel('Domain')
plt.ylabel('Average Likert Scale Response')
plt.show()

domain_wiki_usage, domain_wiki_citing

