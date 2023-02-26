[TOC]

# Guide for Website 

## Saying before 

Our website is a new type of 'Notebook' for learning coding. If you have done any project or testing in Jupyter Notebook before, this website will be familiar to you. You can code any project in this website the AI will understand your question and give you the best answer it can. Most of time it will surprised you! Let's using this example project to find out!

## Pre loading the dataset

In this example we will use `airbnb.csv` as our dataset for analyzing Airbnb's houses. You will be working with for this project is reproduced here: ![ab_dataset](https://github.com/GPT-3-Website-Develop/Autographer-website/blob/b282e5a767734474b863924a8b751547aba0b5a0/ab_dataset.png)

### Preview parts of dataset

Put your requirements like this in the text box:

```python
#Python
# read 'airbnb.csv' csv file then display the first 10000 data from 'neighborhood_group' column
```

 The AI generate output as below:

```python
import pandas as pd

df = pd.read_csv('airbnb.csv')

print(df['neighbourhood_group'][:10000])
```

### Define some functions for future

If we get some questions like: 

*You are expected to call the `process_csv` function correctly, and read the data on `airbnb.csv`. After reading the file, define the `csv_header`, and `csv_rows` and define the `cell` function.*

The `csv_header`, `csv_data`, `csv_rows` are defined:

```python
csv_data = process_csv("airbnb.csv")
csv_header=csv_data[0]
csv_rows=csv_data[1:]
```

You can start to define `process_csv` first, put defined requirements into text box like this:

```python
def process_csv(filename):
    """
    process_csv open the 'filename' and encode in 'utf-8' then read the csv file from it then save the data as list. Last, closed the file  and return the data list
    """
```

Then, the AI will generate the code for you under the defined function:

```python
def process_csv(filename):
    """
    process_csv open the 'filename' and encode in 'utf-8' then read the csv file from it then save the data as list. Last, closed the file  and return the data list
    """
    # YOUR CODE HERE
    f = open(filename, encoding='utf-8')
    data = f.read()
    data = data.split('\n')
    f.close()
    return data

```

Make sure you have left those worked codes in the text box, then keep adding new function:

```python
def cell(row_idx, col_name):
    """
    use the header 'csv_header' we got before, cell(row_idx, col_name) returns                             		 the data value (cell) corresponding to the row index `row_idx` and the column name       		`col_name` of a CSV file.
    """
```

AI:

```python
def cell(row_idx, col_name):
    """
    use the header 'csv_header' we got before, cell(row_idx, col_name) returns                             the data value (cell) 
    corresponding to the row index `row_idx` and the column name `col_name` of a CSV file.
    """
    # YOUR CODE HERE
    col_idx = csv_header.index(col_name)
    return csv_rows[row_idx][col_idx]
```

Those are preset steps for a Data Science project, you can start and try to let AI write codes for you!



## Create some Python file for specific use

In some cases, we will write a `class` for some Analysis work, so it is necessary to write a `class` file prepare for main work. AI is also able to do it for you if you teach them how to precess your codes! Here is a example for implement a `search.py` file.

### BSTs (Binary Search Trees)

In this example, you'll create a BST that can be used to lookup values by a key (it will behave a bit like a Python dict where the all the dict values are lists of values)

#### Basics Node and BST classes

Here is requirement:

*Start by pasting+completing the following:*

```python
class Node():
    def __init__(self, key):
        self.key = ????
        self.values = []
        self.left = None
        ????
```

*Let's create a `BST` class with an `add` method that automatically places a node in a place that preserves the search property (i.e., all keys in left subtree are less than a parent's value, which is less than those in the right tree).*

*Add+complete with the following. Note that this is a non-recursive version of `add`:*

```python
class BST():
    def __init__(self):
        self.root = None


    def add(self, key, val):
        if self.root == None:
            self.root = ????

    curr = self.root
    while True:
        if key < curr.key:
            # go left
            if curr.left == None:
                curr.left = Node(key)
            curr = curr.left
        elif key > curr.key:
             # go right
             ????
             ????
             ????
        else:
            # found it!
            assert curr.key == key
            break

    curr.values.append(val)
```

By analyzing the question requirement, we know that we have two `class` need to procedure. Let's start at first one, so we put the first requirement into text box:

**Input:**

*Start by pasting+completing the following:*

```python
class Node():
    def __init__(self, key):
        self.key = ????
        self.values = []
        self.left = None
        ????
```

*Let's create a `BST` class with an `add` method that automatically places a node in a place that preserves the search property (i.e., all keys in left subtree are less than a parent's value, which is less than those in the right tree).*

*Add+complete with the following. Note that this is a non-recursive version of add:*

**AI:**

```python
class BST():
    def __init__(self):
        self.root = None
        
    def add(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            current = self.root
            while current:
                if key < current.key:
                    if current.left is None:
                        current.left = Node(key)
                        break
                    else:
                        current = current.left
                elif key > current.key:
                    if current.right is None:
                        current.right = Node(key)
                        break
                    else:
                        current = current.right
                else:
                    current.values.append(key)
                    break
```

As we can see, it looks like AI know how to finished the whole question, so it also done the second part for us.

**And** we also noticed that AI was not completing Node() class for us. This is because AI only generates the requirement for the end of the input. But it does not matter, and we can remind AI by requesting a new rewrite movement. **IMPORTANT: AI is not your master, but your ASSISTANT; you are the one who manages the work, and it is pervasive that AI misunderstands your idea. IT DOESN'T MATTER; just keep trying to teach them and explain it. Trust me; it will understand you eventually, and do excellent work!**

**Follow input:**

*# re-write class Node*

**AI:**

```python
class Node():
    def __init__(self, key):
        self.key = key
        self.values = []
        self.left = None
        self.right = None
```

As you see, it do it perfectly!



