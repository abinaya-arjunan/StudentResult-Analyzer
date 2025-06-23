import pandas as pd
import matplotlib.pyplot as plt

# 🔗 Your raw GitHub link here
csv_url = r'D:\\student_marks.csv'

# Read CSV
df = pd.read_csv(csv_url)

# Strip column names to remove extra spaces (if any)
df.columns = df.columns.str.strip()

# Debug: check columns
print("Columns in CSV:", df.columns.tolist())

# Convert marks columns to numbers
df["Maths"] = pd.to_numeric(df["Maths"], errors="coerce")
df["Physics"] = pd.to_numeric(df["Physics"], errors="coerce")
df["Chemistry"] = pd.to_numeric(df["Chemistry"], errors="coerce")

# Create ID if not available
if "ID" not in df.columns:
    df["ID"] = range(1001, 1001 + len(df))

# Total, average and pass/fail
df["Total"] = df[["Maths", "Physics", "Chemistry"]].sum(axis=1)
df["Average"] = df["Total"] / 3
df["Status"] = df[["Maths", "Physics", "Chemistry"]].apply(lambda x: "Pass" if all(x >= 40) else "Fail", axis=1)

# 📊 Summary
print("\n--- Student Results Summary ---")
print(df[["ID", "Maths", "Physics", "Chemistry", "Total", "Average", "Status"]].head())

# 🏆 Topper
top_score = df["Total"].max()
top_students = df[df["Total"] == top_score]
print("\n🎉 Topper(s):")
print(top_students[["ID", "Maths", "Physics", "Chemistry", "Total"]])

# 📚 Subject averages
print("\n📈 Subject-wise Average Marks:")
print(df[["Maths", "Physics", "Chemistry"]].mean())

# 🥧 Pass/Fail chart
status_count = df["Status"].value_counts()
plt.figure(figsize=(5, 5))
plt.pie(status_count, labels=status_count.index, autopct='%1.1f%%', startangle=90, colors=["#90ee90", "#ff9999"])
plt.title("Pass vs Fail Distribution")
plt.axis("equal")
plt.show()
