def get_symptom_input(symptom_name):
    while True:
        user_input = input(f"{symptom_name}? (Y/N): ").lower()
        if user_input in ['y', 'n']:
            return user_input == 'y'
        print("Invalid input. Please enter 'Y' for Yes or 'N' for No.")

def analyze_symptoms(symptoms, age):
    if symptoms['bleeding'] or symptoms['injury']:
        department = "Emergency Room (ER)"
        advice = "Immediate attention required. Proceed to the ER."
    elif symptoms['chest_pain'] or symptoms['short_breath']:
        department = "Cardiology"
        advice = "Cardiac symptoms detected. Visit Cardiology immediately."
    elif symptoms['high_fever'] and age < 12:
        department = "Pediatrics"
        advice = "High fever in child. Visit Pediatrics urgently."
    elif symptoms['high_fever']:
        department = "General Medicine"
        advice = "Consult a general physician for evaluation."
    elif symptoms['dizziness']:
        department = "Neurology"
        advice = "Neurological symptoms present. Visit Neurology."
    elif symptoms['stomach_pain']:
        department = "Gastroenterology"
        advice = "Visit a gastroenterologist for further diagnosis."
    else:
        department = "Outpatient (OPD)"
        advice = "No critical symptoms. You may proceed to OPD."
    return department, advice

def triage_system():
    print("=== Hospital Expert System: Patient Triage Assistant ===")

    name = input("Enter Patient Name: ")
    try:
        age = int(input("Enter Age: "))
    except ValueError:
        print("Invalid age input. Please enter a valid number.")
        return

    print("\nSelect Symptoms (Y/N):")
    symptoms = {
        'chest_pain': get_symptom_input("Chest Pain"),
        'short_breath': get_symptom_input("Shortness of Breath"),
        'bleeding': get_symptom_input("Heavy Bleeding"),
        'high_fever': get_symptom_input("High Fever"),
        'injury': get_symptom_input("Recent Injury"),
        'dizziness': get_symptom_input("Dizziness or Fainting"),
        'stomach_pain': get_symptom_input("Severe Stomach Pain")
    }

    print("\nAnalyzing symptoms...")

    department, advice = analyze_symptoms(symptoms, age)

    print(f"\n=== Patient Report ===")
    print(f"Name: {name}")
    print(f"Recommended Department: {department}")
    print(f"Advice: {advice}")

if __name__ == "__main__":
    triage_system()
