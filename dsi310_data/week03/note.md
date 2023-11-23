**Week 3: Data Preparation and Cleaning**

**Topic: Preparing and Cleaning Data for Further Processing**

**Objectives:**
- Teach students techniques for data cleaning and preparation.
- Provide hands-on experience in transforming and structuring data.

**Keywords:** Data Preparation, Data Cleaning, Data Transformation, Data Structuring.

**Slide 1: Introduction to Data Preparation and Cleaning**

Welcome to Week 3 of our course on Data Processing and Exploration for Data Engineers! In this module, we will dive into the crucial aspects of data preparation and cleaning. Let's get started.

**Slide 2: The Importance of Data Preparation**

Data preparation is a critical step in the data analysis process. It involves getting your data into a suitable format for analysis, ensuring accuracy and consistency. Well-prepared data leads to more accurate and meaningful insights.

**Slide 3: Identifying Missing Values**

One common data issue is missing values. Missing data can skew analysis and lead to incorrect conclusions. Let's explore how to identify missing values and handle them using Python.

**Code Example:**

```python
import pandas as pd

# Load dataset
data = {'A': [1, 2, None, 4, 5],
        'B': [None, 2, 3, 4, 5]}
df = pd.DataFrame(data)

# Count missing values
missing_values = df.isnull().sum()

# Drop rows with missing values
cleaned_df = df.dropna()

print("Original DataFrame:")
print(df)
print("\nMissing Values:")
print(missing_values)
print("\nCleaned DataFrame:")
print(cleaned_df)
```

**Slide 4: Handling Missing Values**

We can handle missing values by imputing them with appropriate values. Mean imputation and median imputation are common techniques.

**Code Example:**

```python
# Mean imputation
df['A'].fillna(df['A'].mean(), inplace=True)

# Median imputation
df['B'].fillna(df['B'].median(), inplace=True)

print("Imputed DataFrame:")
print(df)
```

**Slide 5: Dealing with Outliers**

Outliers can adversely affect analysis. Identifying and handling outliers is crucial. Let's see how we can visualize and handle outliers using Python.

**Code Example:**

```python
import matplotlib.pyplot as plt

# Box plot to visualize outliers
plt.boxplot(df['A'])
plt.title("Box Plot of Column A")
plt.show()

# Handling outliers using Z-score
from scipy.stats import zscore
z_scores = zscore(df['A'])
threshold = 2
outliers = (z_scores > threshold) | (z_scores < -threshold)
cleaned_df = df[~outliers]

print("Cleaned DataFrame:")
print(cleaned_df)
```

**Slide 6: Data Transformation**

Data transformation involves reshaping and reformatting data. Let's explore common transformation techniques using Python's pandas library.

**Code Example:**

```python
# Melting a DataFrame
melted_df = pd.melt(df, id_vars=['B'], value_vars=['A'], var_name='Variable', value_name='Value')

# Pivoting a DataFrame
pivoted_df = melted_df.pivot(index='B', columns='Variable', values='Value')

print("Melted DataFrame:")
print(melted_df)
print("\nPivoted DataFrame:")
print(pivoted_df)
```

**Slide 7: Introduction to Structured and Unstructured Data**

Data can be structured or unstructured. Structured data is organized in a tabular format, while unstructured data lacks a specific structure. Let's explore the differences and how to transform unstructured data.

**Slide 8: Transforming Unstructured Data**

Consider a scenario with unstructured text data. We can use regular expressions to extract structured information.

**Code Example:**

```python
import re

text = "Customer ID: 12345, Name: John, Order Amount: $100"
pattern = r"Customer ID: (\d+), Name: (\w+), Order Amount: (\$\d+)"
match = re.search(pattern, text)

if match:
    customer_id = match.group(1)
    name = match.group(2)
    order_amount = match.group(3)
    print("Customer ID:", customer_id)
    print("Name:", name)
    print("Order Amount:", order_amount)
```

**Slide 9: Using Data Quality Metrics**

Data quality assessment ensures data accuracy. Metrics like completeness, consistency, and accuracy help evaluate data quality.

**Code Example:**

```python
# Calculate completeness
completeness = df.count() / len(df) * 100

# Calculate consistency (e.g., duplicate values)
duplicate_count = df.duplicated().sum()

print("Completeness (%):")
print(completeness)
print("\nDuplicate Count:")
print(duplicate_count)
```

**Slide 10: Dealing with Data Quality Issues**

Addressing data quality issues involves techniques like deduplication and data validation. Let's see how to perform data deduplication.

**Code Example:**

```python
# Remove duplicate rows
deduplicated_df = df.drop_duplicates()

print("Deduplicated DataFrame:")
print(deduplicated_df)
```

**Slide 11: Handling Data Inconsistencies**

Data inconsistencies can arise from various sources. Uniformizing data formats can help resolve such issues.

**Code Example:**

```python
# Convert names to uppercase
df['Name'] = df['Name'].str.upper()

print("DataFrame with Uniform Names:")
print(df)
```

**Slide 12: Applying Data Preparation in Real Projects**

Real-world data projects heavily rely on effective data preparation. Whether it's analyzing customer behavior or predicting stock prices, well-prepared data is essential.

**Slide 13: Assignment Overview**

For this week's assignments:
- Clean and prepare a dataset with missing values and outliers.
- Transform unstructured text data into a structured format using regular expressions.

```python
import pandas as pd
import numpy as np

# Create a sample dataset with missing values and outliers
data = {
    'CustomerID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Helen', 'Ivy', 'Jack'],
    'Age': [25, 32, 28, np.nan, 40, 22, 35, 48, np.nan, 29],
    'OrderAmount': [150, 200, 1000, 50, 300, 30, 8000, 90, 150, 7000]
}

df = pd.DataFrame(data)

# Introduce missing values and outliers
df.loc[3, 'OrderAmount'] = 10000
df.loc[8, 'Age'] = 45

# Display the dataset
print(df)

```

**Slide 14: Tips for Effective Data Preparation**

1. Always understand your data's context.
2. Document every step of data cleaning.
3. Choose appropriate imputation techniques.
4. Visualize data before and after cleaning.
5. Continuously evaluate data quality.

**Slide 15: Conclusion**

Data preparation and cleaning are foundational steps in data analysis. By mastering these techniques, you'll be equipped to handle real-world data challenges and extract meaningful insights. In the next module, we'll explore the exciting world of data transformation and loading. Thank you and see you in the next class!
