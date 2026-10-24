# Student Performance Analytics System

A beginner-friendly Python data-analysis mini project using Python, NumPy and Pandas.

## Features
- Reads 20 sample student records from `students.csv`
- Calculates each student's total and average marks
- Assigns grades using a clearly defined grading rule
- Checks pass/fail (at least 40 in every subject)
- Finds class averages, highest/lowest average, top five students
- Calculates subject-wise and department-wise averages
- Saves complete processed results to `analysis_results.csv`

## Files
- `main.py` — main program
- `students.csv` — sample dataset (replace with approved/anonymized data if required)
- `requirements.txt` — Python packages
- `PROJECT_DOCUMENTATION.md` — report template/content

## Requirements
Python 3.10 or newer is recommended.

## Run the project
1. Install Python.
2. Open a terminal in this folder.
3. Install packages:
   ```bash
   python -m pip install -r requirements.txt
   ```
4. Run:
   ```bash
   python main.py
   ```
5. Check the terminal output and the generated `analysis_results.csv`.

On some Windows systems, use `py` instead of `python`.

## Grading rules
- A+: average >= 90
- A: average >= 80
- B: average >= 70
- C: average >= 60
- D: average >= 50
- F: average < 50

A student passes only if they score at least 40 in every subject. Attendance is reported separately and does not affect the grade in this sample project.

## Important
The included data is sample data for demonstration. Review the grading/pass rules with your trainer and personalize the project before submission. Understand and be able to explain the code; do not submit blindly.
