# Pandas

- Pandas is a Python library used for working with data sets.
- It has functions for analyzing, cleaning, exploring, and manipulating data.
- The name Pandas has a reference to both Panel Data, and Python Data Analysis and was created by Wes McKinney in 2008.
- https://github.com/pandas-dev/pandas

### Import Pandas

Install pandas: 
```bash
conda install pandas
pip install pandas
```

### Import: import pandas as pd
Check Version:  `print(pd.__version__)`

### Data Structures in Pandas
1. Series — 1D
2. DataFrame — 2D
3. Panel — 3D

![[ds-in-pandas.png]]

#### Series

- The Series is the object of the pandas library designed to represent one-dimensional data structures.
- Similar to an array but with some additional features. 
- A series consists of two components.
	- One-dimensional data (Values)
	- Index

![[series.png]]

#### DataFrame

- A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.

![[dframe-operations.png]]

### Reading From CSV File

- A simple way to store big data sets is to use CSV files (comma separated files).
- CSV files contain plain text and are a well know format that can be read by everyone including Pandas.

```py
import pandas as pd
df = pd.read_csv('data.csv')
print(df.to_string())
```

### Analyzing DataFrames

- One of the most used method for getting a quick overview of the DataFrame, is the head() method.
- The `head()` method returns the headers and a specified number of rows, starting from the top.

`print(df.head(10))`

### Pandas - Cleaning Data

- Data cleaning means fixing bad data in your data set.
- Bad data could be:
	- Empty cells
	- Data in wrong format
	- Wrong data
	- Duplicates

#### Handling Empty Cells

- Empty cells can potentially give you a wrong result when you analyse data.

1. Remove Rows with empty cells: dropna()
	- By default, the dropna() method returns a new DataFrame, and will not change the original.
		- If you want to change the original DataFrame, use the inplace = True argument:

2. Replace Empty Values: fillna()
- Another way of dealing with empty cells is to insert a new value instead.
- This way you do not have to delete entire rows just because of some empty cells.

![[dropna.png]]
![[fillna.png]]


#### Fixing Data

- Let’s say that the duration cannot be more than 120.
- Then we can fix it by setting any duration value higher than 120 to 120.

```py
for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.loc[x, "Duration"] = 120
```

#### Handle Duplicates

- Duplicate rows are rows that have been registered more than one time.
![[hand-duplicate.png]]

- To discover duplicates, we can use the `duplicated()` method.
- The duplicated() method returns a Boolean values for each row:

`print(df.duplicated())`

- To remove duplicates, use the drop_duplicates() method.

`df.drop_duplicates(inplace = True)`
