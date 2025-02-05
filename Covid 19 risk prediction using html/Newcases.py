import pandas as pd
import matplotlib.pyplot as plt

def generate_new_cases_graph():
    # Update the path to your actual CSV file
    csv_file_path = r'C:\\Users\\Dell\\OneDrive\\Desktop\\python programmes FDS\\COVID19_Age_Group_Analysis_with_Additional_Columns (1)vaccine.csv'
    
    # Read the CSV file
    data = pd.read_csv(csv_file_path)

    # Check the columns to confirm names
    print("Columns in the dataset:", data.columns)

    # Extract the new cases - use the correct column name 'New Cases'
    new_cases = data['New Cases'].tolist()  # Use 'New Cases' instead of 'new_cases'

    # Generate x values based on the length of new_cases
    days = list(range(1, len(new_cases) + 1))  # Assuming each entry corresponds to a sequential day

    # Create a plot for new cases
    plt.figure(figsize=(10, 6))
    plt.plot(days, new_cases, marker='o', color='blue')  # Use a line plot with markers
    plt.title('New COVID-19 Cases')
    plt.xlabel('Days')  # You can replace this with actual day/dates if available
    plt.ylabel('Number of New Cases')
    plt.grid()
    
    # Save the figure as a PNG file in the specified folder
    file_path = r'C:\Users\Dell\OneDrive\Pictures\Desktop\FDS project\new_cases_graph.png'  # Update this path as needed
    plt.savefig(file_path)  # Save the figure
    plt.show()  # Show the plot

if __name__ == "__main__":
    generate_new_cases_graph()
