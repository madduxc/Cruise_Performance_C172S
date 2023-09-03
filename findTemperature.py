# Author:       Charles D. Maddux
# Revision:     0.0.1
# Date Created: 26 Aug 2023
# Date Revised: 26 Aug 2023
# Description:  given a list of temperatures representing each performance table, find two performance tables that
#               satisfy the requirement, Table1 </= Temp </= Table2, where unless the temperature given is equal to
#               the lowest allowed temperature (Table1 == Temp), then Table1 < Temp </= Table2.


def findTempTable(user_temp, temp_list):
    """
    Function to find where the user-input temperature is in relation to the temperatures given by the input tables.
    If the user input equals the lower limit temperature, then 0, 1, 0 is returned, meaning
        file[0] represents the tables used for the first data points
        file[1] represents the tables used for the second data points
        factor represents the multiplier of the difference between the two tables
        ex. Value = data[file[0] + factor * (data[file[1] - data[file[0])
        In this case, data[file[0] + 0 * (data[file[1] - data[file[0]) = data[file[0]

    :param user_temp: (float)       temperature (in degrees Celsius) corrected for sea level at standard pressure
    :param temp_list: list(float)   list of temperatures represented in the the input tables
    :return: file_1 (index of first temp table), file_2 (index of second table), factor (between the two table values)
    """
    # declare variables
    file_1 = -1
    file_2 = -1
    factor = -1

    # iterate through list
    for val in range(len(temp_list)):
        # handle edge case
        if val == 0:
            if user_temp < temp_list[0]:
                response = 0
                print("WARNING! The temperature you have entered is outside of the range published in the Cruise Performance tables.")
                print("This program cannot return the actual performance values at the temperature entered by the user.")
                while response == 0:
                    cutoff = input("Would you like to use cutoff values?  Enter 'yes' or 'no'")
                    if cutoff.lower() == 'yes' or cutoff.lower() == 'y':
                        file_1 = 0
                        file_2 = 1
                        factor = 0
                        return file_1, file_2, factor
                    elif cutoff.lower() == 'no' or cutoff.lower() == 'n':
                        print("process has ended.  Returning to main function.")
                        return file_1, file_2, factor
                    else:
                        print("This response is not understood. Please try again.")
            # handle exact match. Return temp 1 = user_temp, temp_2 = -999,
            elif user_temp == temp_list[0]:
                file_1 = 0
                file_2 = 1
                factor = 0
                return file_1, file_2, factor
            else:
                continue
        else:
            # handle the case of an exact match
            if user_temp == temp_list[val]:
                file_1 = val - 1
                file_2 = val
                factor = 1
                return file_1, file_2, factor
            elif user_temp < temp_list[val]:
                file_1 = val - 1
                file_2 = val
                factor = (user_temp - temp_list[val - 1]) / (temp_list[val] - temp_list[val - 1])
                return file_1, file_2, factor
            else:
                # handle the case of temp greater than upper bound
                if val == len(temp_list) - 1:
                    response = 0
                    print("WARNING! The temperature you have entered is outside of the range published in the Cruise Performance tables.")
                    print("This program cannot return the actual performance values at the temperature entered by the user.")
                    while response == 0:
                        cutoff = input("Would you like to use cutoff values?  Enter 'yes' or 'no'")
                        if cutoff.lower() == 'yes' or cutoff.lower() == 'y':
                            file_1 = val - 1
                            file_2 = val
                            factor = 1
                            return file_1, file_2, factor
                        elif cutoff.lower() == 'no' or cutoff.lower() == 'n':
                            print("process has ended.  Returning to main function.")
                            return file_1, file_2, factor
                        else:
                            print("This response is not understood. Please try again.")
    return file_1, file_2, factor


def main():
    print("chickens")
    return


if __name__ == "__main__":
    main()
