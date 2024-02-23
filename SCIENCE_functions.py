def find_molars():
    x = float(input("Enter how much molars do you have to enter this programme : "))
    molars = x
    return molars


def velocity():
    x = float(input("Enter velocity in m/s : "))
    user_velocity = x
    return user_velocity


def distance():
    x = float(input("Enter distance in m : "))
    user_distance = x
    return user_distance


def time():
    x = float(input("Enter time in seconds (s) : "))
    user_time = x
    return user_time


def time_different():
    x = float(input("Enter time difference in seconds : "))
    user_time_difference = x
    return user_time_difference


def molar_mass():
    x = float(input("Enter molar mass : "))
    user_molar_mass = x
    return user_molar_mass


def find_mass():
    x = float(input("Enter mass : "))
    user_mass = x
    return user_mass


"""------------------------------------------------------------------------------------------------------------------"""


def find_no_of_moles():
    mass = find_mass()
    user_molar_mass = molar_mass()
    moles = mass/user_molar_mass
    print(f"Your moles are =: {moles}")


def find_speed(x, y):
    distancex = x
    timey = y
    speed = distancex / timey
    print(f"Speed is : {speed}")
