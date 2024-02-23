try:
    # We need math module for this programme
    import math

    """
    This functions are to take the values for the MATHEMATICS programme.
    """

    # To find the radius.
    def get_radius() -> float:
        radius = float(input("Radius : "))
        return radius

    # To find the theta.
    def get_theta() -> float:
        theta = float(input("Theta : "))
        return theta

    # To find the height.
    def get_height():
        height = float(input("Height : "))
        return height

    # To find the length.
    def get_length():
        length = float(input("Length : "))
        return length

    # To find the breadth.
    def get_breadth():
        breadth = float(input("Breadth : "))
        return breadth

    # To get the power
    def get_power():
        power = float(input("Power : "))
        return power

    # To get the normal plus or minus float or integer
    def get_plus_or_minus_float_or_integer():
        plus_or_minus_float_or_integer = float(input("Float or Integer : "))
        return plus_or_minus_float_or_integer

    """
    This functions are the main functions of this file.
    """

    # To find the area of a circle that given by the user.
    def find_area_of_circle(radius, theta: float) -> float:
        pi = math.pi
        circle_area = pi * pow(radius, 2) * theta / 360
        circle_area = round(circle_area, 4)
        return circle_area

    # To find the area of a rectangle that given by the user.
    def find_area_of_rectangle(breadth, length: float) -> float:
        rectangle_area = breadth * length
        rectangle_area = round(rectangle_area, 4)
        return rectangle_area

    # To find the area of a square that given by the user.
    def find_area_of_square(breadth, length: float) -> float:
        square_area = breadth * length
        square_area = round(square_area, 4)
        return square_area

    # To find the volume of a rectangle that given by the user.
    def find_volume_of_rectangle(breadth, length, height: float) -> float:
        rectangle_volume = breadth * length * height
        rectangle_volume = round(rectangle_volume, 4)
        return rectangle_volume

    # To find the volume of a square that given by the user.
    def find_volume_of_square(breadth, length, height: float) -> float:
        square_volume = breadth * length * height
        square_volume = round(square_volume, 4)
        return square_volume

    # To find the circumference of a circle that given by the user.
    def find_circumference_of_circle(radius, theta: float) -> float:
        pi = math.pi
        circumference_circle = 2 * pi * radius * theta / 360
        circumference_circle = round(circumference_circle, 4)
        return circumference_circle

    # To find the logarithm of user given item
    def find_logarithm(item, power: float) -> float:
        log = math.log(item, power)
        return log


except ValueError:
    print('Value error occurred')
    print("please reenter the value")
    breakpoint()

except TypeError:
    print("Type of value is error")
    print("please reenter the value")
    breakpoint()
