import pandas as pd

# Define the path to the activity log file
activity_log_path = '/Users/saaammi/Desktop/IMC/log_data/activity_log.txt'

# Load the activity log file into a pandas DataFrame
# We skip the first row as it is a header description and not part of the data
df_activities = pd.read_csv(activity_log_path, delimiter=';', skiprows=1)

# Filter the DataFrame for the first product (e.g., AMETHYSTS)
df_amethysts = df_activities[df_activities['product'] == 'AMETHYSTS']

# Filter the DataFrame for the second product (e.g., STARFRUIT)
df_starfruit = df_activities[df_activities['product'] == 'STARFRUIT']

# Display the first few rows of each DataFrame to verify
print("AMETHYSTS DataFrame:")
print(df_amethysts.head())
print("\nSTARFRUIT DataFrame:")
print(df_starfruit.head())

# Save the separated DataFrames to CSV files
df_amethysts.to_csv('amethysts.csv', index=False)
df_starfruit.to_csv('starfruit.csv', index=False)
