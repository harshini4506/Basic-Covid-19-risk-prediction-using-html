import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os  # Import os to check folder existence

def generate_symptom_prevalence_graph():
    # Define COVID-19 symptoms and their prevalence
    symptoms = [
        'Fever',
        'Cough',
        'Fatigue',
        'Shortness of breath',
        'Loss of taste or smell',
        'Sore throat',
        'Headache',
        'Muscle or joint pain',
        'Chills',
        'Congestion or runny nose',
    ]

    # Simulate the prevalence of symptoms (random values for demonstration)
    np.random.seed(0)  # For reproducibility
    symptom_prevalence = np.random.randint(10, 100, size=len(symptoms))  # Random values between 10 and 100

    # Create DataFrame
    df = pd.DataFrame({
        'Symptom': symptoms,
        'Prevalence': symptom_prevalence
    })

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.barh(df['Symptom'], df['Prevalence'], color='lightcoral')
    plt.title('Prevalence of COVID-19 Symptoms')
    plt.xlabel('Number of Patients Experiencing Symptoms')
    plt.ylabel('Symptoms')
    plt.grid(axis='x', linestyle='--', alpha=0.7)

    # Define output path (same format as your confirmed cases graph)
    output_path = r'C:\Users\Dell\OneDrive\Pictures\Desktop\FDS project\symptom_prevalence_graph.png'

    # Ensure the directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Save the plot as a PNG image
    plt.tight_layout()  # Adjust layout to prevent clipping of labels
    plt.savefig(output_path, dpi=300)  # Save with a higher dpi for better quality
    plt.show()

if __name__ == "__main__":
    generate_symptom_prevalence_graph()
