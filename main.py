"""
Student Performance Analytics System
Technologies: Python, NumPy and Pandas

Grading rule (based on average marks):
90-100: A+, 80-89.99: A, 70-79.99: B, 60-69.99: C,
50-59.99: D, below 50: F.
Pass rule: at least 40 marks in every subject.
Attendance is shown separately and does not affect the grade.
"""

import numpy as np
import pandas as pd

DATA_FILE = "students.csv"
SUBJECTS = ["Python", "NumPy", "Pandas", "Data_Analysis"]
PASS_MARK = 40


def calculate_grade(average):
    """Return a grade based on the student's average marks."""
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    return "F"


def is_passed(subject_marks):
    """A student passes only if every subject mark is at least 40."""
    for mark in subject_marks:
        if mark < PASS_MARK:
            return False
    return True


def load_data(filename):
    """Read the CSV file into a Pandas DataFrame and validate its columns."""
    df = pd.read_csv(filename)
    required_columns = ["Student_ID", "Name", "Department"] + SUBJECTS + ["Attendance"]
    missing = [column for column in required_columns if column not in df.columns]
    if missing:
        raise ValueError(f"Missing required column(s) in students.csv: {missing}")

    # Convert marks and attendance to numeric values.
    for column in SUBJECTS + ["Attendance"]:
        df[column] = pd.to_numeric(df[column], errors="raise")

    if df[SUBJECTS].isna().any().any():
        raise ValueError("Subject marks cannot be empty.")
    if ((df[SUBJECTS] < 0) | (df[SUBJECTS] > 100)).any().any():
        raise ValueError("Subject marks must be between 0 and 100.")
    if ((df["Attendance"] < 0) | (df["Attendance"] > 100)).any():
        raise ValueError("Attendance must be between 0 and 100.")

    return df


def add_student_results(df):
    """Calculate total, average, grade and pass/fail for every student."""
    result = df.copy()
    marks_array = result[SUBJECTS].to_numpy(dtype=float)

    # NumPy performs row-wise calculations across the subject marks.
    result["Total"] = np.sum(marks_array, axis=1)
    result["Average"] = np.round(np.mean(marks_array, axis=1), 2)

    grades = []
    statuses = []
    for row in marks_array:
        grades.append(calculate_grade(float(np.mean(row))))
        statuses.append("Pass" if is_passed(row) else "Fail")

    result["Grade"] = grades
    result["Result"] = statuses
    return result


def show_analysis(result):
    """Print student results and class-level analysis."""
    display_columns = [
        "Student_ID", "Name", "Department", "Total", "Average",
        "Grade", "Result", "Attendance"
    ]

    print("\n" + "=" * 76)
    print("       STUDENT PERFORMANCE ANALYTICS SYSTEM")
    print("=" * 76)
    print(f"\nNumber of students: {len(result)}")
    print("\nSTUDENT RESULTS")
    print(result[display_columns].to_string(index=False))

    passed = int((result["Result"] == "Pass").sum())
    failed = int((result["Result"] == "Fail").sum())
    print("\nCLASS SUMMARY")
    print("-" * 40)
    print(f"Students passed       : {passed}")
    print(f"Students failed       : {failed}")
    print(f"Overall class average : {result['Average'].mean():.2f}")
    print(f"Highest student average: {result['Average'].max():.2f}")
    print(f"Lowest student average : {result['Average'].min():.2f}")

    topper = result.loc[result["Average"].idxmax()]
    lowest = result.loc[result["Average"].idxmin()]
    print(f"\nTop performer         : {topper['Name']} ({topper['Average']:.2f})")
    print(f"Lowest average        : {lowest['Name']} ({lowest['Average']:.2f})")

    print("\nSUBJECT-WISE AVERAGE MARKS")
    subject_averages = result[SUBJECTS].mean().sort_values(ascending=False)
    for subject, average in subject_averages.items():
        print(f"{subject:16s}: {average:.2f}")
    print(f"Best-performing subject: {subject_averages.index[0]}")

    print("\nDEPARTMENT-WISE AVERAGE")
    department_averages = result.groupby("Department")["Average"].mean().round(2)
    print(department_averages.to_string())

    print("\nTOP 5 STUDENTS")
    top_five = result.nlargest(5, "Average")[["Name", "Department", "Average", "Grade"]]
    print(top_five.to_string(index=False))

    # Save a results file so the analysis can be shared without running the code.
    result.to_csv("analysis_results.csv", index=False)
    print("\nFull results saved to: analysis_results.csv")
    print("\nNote: The dataset is sample data for demonstrating the project.")


def main():
    try:
        data = load_data(DATA_FILE)
        result = add_student_results(data)
        show_analysis(result)
    except FileNotFoundError:
        print("Error: students.csv was not found. Keep it in the same folder as main.py.")
    except (ValueError, KeyError) as error:
        print(f"Could not process the dataset: {error}")


if __name__ == "__main__":
    main()
