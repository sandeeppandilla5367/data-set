import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load fitness tracker data
df_fitness = pd.read_csv('Fitness_Tracker_Data.csv')

# Replace 'None' with 'Rest'
df_fitness['Workout_Type'] = df_fitness['Workout_Type'].replace({'None': 'Rest'})

# Set plot style
sns.set(style="whitegrid")
current_dir = os.getcwd()

# 1. Average Steps by Workout Type
plt.figure(figsize=(10, 6))
steps = df_fitness.groupby('Workout_Type')['Steps'].mean().sort_values()
sns.barplot(x=steps.values, y=steps.index, palette="Blues_d")
plt.title('Average Steps by Workout Type')
plt.xlabel('Steps Taken')
plt.ylabel('Workout Type')
plt.tight_layout()
plt.savefig(os.path.join(current_dir, '1_Steps_by_Workout.png'))
plt.close()

# 2. Average Heart Rate by Workout Type
plt.figure(figsize=(10, 6))
heart_rate = df_fitness.groupby('Workout_Type')['Heart_Rate_avg'].mean().sort_values()
sns.barplot(x=heart_rate.values, y=heart_rate.index, palette="Greens_d")
plt.title('Average Heart Rate by Workout Type')
plt.xlabel('Heart Rate (BPM)')
plt.ylabel('Workout Type')
plt.tight_layout()
plt.savefig(os.path.join(current_dir, '2_Heart_Rate_by_Workout.png'))
plt.close()

# 3. Average Calories Burned by Workout Type
plt.figure(figsize=(10, 6))
calories = df_fitness.groupby('Workout_Type')['Calories_Burned'].mean().sort_values()
sns.barplot(x=calories.values, y=calories.index, palette="Reds_d")
plt.title('Average Calories Burned by Workout Type')
plt.xlabel('Calories Burned')
plt.ylabel('Workout Type')
plt.tight_layout()
plt.savefig(os.path.join(current_dir, '3_Calories_Burned_by_Workout.png'))
plt.close()

# 4. Number of Entries per Workout Type
plt.figure(figsize=(10, 6))
workout_counts = df_fitness['Workout_Type'].value_counts()
sns.barplot(x=workout_counts.values, y=workout_counts.index, palette="Purples_d")
plt.title('Number of Workouts by Type')
plt.xlabel('Count')
plt.ylabel('Workout Type')
plt.tight_layout()
plt.savefig(os.path.join(current_dir, '4_Workout_Type_Counts.png'))
plt.close()

# 5. Daily Steps Trend Over Time
if 'Date' in df_fitness.columns:
    df_fitness['Date'] = pd.to_datetime(df_fitness['Date'])
    daily_steps = df_fitness.groupby('Date')['Steps'].mean()

    plt.figure(figsize=(12, 6))
    sns.lineplot(x=daily_steps.index, y=daily_steps.values)
    plt.title('Daily Average Steps Over Time')
    plt.xlabel('Date')
    plt.ylabel('Average Steps')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(current_dir, '5_Daily_Steps_Trend.png'))
    plt.close()

# 6. Steps vs Calories Burned (Scatter Plot)
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Steps', y='Calories_Burned', data=df_fitness, alpha=0.7, color='teal')
plt.title('Steps vs Calories Burned')
plt.xlabel('Steps Taken')
plt.ylabel('Calories Burned')
plt.grid(True)
plt.tight_layout()
plt.savefig(os.path.join(current_dir, '6_Steps_vs_Calories.png'))
plt.close()

print("All charts saved successfully.")