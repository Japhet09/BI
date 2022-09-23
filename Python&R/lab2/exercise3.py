# Exercise 3: Property Tax
# A constant variable, percentage of the actual value  to get the assessment value
PERCENT = 0.60

# Using a main function to call the property tax function
def main():
    # Ask user for the actual property  value and convert it to float
    actual_value = float(input("Actual Property Value: "))
    property_taxes(actual_value)


# Calculate the property tax based on the assessment value
# the functions accepts one parameter (actual_value)
def property_taxes(actual_value):
    # Calculate the assessment value as the 60% of the actual property value
    assessment_value = actual_value * PERCENT

    # To get the tax per dollar divide $0.72 (72¢) by $100
    tax_per_dollar = 0.72 / 100

    # Calculate the property tax
    property_tax = assessment_value * tax_per_dollar
    # Display the assessment value and  property tax rounded to 2 decimal places
    print(
        f"Assessment value: ${assessment_value:.2f}  Propert Tax: ${property_tax:.2f}"
    )


main()
