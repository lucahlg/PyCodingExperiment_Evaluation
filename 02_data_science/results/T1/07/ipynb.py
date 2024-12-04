

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
    'Domain Count': data['DOMAIN'].value_counts(),
    'Job Position Count': data['UOC_POSITION'].value_counts()
}

# Plotting Age Distribution
plt.figure(figsize=(12, 6))
sns.histplot(data['AGE'], bins=10, kde=True)
plt.title('Age Distribution of Respondents')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid()
plt.show()

# Plotting Years of Experience Distribution
plt.figure(figsize=(12, 6))
sns.histplot(data['YEARSEXP'], bins=10, kde=True)
plt.title('Years of Experience Distribution of Respondents')
plt.xlabel('Years of Experience')
plt.ylabel('Frequency')
plt.grid()
plt.show()

demographics_summary

# Identify Likert scale response columns (assuming they start from 'PU1' to 'SA3' based on the dataset structure)
likert_columns = [
    'PU1', 'PU2', 'PU3', 'PEU1', 'PEU2', 'PEU3',
    'ENJ1', 'ENJ2', 'Qu1', 'Qu2', 'Qu3', 'Qu4', 'Qu5',
    'Vis1', 'Vis2', 'Vis3', 'Im1', 'Im2', 'Im3',
    'SA1', 'SA2', 'SA3', 'Use1', 'Use2', 'Use3', 'Use4', 'Use5',
    'Pf1', 'Pf2', 'Pf3', 'JR1', 'JR2', 'BI1', 'BI2',
    'Inc1', 'Inc2', 'Inc3', 'Inc4', 'Exp1', 'Exp2', 'Exp3', 'Exp4', 'Exp5'
]

# Calculate the percentage of extreme responses (1 or 5) for each question
extreme_responses = data[likert_columns].apply(lambda x: (x.isin([1, 5]).sum() / len(x)) * 100)

# Filter questions with more than 50% extreme responses
extreme_questions = extreme_responses[extreme_responses > 50]

extreme_questions

# Group by DOMAIN and calculate the percentage of users who consult Wikipedia
domain_wiki_usage = data.groupby('DOMAIN')['USERWIKI'].value_counts(normalize=True).unstack().fillna(0) * 100

# Extract the percentage of users who consult Wikipedia (USERWIKI = 1)
domain_wiki_usage = domain_wiki_usage[1]

# Plotting the results
plt.figure(figsize=(12, 6))
domain_wiki_usage.sort_values().plot(kind='barh', color='skyblue')
plt.title('Percentage of Respondents Consulting Wikipedia by Domain')
plt.xlabel('Percentage of Users Consulting Wikipedia')
plt.ylabel('Domain')
plt.grid(axis='x')
plt.show()

# Display the domain usage data
domain_wiki_usage

# Check the unique values in the USERWIKI column
unique_userwiki_values = data['USERWIKI'].unique()
unique_userwiki_values

# Convert USERWIKI to numeric, replacing '?' with NaN
data['USERWIKI'] = pd.to_numeric(data['USERWIKI'], errors='coerce')

# Group by DOMAIN and calculate the percentage of users who consult Wikipedia
domain_wiki_usage = data.groupby('DOMAIN')['USERWIKI'].value_counts(normalize=True).unstack().fillna(0) * 100

# Extract the percentage of users who consult Wikipedia (USERWIKI = 1)
domain_wiki_usage = domain_wiki_usage[1]

# Plotting the results
plt.figure(figsize=(12, 6))
domain_wiki_usage.sort_values().plot(kind='barh', color='skyblue')
plt.title('Percentage of Respondents Consulting Wikipedia by Domain')
plt.xlabel('Percentage of Users Consulting Wikipedia')
plt.ylabel('Domain')
plt.grid(axis='x')
plt.show()

# Display the domain usage data
domain_wiki_usage

# Search for columns related to citation practices in the dataset
citation_columns = [col for col in data.columns if 'cite' in col.lower() or 'reference' in col.lower() or 'citation' in col.lower()]
citation_columns

