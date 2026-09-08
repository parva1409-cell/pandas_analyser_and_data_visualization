import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class SalesDataAnalyzer:

    def __init__(self):
        self.data = None
        self.last_fig = None

    def load_data(self):
        file = input("Enter CSV file name: ")

        if os.path.exists(file):
            self.data = pd.read_csv(file)
            print("Dataset loaded!")
        else:
            print("File not found!")

    def explore(self):
        if self.data is None:
            print("Load dataset first!")
            return

        print("\n1. First 5 rows")
        print("2. Last 5 rows")
        print("3. Columns")
        print("4. Data types")
        print("5. Information")

        ch = input("Enter choice: ")

        if ch == "1":
            print(self.data.head())
        elif ch == "2":
            print(self.data.tail())
        elif ch == "3":
            print(self.data.columns.tolist())
        elif ch == "4":
            print(self.data.dtypes)
        elif ch == "5":
            self.data.info()

    def operations(self):
        if self.data is None:
            print("Load dataset first!")
            return

        print("\n1. Double column")
        print("2. Group by")
        print("3. Convert to NumPy")
        print("4. Pivot table")

        ch = input("Enter choice: ")
        col = input("Enter column: ")

        if col not in self.data.columns:
            print("Column not found!")
            return

        if ch == "1":
            print(self.data[col] * 2)

        elif ch == "2":
            print(self.data.groupby(col).size())

        elif ch == "3":
            print(self.data[col].to_numpy())

        elif ch == "4":
            value = input("Enter value column: ")
            print(pd.pivot_table(self.data, index=col,
                                 values=value, aggfunc="sum"))

    def missing(self):
        if self.data is None:
            print("Load dataset first!")
            return

        print("\n1. Show missing")
        print("2. Fill missing")
        print("3. Drop missing")

        ch = input("Enter choice: ")

        if ch == "1":
            print(self.data.isnull().sum())

        elif ch == "2":
            num = self.data.select_dtypes(include=np.number).columns
            self.data[num] = self.data[num].fillna(self.data[num].mean())
            print("Missing values filled!")

        elif ch == "3":
            self.data.dropna(inplace=True)
            print("Missing rows removed!")

    def statistics(self):
        if self.data is None:
            print("Load dataset first!")
            return

        print(self.data.describe())
        print("\nStandard Deviation:")
        print(self.data.select_dtypes(include=np.number).std())
        print("\nVariance:")
        print(self.data.select_dtypes(include=np.number).var())

    def visualize(self):
        if self.data is None:
            print("Load dataset first!")
            return

        print("""
1. Bar Plot
2. Line Plot
3. Scatter Plot
4. Pie Chart
5. Histogram
6. Stack Plot
7. Heatmap
8. Box Plot
""")

        ch = input("Enter choice: ")
        plt.figure(figsize=(8, 5))

        if ch in ["1", "2", "3"]:
            x = input("Enter x column: ")
            y = input("Enter y column: ")

            if ch == "1":
                plt.bar(self.data[x], self.data[y])
            elif ch == "2":
                plt.plot(self.data[x], self.data[y])
            else:
                plt.scatter(self.data[x], self.data[y])

        elif ch == "4":
            col = input("Enter column: ")
            v = self.data[col].value_counts()
            plt.pie(v, labels=v.index, autopct="%1.1f%%")

        elif ch == "5":
            col = input("Enter numeric column: ")
            plt.hist(self.data[col], bins=5)

        elif ch == "6":
            x = input("Enter x column: ")
            y = input("Enter numeric column: ")
            plt.stackplot(self.data[x], self.data[y], labels=[y])
            plt.legend()

        elif ch == "7":
            num = self.data.select_dtypes(include=np.number)
            sns.heatmap(num.corr(), annot=True)

        elif ch == "8":
            col = input("Enter numeric column: ")
            sns.boxplot(y=self.data[col])

        else:
            print("Invalid choice!")
            plt.close()
            return

        plt.tight_layout()
        plt.show()
        self.last_fig = plt.gcf()

    def save_graph(self):
        if self.last_fig is None:
            print("Create a graph first!")
            return

        name = input("Enter file name: ")
        self.last_fig.savefig(name)
        print("Graph saved!")


def main():
    analyzer = SalesDataAnalyzer()

    while True:
        print("""
========== SALES DATA ANALYZER ==========

1. Load Dataset
2. Explore Data
3. DataFrame Operations
4. Missing Data
5. Statistics
6. Visualization
7. Save Graph
8. Exit
""")

        ch = input("Enter choice: ")

        if ch == "1":
            analyzer.load_data()
        elif ch == "2":
            analyzer.explore()
        elif ch == "3":
            analyzer.operations()
        elif ch == "4":
            analyzer.missing()
        elif ch == "5":
            analyzer.statistics()
        elif ch == "6":
            analyzer.visualize()
        elif ch == "7":
            analyzer.save_graph()
        elif ch == "8":
            print("Thank you!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()