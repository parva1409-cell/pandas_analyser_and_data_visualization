📊 Sales Data Analyzer

A beginner-friendly Python project for exploring, analyzing, transforming, and visualizing CSV datasets using Pandas, NumPy, Matplotlib, and Seaborn.

The program provides a simple menu-driven interface where users can load their own CSV file, inspect the data, perform DataFrame operations, handle missing values, calculate statistics, create different visualizations, and save graphs.

✨ Features

- 📂 Load any CSV dataset
- 👀 Explore dataset contents
- 📋 View first and last five rows
- 🏷️ View column names
- 🔤 Check data types
- ℹ️ Display dataset information
- ➗ Perform DataFrame operations
- 🔢 Convert Pandas columns to NumPy arrays
- 📊 Group data by columns
- 🔄 Create pivot tables
- 🧹 Check missing values
- ✏️ Fill missing numerical values
- 🗑️ Remove rows containing missing values
- 📈 Calculate statistics
- 📉 Calculate standard deviation and variance
- 📊 Create different types of graphs
- 💾 Save the last created graph

🛠️ Technologies Used

Library	Purpose

Python	Main programming language

Pandas	Data loading, manipulation, and analysis

NumPy	Numerical operations

Matplotlib	Creating visualizations

Seaborn	Statistical visualizations

OS	Checking whether the CSV file exists


📂 Dataset

Unlike some of my other projects, this analyzer does not use a fixed dataset.

The user enters the name of the CSV file:

Enter CSV file name:

The program checks whether the file exists before loading it.

Example:

sales_data.csv

The CSV file should be accessible from the folder where the program is being run.

📋 Main Menu

========== SALES DATA ANALYZER ==========

1. Load Dataset

2. Explore Data

3. DataFrame Operations

4. Missing Data

5. Statistics

6. Visualization

7. Save Graph

8. Exit


📂 1. Load Dataset

The program asks for a CSV filename and loads it using:

pd.read_csv()

Before loading, it checks whether the file exists using:

os.path.exists()



🔍 2. Explore Data

This section provides five options:

1. First 5 rows

2. Last 5 rows

3. Columns

4. Data types

5. Information



It uses Pandas functions such as:

head()

tail()

dtypes

info()



🔄 3. DataFrame Operations

The program demonstrates four operations:

Double Column

Multiplies the selected column by 2.

self.data[col] * 2

Group By

Groups the dataset according to a selected column.

self.data.groupby(col).size()

Convert to NumPy

Converts a Pandas column into a NumPy array.

self.data[col].to_numpy()

Pivot Table

Creates a pivot table using the selected index and value column.

pd.pivot_table()

🧹 4. Missing Data

The program provides three ways to handle missing values:

Show Missing Values

self.data.isnull().sum()

Fill Missing Values

Missing values in numerical columns are replaced with their respective column mean.

fillna()

Drop Missing Values

Rows containing missing values are removed using:

dropna()

📊 5. Statistics

The program displays descriptive statistics using:

self.data.describe()

It also calculates:

- Standard deviation

- Variance

for numerical columns.

📈 6. Visualization

The analyzer can create eight different types of visualizations:

1. Bar Plot

Compares two selected columns.

2. Line Plot

Displays trends between two selected columns.

3. Scatter Plot

Shows the relationship between two columns.

4. Pie Chart

Displays the distribution of values in a selected column.

5. Histogram

Shows the distribution of a numerical column.

6. Stack Plot

Creates a stacked area visualization using the selected columns.

7. Heatmap

Displays the correlation between numerical columns using Seaborn.

8. Box Plot

Displays the distribution and spread of a numerical column.

💾 7. Save Graph

After creating a graph, the program stores the figure in:

self.last_fig

The user can then enter a filename to save the graph.

Example:

Enter file name: sales_chart.png

The graph is saved using:


self.last_fig.savefig(name)

🧠 Python Concepts Practiced

This project demonstrates:

- Classes and Objects
- Constructor (__init__)
- Methods
- if-elif-else
- while loops
- User Input
- File Checking
- CSV Handling
- Pandas DataFrames
- NumPy Arrays
- DataFrame Operations
- GroupBy
- Pivot Tables
- Missing Data Handling
- Statistical Analysis
- Data Visualization
- Saving Files

📦 Installation

Make sure Python is installed on your computer.

Install the required libraries:

pip install pandas numpy matplotlib seaborn

▶️ How to Run

Save the program, for example:

sales_data_analyzer.py

Run it using:

python sales_data_analyzer.py

Then enter the name of your CSV file when requested.

📂 Project Structure

Sales-Data-Analyzer/

│

├── sales_data_analyzer.py

├── your_dataset.csv

└── README.md

The dataset can be replaced with any suitable CSV file.

🎯 Project Objective

The main objective of this project is to practice Pandas, NumPy, Matplotlib, and Seaborn through a simple interactive data analysis program.

It demonstrates the basic workflow of loading a dataset, exploring its contents, handling missing data, performing transformations, calculating statistics, 
creating visualizations, and saving results.

🚀 Future Improvements

Possible improvements include:

- Add data filtering and sorting

- Add more statistical functions

- Add automatic column type detection

- Add more visualization options

- Add chart customization

- Export analysis results to CSV

- Add a graphical user interface

- Add error handling for invalid column types
