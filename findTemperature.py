# Author:       Charles D. Maddux
# Revision:     0.0.1
# Date Created: 26 Aug 2023
# Date Revised: 3 Sep 2023
# Description:  given a list of temperatures representing each performance table, find two performance tables that
#               satisfy the requirement, Table1 </= Temp </= Table2, where unless the temperature given is equal to
#               the lowest allowed temperature (Table1 == Temp), then Table1 < Temp </= Table2.

from Response import getResponse

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
                response = getResponse()
                if response == True:
                    user_temp = temp_list[0]
                elif response == False:
                    return file_1, file_2, factor
                else:
                    print("An unspecified error has occurred. Returning to main menu")
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
                    print("WARNING! The temperature you have entered is outside of the range published in the Cruise Performance tables.")
                    print("This program cannot return the actual performance values at the temperature entered by the user.")
                    response = getResponse()
                    if response == True:
                        file_1 = val - 1
                        file_2 = val
                        factor = 1
                        return file_1, file_2, factor
                    elif response == False:
                            return file_1, file_2, factor
                    else:
                        print("An unspecified error has occurred. Returning to main menu")
                        return file_1, file_2, factor
    return file_1, file_2, factor


def main():
    temps = [-5, 15, 35]
    user_temp = 36
    index_1, index_2, temp_factor = findTempTable(user_temp, temps)
    print(index_1, index_2, temp_factor)
    return


if __name__ == "__main__":
    main()
