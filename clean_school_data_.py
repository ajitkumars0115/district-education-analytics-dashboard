"""
School Details Data Cleaning & Anonymization Script
-----------------------------------------------------
This script cleans raw School Details data and removes/anonymizes
sensitive personal information (names, phone numbers, emails) so
the data can be safely used in a GitHub/portfolio project.

ONLY THESE NEED TO BE CHANGED:
1. INPUT_FILE    -> path to your raw Excel file
2. OUTPUT_FOLDER -> folder where the cleaned file will be saved
"""

import pandas as pd
import os

# ============================================
# STEP 1: SET YOUR FILE PATH HERE
# ============================================
INPUT_FILE = "school_details.xlsx"        # <-- set your file name/path here
OUTPUT_FOLDER = "cleaned_data"             # <-- output folder name

# ============================================
# STEP 2: LOAD THE RAW DATA
# ============================================
print(f"Reading file: {INPUT_FILE}")
df = pd.read_excel(INPUT_FILE)

print("Original shape:", df.shape)
print("Original columns:")
for col in df.columns:
    print(" -", col)

# ============================================
# STEP 3: DROP SENSITIVE / UNUSED COLUMNS
# ============================================
# You can edit this list if you want to keep or drop
# any additional column
columns_to_drop = [
    'SL#',
    'Head Of School',
    'Head Of School Number',
    'Respodent Type ',
    'Respodent  Name',
    'Respodent  Number',
    'HOS Email',
    'Parliamentary Name',
    'Assembly Name',
    'School Udise Code',
    'School Uschcd Code',
]

# Only drop columns that actually exist in the file
# (avoids errors if a column name is slightly different)
columns_to_drop = [c for c in columns_to_drop if c in df.columns]
df_clean = df.drop(columns=columns_to_drop)

print("\nDropped columns:", columns_to_drop)

# ============================================
# STEP 4: ANONYMIZE SCHOOL NAME
# ============================================
if 'School Name' in df_clean.columns:
    unique_schools = df_clean['School Name'].unique()
    school_mapping = {name: f"School_{i+1}" for i, name in enumerate(unique_schools)}
    df_clean['School Name'] = df_clean['School Name'].map(school_mapping)
    print(f"\n{len(unique_schools)} unique schools anonymized (School_1, School_2, ...)")

# ============================================
# STEP 5: CREATE A CLEAN SCHOOL_ID (FOR SQL JOINS)
# ============================================
df_clean.insert(0, 'School_ID', range(1, len(df_clean) + 1))

# ============================================
# STEP 6: CHECK DUPLICATE ROWS AND MISSING VALUES
# ============================================
duplicate_count = df_clean.duplicated().sum()
print(f"\nDuplicate rows found: {duplicate_count}")
if duplicate_count > 0:
    df_clean = df_clean.drop_duplicates()
    print("Duplicates removed.")

print("\nMissing values per column:")
print(df_clean.isnull().sum()[df_clean.isnull().sum() > 0])

# ============================================
# STEP 7: SAVE THE CLEANED DATA
# ============================================
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

output_xlsx = os.path.join(OUTPUT_FOLDER, "school_details_clean.xlsx")
output_csv = os.path.join(OUTPUT_FOLDER, "school_details_clean.csv")

df_clean.to_excel(output_xlsx, index=False)
df_clean.to_csv(output_csv, index=False)

print(f"\nCleaned shape: {df_clean.shape}")
print(f"Cleaned columns: {list(df_clean.columns)}")
print(f"\nFiles saved:")
print(f" - {output_xlsx}")
print(f" - {output_csv}")
print("\nDone! You can now load this cleaned file into SQL Server / Power BI.")
