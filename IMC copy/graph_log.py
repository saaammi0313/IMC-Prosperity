import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset (Replace 'amethysts.csv' with 'starfruit.csv' if you want to plot for Starfruit)
data_path = 'amethysts.csv'  # or 'starfruit.csv'
df = pd.read_csv(data_path)

df['price_difference'] = df['ask_price_1'] - df['bid_price_1']
len = 500

# Plotting
plt.figure(figsize=(10, 6))  # Set the figure size (optional)
plt.plot(df['timestamp'][:len], df['bid_price_1'][:len], linestyle='-', color='b')  # Plot bid_price_1 vs. timestamp
plt.plot(df['timestamp'][:len], df['ask_price_1'][:len], linestyle='-', color='r') 

plt.axhline(y=10001, color='gray', linestyle='--', label='Line at 10001')
plt.axhline(y=9999, color='gray', linestyle='--', label='Line at 9999')
plt.ylim(9970, 10030)
plt.title('Bid Price 1 over Time')  # Title of the plot
plt.xlabel('Timestamp')  # X-axis label
plt.ylabel('Bid Price 1')  # Y-axis label
plt.grid(True)  # Show grid
plt.show()  # Display the plot

# Plotting the difference between 'bid_price_1' and 'ask_price_1' over time
plt.figure(figsize=(12, 6))
plt.plot(df['timestamp'][:len], df['price_difference'][:len], label='Price Difference', linestyle='-', color='green')
plt.title('Price Difference (Ask - Bid) over Time')
plt.ylim(-2, 10)
plt.xlabel('Timestamp')
plt.ylabel('Price Difference')
plt.legend()
plt.grid(True)
plt.show()