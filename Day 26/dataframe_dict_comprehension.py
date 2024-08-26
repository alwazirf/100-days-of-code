# Working dictionary comprehension with pandas DataFrame
import pandas as pd

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

students_data_frame = pd.DataFrame(student_dict)
# print(students_data_frame)

# Loop through a data frame
# for (key, value) in students_data_frame.items():
#     print(value)

for (index, row) in students_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)