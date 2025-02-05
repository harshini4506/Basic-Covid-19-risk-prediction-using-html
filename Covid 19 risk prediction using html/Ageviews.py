import pandas as pd
import matplotlib.pyplot as plt

def create_age_groups(age):
    """Function to categorize ages into defined age groups."""
    if age <= 19:
        return '0-19'
    elif age <= 39:
        return '20-39'
    elif age <= 59:
        return '40-59'
    else:
        return '60+'

def generate_age_group_graph():
    # Update the path to your actual CSV file
    csv_file_path = 'C:\\Users\\Dell\\OneDrive\\Desktop\\python programmes FDS\\COVID19_Age_Group_Analysis_with_Additional_Columns (1)vaccine.csv'
    
    # Read the CSV file
    data = pd.read_csv(csv_file_path)

    # Check the columns to confirm names
    print("Columns in the dataset:", data.columns)

    # Create age groups
    data['Age Group'] = data['Age'].apply(create_age_groups)

    # Group the data by age groups and sum the confirmed cases
    age_group_data = data.groupby('Age Group')['Confirmed'].sum().reset_index()

    # Create a bar plot for confirmed cases by age group
    plt.figure(figsize=(12, 6))
    plt.bar(age_group_data['Age Group'], age_group_data['Confirmed'], color='skyblue')
    plt.title('Confirmed COVID-19 Cases by Age Group')
    plt.xlabel('Age Group')
    plt.ylabel('Number of Confirmed Cases')
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    
    # Save the figure
    file_path = 'C:/Users/Dell/OneDrive/Pictures/Desktop/FDS project/age_group_confirmed_cases_graph.png'
    plt.savefig(file_path)  # Ensure this directory exists
    plt.show()

if __name__ == "__main__":
    generate_age_group_graph()
