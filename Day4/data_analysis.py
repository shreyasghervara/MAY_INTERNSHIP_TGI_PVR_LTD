# student_csv_chart.py

import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------------
# STEP 1: CREATE CSV FILE
# -----------------------------------

print("Create Student Dataset")

num = int(input("Enter number of students: "))

names = []
math_marks = []
science_marks = []
english_marks = []

for i in range(num):
    print(f"\nEnter details for Student {i+1}")

    name = input("Name: ")
    math = int(input("Math Marks: "))
    science = int(input("Science Marks: "))
    english = int(input("English Marks: "))

    names.append(name)
    math_marks.append(math)
    science_marks.append(science)
    english_marks.append(english)

# Create DataFrame
data = {
    "Name": names,
    "Math": math_marks,
    "Science": science_marks,
    "English": english_marks
}

df = pd.DataFrame(data)

# Save CSV file
csv_file = "students.csv"
df.to_csv(csv_file, index=False)

print(f"\nCSV file '{csv_file}' created successfully!")

# -----------------------------------
# STEP 2: READ CSV FILE
# -----------------------------------

print("\nReading CSV File...\n")

df = pd.read_csv(csv_file)

print(df)

# -----------------------------------
# STEP 3: ANALYZE DATA
# -----------------------------------

print("\nSummary Statistics:\n")
print(df.describe())

# -----------------------------------
# STEP 4: GENERATE CHART
# -----------------------------------

# Set Name column as index
chart_df = df.set_index("Name")

# Create bar chart
chart_df.plot(
    kind="bar",
    figsize=(10, 6),
    title="Student Marks Chart"
)

plt.xlabel("Students")
plt.ylabel("Marks")
plt.xticks(rotation=0)
plt.tight_layout()

# Save chart image
chart_image = "student_marks_chart.png"
plt.savefig(chart_image)

print(f"\nChart saved as '{chart_image}'")

# Show chart
plt.show()

# -----------------------------------
# STEP 5: SAVE CHART INFO INTO CSV
# -----------------------------------

# Add chart filename column into CSV
df["Chart_File"] = chart_image

# Save updated CSV
updated_csv = "students_with_chart.csv"
df.to_csv(updated_csv, index=False)

print(f"\nUpdated CSV saved as '{updated_csv}'")