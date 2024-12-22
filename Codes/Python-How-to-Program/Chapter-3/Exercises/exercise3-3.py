# Question 3.3:
# Drivers are concerned with the mileage obtained by their automobiles. One driver has kept
# track of several tankfuls of gasoline by recording miles driven and gallons used for each tankful.
# Develop a Python program that prompts the user to input the miles driven and gallons used for each tankful.
# The program should calculate and display the miles per gallon obtained for each tankful. After
# processing all input information, the program should calculate and print the combined miles per gallon
# obtained for all tankful (= total miles driven divide by total gallons used).

def get_miles():
    val = None
    while val is None or val <= 0:
        try:
            val = float(input("Enter the miles driven: "))
            if val <= 0:
                print("Invalid input. Please enter a positive number.")

        except ValueError:
            print("Invalid input. Please enter a numeric value.")
    return val


def get_gallons():
    val = None
    while val is None or val <= 0:
        try:
            val = float(input("Enter the gallons used (-1 to end): "))
            if val == -1:
                return val
            if val <= 0:
                print("Invalid input. Please enter a positive number.")

        except ValueError:
            print("Invalid input. Please enter a numeric value.")
    return val


gallons = get_gallons()
if gallons == -1:
    print("No data to process.")
else:
    miles = get_miles()
    miles_per_gallons = miles / gallons
    print(f"The miles / gallon for this tank was {miles_per_gallons:.6f}")
    sum_miles = miles
    sum_gallons = gallons

    while gallons != -1:
        gallons = get_gallons()
        if gallons != -1:
            miles = get_miles()
            miles_per_gallons = miles / gallons
            print(f"The miles / gallon for this tank was {miles_per_gallons:.6f}")
            sum_miles += miles
            sum_gallons += gallons

    average_miles_per_gallons = sum_miles / sum_gallons
    print(f"The overall average miles/gallon was {average_miles_per_gallons:.6f}")
