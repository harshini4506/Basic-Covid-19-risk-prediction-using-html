import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
import seaborn as sns

# Load the dataset
file_path = r"C:\Users\Dell\OneDrive\Desktop\python programmes FDS\covid_analysis_1000_rows (1).csv"
df = pd.read_csv(file_path)

# Clean column names (remove leading/trailing spaces and convert to lowercase)
df.columns = df.columns.str.strip().str.lower()

# Check the structure of the dataset
print(df.head())
print(df.columns)  # Verify the column names

# Calculate Active cases if the relevant columns exist
if 'confirmed' in df.columns and 'deaths' in df.columns and 'recovered' in df.columns:
    df['active'] = df['confirmed'] - df['deaths'] - df['recovered']

# Linear Regression Model
if 'confirmed' in df.columns and 'deaths' in df.columns:
    X = df['confirmed'].values.reshape(-1, 1)  # Features (Confirmed cases)
    y = df['deaths'].values  # Target variable (Deaths)

    # Create and train the model
    model = LinearRegression()
    model.fit(X, y)

    # Make predictions
    df['predicted deaths'] = model.predict(X)

    # Output model parameters
    print(f"Linear Regression Coefficient: {model.coef_[0]}")
    print(f"Linear Regression Intercept: {model.intercept_}")

# 1. Scatter Plot for Confirmed vs Active Cases
if 'confirmed' in df.columns and 'active' in df.columns and 'deaths' in df.columns:
    plt.figure(figsize=(12, 6))
    plt.scatter(df['confirmed'], df['active'], color='blue', alpha=0.6, label='Active Cases')
    plt.scatter(df['confirmed'], df['deaths'], color='red', alpha=0.6, label='Deaths')
    if 'predicted deaths' in df.columns:
        plt.plot(df['confirmed'], df['predicted deaths'], color='orange', label='Predicted Deaths')
    plt.title('Scatter Plot: Confirmed Cases vs Active Cases and Deaths')
    plt.xlabel('Confirmed Cases')
    plt.ylabel('Number of Cases')
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()

# 2. Histogram for Total Confirmed, Recovered, and Death Cases
if 'confirmed' in df.columns and 'recovered' in df.columns and 'deaths' in df.columns:
    plt.figure(figsize=(12, 6))
    plt.hist(df['confirmed'], bins=30, alpha=0.5, label='Confirmed Cases', color='blue')
    plt.hist(df['recovered'], bins=30, alpha=0.5, label='Recovered Cases', color='green')
    plt.hist(df['deaths'], bins=30, alpha=0.5, label='Death Cases', color='red')
    plt.title('Histogram: Distribution of COVID-19 Cases')
    plt.ylabel('Frequency')
    plt.xlabel('Number of Cases')
    plt.legend()
    plt.tight_layout()
    plt.show()

# 3. Blood Group Distribution
if 'blood group' in df.columns:
    blood_group_counts = df['blood group'].value_counts().sort_index()

    # Prepare data for "candlestick" chart
    blood_group_counts = blood_group_counts.reset_index()
    blood_group_counts.columns = ['Blood Group', 'Count']

    # Define the candlestick "high" and "low" values
    blood_group_counts['High'] = blood_group_counts['Count'] + 5
    blood_group_counts['Low'] = blood_group_counts['Count'] - 5

    # Plotting candlestick-like chart
    fig, ax = plt.subplots(figsize=(10, 6))
    for i in range(len(blood_group_counts)):
        ax.plot([i, i], [blood_group_counts['Low'][i], blood_group_counts['High'][i]], color='black')
        ax.add_patch(plt.Rectangle((i - 0.2, blood_group_counts['Count'][i]), 0.4, 1, color='blue', alpha=0.5))

    ax.set_xticks(np.arange(len(blood_group_counts)))
    ax.set_xticklabels(blood_group_counts['Blood Group'])
    ax.set_title('Blood Group Distribution (Candlestick-like Representation)')
    ax.set_ylabel('Count')
    plt.tight_layout()
    plt.show()

# 4. Heatmap of Confirmed Cases by Country
if 'country' in df.columns and 'confirmed' in df.columns:
    plt.figure(figsize=(12, 8))
    heatmap_data = df.pivot_table(values='confirmed', index='country', aggfunc='sum')
    sns.heatmap(heatmap_data, cmap='YlGnBu', annot=True, fmt='.0f')
    plt.title('Heatmap of Confirmed COVID-19 Cases by Country')
    plt.xlabel('Country')
    plt.ylabel('Number of Confirmed Cases')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

# 5. Radar Chart for Vaccine Distribution
if 'vaccine' in df.columns:
    vaccine_counts = df['vaccine'].value_counts()

    # Prepare data for radar chart
    categories = vaccine_counts.index
    values = vaccine_counts.values

    num_vars = len(categories)
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

    values = np.concatenate((values, [values[0]]))
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
    ax.fill(angles, values, color='orange', alpha=0.25)
    ax.set_yticklabels([])  # Hide the radial labels
    ax.set_xticks(angles[:-1])  # Set the angular ticks
    ax.set_xticklabels(categories)  # Set the category labels
    ax.set_title('Vaccine Distribution Radar Chart')
    plt.show()

# 6. Symptoms Pie Chart
if 'symptoms' in df.columns:
    symptom_list = []
    for symptoms in df['symptoms']:
        symptom_list.extend(symptoms.split(', '))

    symptom_counts = pd.Series(symptom_list).value_counts()
    plt.figure(figsize=(8, 8))
    plt.pie(symptom_counts, labels=symptom_counts.index, autopct='%1.1f%%', startangle=140)
    plt.title('Symptoms Distribution')
    plt.axis('equal')
    plt.tight_layout()
    plt.show()

# 7. Bar Chart for Age Group Distribution (New Feature)
if 'age group' in df.columns:
    plt.figure(figsize=(10, 6))
    age_group_counts = df['age group'].value_counts()
    plt.bar(age_group_counts.index, age_group_counts.values, color='purple')
    plt.title('Age Group Distribution')
    plt.xlabel('Age Group')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.show()

# 8. Line Plot for New Cases over Time (New Feature)
if 'date' in df.columns and 'new cases' in df.columns:
    df['date'] = pd.to_datetime(df['date'])
    plt.figure(figsize=(12, 6))
    plt.plot(df['date'], df['new cases'], marker='o', color='green')
    plt.title('New COVID-19 Cases Over Time')
    plt.xlabel('Date')
    plt.ylabel('New Cases')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# 9. Side Effect Bar Plot (New Feature)
if 'side effects' in df.columns:
    side_effect_counts = df['side effects'].value_counts()
    plt.figure(figsize=(10, 6))
    plt.bar(side_effect_counts.index, side_effect_counts.values, color='red')
    plt.title('Vaccine Side Effects Distribution')
    plt.xlabel('Side Effects')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# 10. Vaccine with Most Side Effects
if 'vaccine' in df.columns and 'side effects' in df.columns:
    vaccine_side_effects = df.groupby('vaccine')['side effects'].value_counts().unstack().fillna(0)
    
    # Plot the side effects for each vaccine
    plt.figure(figsize=(12, 8))
    vaccine_side_effects.plot(kind='bar', stacked=True, colormap='tab20', figsize=(12, 8))
    plt.title('Side Effects for Each Vaccine')
    plt.xlabel('Vaccine')
    plt.ylabel('Count of Side Effects')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Displaying DataFrame for summary
print("\nCOVID-19 Data Summary:")
summary_columns = ['country', 'blood group', 'predicted deaths', 'age group', 'side effects']
available_columns = [col for col in summary_columns if col in df.columns]
print(df[available_columns])