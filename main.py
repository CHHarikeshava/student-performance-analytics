
"""
Student Performance Analytics System
Technologies: Python, NumPy, Pandas and Matplotlib

Grading rule:
90-100: A+, 80-89.99: A, 70-79.99: B,
60-69.99: C, 50-59.99: D, below 50: F.

Pass rule: At least 40 marks in every subject.
Attendance does not affect the grade.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

DATA_FILE = "students.csv"
SUBJECTS = ["Python", "NumPy", "Pandas", "Data_Analysis"]
PASS_MARK = 40


def calculate_grade(average):
    """Return a grade based on average marks."""
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
    """Pass only if every subject mark is at least 40."""
    return all(mark >= PASS_MARK for mark in subject_marks)


def load_data(filename):
    """Load and validate student data from a CSV file."""
    df = pd.read_csv(filename)

    required_columns = (
        ["Student_ID", "Name", "Department"]
        + SUBJECTS
        + ["Attendance"]
    )

    missing = [
        column for column in required_columns
        if column not in df.columns
    ]

    if missing:
        raise ValueError(
            f"Missing required column(s) in students.csv: {missing}"
        )

    for column in SUBJECTS + ["Attendance"]:
        df[column] = pd.to_numeric(df[column], errors="raise")

    if df.empty:
        raise ValueError("The CSV file contains no student records.")

    if df[SUBJECTS].isna().any().any():
        raise ValueError("Subject marks cannot be empty.")

    if df[["Attendance"]].isna().any().any():
        raise ValueError("Attendance cannot be empty.")

    if ((df[SUBJECTS] < 0) | (df[SUBJECTS] > 100)).any().any():
        raise ValueError("Subject marks must be between 0 and 100.")

    if ((df["Attendance"] < 0) | (df["Attendance"] > 100)).any().any():
        raise ValueError("Attendance must be between 0 and 100.")

    return df


def add_student_results(df):
    """Calculate total, average, grade and pass/fail."""
    result = df.copy()
    marks_array = result[SUBJECTS].to_numpy(dtype=float)

    result["Total"] = np.sum(marks_array, axis=1)
    result["Average"] = np.round(
        np.mean(marks_array, axis=1), 2
    )

    result["Grade"] = [
        calculate_grade(float(average))
        for average in result["Average"]
    ]

    result["Result"] = [
        "Pass" if is_passed(row) else "Fail"
        for row in marks_array
    ]

    return result


def show_analysis(result):
    """Print student results and class-level analysis."""
    display_columns = [
        "Student_ID", "Name", "Department", "Total",
        "Average", "Grade", "Result", "Attendance"
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
    print(f"Students passed        : {passed}")
    print(f"Students failed        : {failed}")
    print(f"Overall class average  : {result['Average'].mean():.2f}")
    print(f"Highest student average: {result['Average'].max():.2f}")
    print(f"Lowest student average : {result['Average'].min():.2f}")

    topper = result.loc[result["Average"].idxmax()]
    lowest = result.loc[result["Average"].idxmin()]

    print(
        f"\nTop performer          : "
        f"{topper['Name']} ({topper['Average']:.2f})"
    )
    print(
        f"Lowest average         : "
        f"{lowest['Name']} ({lowest['Average']:.2f})"
    )

    print("\nSUBJECT-WISE AVERAGE MARKS")
    subject_averages = result[SUBJECTS].mean().sort_values(
        ascending=False
    )

    for subject, average in subject_averages.items():
        print(f"{subject:16s}: {average:.2f}")

    print(f"Best-performing subject: {subject_averages.index[0]}")

    print("\nDEPARTMENT-WISE AVERAGE")
    department_averages = (
        result.groupby("Department")["Average"].mean().round(2)
    )
    print(department_averages.to_string())

    print("\nTOP 5 STUDENTS")
    top_five = result.nlargest(5, "Average")[
        ["Name", "Department", "Average", "Grade"]
    ]
    print(top_five.to_string(index=False))

    result.to_csv("analysis_results.csv", index=False)
    print("\nFull results saved to: analysis_results.csv")
    print("Note: The dataset is sample data for demonstrating the project.")
      

def plot_student_performance(result):
    """Display a bar chart comparing student average marks."""
    plt.figure(figsize=(10, 5))

    bars = plt.bar(
        result["Name"],
        result["Average"]
    )

    plt.title("Student Performance Comparison")
    plt.xlabel("Student Name")
    plt.ylabel("Average Marks")
    plt.ylim(0, 110)
    plt.xticks(rotation=45)

    # Display each student's average above the bar.
    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            height + 1,
            f"{height:.1f}",
            ha="center",
            va="bottom"
        )

    plt.tight_layout()



def plot_subject_performance(result):
    """Display average marks for each subject."""
    subjects = ["Python", "NumPy", "Pandas", "Data_Analysis"]
    averages = result[subjects].mean()

    plt.figure(figsize=(9, 5))
    bars = plt.bar(averages.index, averages.values)

    plt.title("Average Performance by Subject")
    plt.xlabel("Subject")
    plt.ylabel("Average Marks")
    plt.ylim(0, 110)

    # Display numbers above each bar
    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            height + 1,
            f"{height:.1f}",
            ha="center",
            va="bottom"
        )

    plt.tight_layout()


def plot_pass_fail(result):
    """Display a pie chart of pass and fail counts."""
    counts = result["Result"].value_counts()

    labels = counts.index
    values = counts.values

    plt.figure(figsize=(6, 6))
    plt.pie(
        values,
        labels=labels,
        autopct="%1.1f%%",
        startangle=90
    )

    plt.title("Student Pass vs Fail")
    plt.axis("equal")

def main():
    try:
        data = load_data(DATA_FILE)
        result = add_student_results(data)

        # Print the analysis and save the results.
        show_analysis(result)

        # Create both charts before displaying them.
        plot_student_performance(result)
        plot_subject_performance(result)
        plot_pass_fail(result)
        # Display both chart windows.
        plt.show()

    except FileNotFoundError:
        print(
            "Error: students.csv was not found. "
            "Keep it in the same folder as main.py."
        )
    except (ValueError, KeyError) as error:
        print(f"Could not process the dataset: {error}")


if __name__ == "__main__":
    main()
