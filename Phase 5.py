import random
import time

# Simulated IoT health data
def get_iot_data():
    return {
        'heart_rate': random.randint(60, 100),
        'oxygen_level': random.randint(90, 100),
        'body_temp': round(random.uniform(36.0, 38.5), 1)
    }

# Diagnosis logic
def diagnose(symptoms, iot_data):
    if 'fever' in symptoms or iot_data['body_temp'] > 37.5:
        return "You may have a fever or infection. Monitor your temperature and stay hydrated."
    elif 'cough' in symptoms and iot_data['oxygen_level'] < 95:
        return "You may have a respiratory issue. Please consult a doctor."
    elif 'headache' in symptoms and iot_data['heart_rate'] > 90:
        return "High heart rate with headache may indicate stress or high blood pressure."
    elif 'sore throat' in symptoms:
        return "Sore throat detected. Consider warm fluids and monitor for fever."
    elif 'fatigue' in symptoms:
        return "Fatigue detected. Ensure proper rest, hydration, and nutrition."
    else:
        return "Symptoms are unclear. Please seek medical advice."

# Feedback collection
def collect_feedback():
    rating = input("\n[Feedback] How would you rate the assistant's recommendation (1-5)? ")
    print("Thank you for your feedback!")
    return rating

# Main function
def run_healthcare_assistant():
    print("==== Welcome to AI-Powered Healthcare Assistant ====\n")
    
    # Patient Details
    name = input("Enter your full name: ")
    age = input("Enter your age: ")
    gender = input("Enter your gender (M/F/Other): ")
    
    # Symptom Input
    print("\nPlease list your symptoms (e.g., fever, cough, headache, sore throat, fatigue):")
    symptoms = input().lower().replace(" ", "").split(',')

    print("\nCollecting your real-time IoT health data...")
    time.sleep(1)
    iot_data = get_iot_data()

    # Display IoT Data
    print("\n--- IoT Health Data ---")
    print(f"Heart Rate      : {iot_data['heart_rate']} bpm")
    print(f"Oxygen Level    : {iot_data['oxygen_level']}%")
    print(f"Body Temperature: {iot_data['body_temp']}°C")

    # Diagnosis
    recommendation = diagnose(symptoms, iot_data)
    print(f"\n--- AI Diagnosis ---\n{recommendation}")

    # Feedback
    feedback = collect_feedback()

    # Summary
    print("\n--- Patient Summary ---")
    print(f"Name       : {name}")
    print(f"Age        : {age}")
    print(f"Gender     : {gender}")
    print(f"Symptoms   : {', '.join(symptoms)}")
    print(f"Diagnosis  : {recommendation}")
    print(f"Feedback   : {feedback}/5")

# Run the assistant
if __name__== "__main__":
    run_healthcare_assistant()