# Exercise 3: Property Tax
# Calculate the property tax based on the assessment value
def propert_taxes():
    # The percentage to get the assessment value from the actual value
    percent_actual_value = 0.60

    # Ask user for the actual property  value and convert it to float
    actual_value = float(input("Actual Property Value: "))

    # Calculate the assessment value from the actual property value
    assessment_value = actual_value * percent_actual_value

    # to get the tax per dollar divide $0.72 (72¢) by $100
    tax_per_dollar = 0.72 / 100

    # Calculate the property tax
    property_tax = assessment_value * tax_per_dollar

    print(f"Assessment value : ${assessment_value}.  Propert Tax: ${property_tax}")
