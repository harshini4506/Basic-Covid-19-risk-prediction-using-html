import pandas as pd
import matplotlib.pyplot as plt

def generate_death_cases_by_age_graph():
    # Update the path to your actual CSV file
    csv_file_path = 'C:\\Users\\Dell\\OneDrive\\Desktop\\python programmes FDS\\COVID19_Age_Group_Analysis_with_Additional_Columns (1)vaccine.csv'
    
    # Read the CSV file
    data = pd.read_csv(csv_file_path)

    # Check the columns to confirm names
    print("Columns in the dataset:", data.columns)

    # Group data by age and sum the death cases
    age_death_cases = data.groupby('Age')['Deaths'].sum().reset_index()  # Adjust the column name if needed

    # Create a bar plot for death cases by age group
    plt.figure(figsize=(10, 6))
    plt.bar(age_death_cases['Age'], age_death_cases['Deaths'], color='salmon', edgecolor='black')
    plt.title('COVID-19 Death Cases by Age Group')
    plt.xlabel('Age Group')
    plt.ylabel('Number of Deaths')
    plt.xticks(rotation=45)  # Rotate labels for better visibility
    plt.grid(axis='y')

    # Save the figure
    file_path = 'C:/Users/Dell/OneDrive/Pictures/Desktop/FDS project/death_cases_by_age_graph.png'
    plt.savefig(file_path)  # Ensure this directory exists
    plt.show()

if __name__ == "__main__":
    generate_death_cases_by_age_graph()
