import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('Fitness_Tracker_Data.csv')

# Display basic info
print("First 5 rows:")
print(df.head())

print("\nBasic Statistics:")
print(df.describe())

# Set style
sns.set(style="whitegrid")

# 1. Scatter Plot: Steps vs Calories Burned
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Steps', y='Calories_Burned', data=df, alpha=0.7)
plt.title('Steps vs Calories Burned')
plt.xlabel('Steps Taken')
plt.ylabel('Calories Burned')
plt.tight_layout()
plt.show()

# 2. Bar Chart: Average Heart Rate by Workout Type
plt.figure(figsize=(10, 6))
workout_hr = df.groupby('Workout_Type')['Heart_Rate_avg'].mean().sort_values()
sns.barplot(x=workout_hr.values, y=workout_hr.index, palette="viridis")
plt.title('Average Heart Rate by Workout Type')
plt.xlabel('Average Heart Rate')
plt.ylabel('Workout Type')
plt.tight_layout()
plt.show()

# 3. Line Chart: Daily Steps Over Time
if 'Date' in df.columns:
    # Convert Date to datetime
    df['Date'] = pd.to_datetime(df['Date'])
    daily_steps = df.groupby('Date')['Steps'].mean()  # You can use sum() if per-user

    plt.figure(figsize=(12, 6))
    sns.lineplot(x=daily_steps.index, y=daily_steps.values)
    plt.title('Average Daily Steps Over Time')
    plt.xlabel('Date')
    plt.ylabel('Average Steps')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
else:
    print("No 'Date' column found. Skipping time series visualization.")