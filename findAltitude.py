# Author:       Charles D. Maddux
# Revision:     0.0.1
# Date Created: 2 Sep 2023
# Date Revised: 3 Sep 2023
# Description:  given a dictionary of performance data, find two altitude tables that satisfy the requirements:
#               alt_table_1 </= alt </= alt_table_2, where unless the altitude given is equal to
#               the lowest allowed altitude (alt_table_1 == alt), then alt_table_1 < alt </= alt_table_2.

from getPerformanceLibraries import readCSV
from Response import getResponse


def findAltitudeTable(user_alt, alt_table):

    # declare variables
    altitudes = list()
    alt_1 = -1
    alt_2 = -1
    factor = -1

    for altitude in alt_table:
        current_alt = alt_table[altitude]['alt']
        # build list of altitudes for handling of edge cases
        altitudes.append(current_alt)
        # handle edge case
        if len(altitudes) == 1:
            if user_alt < current_alt:
                print("WARNING! The altitude you have entered is outside of the range published in the Cruise Performance tables.")
                print("This program cannot return the actual performance values at the altitude entered by the user.")
                response = getResponse()
                if response == True:
                    user_alt = current_alt
                elif response == False:
                    return alt_1, alt_2, factor
                else:
                    print("An unspecified error has occurred. Returning to main menu")
                    return alt_1, alt_2, factor
        else:
            if user_alt < current_alt:
                alt_1 = altitudes[len(altitudes) - 2]
                alt_2 = altitudes[len(altitudes) - 1]
                factor = (user_alt - alt_1) / (alt_2 - alt_1)
                return alt_1, alt_2, factor
            else:
                # handle the case of temp greater than upper bound
                pass

    # handle the edge case where user_alt is greater than any altitude in the list
    if user_alt > altitudes[len(altitudes) - 1]:
        print("WARNING! The altitude you have entered is outside of the range published in the Cruise Performance tables.")
        print("This program cannot return the actual performance values at the altitude entered by the user.")
        response = getResponse()
        if response == True:
            user_alt = altitudes[len(altitudes) - 1]
        elif response == False:
            return alt_1, alt_2, factor
        else:
            print("An unspecified error has occurred. Returning to main menu")
            return alt_1, alt_2, factor

    # handle edge case where user_alt equals alt of last table
    if user_alt == altitudes[len(altitudes) - 1]:
        alt_1 = altitudes[len(altitudes) - 2]
        alt_2 = altitudes[len(altitudes) - 1]
        factor = 1
    return alt_1, alt_2, factor


def main():
    belowSTP = dict()
    belowSTP = readCSV("C172S_STP_low.csv", belowSTP)
    alt1, alt2, factor = findAltitudeTable(12001, belowSTP)
    print(alt1, alt2, factor)
    return


if __name__ == "__main__":
    main()