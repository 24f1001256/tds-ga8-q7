# Employee Performance Analysis
# Email for verification: 24f1001256@ds.study.iitm.ac.in

import pandas as pd
import matplotlib.pyplot as plt
import mpld3

# -------------------------------
# 1. LOAD EMPLOYEE DATA
# -------------------------------
data = """employee_id,department,region,performance_score,years_experience,satisfaction_rating
EMP001,IT,Africa,85.94,14,3.1
EMP002,Sales,Latin America,77.79,14,3.4
EMP003,Operations,Africa,60.81,11,3.9
EMP004,Marketing,North America,60.97,2,3.7
EMP005,R&D,North America,87.44,10,3.4
EMP006,Finance,Europe,91.12,12,4.1
EMP007,Finance,Asia,88.55,7,3.8
EMP008,Finance,Africa,72.44,5,3.5
EMP009,IT,Asia,69.21,9,4.2
EMP010,Marketing,Europe,75.90,6,3.6
"""

with open("employee_data.csv", "w") as f:
    f.write(data)

df = pd.read_csv("employee_data.csv")

# -------------------------------
# 2. CALCULATE FINANCE FREQUENCY
# -------------------------------
finance_count = (df["department"] == "Finance").sum()

# Print frequency to the console
print("Frequency count for Finance department:", finance_count)

# -------------------------------
# 3. CREATE HISTOGRAM OF DEPARTMENTS
# -------------------------------
plt.figure(figsize=(8,5))
df["department"].value_counts().plot(kind="bar")
plt.title("Distribution of Employees Across Departments")
plt.xlabel("Department")
plt.ylabel("Count")

# -------------------------------
# 4. SAVE THE PLOT AS HTML
# -------------------------------
html_output = mpld3.fig_to_html(plt.gcf())

with open("employee_visualization.html", "w") as f:
    f.write(html_output)

print("HTML file 'employee_visualization.html' generated successfully!")
