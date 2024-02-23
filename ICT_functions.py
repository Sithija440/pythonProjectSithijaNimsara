"""
This file stored all the functions of the main.py file.
Create any new function here.
"""

try:
    """
    --------------------------------------------------------------------------------------------------------------------------------------
                        Those functions started with decimal.
    """


    def decimal_into_binary():
        # Take inputs from the users
        decimal_value = int(input("Enter the decimal value to convert to binary value : "))
        translated_value = bin(decimal_value)[2:]
        print(f"You entered {decimal_value} == {translated_value}.")


    def decimal_into_octal():
        # Take inputs from the users
        decimal_value = int(input("Enter the decimal value to convert to octal value : "))
        translated_value = oct(decimal_value)
        # Below code to remove Ox from the output
        translated_value = translated_value[2:]
        print(f"You entered {decimal_value} == {translated_value}.")


    def decimal_into_hexa():
        # Take inputs from the users
        decimal_value = int(input("Enter the decimal value to convert to hexadecimal value : "))
        hexadecimal_result = hex(decimal_value)
        # Below code to remove Ox from the output
        translated_value = hexadecimal_result[2:]
        print(f"You entered {decimal_value} == {translated_value}.")


    """
    --------------------------------------------------------------------------------------------------------------------------------------
                        Those functions started with binary.
    """


    def binary_into_decimal():
        # Take inputs from the users
        binary_value = str(input("Enter the binary value to convert to decimal value : "))
        translated_value = int(binary_value, 2)
        print(f"You entered {binary_value} == {translated_value}.")
        
        
    def binary_into_octal():
        # Take inputs from the users
        binary_value = str(input("Enter the binary value to convert to octal value : "))
        binary_value = int(binary_value)
        translated_value = oct(binary_value)
        translated_value = translated_value[2:]
        print(f"You entered {binary_value} == {translated_value}.")
        
        
    def binary_into_hexa():
        # Take inputs from the users
        binary_value = str(input("Enter the binary value to convert to hexadecimal value : "))
        binary_value = int(binary_value)
        translated_value = hex(binary_value)
        # Below code to remove Ox from the output
        translated_value = translated_value[2:]
        print(f"You entered {binary_value} == {translated_value}.")


    """ 
    --------------------------------------------------------------------------------------------------------------------------------------
                        Those functions started with octal.
    """


    def octal_into_binary():
        # Take inputs from the users
        octal_value = str(input("Enter the octal value to convert to binary value : "))
        translated_value = bin(int(octal_value, 8))[2:]
        translated_value = translated_value.zfill(3)
        print(f"You entered {octal_value} == {translated_value}.")


    def octal_into_decimal():
        # Take inputs from the users
        octal_value = str(input("Enter the octal value to convert to decimal value : "))
        translated_value = int(octal_value, 8)
        print(f"You entered {octal_value} == {translated_value}.")


    def octal_into_hexa():
        # Take inputs from the users
        octal_value = str(input("Enter the octal value to convert to hexadecimal value : "))
        decimal_value = int(octal_value, 8)
        translated_value = hex(decimal_value)
        # Below code to remove Ox from the output
        translated_value = translated_value[2:]
        print(f"You entered {octal_value} == {translated_value}.")


    """ 
    --------------------------------------------------------------------------------------------------------------------------------------
                    Those functions started with hexadecimal.
    """


    def hexa_into_binary():
        # Take inputs from the users
        hexa_value = str(input("Enter the hexadecimal value to convert to binary value : "))
        translated_value = bin(int(hexa_value, 16))[2:]
        translated_value = translated_value.zfill(4 * len(hexa_value))
        print(f"You entered {hexa_value} == {translated_value}.")


    def hexa_into_decimal():
        # Take inputs from the users
        hexa_value = str(input("Enter the hexadecimal value to convert to decimal value : "))
        translated_value = int(hexa_value, 16)
        print(f"You entered {hexa_value} == {translated_value}.")

    def hexa_into_octal():
        # Take inputs from the users
        hexa_value = str(input("Enter the hexadecimal value to convert to octal value : "))
        decimal_value = int(hexa_value, 16)
        translated_value = oct(decimal_value)
        # Below code to remove Ox from the output
        translated_value = translated_value[2:]
        print(f"You entered {hexa_value} == {translated_value}.")


    """ 
    --------------------------------------------------------------------------------------------------------------------------------------
                    Those functions to convert into BCD values
    """

    def find_bcd_value():
        # Function to convert a decimal digit to BCD (4-bit binary)

        def decimal_digit_to_bcd(decimal_digit):
            bcd = bin(int(decimal_digit))[2:].zfill(4)
            return bcd

        # Function to convert a string of decimal digits to BCD

        def string_to_bcd():
            input_string = str(input("Enter your value : "))
            bcd_string = ""
            for char in input_string:
                if char.isdigit():
                    bcd_digit = decimal_digit_to_bcd(char)
                    bcd_string += bcd_digit
                else:
                    # If the character is not a digit, skip it
                    pass
            print(f"You entered {input_string} == {bcd_string}")

        string_to_bcd()

    """ 
    --------------------------------------------------------------------------------------------------------------------------------------
                    Those functions to convert into ASCII values
    """


    def string_to_ascii():
        string = str(input("Enter your string here : "))
        ascii_list = []
        translated_value = ascii_correct_list = []
        for char in string:
            ascii_code = ord(char)
            ascii_list.append(ascii_code)
        for items in ascii_list:
            decimal = items
            output = bin(decimal)[2:]
            ascii_correct_list.append(output)
        print(f"You entered {string} == "
              f"{ascii_list} = "
              f"{translated_value}.")


except ValueError as value_error:
    print()
    print(f"You entered Choose is invalid for integer type")
    print(f"Please reenter value for 'Choose'")
    print()

except TypeError as type_error:
    print()
    print(f"You entered Choose is invalid type")
    print(f"Please reenter value for 'Choose'")
    print()

except KeyboardInterrupt as keyboard_irruption_error:
    print()
    print("You stopped this programme or failure of keyboard")
    print()

except SyntaxError as syntax_error:
    print()
    print("Please go and return to the programme again!!!")

except NameError as name:
    print(name)

except ModuleNotFoundError:
    print("Sorry !!!")
    print("Please inform us to solve this problem")

finally:
    print()
