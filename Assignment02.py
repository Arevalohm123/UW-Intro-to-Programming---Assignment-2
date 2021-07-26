#------------------------------------------------------------#
# Title:        Basic Math Script
# Dev:          Andrei Arevalo
# Date:         Jan 19th, 2021
# Changelog:
#   Andrei Arevalo, 1/19/21, Initial Rev
#------------------------------------------------------------#

# Assignment Task - Create a new program that asks the user to input
#   two numbers then prints out the sum, difference, product, and quotient

#------------------------------------------------------------#
# Print the main screen
print("\n\nWelcome to the 2-Number Calculator!")
print("\nThis calculator will add, subtract, multiply and divide the two numbers")
#------------------------------------------------------------#
# Get the user input data
num1_flt    = float(input("\n\nPlease enter the first number:"))
num2_flt    = float(input("\nPlease enter the second number:"))
#------------------------------------------------------------#
# Process the data
sum         = num1_flt + num2_flt
diff        = abs(num1_flt - num2_flt)
diffv2      = num1_flt - num2_flt
multiply    = num1_flt * num2_flt
divide      = num1_flt / num2_flt
#------------------------------------------------------------#
# Display the data
print("\n\nThe sum of",         num1_flt, "and", num2_flt, "is:", sum)
print("\nThe difference of",       num1_flt, "and", num2_flt, "is:", diff)
print("\nThe multiplication of",num1_flt, "and", num2_flt, "is:", multiply)
print("\nThe division of",      num1_flt, "and", num2_flt, "is:", divide)
#------------------------------------------------------------#
# End the program
end = input("\n\n(Press enter to end program)")
print(end)

 
















