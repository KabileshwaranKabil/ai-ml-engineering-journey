# Pandas

## Creating, Reading and Writing
- To use pandas, you'll typically start with the following line of code.

```python
import pandas as pd
```
### Creating data
There are 2 core objects in pandas: the **DataFrame** and the **Series**.

#### DataFrame
- A DataFrame is a table. It contains an array of individual entries, each of which has a certain value. Each entry corresponds to a row(or record) and column.

For example, consider the following simple DataFrame:

```python
pd.DataFrame({'Yes':[50,21], 'No':[131,2]})
```

In this example, the "0, No" entry has the value of 131. The "0, Yes" entry has a value of 50, and so on.

DataFrame entries are not limited to integers. For instance, here's a DataFrame whose values are strings:


```python
pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']})
```

We are using the pd.DataFrame() constructor to generate these DataFrame objects. The syntax for declaring a new one is a dictionary whose keys are the column names (Bob and Sue in this example), and whose values are a list of entries. This is the standard way of constructing a new DataFrame, and the one you are most likely to encounter.


The dictionary-list constructor assigns values to the column labels, but just uses an ascending count from 0 (0, 1, 2, 3, ...) for the row labels. Sometimes this is OK, but oftentimes we will want to assign these labels ourselves.

The list of row labels used in a DataFrame is known as an Index. We can assign values to it by using an index parameter in our constructor:


```python
pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 
              'Sue': ['Pretty good.', 'Bland.']},
             index=['Product A', 'Product B'])
```

#### Series
A Series, by contrast, is a sequence of data values. If a DataFrame is a table, a Series is a list. And in fact you can create one with nothing more than a list:

```python
pd.Series([1,2,3,4,5])
```

A Series is, in essence, a single column of a DataFrame. So you can assign row labels to the Series the same way as before, using an index parameter. However, a Series does not have a column name, it only has one overall name:

```python
pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')
```

*The Series and the DataFrame are intimately related. It's helpful to think of a DataFrame as actually being just a bunch of Series "glued together*


#### Reading data files
Being able to create a DataFrame or Series by hand is handy. But, most of the time, we won't actually be creating our own data by hand. Instead, we'll be working with data that already exists.

Data can be stored in any of a number of different forms and formats. By far the most basic of these is the humble CSV file.

When you open a CSV file you get something that looks like this:
```
Product A,Product B,Product C,
30,21,9,
35,34,1,
41,11,11
```

So a CSV file is a table of values separated by commas. Hence the name: "Comma-Separated Values", or CSV.

Let's now set aside our toy datasets and see what a real dataset looks like when we read it into a DataFrame. We'll use the `pd.read_csv()`function to read the data into a DataFrame. This goes thusly:

```python
wine_reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv")

# We can use the shape attribute to check how large the resulting DataFrame is:
wine.wine_reviews.shape
```

We can examine the contents of the resultant DataFrame using the `head()` command, which grabs the first five rows:

```python
wine_reviews.head()
```
The `pd.read_csv()` function is well-endowed, with over 30 optional parameters you can specify. For example, you can see in this dataset that the CSV file has a built-in index, which pandas did not pick up on automatically. To make pandas use that column for the index (instead of creating a new one from scratch), we can specify an `index_col`.

```python
wine_reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)
wine_reviews.head()
```

---

## Indexing, Selecting & Assigning

```python
import pandas as pd
reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)
pd.set_option('display.max_rows', 5)
```

### Native accessors
Native Python objects provide good ways of indexing data. Pandas carries all of these over, which helps make it easy to start with.


In Python, we can access the property of an object by accessing it as an attribute. A book object, for example, might have a title property, which we can access by calling book.title. Columns in a pandas DataFrame work in much the same way.

Hence to access the country property of reviews we can use:

`reviews.country`

If we have a Python dictionary, we can access its values using the indexing ([]) operator. We can do the same with columns in a DataFrame:

