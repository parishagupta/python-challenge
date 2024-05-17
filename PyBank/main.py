# Define and link csv
import os
import csv
budget_data = os.path.join(os.path.dirname(__file__), "Resources", "budget_data.csv") # Navigate to cwd and search for Resourcess\budget_data.csv

# Open and read csv
with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_data = list(csvreader)[1:]
   
# Define date and profits/losses as lists
months = []
profits_losses=[]

# Store months and profits as list, profits as integer list
months = [row[0] for row in csv_data]
profits_losses = [int(row[1]) for row in csv_data]

# Calculate total number of months
total_months = len(months)

# Calculate P/L total
pl_total = sum(profits_losses)

# Calculate changes in profit/losses over entire period
pl_change = [profits_losses[i + 1] - profits_losses[i] for i in range(total_months - 1)]

# Calculate average revenue change
pl_average = sum(pl_change) / len(pl_change)

# Calculate greatest increase in P/L
max_pl = max(pl_change)
# Calculate greatest decrease in P/L
min_pl = min(pl_change)

# Locate max p/l amount and corresponding month
max_index = pl_change.index(max_pl)
max_month = months[max_index + 1]
# Locate min p/l amount and corresponding month
min_index = pl_change.index(min_pl)
min_month = months[min_index + 1]

# Check calc
# print(pl_change[:4])  # display first 6 rows
# print(profits_losses[1:5])  # current 4 months
# print(profits_losses[:4])  # prev 4 months
# print(pl_change[:4])  # difference
# print(max_pl) # max p/l record
# print(min_pl) # min p/l record
# print(max_month) # max p/l record month
# print(min_month) # min p/l record month

# Display analysis report using f strings over rows of 48 characters
report = (
    f"{' Financial Analysis ':-^48}\n" 
    f"{'Total Months:':24}{total_months:24,.0f}\n"
    f"{'Net Profits:':24}{pl_total:24,.0f}\n"
    f"{'Avgerage Change:':24}{pl_average:24,.0f}\n"
    f"{'Greatest Increase:':18}{max_month:^20}{max_pl:10,.0f}\n"
    f"{'Greatest Decrease:':18}{min_month:^20}{min_pl:10,.0f}\n"
    f"{'--':-^48}"
)
print(report)

# Assemble the output text file path, starting from the cwd
textfile_path = os.path.join(
    os.path.dirname(__file__), "Analysis", "budget_analysis.txt"
)

# Open the budget_analysis text file and write the report in it
with open(textfile_path, "w", encoding="utf-8") as textfile:
    textfile.write(report)
