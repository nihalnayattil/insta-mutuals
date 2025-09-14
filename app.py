import pandas as pd
import streamlit as st

# -----------------------------
# Input Excel files for two accounts
# -----------------------------
file1 = "account1_following.xlsx"  # Following list of account 1
file2 = "account2_following.xlsx"  # Following list of account 2

# -----------------------------
# Load Excel files into Pandas DataFrames
# -----------------------------
df1 = pd.read_excel(file1)
df2 = pd.read_excel(file2)

# -----------------------------
# Find mutual accounts based on "User Name"
# 'how="inner"' keeps only rows present in both DataFrames
# 'suffixes' distinguishes columns from each account
# -----------------------------
mutuals = pd.merge(df1, df2, on="User Name", how="inner", suffixes=("_a1", "_a2"))

# -----------------------------
# Select only the columns we want to keep
# Some columns may not exist, so check dynamically
# -----------------------------
columns_to_keep = ["ID", "Full Name", "Profile Url", "Avatar", "Verified"]
selected_columns = []

for col in columns_to_keep:
    matched_col = f"{col}_a1"  # Pick the column from account1 as reference
    if matched_col in mutuals.columns:
        selected_columns.append(matched_col)

# Always include the User Name
selected_columns = ["User Name"] + selected_columns

# Create a clean DataFrame with only selected columns
mutuals_clean = mutuals[selected_columns]

# -----------------------------
# Rename columns to a clean, consistent format
# -----------------------------
rename_map = {
    "User Name": "User Name",
    "ID_a1": "ID",
    "Full Name_a1": "Full Name",
    "Profile Url_a1": "Profile Url",
    "Avatar_a1": "Avatar",
    "Verified_a1": "Verified"
}
mutuals_clean = mutuals_clean.rename(columns=rename_map)

# Reorder columns for better display
mutuals_clean = mutuals_clean[["ID", "User Name", "Full Name", "Profile Url", "Avatar", "Verified"]]

# -----------------------------
# Optional: sort mutual accounts by ID
# -----------------------------
mutuals_clean = mutuals_clean.sort_values(by="ID")

# -----------------------------
# Streamlit UI setup
# -----------------------------
st.set_page_config(page_title="Mutual Followers Finder", layout="wide")
st.title("👥 Mutual Followers Finder")

# Show total number of mutual accounts
st.write(f"Total mutual accounts: **{len(mutuals_clean)}**")

# Display the DataFrame in an interactive table
st.dataframe(mutuals_clean, use_container_width=True)
