import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns 
import pandas as pd


# Set the professional style instantly
sns.set_style('whitegrid')

# Create a sample data pipeline 
data = {
    'Age': [24, 25, 28, 30, 32, 35, 40, 41, 45, 50, 23, 52],
    'Experience': [1, 2, 4, 5, 6, 8, 11, 12, 15, 20, 0, 22],
    'Salary': [85, 90, 115, 120, 135, 150, 180, 185, 210, 240, 75, 450], # Note: 450 is a massive outlier
    'Language': ['Python', 'Python', 'R', 'Python', 'Julia', 'Python', 'Julia', 'Python', 'Python', 'R', 'R', 'Python']
}

df = pd.DataFrame(data)
print(df)


# Calculate the correlation math first
math = df.corr(numeric_only=True)


#Generate the plot

sns.heatmap(math, annot=True, cmap='coolwarm', fmt=".2f", vmin=-1, vmax=1)
plt.title("Correlation Matrix of Features")
plt.show()



#Histplot

sns.histplot(data=df, x='Salary', kde=True, bins=6, color='teal')
plt.title("Salary Distribution with KDE Curve")
plt.show()


#boxplot

sns.boxplot(data=df, x='Language', y='Salary', palette='Set2')
plt.title("Salary Ranges & Outliers by Language")
plt.show()


#scatterplot

sns.scatterplot(data=df, x='Age', y='Salary', hue='Language', style='Language', s=100)
plt.title("Salary vs. Age Progression")
plt.show()


#barplot

sns.barplot(data=df, x='Language', y='Salary', errorbar='ci', color='royalblue')
plt.title("Average Salary by Language Category")
plt.show()
