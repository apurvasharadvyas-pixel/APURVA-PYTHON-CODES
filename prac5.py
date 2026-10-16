
import pandas as pd

# 1. Create a Series
print("1. CREATE SERIES")
s = pd.Series([10, 20, 30, 40, 50])
print(s)

# 2. Create a DataFrame
print("\n2. CREATE DATAFRAME")
data = {
    "Name": ["Amit", "Priya", "Rahul"],
    "Age": [20, 21, 19],
    "Marks": [85, 90, 78]
}
df = pd.DataFrame(data)
print(df)

# 3. Import CSV file
print("\n3. IMPORT CSV FILE")
# Create a sample CSV file
df.to_csv("students.csv", index=False)

# Read CSV file
df = pd.read_csv("students.csv")
print(df)

# 4. Display first and last rows
print("\n4. FIRST FIVE ROWS")
print(df.head())

print("\nLAST FIVE ROWS")
print(df.tail())

# 5. Display DataFrame information
print("\n5. SHAPE")
print(df.shape)

print("\nCOLUMN NAMES")
print(df.columns)

print("\nDATA TYPES")
print(df.dtypes)

print("\nSUMMARY")
print(df.describe())

# 6. Select columns
print("\n6. SELECT NAME COLUMN")
print(df["Name"])

print("\nSELECT NAME AND MARKS")
print(df[["Name", "Marks"]])

# 7. Select rows
print("\n7. FIRST ROW")
print(df.iloc[0])

# 8. Filter records
print("\n8. MARKS GREATER THAN 80")
print(df[df["Marks"] > 80])

# 9. Add a new column
print("\n9. ADD GRADE COLUMN")
df["Grade"] = ["B", "A", "C"]
print(df)

# 10. Modify a column
print("\n10. INCREASE MARKS BY 5")
df["Marks"] = df["Marks"] + 5
print(df)

# 11. Sort DataFrame
print("\n11. SORT BY MARKS")
print(df.sort_values(by="Marks", ascending=False))

# 12. Basic Series operations
print("\n12. SERIES OPERATIONS")
s = pd.Series([10, 20, 30, 40, 50])
print("Sum:", s.sum())
print("Mean:", s.mean())
print("Maximum:", s.max())
print("Minimum:", s.min())

# 13. Check missing values
print("\n13. MISSING VALUES")
print(df.isnull().sum())

# 14. Save DataFrame to CSV
df.to_csv("result.csv", index=False)
print("\nData saved to result.csv")
