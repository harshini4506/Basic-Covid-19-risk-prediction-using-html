import pandas as pd
import matplotlib.pyplot as plt

def generate_blood_group_affected_graph():
    # Update the path to your actual CSV file
    csv_file_path = 'C:\\Users\\Dell\\OneDrive\\Desktop\\python programmes FDS\\COVID19_Age_Group_Analysis_with_Additional_Columns (1)vaccine.csv'
    
    # Read the CSV file
    data = pd.read_csv(csv_file_path)

    # Check the columns to confirm names
    print("Columns in the dataset:", data.columns)

    # Extract blood groups and count occurrences
    blood_group_counts = data['Blood Group Affected More'].value_counts()  # Count occurrences of each blood group

    # Create a bar plot for blood group affected
    plt.figure(figsize=(10, 6))
    blood_group_counts.plot(kind='bar', color='skyblue', edgecolor='black')
    plt.title('COVID-19 Cases by Blood Group Affected')
    plt.xlabel('Blood Group')
    plt.ylabel('Number of Cases Affected')
    plt.xticks(rotation=45)  # Rotate labels for better visibility
    plt.grid(axis='y')

    # Save the figure
    file_path = 'C:/Users/Dell/OneDrive/Pictures/Desktop/FDS project/blood_group_affected_graph.png'
    plt.savefig(file_path)  # Ensure this directory exists
    plt.show()

if __name__ == "__main__":
    generate_blood_group_affected_graph()
