import pandas as pd
import matplotlib.pyplot as plt

def generate_recovered_cases_age_group_graph():
    # Update the path to your actual CSV file
    csv_file_path = 'C:\\Users\\Dell\\OneDrive\\Desktop\\python programmes FDS\\COVID19_Age_Group_Analysis_with_Additional_Columns (1)vaccine.csv'
    
    # Read the CSV file
    data = pd.read_csv(csv_file_path)

    # Check the columns to confirm names
    print("Columns in the dataset:", data.columns)

    # Filter data for age groups between 20 and 49
    age_group_recovered_cases = data[data['Age'].between(20, 49)]

    # Group by age and sum the recovery cases
    age_recovery_counts = age_group_recovered_cases.groupby('Age')['Recovered'].sum().reset_index()

    # Plotting the graph
    plt.figure(figsize=(10, 6))
    plt.bar(age_recovery_counts['Age'], age_recovery_counts['Recovered'], color='lightgreen', edgecolor='black')
    plt.title('COVID-19 Recovery Cases for Age Group 20 to 49')
    plt.xlabel('Age Group')
    plt.ylabel('Number of Recovered Cases')
    plt.xticks(rotation=0)  # Rotate labels for better visibility
    plt.grid(axis='y')

    # Save the figure
    file_path = 'C:/Users/Dell/OneDrive/Pictures/Desktop/FDS project/recovered_cases_age_group_20_49_graph.png'
    plt.savefig(file_path)  # Ensure this directory exists
    plt.show()

if __name__ == "__main__":
    generate_recovered_cases_age_group_graph()