`reviews['country']`

These are the two ways of selecting a specific Series out of a DataFrame. Neither of them is more or less syntactically valid than the other, but the indexing operator [] does have the advantage that it can handle column names with reserved characters in them (e.g. if we had a country providence column, reviews.country providence wouldn't work).

Doesn't a pandas Series look kind of like a fancy dictionary? It pretty much is, so it's no surprise that, to drill down to a single specific value, we need only use the indexing operator [] once more:


`reviews['country'][0]`

### Indexing in pandas
The indexing operator and attribute selection are nice because they work just like they do in the rest of the Python ecosystem. As a novice, this makes them easy to pick up and use. However, pandas has its own accessor operators, `loc` and `iloc`. 
For more advanced operations, these are the ones you're supposed to be using.

**Index-based selection**
- Pandas indexing works in one of two paradigms. The first is index-based selection: selecting data based on its numerical position in the data. iloc follows this paradigm.

To select the first row of data in a DataFrame, we may use the following:

`reviews.iloc[0]`

Both loc and iloc are row-first, column-second. This is the opposite of what we do in native Python, which is column-first, row-second.

This means that it's marginally easier to retrieve rows, and marginally harder to get retrieve columns. To get a column with iloc, we can do the following:

`reviews.iloc[:,0]`

On its own, the : operator, which also comes from native Python, means "everything". When combined with other selectors, however, it can be used to indicate a range of values. For example, to select the country column from just the first, second, and third row, we would do:

`reviews.iloc[:3,0`

Or, to select just the second and third entries, we would do:

`reviews.iloc[1:3,0]`

it's also possible to pass a list:

`reviews.iloc[[0,1,2],0]`

Negative numbers can be used in selection. This will start counting forwards from the end of the values.

`reviews.iloc[-5:]`

### Label-based selection
The second paradigm for attribute selection is the one followed by the loc operator:
**label-based selection**. In this paradigm, it's the data index value, not it's position, which matters.

For example, to get the first entry in `reviews`, we would now do the following:

`reviews.loc[0,'country']`


iloc is conceptually simpler than loc because it ignores the dataset's indices. When we use iloc we treat the dataset like a big matrix (a list of lists), one that we have to index into by position. loc, by contrast, uses the information in the indices to do its work. Since your dataset usually has meaningful indices, it's usually easier to do things using loc instead. For example, here's one operation that's much easier using loc:

`reviews.loc[:, ['taster_name', 'taster_twitter_handle', 'points']]`

### Choosing between loc and iloc

When choosing or transitioning between loc and iloc, there is one "gotcha" worth keeping in mind, which is that the two methods use slightly different indexing schemes.

iloc uses the Python stdlib indexing scheme, where the first element of the range is included and the last one excluded. So 0:10 will select entries 0,...,9. loc, meanwhile, indexes inclusively. So 0:10 will select entries 0,...,10.

Why the change? Remember that loc can index any stdlib type: strings, for example. If we have a DataFrame with index values Apples, ..., Potatoes, ..., and we want to select "all the alphabetical fruit choices between Apples and Potatoes", then it's a lot more convenient to index df.loc['Apples':'Potatoes'] than it is to index something like df.loc['Apples', 'Potatoet'] (t coming after s in the alphabet).

This is particularly confusing when the DataFrame index is a simple numerical list, e.g. 0,...,1000. In this case df.iloc[0:1000] will return 1000 entries, while df.loc[0:1000] return 1001 of them! To get 1000 elements using loc, you will need to go one lower and ask for df.loc[0:999].

Otherwise, the semantics of using loc are the same as those for iloc.

### Manipulating the index
Label-based selection derives its power from the labels in the index. Critically, the index we use is not immutable. We can manipulate the index in any way we see fit.

The set_index() method can be used to do the job. Here is what happens when we set_index to the title field:

`reviews.set_index("title")`

### Conditional Selection

So far we've been indexing various strides of data, using structural properties of the DataFrame itself. To do interesting things with the data, however, we often need to ask questions based on conditions.

For example, suppose that we're interested specifically in better-than-average wines produced in Italy.

We can start by checking if each wine is Italian or not:

`reviews.country == 'Italy'`

This operation produced a Series of True/False booleans based on the country of each record. This result can then be used inside of loc to select the relevant data:

`reviews.loc[reviews.country == 'Italy']`


We also wanted to know which ones are better than average. Wines are reviewed on a 80-to-100 point scale, so this could mean wines that accrued at least 90 points.

We can use the ampersand (&) to bring the two questions together:

`reviews.loc[(reviews.country == 'Italy') & (reviews.points >= 90)]`

Suppose we'll buy any wine that's made in Italy or which is rated above average. For this we use a pipe (|):

`reviews.loc[(reviews.country == 'Italy') | (reviews.points >= 90)]`

Pandas comes with a few built-in conditional selectors, two of which we will highlight here.

The first is isin. isin is lets you select data whose value "is in" a list of values. For example, here's how we can use it to select wines only from Italy or France

`reviews.loc[reviews.isin(['Italy','France'])]`

The second is `isnull` (and it's companion `notnull`). These methods let you highlight values which are (or are not) empty (NaN). For example, to filter out wines lacking a price tag in the dataset, here's what we would do"

`reviews.loc[reviews.price.notnull()]`

### Assigning data

we can assign either a constant value.

`reviews['critic']='everyone'`

Or with an iterable of values

```python
reviews['index_backwards'] = range(len(reviews),0,-1)
reviews['index_backwards']
```

---

## Summary Functions and Maps


```python
import pandas as pd
pd.set_option('display.max_rows',5)

import numpy as np 
reviews = pd.read_csv('../input..',index_col=0)
```

### Summary functions

Pandas provides many simple "summary functions"(not an official name) which restructure the data in some useful way. For example, consider the `describe()` method:

`reviews.points.describe()`

This method generates a high-level summary of the attributes of the given column. It is type-aware, meaning that its output changes based on the data type of the input. The output above only makes sense for numerical data; for string data here's what we get:

`reviews.taster_name.describe()`

If you want to get some particular simple summary statistic about a column in a DataFrame or a Series, there is usually a helpful pandas function that makes it happen.

For example, to see the mean of the points allotted (e.g. how well an averagely rated wine does), we can use the mean() function:

`reviews.points.mean()`

To see a list of unique values we can use the `unique()` function:

`reviews.taster_name.unique()`

To see a list of unique values and how often they occur in the dataset, we can use the value_counts() method:

`reviews.taster_name.value_counts()`


### Maps

A map is a term, borrowed from mathematics, for a function that takes one set of values and "maps" them to another set of values. In data science we often have a need for creating new representations from existing data, or for transforming data from the format it is in now to the format that we want it to be in later. Maps are what handle this work, making them extremely important for getting your work done!

There are two mapping methods that you will use often.

`map()`  is the first, and slightly simpler one. For example, suppose that we wanted to remean the scores the wines received to 0. We can do this as follows:

```python
review_points_mean = reviews.points.mean()
reviews.points.map(lambda p: p - review_points_mean)
```

The function you pass to map() should expect a single value from the Series (a point value, in the above example), and return a transformed version of that value. map() returns a new Series where all the values have been transformed by your function.

apply() is the equivalent method if we want to transform a whole DataFrame by calling a custom method on each row.

```python
def remean_points(row):
    row.points = row.points-review_points_mean
    return row 

reviews.apply(remean_points,axis='columns')

```

f we had called reviews.apply() with axis='index', then instead of passing a function to transform each row, we would need to give a function to transform each column.

Note that map() and apply() return new, transformed Series and DataFrames, respectively. They don't modify the original data they're called on. If we look at the first row of reviews, we can see that it still has its original points value.



