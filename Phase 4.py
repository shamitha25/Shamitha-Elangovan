# Simple AI Diagnosis and Treatment System

# Step 1: Get symptoms from the user
symptoms_input = input("Enter your symptoms (comma-separated): ").lower().split(',')

# Step 2: Diagnose based on symptoms
def diagnose(symptoms):
    if 'fever' in symptoms and 'cough' in symptoms:
        return "Flu"
    elif 'headache' in symptoms and 'blurred vision' in symptoms:
        return "Migraine"
    elif 'chest pain' in symptoms and 'shortness of breath' in symptoms:
        return "Heart Issue"
    else:
        return "Unknown Condition - Please consult a doctor."

# Step 3: Get wearable IoT data (simulated)
def get_wearable_data():
    return {
        'heart_rate': 85,
        'oxygen_level': 96,
        'temperature': 99.1
    }

# Step 4: Suggest treatment based on diagnosis and IoT data
def suggest_treatment(diagnosis, iot_data):
    if diagnosis == "Flu":
        return "Rest, drink fluids, and consider paracetamol."
    elif diagnosis == "Migraine":
        return "Take pain relievers and rest in a dark room."
    elif diagnosis == "Heart Issue":
        if iot_data['heart_rate'] > 100:
            return "Seek emergency medical attention immediately."
        else:
            return "Visit a cardiologist for detailed diagnosis."
    else:
        return "No treatment suggestion available."

# Run the diagnosis system
diagnosis = diagnose(symptoms_input)
iot_data = get_wearable_data()
treatment = suggest_treatment(diagnosis, iot_data)

# Step 5: Show the results
print("\nDiagnosis:", diagnosis)
print("IoT Data:", iot_data)
print("Treatment Suggestion:", treatment)