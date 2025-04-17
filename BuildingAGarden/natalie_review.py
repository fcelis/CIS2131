#Overall Feedback
#Great job! Here is another way to write this with a loop:


# *****************************************************
# Developer: Fernando Celis
# Date: 01/14/2025
# Class: CIS2131 / Python Programming
# ProjectID: 01
# Project Name: Building a Garden Calculator
# Project Objective: Create a Python program that helps users plan and estimate
# the cost of building a garden with various types of plants
# *****************************************************

# Function to validate positive float input
def get_positive_float(prompt, max_value=None):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a positive number.")
            elif max_value and value > max_value:
                print(f"Please enter a number less than or equal to {max_value}.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Gather Garden Dimensions
garden_length = get_positive_float("Enter the length of your garden in feet: ")
garden_width = get_positive_float("Enter the width of your garden in feet: ")
total_garden_area = garden_length * garden_width

print(f"Total garden area: {total_garden_area} square feet\n")

# Display plant selection and price
plants = {'Roses': 2.50, 'Tulips': 1.75, 'Daisies': 1.00}

print("- Roses: $2.50 per square foot")
print("- Tulips: $1.75 per square foot")
print("- Daisies: $1.00 per square foot")

# Allocate Garden Area for Each Plant
print("\nAllocate area for each plant type:")
allocated_area_roses = get_positive_float("Enter the area to dedicate to Roses (in square feet): ", total_garden_area)

remaining_area = total_garden_area - allocated_area_roses
allocated_area_tulips = get_positive_float(f"Enter the area to dedicate to Tulips (remaining area: {remaining_area:.2f} sq ft): ", remaining_area)

remaining_area -= allocated_area_tulips
allocated_area_daisies = get_positive_float(f"Enter the area to dedicate to Daisies (remaining area: {remaining_area:.2f} sq ft): ", remaining_area)

# Calculate Costs and Display Results
cost_roses = allocated_area_roses * plants['Roses']
cost_tulips = allocated_area_tulips * plants['Tulips']
cost_daisies = allocated_area_daisies * plants['Daisies']
grand_total_cost = cost_roses + cost_tulips + cost_daisies

print("\nGarden Allocation and Cost Summary:")
print("----------------------------------------------------------")
print(f"Roses: {allocated_area_roses:.2f} sq ft, Cost: ${cost_roses:.2f}")
print(f"Tulips: {allocated_area_tulips:.2f} sq ft, Cost: ${cost_tulips:.2f}")
print(f"Daisies: {allocated_area_daisies:.2f} sq ft, Cost: ${cost_daisies:.2f}")
print("----------------------------------------------------------")
print(f"Total allocated area: {allocated_area_roses + allocated_area_tulips + allocated_area_daisies:.2f} sq ft")
print(f"Grand Total Cost: ${grand_total_cost:.2f}")
print("----------------------------------------------------------")
