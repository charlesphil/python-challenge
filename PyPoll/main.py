# Import required modules
import os
import csv

# Agnostic relative file path to election_data.csv
data_path = os.path.join("Resources", "election_data.csv")

# Agnostic relative file path to save results.txt
results_path = os.path.join("Analysis", "results.txt")

# Open election data for use with csv module
with open(data_path, "r") as election_file:

    # Variables that need to be referenced inside scopes later
    candidates = {}
    total_votes = 0

    # Create csv reader object
    csvreader = csv.reader(election_file, delimiter=",")

    # Skip header
    header = next(csvreader, None)

    # For each vote...
    for row in csvreader:
        # Store unique candidate into the candidates dictionary with 1 starting vote if they are not already in it.
        if row[2] not in candidates:
            candidates[row[2]] = 1
        # If the candidate appears again, add a vote for them.
        else:
            candidates[row[2]] += 1

    # Calculate total votes from the dictionary
    for candidate_votes in candidates.values():
        total_votes += candidate_votes

    # Function to calculate and format percentages from the dictionary. Returns a string.
    def calc_percent():

        # Create temporary variable in this scope to attached formatted f-strings to it
        formatted_line = ""

        # For (key, value) in items in candidates dictionary...
        for (candidate, votes) in candidates.items():

            # If current candidate is not the last key, concatenate to formatted_line with a newline (\n)
            if candidate != list(candidates)[-1]:
                # Format percentages to two decimal places after dividing candidate's votes by total votes
                formatted_line += f"{candidate}: {'{:.2%}'.format(votes / total_votes)} ({votes})\n"
            # Otherwise, if it is the last key, concatenate to formatted_line with no newline
            else:
                formatted_line += f"{candidate}: {'{:.2%}'.format(votes / total_votes)} ({votes})"

        # Return the whole string
        return formatted_line

    # Format the results into a list for outputting to the console and text file later.
    # Calls calc_percent function to get the formatted string and stores it inside the list.
    results_output = [
        "Election Results",
        "------------------------",
        f"Total Votes: {total_votes}",
        "------------------------",
        calc_percent(),
        "------------------------",
        f"Winner: {max(candidates, key=candidates.get)}",
        "------------------------"
    ]

    # Print to console
    for line in results_output:
        print(line)

# Write to text file, will create a new text file if file not found on path
with open(results_path, "w") as text_file:
    for text in results_output:
        text_file.write(f"{text}\n")
