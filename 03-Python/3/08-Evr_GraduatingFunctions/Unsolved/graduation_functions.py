import os
import csv

# Path to collect data from the Resources folder
graduation_csv = os.path.join('..', 'Resources', 'graduation_data.csv')

# Define the function and have it accept the 'state_data' as its sole parameter
def print_percentages(state_data):
    state = str(state_data[0])
    public_students = int(state_data[1])
    public_graduates = int(state_data[2])
    nonprofit_students = int(state_data[3])
    nonprofit_graduates = int(state_data[4])
    forprofit_students = int(state_data[5])
    forprofit_graduates = int(state_data[6])

# Find the total students
    total_students = public_students + nonprofit_students + forprofit_students
# Find the total graduates
    total_graduates = public_graduates + nonprofit_graduates + forprofit_graduates
# Find the public school graduation rate
    public_grad_rate = (public_graduates / public_students) * 100
# Remember that some states do not have nonprofit or forprofit private schools
# Find the non-profit school graduation rate

# Find the for-profit school graduation rate
    if nonprofit_students == 0:
        nonprofit_grad_rate = 0
    else:
        nonprofit_grad_rate = (nonprofit_graduates / nonprofit_students) * 100

# Calculate the overall graduation rate
    if forprofit_students == 0:
        forprofit_grad_rate = 0
    else:
        forprofit_grad_rate = (forprofit_graduates / forprofit_students) * 100

# Print out the state's name and its graduation rates

    overall_grad_rate = (total_graduates / total_students) * 100
    if overall_grad_rate > 50:
        message = "Graduation success"
    else:
        message = "State needs improvement"
    print(f"Stats for {state}")
    print(f"Public School Graduation Rate: {str(public_grad_rate)}")
    print(f"Private Non-Profit School Graduation Rate: {str(nonprofit_grad_rate)}")
    print(f"Private For-Profit School Graduation Rate: {str(forprofit_grad_rate)}")
    print(f"Overall Graduation Rate: {str(overall_grad_rate)}")
    print(f"{message}")


# Read in the CSV file
with open(graduation_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    # Prompt the user for what state they would like to search for
    state_to_check = input("What state do you want to look for? ")

    # Loop through the data
    for row in csvreader:

        # If the state's name in a row is equal to that which the user input, run the 'print_percentages()' function
        if state_to_check == row[0]:
            print_percentages(row)
