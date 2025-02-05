import pandas as pd
import matplotlib.pyplot as plt

def generate_confirmed_cases_graph():
    # Update the path to your actual CSV file
    csv_file_path = 'C:\\Users\\Dell\\OneDrive\\Desktop\\python programmes FDS\\COVID19_Age_Group_Analysis_with_Additional_Columns (1)vaccine.csv'
    
    # Read the CSV file
    data = pd.read_csv(csv_file_path)

    # Check the columns to confirm names
    print("Columns in the dataset:", data.columns)

    # Extract the confirmed cases
    confirmed_cases = data['Confirmed'].tolist()  # Updated column name

    # Generate x values based on the length of confirmed_cases
    days = list(range(1, len(confirmed_cases) + 1))  # Assuming each entry corresponds to a sequential day

    # Create a plot for confirmed cases
    plt.figure(figsize=(10, 6))
    plt.plot(days, confirmed_cases, marker='o')
    plt.title('Confirmed COVID-19 Cases')
    plt.xlabel('Days')  # or use the actual day/dates if available
    plt.ylabel('Number of Confirmed Cases')
    plt.grid()
    
    # Save the figure
    file_path = 'C:/Users/Dell/OneDrive/Pictures/Desktop/FDS project/confirmed_cases_graph.png'
    plt.savefig(file_path)  # Ensure this directory exists
    plt.show()

if __name__ == "__main__":
    generate_confirmed_cases_graph()
