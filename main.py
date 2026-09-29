import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

# Load dataset
data = pd.read_excel("dataset.xlsx")

# Features and target
X = data[["Food", "Transport", "Shopping", "Bills", "Entertainment"]]
y = data["Total_Expenses"]

# Split the data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create and train the model
model = DecisionTreeRegressor(random_state=42)
model.fit(X_train, y_train)

# Get user input
income = float(input("Enter your monthly income: "))

food = float(input("Enter Food expense: "))
transport = float(input("Enter Transport expense: "))
shopping = float(input("Enter Shopping expense: "))
bills = float(input("Enter Bills expense: "))
entertainment = float(input("Enter Entertainment expense: "))

# Create input for prediction
user_data = pd.DataFrame({
    "Food": [food],
    "Transport": [transport],
    "Shopping": [shopping],
    "Bills": [bills],
    "Entertainment": [entertainment]
})

# Predict total expenses
prediction = model.predict(user_data)[0]

# Calculate actual total expenses
total_expenses = food + transport + shopping + bills + entertainment

# Calculate savings
savings = income - total_expenses

print("\n----- Budget Report -----")
print("Predicted Total Expenses:", round(prediction, 2))
print("Actual Total Expenses:", round(total_expenses, 2))
print("Savings:", round(savings, 2))

# Budget suggestions
print("\n----- Budget Suggestions -----")

expenses = {
    "Food": food,
    "Transport": transport,
    "Shopping": shopping,
    "Bills": bills,
    "Entertainment": entertainment
}

for category, amount in expenses.items():
    if amount > total_expenses * 0.25:
        print("Try reducing your", category, "expenses.")

if savings < 0:
    print("You are spending more than your income.")
else:
    print("You are saving money. Keep maintaining your budget.")

# Pie chart
plt.figure()
plt.pie(
    expenses.values(),
    labels=expenses.keys(),
    autopct="%1.1f%%"
)
plt.title("Monthly Expense Distribution")
plt.show()

# Bar chart
plt.figure()
plt.bar(expenses.keys(), expenses.values())
plt.xlabel("Expense Category")
plt.ylabel("Amount")
plt.title("Monthly Expenses")
plt.xticks(rotation=20)
plt.show()
