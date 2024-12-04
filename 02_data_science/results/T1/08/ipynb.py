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

# Plotting Domain Count
plt.figure(figsize=(12, 6))
sns.countplot(data=data, x='DOMAIN', order=data['DOMAIN'].value_counts().index)
plt.title('Distribution of Domains among Respondents')
plt.xlabel('Domain')
plt.ylabel('Number of Respondents')
plt.xticks(rotation=45)
plt.grid()
plt.show()

# Plotting Job Position Count
plt.figure(figsize=(12, 6))
sns.countplot(data=data, x='UOC_POSITION', order=data['UOC_POSITION'].value_counts().index)
plt.title('Distribution of Job Positions among Respondents')
plt.xlabel('Job Position')
plt.ylabel('Number of Respondents')
plt.xticks(rotation=45)
plt.grid()
plt.show()

# Identifying Likert scale response columns
likert_columns = [
    'PU1', 'PU2', 'PU3', 'PEU1', 'PEU2', 'PEU3',
    'ENJ1', 'ENJ2', 'Qu1', 'Qu2', 'Qu3', 'Qu4', 'Qu5',
    'Vis1', 'Vis2', 'Vis3', 'Im1', 'Im2', 'Im3',
    'SA1', 'SA2', 'SA3', 'Use1', 'Use2', 'Use3', 'Use4', 'Use5',
    'Pf1', 'Pf2', 'Pf3', 'JR1', 'JR2', 'BI1', 'BI2',
    'Inc1', 'Inc2', 'Inc3', 'Inc4', 'Exp1', 'Exp2', 'Exp3', 'Exp4', 'Exp5'
]

# Calculating the percentage of extreme responses (1 and 5) for each Likert scale question
extreme_responses = data[likert_columns].apply(lambda x: (x == 1).sum() + (x == 5).sum(), axis=0) / len(data) * 100

# Identifying questions with majority extreme responses (more than 50%)
extreme_questions = extreme_responses[extreme_responses > 50]

extreme_questions.sort_values(ascending=False)

# Analyzing Wikipedia usage by domain
# Assuming 'Use1' to 'Use5' represent the frequency of Wikipedia usage for issues related to their field of expertise
usage_columns = ['Use1', 'Use2', 'Use3', 'Use4', 'Use5']

# Calculating the average usage of Wikipedia by domain
domain_usage = data.groupby('DOMAIN')[usage_columns].mean()

# Calculating the average usage across all domains
average_usage = domain_usage.mean(axis=1)

# Adding the average usage to the domain_usage DataFrame
domain_usage['Average Usage'] = average_usage

# Sorting the domains by average usage
sorted_domain_usage = domain_usage['Average Usage'].sort_values(ascending=False)

sorted_domain_usage

# Convert usage columns to numeric, forcing errors to NaN
data[usage_columns] = data[usage_columns].apply(pd.to_numeric, errors='coerce')

# Recalculating the average usage of Wikipedia by domain
domain_usage = data.groupby('DOMAIN')[usage_columns].mean()

# Calculating the average usage across all domains
average_usage = domain_usage.mean(axis=1)

# Adding the average usage to the domain_usage DataFrame
domain_usage['Average Usage'] = average_usage

# Sorting the domains by average usage
sorted_domain_usage = domain_usage['Average Usage'].sort_values(ascending=False)

sorted_domain_usage

# Searching for keywords related to citations in the dataset
search_terms = ['cite', 'citation', 'refer', 'reference']
search_results = {term: data.filter(like=term).columns.tolist() for term in search_terms}
search_results

