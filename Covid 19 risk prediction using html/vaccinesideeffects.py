import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Define age groups
age_groups = ['0-17', '18-29', '30-39', '40-49', '50-59', '60+']

# Define vaccine side effects
side_effects = [
    'Fever',
    'Fatigue',
    'Headache',
    'Muscle Pain',
    'Joint Pain',
    'Nausea',
    'Chills',
    'Swelling at Injection Site',
]

# Simulate frequency of side effects for each age group
np.random.seed(0)  # For reproducibility
side_effects_data = {
    'Age Group': [],
    'Side Effect': [],
    'Frequency': []
}

for age_group in age_groups:
    for side_effect in side_effects:
        frequency = np.random.randint(5, 100)  # Random frequency between 5 and 100
        side_effects_data['Age Group'].append(age_group)
        side_effects_data['Side Effect'].append(side_effect)
        side_effects_data['Frequency'].append(frequency)

# Create DataFrame
df = pd.DataFrame(side_effects_data)

# Calculate total frequency for each side effect
total_frequency = df.groupby('Side Effect')['Frequency'].sum()

# Plotting
plt.figure(figsize=(10, 8))
plt.pie(total_frequency, labels=total_frequency.index, autopct='%1.1f%%', startangle=140)
plt.title('Vaccine Side Effects Distribution')
plt.axis('equal')  # Equal aspect ratio ensures that pie chart is circular

# Save the plot as a PNG image with the name "vaccine_side_effects_graph.png"
plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.savefig('vaccine_side_effects_graph.png')  # Save as PNG file with specified name

# Show plot
plt.show()
