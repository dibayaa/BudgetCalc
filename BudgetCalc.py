import pandas as pd 
import matplotlib.pyplot as plt

# HOW TO RUN: PLEASE CHECK README ON HOW TO PROPERLY RUN THIS PROJECT
# I STARTED THIS OUT IN VSCODE AND TRIED TO MOVE OVER TO JUPYTER BUT
# HAD PROBLEMS WITH MY MACBOOK CONFIGS SO I JUST FINISHED IT ON COLAB 
# ON GOOGLE 

#Feature: Read data from an external file, such as text, JSON, CSV, etc and use that data in your application
#Feature: Create a dictionary or list, populate it with several values, retrieve at least one value, and use it in your program
#Feature: Visualize data in a graph, chart, or other visual representation of data


#author: @Anthony Dibaya

# read in file
df = pd.read_csv('cashflow.csv', index_col ='Date', 
parse_dates = True)
df.head()

# Avg spending per category
avg_spending_cat = df.groupby('Category').mean().sort_values(by='Amount')
print(avg_spending_cat)

# Sum Expense & Income 
sum_transactions = df.groupby('Transaction Type').sum().sort_values(by='Amount')
print(sum_transactions)

# Calculate Savings (sum column "Amount" to add expenses vs income; positive = savings)
column_name = "Amount"
calc_savings = df[column_name].sum()
print(calc_savings)

fig, ax = plt.subplots()
avg_spending_cat.plot(kind='barh', ax=ax, figsize= (17,6))
ax.set_xlabel('Amount', size=20)
ax.set_ylabel('Category', size=20);

#Organize expenses within categories as "necessary" or "unnecessary" 
expense_type={
    'housing':'necessary',
    'groceries':'necessary',
    'car_insurance':'necessary',
    'phone_bill':'necessary',
    'health_insurance':'necessary',
    'clothing':'unnecessary',
    'debt':'necessary',
    'savings':'necessary',
    'emergency_fund':'necessary',
    'night_out':'unnecessary',
    'gas':'necessary',
    'snacks':'unnecessary',
    'netflix':'unnecessary',
    'stocks':'unnecessary',
    'gym_membership':'unnecessary',
    'phone_apps':'unnecessary',
    'cc_membership':'unnecessary',
    'charity':'unnecessary'
}
df['Expense Type'] = df['Category'].map(expense_type)
df.head()

# Calculate Descriptive Statistics for each expense type (NEEDS WORK)

df.groupby('Expense Type').describe()









