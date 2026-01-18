print("Pay Check Calculator")
print("Program calculates net pay based upon hours worked, hourly rate, and taxes paid.")
print()
print("Program Requirements:")
print("Developer: Joshua Mann")
print("1. Must use float data type for user input.")
print("2. Must round calculations to two decimal places.")
print("3. Must format currency with dollar sign, and two decimal places.")

print("\nUser Input:")
hours_worked = float(input("Hours Worked: "))
hourly_rate = float(input("Hourly Rate: $ "))
tax_rate = float(input("Tax Rate (percent): "))

gross_pay = hours_worked * hourly_rate
tax_amount = gross_pay * (tax_rate / 100)
net_pay = gross_pay - tax_amount

print("\nProgram Output:")
print("Gross Pay:\t", "${0:,.2f}".format(gross_pay))
print("Tax Rate:\t", "{0:.2%}".format(tax_rate/100))
print("Tax Amount:\t", "${0:,.2f}".format(tax_amount))
print("Net Pay:\t", "${0:,.2f}".format(net_pay))
