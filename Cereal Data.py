import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

data = pd.read_csv(r'C:\Users\joema\Downloads\archive (17)\cereal.csv')

print(data.head(1))

Columns_of_interest = [ 'calories', 'protein' , 'fat', 
                       'fiber', 'sodium',  'fiber',  'carbo',  
                       'sugars',  'potass',  'vitamins', 'shelf',
                        'weight',  'cups', 'rating']

sorted_by_calories = data.sort_values(by='calories', ascending=False)

# Get the top 4 cereals with the highest calories
top_4_high_calories = sorted_by_calories.head(4)
print("Top 4 Cereals with the Highest Calories:")
print(top_4_high_calories[['name', 'calories', 'mfr']])

# Get the top 4 cereals with the lowest calories 
top_4_low_calories = sorted_by_calories.tail(4)
print("Top 4 lowest calorie cereals: ")
print(top_4_low_calories[['name', 'calories', 'mfr']])


mean_values = data[Columns_of_interest].mean()
median_values = data[Columns_of_interest].median()
variance_values = data[Columns_of_interest].var()
std_values = data[Columns_of_interest].std() 
min_value = data[Columns_of_interest].min()
max_value = data[Columns_of_interest].max()

summary_stats = pd.DataFrame({'mean' :mean_values,
                                 'median' : median_values,
                                 'variance': variance_values, 
                                 'std' : std_values, 
                                 'min' : min_value,
                                 'max' : max_value})

print(summary_stats)

# Count the number of cereals for each manufacturer
mfr_counts = data['mfr'].value_counts().reset_index()
mfr_counts.columns = ['mfr', 'count']

# Display the result
print("Number of cereals by manufacturer:")
print(mfr_counts)

mfr_data = {'mfr': ['K', 'G', 'P', 'Q', 'R', 'N', 'A'],
        'count': [23, 22, 9, 8, 8, 6, 1]}
mfr_percentage = pd.DataFrame(mfr_data)

# Calculate percentage
mfr_percentage['percentage'] = (mfr_percentage['count'] / mfr_percentage['count'].sum()) * 100

# Display the result
print("Percentage of cereals by manufacturer:")
print(mfr_percentage)

# Plotting the bar chart
fig, ax1 = plt.subplots(figsize=(10, 6))

#width of bar 
bar_width = 0.3 

# Bar chart for 'count'
ax1.bar(mfr_percentage['mfr'], mfr_percentage['count'], color='purple', label='Count', alpha=0.7, width=bar_width)
ax1.set_xlabel('Manufacturer')
ax1.set_ylabel('Count', color='purple')
ax1.tick_params(axis='y', labelcolor='purple')

# Create a second y-axis for the percentage
ax2 = ax1.twinx()
ax2.plot(mfr_percentage['mfr'], mfr_percentage['percentage'], color='darkblue', marker='o', label='Percentage', linewidth=1)
ax2.set_ylabel('Percentage', color='purple')
ax2.tick_params(axis='y', labelcolor='purple')

# Title and show the plot
plt.title('Cereal Count and Percentage by Manufacturer')
fig.tight_layout()
plt.show() 

# Assuming 'data' is your DataFrame containing the cereal data

# Compute the correlation matrix using Pearson correlation (default)
corr_matrix = data[['calories', 'rating', 'sugars', 'fiber', 'sodium']].corr()

# Print the correlation matrix
print(corr_matrix)

# Plotting the heatmap to visualize the correlations
plt.figure(figsize=(10, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', cbar=True)
plt.title('Correlation Heatmap of Cereal Data')
plt.show()