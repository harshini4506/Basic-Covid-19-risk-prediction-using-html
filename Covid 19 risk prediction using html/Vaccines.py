import pandas as pd
import matplotlib.pyplot as plt

def generate_vaccine_usage_graph():
    # Load the dataset
    file_path = r'C:\Users\Dell\OneDrive\Desktop\python programmes FDS\COVID19_Age_Group_Analysis_with_Additional_Columns (1)vaccine.csv'
    data = pd.read_csv(file_path)

    # Check columns to confirm 'Vaccine' column exists
    print("Columns in the dataset:", data.columns)
    
    # Group by vaccine and count occurrences
    vaccine_counts = data['Vaccine'].value_counts().reset_index()
    vaccine_counts.columns = ['Vaccine', 'Count']  # Rename columns for clarity

    # Plotting vaccine usage
    plt.figure(figsize=(10, 6))
    plt.bar(vaccine_counts['Vaccine'], vaccine_counts['Count'], color='lightblue')
    plt.xlabel('Vaccine')
    plt.ylabel('Number of Uses')
    plt.title('COVID-19 Vaccine Usage')
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    plt.tight_layout()

    # Save the vaccine usage graph as a PNG file
    vaccine_graph_path = 'C:/Users/Dell/OneDrive/Pictures/Desktop/FDS project/vaccine_usage_graph.png'
    plt.savefig(vaccine_graph_path)
    plt.show()

if __name__ == "__main__":
    generate_vaccine_usage_graph()
