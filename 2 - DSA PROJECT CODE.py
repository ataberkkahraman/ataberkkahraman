import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr
import statsmodels.api as sm


# 1. Load Data
file_path = "Process.xlsx" 
data = pd.read_excel(file_path)

# 2. Data Cleaning
# Convert date format
data['TARİH'] = pd.to_datetime(data['TARİH'])

# Fill missing values with the mean
print("Missing values:")
print(data.isnull().sum())
data.fillna(data.mean(), inplace=True)

# 3. Correlation Analysis
# Correlation matrix
correlation_matrix = data.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix')
plt.show()

# 4. Visualizations
# Protein vs Bench Press
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Protein', y='Bench', data=data)
plt.title('Protein vs Bench Press')
plt.xlabel('Protein Intake (g)')
plt.ylabel('Bench Press (kg)')
plt.show()

# New Visualization: Carbs vs Bench Press
plt.figure(figsize=(8, 6))
sns.scatterplot(x='CARB', y='Bench', data=data)
plt.title('Carbs vs Bench Press')
plt.xlabel('Carbs Intake (g)')
plt.ylabel('Bench Press (kg)')
plt.show()

# New Visualization: Calories vs Sleep Duration
plt.figure(figsize=(8, 6))
sns.scatterplot(x='KCAL', y='Uyku', data=data)
plt.title('Calories vs Sleep Duration')
plt.xlabel('Calories Intake')
plt.ylabel('Sleep Duration (hours)')
plt.show()

# New Visualization: Weekly Progress
plt.figure(figsize=(10, 6))
plt.plot(data['TARİH'], data['Bench'], marker='o', label='Bench Press')
plt.plot(data['TARİH'], data['weight'], marker='s', label='Weight')
plt.title('Weekly Progress')
plt.xlabel('Date')
plt.ylabel('Performance / Weight')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# New Visualization: Sleep Quality vs RPM
plt.figure(figsize=(8, 6))
sns.boxplot(x='Uyku Kalite', y='RPM', data=data)
plt.title('Sleep Quality vs RPM')
plt.xlabel('Sleep Quality')
plt.ylabel('Repetitions Per Minute (RPM)')
plt.show()

# 5. Regression Analysis
X = data['Protein']
y = data['Bench']
X = sm.add_constant(X)  # Add constant to predictor
model = sm.OLS(y, X).fit()
print(model.summary())

# 6. Hypothesis Testing
correlation, p_value = pearsonr(data['Protein'], data['Bench'])
print("Correlation:", correlation)
print("P-Value:", p_value)
if p_value < 0.05:
    print("Significant relationship.")
else:
    print("No significant relationship.")

# 7. Additional Analysis
# Day Difficulty vs Bench Press
plt.figure(figsize=(8, 6))
sns.boxplot(x='Günün zorl', y='Bench', data=data)
plt.title('Day Difficulty vs Bench Press')
plt.xlabel('Day Difficulty')
plt.ylabel('Bench Press (kg)')
plt.show()

# Weekly Calorie Intake Trend
plt.figure(figsize=(10, 6))
plt.plot(data['TARİH'], data['KCAL'], marker='o', color='green')
plt.title('Weekly Calorie Intake')
plt.xlabel('Date')
plt.ylabel('Calories (kcal)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

import os
print(os.getcwd())
