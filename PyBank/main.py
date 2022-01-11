# Import modules
import os
import csv

# Agnostic relative file path to budget_data.csv
data_path = os.path.join("Resources", "budget_data.csv")

# Agnostic relative file path to save analysis.txt
analysis_path = os.path.join("Analysis", "analysis.txt")

# Open file to read with csv module
with open(data_path, "r") as csv_file:

    # Create csv reader object
    csvreader = csv.reader(csv_file, delimiter=",")

    # Skip header
    header = next(csvreader, None)

    # "Skipped" first month acts as the base for ease of calculations
    first_month = next(csvreader, None)

    # Set variables that need to be referenced inside the different scopes
    # months starts at 1 to account for the first month
    months = 1
    # net_total starts with the profit/loss of the first month
    net_total = int(first_month[1])
    # previous_amt starts with the profit/loss of the first month to avoid needing to delete the first month later
    previous_amt = int(first_month[1])
    # list to store all the profit/loss differences between months
    list_of_diff = []
    # keeps track of the greatest increase and decreases in profit/loss between months
    greatest_increase = 0
    greatest_decrease = 0

    # For each row (as list) in the csv...
    for row in csvreader:

        # Increment months variable (each row is a unique month)
        months += 1

        # Add profit/loss to net total after casting to int
        net_total += int(row[1])

        # Find the difference between the current profit/loss and the previous profit/loss
        difference = int(row[1]) - previous_amt
        list_of_diff.append(difference)

        # If the difference between the previous row and the current one exceeds the current greatest increase,
        # the new greatest increase is the current difference. The corresponding month becomes the best month.
        if difference > greatest_increase:
            greatest_increase = difference
            best_month = row[0]
        # If the difference is instead lower than the greatest decrease, the new greatest decrease is the current
        # difference. The corresponding month becomes the worst month.
        elif difference < greatest_decrease:
            greatest_decrease = difference
            worst_month = row[0]

        # Update the previous_amt variable to the current profit/loss before moving onto the next row
        previous_amt = int(row[1])

    # After the csv has been read entirely...

    # Find the mean among the values found from the differences between each month and round to two cents
    avg_change = round(sum(list_of_diff) / len(list_of_diff), 2)

    # Format analysis and store into a list for later output in terminal and text file
    analysis_output = ["Financial Analysis",
                       "--------------------------------------",
                       f"Total Months: {months}",
                       f"Total: ${net_total}",
                       f"Average Change: ${avg_change}",
                       f"Greatest Increase in Profits: {best_month} (${greatest_increase})",
                       f"Greatest Decrease in Profits: {worst_month} (${greatest_decrease})"]

    # Print each line into the console
    for line in analysis_output:
        print(line)

# Write to text file, will create a new text file if file not found on path
with open(analysis_path, "w") as text_file:
    for text in analysis_output:
        text_file.write(f"{text}\n")
