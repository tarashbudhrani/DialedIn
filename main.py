import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import streamlit as st

# title of our page
st.title("Demo Analytics App")

# header
st.header("Value counts of cat columns")

def univariate_categorical_analysis(ser: pd.Series, show_categories=False, top_k=5, figsize=(12,8)):
    """
    It performs univariate analysis on categorical variables.
    """
    # # number of unique values
    # num_unique_values = ser.nunique()
    # print(f"The number of unique values in {ser.name} are: {num_unique_values}", end="\n\n")

    # # unique categories in the data
    # if show_categories:
    #     unique_categories = ser.unique().tolist()
    #     for i, category in enumerate(unique_categories, start=1):
    #         print(f"{i}.: {category}")

    # value counts
    value_counts_in_num = ser.value_counts()
    value_counts_in_per = ser.value_counts(normalize=True).mul(100).round(2)
    value_counts_info = pd.concat([value_counts_in_num, value_counts_in_per], axis=1)
    # if top_k:
    #     display(value_counts_info.head(top_k))
    # else:
    #     display(value_counts_info)

    # # missing values
    # missing_values = ser.isna().sum()
    # print(f"\nThe number of missing values in {ser.name} are: {missing_values}", end="\n\n\n")

    if top_k:
        top_cat = value_counts_info.head(top_k).index.to_list()
        filtered_ser = ser.loc[ser.isin(top_cat)]

    # plotting
    fig, ax = plt.subplots(2,1,figsize=figsize)
    # count plot
    ax[0].set_title(f"Countplot of {ser.name}")
    sns.countplot(x=filtered_ser, ax=ax[0],)
    # pie chart
    ax[1].set_title(f"Pie chart of {ser.name}")
    value_counts_in_num.head(top_k).plot(kind="pie", ax=ax[1], autopct="%0.2f%%")
    plt.tight_layout()
    return fig


# load the data
data_path = "./data/smartphones_data.csv"

df = pd.read_csv(data_path)

# first 10 rows of data
st.dataframe(data=df.head(10))

# sample dict
sample_dict = {1: {
    "name": "Mukesh",
    "age": 30,
    "city": "Mumbai"
},
    2: {
        "name": "Rahul",
        "age": 23,
        "city": "Pune"
    },
    3: {
        "name": "Anaya",
        "age": 27,
        "city": "Indore"
    }}

# display as json
st.json(sample_dict, expanded=True)

figure = univariate_categorical_analysis(df["memory"])

# plot graph
st.pyplot(figure)