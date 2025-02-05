import pandas as pd
import matplotlib.pyplot as plt

def generate_active_cases_graph():
    # Update the path to your actual CSV file
    csv_file_path = r'C:\\Users\\Dell\\OneDrive\\Desktop\\python programmes FDS\\COVID19_Age_Group_Analysis_with_Additional_Columns (1)vaccine.csv'
    
    # Read the CSV file
    data = pd.read_csv(csv_file_path)

    # Check the columns to confirm names
    print("Columns in the dataset:", data.columns)

    # Using 'Age Group Affected More' if that's the intended grouping
    active_cases_by_age = data.groupby('Age Group Affected More')['Active'].sum().reset_index()  # Use 'Active' column for active cases

    # Create a bar plot for active cases by age group
    plt.figure(figsize=(10, 6))
    plt.bar(active_cases_by_age['Age Group Affected More'], active_cases_by_age['Active'], color='orange')
    plt.title('Active COVID-19 Cases by Age Group')
    plt.xlabel('Age Group')
    plt.ylabel('Number of Active Cases')
    plt.xticks(rotation=45)  # Rotate x labels for better readability
    plt.grid(axis='y')

    # Save the figure as a PNG file in the specified folder
    file_path = r'C:\Users\Dell\OneDrive\Pictures\Desktop\FDS project\active_cases_by_age_group_graph.png'  # Update this path as needed
    plt.savefig(file_path)  # Save the figure
    plt.show()  # Show the plot

if __name__ == "__main__":
    generate_active_cases_graph()
