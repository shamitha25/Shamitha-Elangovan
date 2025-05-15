def get_symptom_severity(symptom):
    critical_symptoms = ['chest pain', 'shortness of breath', 'unconsciousness', 'severe bleeding']
    moderate_symptoms = ['fever', 'persistent cough', 'vomiting', 'rash', 'headache']

    if symptom.lower() in critical_symptoms:
        return 'critical'
    elif symptom.lower() in moderate_symptoms:
        return 'moderate'
    else:
        return 'mild'

def triage():
    print("Welcome to the AI Health Assistant")
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    symptoms = input("Describe your main symptom: ").strip()

    severity = get_symptom_severity(symptoms)

    print(f"\n{name}, based on the symptom '{symptoms}':")

    if severity == 'critical':
        print("This could be a critical condition. Please seek emergency medical attention immediately.")
    elif severity == 'moderate':
        print("This may require a doctor's consultation. Schedule a visit or use telehealth services.")
    else:
        print("It seems mild. Home remedies and rest may be sufficient. Monitor your symptoms.")

    print("\nNote: This is not a professional diagnosis. Always consult a doctor if unsure.")

# Run the program
triage()