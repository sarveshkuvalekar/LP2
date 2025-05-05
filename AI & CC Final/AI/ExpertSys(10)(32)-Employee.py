def get_performance_input(category):
    while True:
        try:
            score = int(input(f"{category} (1: Poor, 5: Excellent): "))
            if 1 <= score <= 5:
                return score
            else:
                print("Invalid input! Please enter a score between 1 and 5.")
        except ValueError:
            print("Invalid input! Please enter an integer value between 1 and 5.")

def evaluate_employee():
    print("=== Expert System: Employee Performance Evaluation ===")
    
    name = input("Enter Employee Name: ")
    role = input("Enter Role/Department: ")

    # Ensure that the role is not empty
    if not role.strip():
        print("Role/Department cannot be empty.")
        return

    print("\nRate the following on a scale of 1 (Poor) to 5 (Excellent):")
    teamwork = get_performance_input("Teamwork")
    punctuality = get_performance_input("Punctuality")
    task_completion = get_performance_input("Task Completion")
    communication = get_performance_input("Communication Skills")
    problem_solving = get_performance_input("Problem Solving")
    leadership = get_performance_input("Leadership (if applicable, else rate as 3)")

    total_score = teamwork + punctuality + task_completion + communication + problem_solving + leadership
    average_score = total_score / 6

    if average_score >= 4.5:
        remark = "Outstanding"
        suggestion = "Keep up the great work. Consider for leadership roles or promotions."
    elif average_score >= 3.5:
        remark = "Good"
        suggestion = "Consistent performance. Minor improvements will boost further."
    elif average_score >= 2.5:
        remark = "Average"
        suggestion = "Needs improvement in some areas. Consider targeted training."
    else:
        remark = "Below Average"
        suggestion = "Immediate attention needed. Schedule a performance review and support plan."

    print("\n=== Performance Report ===")
    print(f"Employee Name: {name}")
    print(f"Department/Role: {role}")
    print(f"Average Score: {average_score:.2f}/5")
    print(f"Performance Remark: {remark}")
    print(f"Recommendation: {suggestion}")

if __name__ == "__main__":
    evaluate_employee()
