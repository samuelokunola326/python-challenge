
# PyBank Script

# Dependecies
import pandas as pd

# Get dataset
data_file = 'Resources.PyB/budget_data.csv'

# Use pandas library to read data set
data_file_df = pd.read_csv(data_file)

# Check to make sure pandas is reading csv file
print(data_file_df.head())

# Calc Total Number of Months in Overall Analysis
total_months = len(data_file_df['Date'].unique())
print(total_months)


# Net Profit/Loss
total = data_file_df['Profit/Losses'].sum()
print(total)

# Average change in profit/loss
average_change = data_file_df['Profit/Losses'].mean()
print(average_change)

# Calc for Greatest Increase
Greatest_Increase_PercentageV = data_file_df['Profit/Losses'].max()
print(Greatest_Increase_PercentageV)

#Creating a dataframe for greatest increase
GIPD = data_file_df[data_file_df['Profit/Losses'] == Greatest_Increase_PercentageV]
print(GIPD)

# Calc for Greatest Decrease
Greatest_Decrease_PercentageV = data_file_df['Profit/Losses'].min()
print(Greatest_Decrease_PercentageV)

# Creating a df for greatest decrease
GDPD = data_file_df[data_file_df['Profit/Losses'] == Greatest_Decrease_PercentageV]
print(GDPD)





# Printing to CSV file

GIPD.to_csv("Analysis.PyB/Final_Analysis", index=False, header=True)
GDPD.to_csv("Analysis.PyB/Final_Analysis", index=False, header=True)


# Printing to terminal
print(f'Total Months: {total_months} ')
print(f'Total: ${total} ')
print(f'Average Change: ${average_change} ')
print(f'Greatest Increase in Profits: {GIPD} ')
print(f'Greatest Decrease in Profits: {GDPD} ')