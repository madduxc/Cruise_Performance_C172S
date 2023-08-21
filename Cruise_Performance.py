# Author:       Charles D. Maddux
# Revision:     0.0.1
# Date Revised: 19 Aug 2023
# Description:  Control the Cruise_Performance app and call modules as necessary to
#               get data,
#               perform calculations,
#               save data,
#               return results

import csv
from getPerformanceLibraries import readCSV
from getUserData import getData
from tempAtMSL import tempAtMSL



def main():
    """
    Controlling function for Cruise_Performance app.  Calls all other functions to
        - load data,
        - gather user info
        - calculate values
        - return requested data
    All inputs are gathered from the user.
    Data is retrieved from csv files currently only C172S_STP_low, C172S_STP, and C172S_STP_high
    :return: (float)    True Airspeed (TAS, kts),
             (int)      percent horsepower (%MCP, ),
             (float)    fuel flow (, GPH)
    """

    # declare & initialize variables
    filename_low = "C172S_STP_low.csv"
    belowSTP = dict()
    belowSTP = readCSV(filename_low, belowSTP)

    print(belowSTP)
    user_inputs = getData()
    print("The temperature entered is ", user_inputs[0], "degrees Celsius.")
    print("The altitude entered is", user_inputs[1], "feet.")
    print("The engine speed entered is", user_inputs[2], "RPMs.")
    temp_at_SL = tempAtMSL(user_inputs[0], user_inputs[1])
    print("The temperature at Mean Sea Level is ", round(temp_at_SL, 2), "degrees Celsius.")

    for data in belowSTP:
        if str(user_inputs[1]) == data:
            index = 0
            for rpm in belowSTP[data]['RPM'][index]:
                if belowSTP[data]['RPM'][index]['rpm'] == user_inputs[2]:
                    tas = belowSTP[data]['RPM'][index]['TAS']
                    print("True Airspeed at", user_inputs[0], "degrees,", user_inputs[1], "feet altitude, and ", user_inputs[2], "RPMs is ", tas)
                index += 1
    return

if __name__ == "__main__":
    main()

