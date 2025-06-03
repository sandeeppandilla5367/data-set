import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load the dataset
df = pd.read_csv('Fitness_Tracker_Data.csv')

# Replace 'None' with 'Rest' or drop rows where Workout_Type is missing
df['Workout_Type'] = df['Workout_Type'].replace({'None': 'Rest'})

# Group by workout type and calculate averages
metrics_by_workout = df.groupby('Workout_Type')[['Steps', 'Heart_Rate_avg', 'Calories_Burned']].mean()

# Reset index to make 'Workout_Type' a column again for plotting
metrics_by_workout = metrics_by_workout.reset_index()

# Melt dataframe for easier plotting (from wide to long format)
metrics_long = metrics_by_workout.melt(id_vars='Workout_Type',value_vars=['Steps', 'Heart_Rate_avg', 'Calories_Burned'],var_name='Metric',value_name='Average Value')

# Set plot style
sns.set(style="whitegrid")

# Plotting
plt.figure(figsize=(12, 7))
barplot = sns.barplot(x='Workout_Type', y='Average Value', hue='Metric', data=metrics_long, ci=None, palette="muted")

# Add title and labels
plt.title('Average Fitness Metrics by Workout Type', fontsize=16)
plt.xlabel('Workout Type', fontsize=12)
plt.ylabel('Average Value', fontsize=12)

# Rotate x-axis labels for readability
plt.xticks(rotation=0)

# Add legend with title
plt.legend(title='Metric')

# Add value labels on top of bars
for p in barplot.patches:
    barplot.annotate(format(p.get_height(), '.1f'), (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='center',xytext=(0, 9),textcoords='offset points')

# Adjust layout
plt.tight_layout()

# Save the graph in the same folder
current_dir = os.getcwd()
graph_path = os.path.join(current_dir, 'Combined_Fitness_Metrics.png')
plt.savefig(graph_path)

# Show the plot
plt.show()

print(f"Chart saved at: {graph_path}")