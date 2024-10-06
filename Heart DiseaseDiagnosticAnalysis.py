import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("Heart Disease data.csv")

#Exploratory Data Analysis (EDA)

# Displays the first few rows of the dataset
print(df.head())

# Displays the last few rows of the dataset
print(df.tail()) 

# Finds Shape of  Dataset
print(df. shape) 
print ("Number of Rows", df. shape [0])
print ("Number of Columns", df. shape [1])

# Displays info of the dataset
print(df.info())

# check for duplicated
data_dup = df.duplicated ().any ()
print (data_dup)
df = df.drop_duplicates ()
print(df. shape) 

# Displays summary statistics
print(df.describe())

# Check for missing values
print(df.isnull().sum())

# Check the data types of the columns
print(df.dtypes) 



#Data Preprocessing
# Converting categorical columns to numeric 
# For example, converting 'sex' column to numeric
df['sex'] = df['sex'].astype('int')

# Create Age Groups including age 29
df['AgeGroup'] = pd.cut(df['age'], bins=[29, 30, 40, 50, 60, 70, 80, 90], labels=['29-30', '30-40', '40-50', '50-60', '60-70', '70-80', '80-90'], right=False)


# Drop non-numeric columns or convert them to numeric 
numeric_df = df.select_dtypes(include=['float64', 'int64'])


# Exploratory Data Analysis (EDA)
# Correlation Heatmap
plt.figure(figsize=(12, 10))
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.show() 

# Pairplot for Key Attributes (only numeric columns)
sns.pairplot(numeric_df, hue='target')
plt.suptitle('Pairplot of Key Attributes', y=1.02)
plt.show()

# Heart Disease by target
plt.figure(figsize=(10, 6))
sns.countplot(x='target', data=df)
plt.title('Heart Disease by target')
plt.xlabel('target(1 = heart disease, 0 = no heart disease)')
plt.ylabel('Count')
plt.show()

# Heart Disease by target
plt.figure(figsize=(10, 6))
sns.countplot(x='target', data=df, hue='sex', palette='dark:green')  
plt.title('Heart Disease by Target with Male and Female Differentiation')
plt.xlabel('Target (1 = Heart Disease, 0 = No Heart Disease)')
plt.ylabel('Count')
plt.legend(title='Sex (0 = Female, 1 = Male)')
plt.show()


# Gender distribution, according to the target variable
plt.figure(figsize=(10, 6))
sns.countplot(x='sex', hue='target', data=df)
plt.title('Heart Disease by Gender')
plt.xlabel('Gender (1 = Male, 0 = Female)')
plt.ylabel('Count')
plt.legend(title='Heart Disease')
plt.show()

# Heart Disease by Age Group
plt.figure(figsize=(12, 8))
sns.countplot(x='AgeGroup', hue='target', data=df)
plt.title('Heart Disease by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Count')
plt.legend(title='Heart Disease')
plt.show()

# Heart Disease by Age Group and Gender using sns.catplot
g = sns.catplot(x='AgeGroup', hue='target', col='sex', data=df, kind='count', height=5, aspect=1.5)
g.fig.suptitle('Heart Disease by Age Group and Gender', fontsize=16)
g.fig.subplots_adjust(top=0.85)  # Adjust the title to fit
plt.show() 

# Chest Pain Count Plot
plt.figure(figsize=(12, 8))
sns.countplot(x='cp', data=df, color='green') 
plt.title('Distribution of Chest Pain Types')
plt.xticks([0, 1, 2, 3], ["Typical Angina", "Atypical Angina", "Non-anginal Pain", "Asymptomatic"])
plt.xlabel('Chest Pain Type')
plt.ylabel('Count')
plt.show()

# Chest Pain as per target 
plt.figure(figsize=(12, 8))
sns.countplot(x='cp',hue='target', data=df, palette='Set2')  
plt.title('Distribution of Chest Pain Types')
plt.xticks([0, 1, 2, 3], ["Typical Angina", "Atypical Angina", "Non-anginal Pain", "Asymptomatic"])
plt.xlabel('Chest Pain Type')
plt.ylabel('Count')
plt.show()

#  Shows Fasting Blood Sugar Distribution According To Target Variable
plt.figure(figsize=(12, 8))
sns.countplot(x='fbs',hue='target', data=df, palette='Set2')  
plt.title('Distribution of Fasting blood sugar ')
plt.xlabel('Fasting blood sugar')
plt.ylabel('Count')
plt.show()


# Checks Resting Blood Pressure Distribution using Seaborn
plt.figure(figsize=(12, 8))
sns.histplot(data=df, x='trestbps', bins=30, color='blue')  
plt.title('Resting Blood Pressure Distribution')
plt.xlabel('Resting Blood Pressure')
plt.ylabel('Count')
plt.show()

# Compares Resting Blood Pressure As Per Sex Column
g = sns.FacetGrid(df, hue="sex", aspect=4)
g.map(sns.kdeplot, 'trestbps', fill=True)



# Adds a legend and set the titles
g.add_legend(title="Sex (0 = Female, 1 = Male)")
g.set_axis_labels('Resting Blood Pressure', 'Density')
plt.title('Resting Blood Pressure Distribution by Sex')
plt.show()
# Show Distribution of Serum cholesterol
plt.figure(figsize=(12, 8))
sns.histplot(x='chol', data=df,bins=30, color='blue')  
plt.title('Distribution of Serum cholesterol')
plt.xlabel('Serum cholesterol ')
plt.ylabel('Count')
plt.show()
# Identify categorical and continuous variables
cate_val = []
cont_val = []
for column in df.columns:
    if df[column].nunique() <= 10:
        cate_val.append(column)
    else:
        cont_val.append(column)

# Plots histograms for continuous variables
plt.figure(figsize=(16, len(cont_val) * 4))  
for i, column in enumerate(cont_val, 1):
    plt.subplot(len(cont_val), 1, i)  # Create subplots
    sns.histplot(data=df, x=column, kde=True, color='skyblue')  
    plt.title(f'Distribution of {column}')
    plt.xlabel(column)
    plt.ylabel('Count')

plt.tight_layout()  
plt.show()


df.to_excel('Heart_Disease_Final_Dataset.xlsx', index=False)
