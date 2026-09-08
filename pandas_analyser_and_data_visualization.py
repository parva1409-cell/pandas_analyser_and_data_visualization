import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


FILE_NAME = os.path.join(os.path.dirname(__file__), "sales_data.csv")

class SalesDataAnalyzer:

    def __init__(self):
        self.df = None

    def load_data(self):
        if not os.path.exists(FILE_NAME):
            print("\nFile not found!")
            return

        self.df = pd.read_csv(FILE_NAME)
        self.df.dropna(inplace=True)
        self.df.drop_duplicates(inplace=True)

        self.df["Date"] = pd.to_datetime(self.df["Date"])

        self.df["month"] = self.df["Date"].dt.month_name()
        self.df["month_no"] = self.df["Date"].dt.month

        print("\nDataset loaded successfully!")

    def check_data(self):
        if self.df is None:
            print("\nPlease load the dataset first!")
            return

        print("\n========== DATA INFORMATION ==========")
        print("Shape:", self.df.shape)
        print("\nData Types:")
        print(self.df.dtypes)
        print("\nMissing Values:")
        print(self.df.isnull().sum())

    def view_data(self):
        if self.df is None:
            print("\nPlease load the dataset first!")
            return

        print("\n========== DATA PREVIEW ==========")
        print("\nFirst 5 rows:")
        print(self.df.head())

        print("\nLast 5 rows:")
        print(self.df.tail())

    def statistics(self):
        if self.df is None:
            print("\nPlease load the dataset first!")
            return

        sales = np.array(self.df["Sales"])
        profit = np.array(self.df["Profit"])

        print("\n========== SALES STATISTICS ==========")
        print("Total Sales:", round(np.sum(sales), 2))
        print("Total Profit:", round(np.sum(profit), 2))
        print("Average Sales:", round(np.mean(sales), 2))
        print("Average Profit:", round(np.mean(profit), 2))
        print("Best Product:",
              self.df.groupby("Product")["Sales"].sum().idxmax())

    def category_filter(self):
        if self.df is None:
            print("\nPlease load the dataset first!")
            return

        category = input("\nEnter category: ")

        result = self.df[
            self.df["Category"].str.lower() == category.lower()
        ]

        if result.empty:
            print("No records found!")
        else:
            print(result[
                ["Transaction_ID", "Product", "Category", "Sales", "Profit"]
            ].head(10))

    def category_chart(self):
        if self.df is None:
            print("\nPlease load the dataset first!")
            return

        data = self.df.groupby("Category")["Sales"].sum()

        plt.figure(figsize=(8, 5))
        sns.barplot(x=data.index, y=data.values)

        plt.title("Sales by Category")
        plt.xlabel("Category")
        plt.ylabel("Sales")
        plt.xticks(rotation=30)
        plt.show()

    def monthly_chart(self):
        if self.df is None:
            print("\nPlease load the dataset first!")
            return

        data = self.df.groupby(
            ["month_no", "month"]
        )["Sales"].sum().reset_index()

        data = data.sort_values("month_no")

        plt.figure(figsize=(9, 5))
        sns.lineplot(
            data=data,
            x="month",
            y="Sales",
            marker="o"
        )

        plt.title("Monthly Sales")
        plt.xlabel("Month")
        plt.ylabel("Sales")
        plt.xticks(rotation=45)
        plt.show()

    def payment_chart(self):
        if self.df is None:
            print("\nPlease load the dataset first!")
            return

        data = self.df["Payment_Method"].value_counts()

        plt.figure(figsize=(7, 7))
        plt.pie(
            data.values,
            labels=data.index,
            autopct="%1.1f%%"
        )

        plt.title("Payment Methods")
        plt.show()


def menu():
    print("""
========== SALES DATA ANALYZER ==========

1. Load Dataset
2. Dataset Information
3. View Data
4. Sales Statistics
5. Filter by Category
6. Category Sales Chart
7. Monthly Sales Chart
8. Payment Method Chart
9. Exit

=========================================
""")


def main():

    analyzer = SalesDataAnalyzer()

    while True:

        menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            analyzer.load_data()

        elif choice == "2":
            analyzer.check_data()

        elif choice == "3":
            analyzer.view_data()

        elif choice == "4":
            analyzer.statistics()

        elif choice == "5":
            analyzer.category_filter()

        elif choice == "6":
            analyzer.category_chart()

        elif choice == "7":
            analyzer.monthly_chart()

        elif choice == "8":
            analyzer.payment_chart()

        elif choice == "9":
            print("\nGoodbye!")
            break

        else:
            print("\nInvalid choice!")


if __name__ == "__main__":
    main()
