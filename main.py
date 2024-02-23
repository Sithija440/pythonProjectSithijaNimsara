import sys
from functions import ICT_functions as functions1
from functions import MATHEMATIS_functions as functions2
from functions import SCIENCE_functions as functions3
import Output_list as outlist


try:

    """
    This is the users selection function.
    It will more help full for programmers who use this programme to develop.
    """

    # This will the ICT all function loop code
    def user_selections_1():
        while True:
            choose = int(input("Enter choose : "))  # Take which block need to execute
            # User will choose the following case from the below.
            match choose:
                # To convert decimal into binary
                case 1:
                    print()
                    functions1.decimal_into_binary()
                    print()
                # To convert decimal into octal
                case 2:
                    print()
                    functions1.decimal_into_octal()
                    print()
                # To convert decimal into hexadecimal
                case 3:
                    print()
                    functions1.decimal_into_hexa()
                    print()
                # To convert binary into decimal
                case 4:
                    print()
                    functions1.binary_into_decimal()
                    print()
                # To convert binary into octal
                case 5:
                    print()
                    functions1.binary_into_octal()
                    print()
                # To convert binary into hexadecimal
                case 6:
                    print()
                    functions1.binary_into_hexa()
                    print()
                # To convert octal into binary
                case 7:
                    print()
                    functions1.octal_into_binary()
                    print()
                # To convert octal into decimal
                case 8:
                    print()
                    functions1.octal_into_decimal()
                    print()
                # To convert octal into hexadecimal
                case 9:
                    print()
                    functions1.octal_into_hexa()
                    print()
                # To convert hexadecimal into binary
                case 10:
                    print()
                    functions1.hexa_into_binary()
                    print()
                # To convert hexadecimal into decimal
                case 11:
                    print()
                    functions1.hexa_into_decimal()
                    print()
                # To convert hexadecimal into octal
                case 12:
                    print()
                    functions1.hexa_into_octal()
                    print()
                # To convert value into BCD value
                case 13:
                    print()
                    functions1.find_bcd_value()
                    print()
                # To convert string into ASCII value
                case 14:
                    print()
                    functions1.string_to_ascii()
                    print()
                # This will return to execution code block
                case 99:
                    print()
                    execution_code()

    # This will the Mathematics all function loop code
    def user_selection_2():
        while True:
            choose = int(input("Enter choose : "))  # Take which block need to execute
            # User will choose the following case from the below.
            match choose:
                # This is to find the area of a square
                case 1:
                    print()

                    def area_square():
                        breadth = functions2.get_breadth()
                        length = functions2.get_length()
                        area = functions2.find_area_of_square(breadth, length)
                        print(area)

                    area_square()
                    print()
                # This is to find the area of a rectangle
                case 2:
                    print()

                    def area_rectangle():
                        breadth = functions2.get_breadth()
                        length = functions2.get_length()
                        area = functions2.find_area_of_rectangle(breadth, length)
                        print(area)

                    area_rectangle()
                    print()
                # This is to find the area of a circle
                case 3:
                    print()

                    def area_circle():
                        radius = functions2.get_radius()
                        theta = functions2.get_theta()
                        area = functions2.find_area_of_circle(radius, theta)
                        print(area)

                    area_circle()
                    print()
                # This is to find the volume of a square
                case 4:
                    print()

                    def volume_square():
                        breadth = functions2.get_breadth()
                        length = functions2.get_length()
                        height = functions2.get_height()
                        volume = functions2.find_volume_of_square(breadth, length, height)
                        print(volume)

                    volume_square()
                    print()
                # This is to find the volume of a rectangle
                case 5:
                    print()

                    def volume_rectangle():
                        breadth = functions2.get_breadth()
                        length = functions2.get_length()
                        height = functions2.get_height()
                        volume = functions2.find_volume_of_rectangle(breadth, length, height)
                        print(volume)

                    volume_rectangle()
                    print()
                # This is to find the volume of a circle
                case 6:
                    print()

                    def circumference_circle():
                        radius = functions2.get_radius()
                        theta = functions2.get_theta()
                        circumference = functions2.find_circumference_of_circle(radius, theta)
                        print(circumference)

                    circumference_circle()
                    print()
                case 7:
                    print()

                    item_value = functions2.get_plus_or_minus_float_or_integer()
                    power = functions2.get_power()
                    print(functions2.find_logarithm(item_value, power))
                # This will return to execution code block
                case 99:
                    print()
                    execution_code()

    def user_selection_3():
        while True:
            choose = int(input("Enter choose : "))  # Take which block need to execute
            # User will choose the following case from the below.
            match choose:
                case 1:
                    print()
                    functions3.find_no_of_moles()
                    print()
                case 2:
                    print()
                    distance = functions3.distance()
                    time = functions3.time()
                    functions3.find_speed(distance, time)
                    print()
                case 99:
                    print()
                    execution_code()

    """
    This below code will execute the functions in functions module.
    """

# Execution block will call this function.


    def case_match(choose):
        match choose:
            case 1:
                print()
                outlist.printout_list_1()
                new_func2()
                print()
            case 2:
                print()
                outlist.printout_list_2()
                user_selection_2()
                print()
            case 3:
                print()
                outlist.printout_list_3()
                user_selection_3()
                print()
            case 99:
                sys.exit(1)

    
    def users_select():
        outlist.main_list()
        choose = int(input("Enter your choose : "))
        new_func1(choose)

    def new_func():
        users_select()

    def new_func1(choose):
        case_match(choose)

    def new_func2():
        user_selections_1()


    def execution_code():
        # This loop will end with the user select only 99.
        while True:
            new_func()



    """
    This is the class code.
    It is the oop code.
    """

    class Calculator:
        execution_code()


    Calculator = Calculator()
    print(Calculator)


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


except ZeroDivisionError:
    print("Zero Division Error occurred")

finally:
    print("Thank you to choose our programme...")
