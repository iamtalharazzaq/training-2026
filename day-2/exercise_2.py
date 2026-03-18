# Random data for 5 students
students = [
    {"name": "Alice", "scores": [85, 92, 78], "subject": "Math"},
    {"name": "Bob", "scores": [72, 68, 74], "subject": "Chemistry"},
    {"name": "Charlie", "scores": [95, 90, 93], "subject": "English"},
    {"name": "David", "scores": [60, 65, 58], "subject": "Math"},
    {"name": "Eva", "scores": [88, 84, 91], "subject": "Physics"},
    {"name": "Josh", "scores": [23, 15, 16], "subject": "Computer"}
]

# Function: calculate average
def calculate_average(scores):
    return sum(scores) / len(scores)

# Function: get grade
def get_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "D"

# Function: find class topper
def class_topper(students_list):
    averages = [(s['name'], calculate_average(s['scores'])) for s in students_list]
    averages.sort(key=lambda x: x[1], reverse=True)
    return averages[0]  # (name, avg)

# Function: generate and print report
def generate_report(students_list):
    # Compute student reports
    student_reports = []
    for s in students_list:
        avg = calculate_average(s['scores'])
        grade = get_grade(avg)
        student_reports.append({"name": s['name'], "avg": avg, "grade": grade})

    # Find topper
    topper_name, _ = class_topper(students_list)

    # Sort by average descending
    sorted_report = sorted(student_reports, key=lambda x: x['avg'], reverse=True)

    # Print formatted report
    print(f"{'Student Name':<12} | {'Average':<7} | {'Grade'}")
    print("-" * 34)
    for student_report in sorted_report:
        mark = " *** TOP ***" if student_report['name'] == topper_name else ""
        print(f"{student_report['name']:<12} | {student_report['avg']:<7.2f} | {student_report['grade']}{mark}")


# Call the function to print report
generate_report(students)