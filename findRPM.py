# Author:       Charles D. Maddux
# Revision:     0.0.1
# Date Created: 2 Sep 2023
# Date Revised: 2 Sep 2023
# Description:  given a dictionary of performance data, find two RPM values that satisfy the requirements:
#               rpm_value_1 </= user_rpm </= rpm_value_2, where unless the RPM given is equal to
#               the lowest allowed RPM (rpm_value_1 == user_rpm), then rpm_value_1 < user_rpm </= rpm_value_2.

from getPerformanceLibraries import readCSV
from Response import getResponse


def findRPMData(user_rpm, rpm_list):

    # declare variables
    rpms = list()
    rpm_1 = -1
    rpm_2 = -1
    factor = -1

    for rpm in rpm_list['RPM']:
        current_rpm = rpm['rpm']
        # build list for handling of edge cases
        rpms.append(current_rpm)
        index = len(rpms) - 1

        if index == 0:
            if user_rpm < current_rpm:
                print("WARNING! The engine RPM you have entered is outside of the range published in the Cruise Performance tables.")
                print("This program cannot return the actual performance values for the RPM value at the altitude entered by the user.")
                response = getResponse()
                if response == True:
                    user_rpm = current_rpm
                elif response == False:
                    return rpm_1, rpm_2, factor
                else:
                    print("An unspecified error has occurred. Returning to main menu")
                    return rpm_1, rpm_2, factor
        else:
            if user_rpm < current_rpm:
                rpm_1 = index - 1
                rpm_2 = index
                factor = (user_rpm - rpms[index - 1]) / (rpms[index] - rpms[index - 1])
                return rpm_1, rpm_2, factor
            else:
                # handle the case of temp greater than upper bound
                pass

    # handle the edge case where user_alt is greater than any altitude in the list
    index = len(rpms) - 1
    if user_rpm > rpms[index]:
        print("WARNING! The engine RPM you have entered is outside of the range published in the Cruise Performance tables.")
        print("This program cannot return the actual performance values for the RPM at the altitude entered by the user.")
        response = getResponse()
        if response == True:
            user_rpm = rpms[index]
        elif response == False:
            return rpm_1, rpm_2, factor
        else:
            print("An unspecified error has occurred. Returning to main menu")
            return rpm_1, rpm_2, factor

    # handle edge case where user_alt equals alt of last table
    if user_rpm == rpms[index]:
        rpm_1 = index - 1
        rpm_2 = index
        factor = 1
    return rpm_1, rpm_2, factor


def main():
    belowSTP = dict()
    belowSTP = readCSV("C172S_STP_low.csv", belowSTP)
    rpm1, rpm2, factor = findRPMData(2345, belowSTP['2000'])
    print(rpm1, rpm2, factor)
    return


if __name__ == "__main__":
    main()