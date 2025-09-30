# FILE NAME - convert_C_to_F_02.py

# NAME: Michael Glazier
# DATE: 09/30/2025
# BRIEF DESCRIPTION:  convert c to f with cases

########## ENTER YER CODE BELOW THIS LINE ##########

def main():

  menu_choice = int(input(f"===== Temperature Converter =====\n\n  1. Convert from Celsius to Fahrenheit\n  2. Convert from Fahrenheit to Celsius\n\nPlease choose from the above menu: "))
  orginal_temperature = float(input("Enter a temperature to convert: "))

  if menu_choice == 1:
    result_temperature = ((orginal_temperature*(9/5))+32)
    print(f"{orginal_temperature} degrees Celsius is {result_temperature} degrees Fahrenheit.")

  elif menu_choice == 2:
    result_temperature = ((orginal_temperature-32)*(5/9))
    print(f"{orginal_temperature} degrees Fahrenheit is {result_temperature} degrees Celsius.")
  
  else:
    print("invalid entry")

main()

########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 1
Enter a temperature to convert: 100

100.0 degrees Celsius is 212.0 degrees Fahrenheit.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 2
Enter a temperature to convert: 32

32.0 degrees Fahrenheit is 0.0 degrees Celsius.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 1
Enter a temperature to convert: -40

-40.0 degrees Celsius is -40.0 degrees Fahrenheit.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 2
Enter a temperature to convert: -40

-40.0 degrees Fahrenheit is -40.0 degrees Celsius.
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is one lesson you learned in this lab?

how to format using print f with multiple new lines and spacing





'''