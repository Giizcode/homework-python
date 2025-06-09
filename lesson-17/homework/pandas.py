import pandas as pd
import random
# Step 1: 
data = {
    'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)
# Step 2: 
df.rename(columns=lambda x: x.lower().replace(' ', '_'), inplace=True)
# Step 3: 
print(df.head(3))
# Step 4:
mean_age = df['age'].mean()
print("Mean Age:", mean_age)
# Step 5: 
print(df[['first_name', 'city']])
# Step 6:
df['salary'] = [random.randint(50000, 100000) for _ in range(len(df))]
# Step 7: 
print(df.describe())
#########################################################
#2solution
import pandas as pd
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'Sales': [5000, 6000, 7500, 8000],
    'Expenses': [3000, 3500, 4000, 4500]
}

sales_and_expenses = pd.DataFrame(data)
print (sales_and_expenses)

max_sales = sales_and_expenses ['Sales'].max()
max_expenses= sales_and_expenses['Expenses'].max()
min_sales = sales_and_expenses ['Sales'].min()
min_expenses= sales_and_expenses['Expenses'].min()
avg_sales = sales_and_expenses ['Sales'].mean()
avg_expenses= sales_and_expenses['Expenses'].mean()
print('Maximum Sales', max_sales)
print('Maximum expenses', max_expenses)
print('Minimum Sales', min_sales)
print('Minimum expenses', min_expenses)
print('Average Sales', avg_sales)
print('Average expenses', avg_expenses)

###################################################

#3 solution
import pandas as pd
data = {
    'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
    'January': [1200, 200, 300, 150],
    'February': [1300, 220, 320, 160],
    'March': [1400, 240, 330, 170],
    'April': [1500, 250, 350, 180]
}

expenses = pd.DataFrame(data)
expenses = expenses.set_index('Category')
max_expense = expenses.max(axis=1)
print("Maximum expense per category:")
print(max_expense)

min_expense = expenses.min(axis=1)
print("\nMinimum expense per category:")
print(min_expense)

avg_expense = expenses.mean(axis=1)
print("\nAverage expense per category:")
print(avg_expense)

