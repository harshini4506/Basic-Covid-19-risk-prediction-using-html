import matplotlib.pyplot as plt

# Function to display the organs affected by COVID-19 and plot a graph
def display_affected_organs():
    # Data for the affected organs
    affected_organs = {
        "Lungs": 80,
        "Heart": 60,
        "Kidneys": 50,
        "Liver": 40,
        "Brain": 30,
        "Intestines": 25,
        "Skin": 20,
    }

    # Print the affected organs
    print("Organs Most Affected by COVID-19:\n")
    for organ, severity in affected_organs.items():
        print(f"{organ}: Severity Level {severity}")

    # Plotting the graph
    organs = list(affected_organs.keys())
    severity_levels = list(affected_organs.values())
    plt.figure(figsize=(10, 6))
    plt.barh(organs, severity_levels, color='skyblue')
    plt.xlabel('Severity Level')
    plt.title('Organs Most Affected by COVID-19')
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.xlim(0, 100)  # Assuming severity levels are out of 100

    # Save the figure
    output_path = 'C:/Users/Dell/OneDrive/Pictures/Desktop/FDS project/affected_organs_graph.png'  # Set the output path
    plt.savefig(output_path)  # Save the graph as a PNG file
    plt.show()

# Run the function to display the organs and plot the graph
if __name__ == "__main__":
    display_affected_organs()
