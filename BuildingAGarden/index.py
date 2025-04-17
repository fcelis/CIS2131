# *****************************************************
# Developer: Fernando Celis
# Date: 01/14/2025
# Class: CIS2131 / Python Programming
# ProjectID: 01
# Project Name: Building a Garden calculator
# Project Objective: Create a Python program that helps users plan and estimate
# the cost of building a garden with various types of plants
# *****************************************************

# Gather Garden Dimensions
try:
    garden_length = float(input("Enter the length of your garden in feet: "))
    if garden_length < 0:
        print("Please enter a positive number")
        exit()
except ValueError:
    print("Please enter a valid number")
    exit()

try:
    garden_width = float(input("Enter the width of your garden in feet: "))
    if garden_width < 0:
        print("Please enter a positive number")
        exit()
except ValueError:
    print("Please enter a valid number")
    exit()

total_garden_area = garden_length * garden_width
print(f"Total garden area: {total_garden_area} square feet\n")

# Display plant selection and price
plants = { 'Roses': 2.50, 'Tulips': 1.75, 'Daisies': 1.00}

# print each plant price
#for plant in plants:
#    print(f"- {plant}: ${plants[plant]:.2f} per square foot")

print("- Roses: $2.50 per square foot")
print("- Tulips: $1.75 per square foot")
print("- Daisies: $1.00 per square foot")

# Allocate Garden Area for Each Plant

try:
    allocated_area_roses = float(input("Enter the area to dedicate to Roses (in square feet): "))
    if allocated_area_roses <= 0 or allocated_area_roses > total_garden_area:
        print("Invalid area for Roses. Please restart.")
        exit()
except ValueError:
    print("Please enter a valid number")
    exit()


try:
    allocated_area_tulips = float(input("Enter the area to dedicate to Tulips (in square feet): "))
    if allocated_area_tulips <= 0 or allocated_area_roses + allocated_area_tulips > total_garden_area:
        print("Invalid area for Tulips. Please restart.")
        exit()
except ValueError:
    print("Please enter a valid number")
    exit()

try:
    allocated_area_daisies = float(input("Enter the area to dedicate to Daisies (in square feet): "))
    if allocated_area_daisies <= 0 or allocated_area_roses + allocated_area_tulips + allocated_area_daisies > total_garden_area:
        print("Invalid area for Daisies. Please restart.")
        exit()
except ValueError:
    print("Please enter a valid number")
    exit()

# Calculate Costs and Display Results
cost_roses = allocated_area_roses *  2.50  # plants['Roses']
cost_tulips = allocated_area_tulips * 1.75 # plants['Tulips']
cost_daisies = allocated_area_daisies * 1.00 # plants['Daisies']
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
