# Project Documentation: Student Performance Analytics System

## 1. Project Title and Student Details
**Project Title:** Student Performance Analytics System  
**Student Name:** [Enter your name]  
**Course:** Python with AI  
**Organization:** EWB Courses  
**Submission Date:** [Enter date]

## 2. Objective
The objective is to build a Python program that reads student marks and attendance from a CSV dataset, analyzes the data, and presents useful performance information such as totals, averages, grades, pass/fail status, subject averages, and top performers.

## 3. Technologies Used
- Python
- Pandas — loading and organizing data in a DataFrame
- NumPy — numerical calculations
- CSV — storing the sample student records
- GitHub — version control and project submission

## 4. Dataset Description
The supplied demonstration dataset contains 20 sample student records. Columns include Student_ID, Name, Department, marks in Python, NumPy, Pandas and Data_Analysis, and Attendance. Replace or personalize sample data only in a way permitted by your trainer; do not upload private student information without permission.

## 5. Implementation
1. `load_data()` reads `students.csv` using `pandas.read_csv()` and checks the required columns and valid ranges.
2. `calculate_grade()` assigns a grade according to the average-mark rule.
3. `is_passed()` uses a loop to check that every subject mark is at least 40.
4. `add_student_results()` converts the subject marks to a NumPy array and calculates each student's total and average. It then adds Grade and Result columns.
5. `show_analysis()` prints student results, class pass/fail counts, class average, highest and lowest averages, subject-wise averages, department averages, and the top five students.
6. The processed DataFrame is saved to `analysis_results.csv`.

## 6. Key Features
- Student data loaded through Pandas
- Numerical operations with NumPy
- Reusable functions, loops and conditions
- Total and average marks
- Grade and pass/fail status
- Class, subject and department analysis
- Top-five student list
- Export of processed results to CSV

## 7. Output / Screenshots
After running `python main.py`, take screenshots of:
- The student-results table
- Class summary and subject-wise averages
- Top-five students and the generated `analysis_results.csv`

Insert your real screenshots here before submission.

## 8. Final Outcome
The program processes the dataset and produces a readable summary of student performance. It helps identify high-performing students, compare subjects and departments, and count students who pass or fail according to the stated rules.

## 9. Challenges and Learning
Edit this section to describe what you personally encountered and learned. Possible topics, if they match your actual experience:
- Installing Pandas and NumPy
- Reading a CSV file with Pandas
- Calculating row-wise values with NumPy
- Writing reusable functions and checking conditions
- Debugging file paths or invalid data

Do not claim challenges you did not experience; write your own experience.

## 10. GitHub Repository
**Repository URL:** [https://github.com/CHHarikeshava/student-performance-analytics.git]

## Grading Rules Used
- A+: average >= 90
- A: average >= 80
- B: average >= 70
- C: average >= 60
- D: average >= 50
- F: average < 50
- Pass: at least 40 marks in every subject; otherwise Fail

These are sample rules chosen for this project. Confirm with your trainer whether they are acceptable.
