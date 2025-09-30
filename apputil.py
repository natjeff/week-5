import plotly.express as px
import pandas as pd

# update/add code below ...

#Exercise 1:
def survival_demographics(df: pd.DataFrame) -> pd.DataFrame:
    """
    Analyze Titanic survival patterns by class, sex, and age group.
    """

    # Step 1: Add AgeGroup column
    age_bins = [0, 12, 19, 59, float("inf")]
    age_labels = ["Child", "Teen", "Adult", "Senior"]

    df["AgeGroup"] = pd.cut(
        df["Age"], bins=age_bins, labels=age_labels, right=True
    )

    # Step 2 & 3: Group by class, sex, and age group
    grouped = df.groupby(["Pclass", "Sex", "AgeGroup"]).agg(
        n_passengers=("Survived", "count"),
        n_survivors=("Survived", "sum")
    )
    grouped["survival_rate"] = grouped["n_survivors"] / grouped["n_passengers"]

    # Step 4: Establish combinations
    all_combinations = pd.MultiIndex.from_product(
        [df["Pclass"].unique(),
         df["Sex"].unique(),
         df["AgeGroup"].cat.categories],
        names=["Pclass", "Sex", "AgeGroup"]
    )
    grouped = grouped.reindex(all_combinations, fill_value=0).reset_index()

    # Step 5: Sort results
    grouped = grouped.sort_values(by=["Pclass", "Sex", "AgeGroup"]).reset_index(drop=True)

    return grouped

# Read and display results
df = pd.read_csv('https://raw.githubusercontent.com/leontoddjohnson/datasets/main/data/titanic.csv')
results = survival_demographics(df)
print(results.head(12))



#Exercise 2:

def family_groups(df: pd.DataFrame) -> pd.DataFrame:
    """
    Explore the relationship between family size, passenger class, and ticket fare.     
    """
    # Step 1: Create family_size column
    df["family_size"] = df["SibSp"] + df["Parch"] + 1

    # Step 2 & 3: Group and aggregate
    grouped = df.groupby(["Pclass", "family_size"]).agg(
        n_passengers=("Fare", "count"),
        avg_fare=("Fare", "mean"),
        min_fare=("Fare", "min"),
        max_fare=("Fare", "max")
    ).reset_index()

    # Step 4: Sort
    grouped = grouped.sort_values(by=["Pclass", "family_size"]).reset_index(drop=True)

    return grouped


def last_names(df: pd.DataFrame) -> pd.Series:
    """
    Extract last names from the Titanic dataset and count their occurrences.
    """
    # Extract last name and count occurrences
    df["LastName"] = df["Name"].str.split(",").str[0].str.strip()
    last_name_counts = df["LastName"].value_counts()

    return last_name_counts


df = pd.read_csv("https://raw.githubusercontent.com/leontoddjohnson/datasets/main/data/titanic.csv")

# Family Groups
family_results = family_groups(df)
print(family_results.head(10))

# Last Names
surname_counts = last_names(df)
print(surname_counts.head(10))
