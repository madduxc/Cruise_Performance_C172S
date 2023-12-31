# Author:       Charles D. Maddux
# Revision:     0.0.1
# Date Created: 19 Aug 2023
# Date Revised: 3 Sep 2023
# Description:  Control the Cruise_Performance app and call modules as necessary to
#               get data,
#               perform calculations,
#               save data,
#               return results

from getPerformanceLibraries import readCSV
from getUserData import getData
from tempAtMSL import tempAtMSL
from findTemperature import findTempTable
from findAltitude import findAltitudeTable
from findRPM import findRPMData

# global variables
STP = 15


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
    # file names for data libraries - hard coded for now (1st airplane)
    filename_low  = "C172S_STP_low.csv"
    filename_stp  = "C172S_STP.csv"
    filename_high = "C172S_STP_high.csv"

    # temperatures and return date - hard coded
    temps = [STP - 20, STP, STP + 20]
    return_vals = ['pctPwr', 'TAS', 'gph']
    final_vals = list()

    # create dictionaries for libraries
    belowSTP = dict()
    atSTP    = dict()
    aboveSTP = dict()

    # read files and load data into dictionaries
    belowSTP = readCSV(filename_low, belowSTP)
    atSTP    = readCSV(filename_stp, atSTP)
    aboveSTP = readCSV(filename_high, aboveSTP)
    tables = [belowSTP, atSTP, aboveSTP]

    # get user altitude, temperature at altitude, and RPM setting
    user_inputs = getData()
    print("The temperature entered is ", user_inputs[0], "degrees Celsius.")
    print("The altitude entered is", user_inputs[1], "feet.")
    print("The engine speed entered is", user_inputs[2], "RPMs.")

    # calculate the temperature at sea level (0 feet pressure altitude)
    temp_at_SL = tempAtMSL(user_inputs[0], user_inputs[1])
    print("The temperature at Mean Sea Level is ", round(temp_at_SL, 2), "degrees Celsius.")

    # find the temperature tables from which to interpolate data and the factor between them
    temp_index_1, temp_index_2, temp_factor = findTempTable(temp_at_SL, temps)

    # find the relevant altitudes at each temperature
    temp1_alt1, temp1_alt2, temp1_alt_factor = findAltitudeTable(user_inputs[1], tables[temp_index_1])
    temp2_alt1, temp2_alt2, temp2_alt_factor = findAltitudeTable(user_inputs[1], tables[temp_index_2])

    temp1_alt1_rpm1,temp1_alt1_rpm2, temp1_alt1_factor = findRPMData(user_inputs[2], tables[temp_index_1][str(temp1_alt1)])
    temp1_alt2_rpm1,temp1_alt2_rpm2, temp1_alt2_factor = findRPMData(user_inputs[2], tables[temp_index_1][str(temp1_alt2)])
    temp2_alt1_rpm1,temp2_alt1_rpm2, temp2_alt1_factor = findRPMData(user_inputs[2], tables[temp_index_2][str(temp2_alt1)])
    temp2_alt2_rpm1,temp2_alt2_rpm2, temp2_alt2_factor = findRPMData(user_inputs[2], tables[temp_index_2][str(temp2_alt2)])

    for val in return_vals:
        temp1_alt1_val = tables[temp_index_1][str(temp1_alt1)]['RPM'][temp1_alt1_rpm1][val] \
                         + temp1_alt1_factor \
                         * (tables[temp_index_1][str(temp1_alt1)]['RPM'][temp1_alt1_rpm2][val] - \
                            tables[temp_index_1][str(temp1_alt1)]['RPM'][temp1_alt1_rpm1][val] )
        temp1_alt2_val = tables[temp_index_1][str(temp1_alt2)]['RPM'][temp1_alt2_rpm1][val] \
                        + temp1_alt2_factor \
                        * (tables[temp_index_1][str(temp1_alt2)]['RPM'][temp1_alt2_rpm2][val]
                        - tables[temp_index_1][str(temp1_alt2)]['RPM'][temp1_alt2_rpm1][val])
        temp1_val = temp1_alt1_val + temp1_alt_factor * (temp1_alt2_val - temp1_alt1_val)
        temp2_alt1_val = tables[temp_index_2][str(temp2_alt1)]['RPM'][temp2_alt1_rpm1][val] \
                         + temp2_alt1_factor \
                         * (tables[temp_index_2][str(temp2_alt1)]['RPM'][temp2_alt1_rpm2][val]
                            - tables[temp_index_2][str(temp2_alt1)]['RPM'][temp2_alt1_rpm1][val])
        temp2_alt2_val = tables[temp_index_2][str(temp2_alt2)]['RPM'][temp2_alt2_rpm1][val] \
                         + temp2_alt2_factor \
                         * (tables[temp_index_2][str(temp2_alt2)]['RPM'][temp2_alt2_rpm2][val]
                            - tables[temp_index_2][str(temp2_alt2)]['RPM'][temp2_alt2_rpm1][val])
        temp2_val = temp2_alt1_val + temp2_alt_factor * (temp2_alt2_val - temp2_alt1_val)
        value = temp1_val + temp_factor * (temp2_val - temp1_val)
        final_vals.append(value)

    print("At " + str(user_inputs[0]) + " degrees Celsius, " + str(user_inputs[1]) + " feet pressure altitude and " + str(user_inputs[2]) + " RPMs:")
    print("   The power setting is " + str(final_vals[0]) + " %.")
    print("   The true airspeed is " + str(final_vals[1]) + " knots.")
    print("   The fuel flow is " + str(final_vals[2]) + " gallons per hour.")
    return


def lookUpData(belowSTP, user_inputs):
    for data in belowSTP:
        # B: Find altitude or interpolate - return error if outside of bounds
        if str(user_inputs[1]) == data:
            index = 0
            for rpm in belowSTP[data]['RPM'][index]:
                if belowSTP[data]['RPM'][index]['rpm'] == user_inputs[2]:
                    # C: Find RPM or interpolate - return error if outside of bounds
                    # data is the pressure altitude dictionary key (string)
                    # case 1: if index == 0: Check if user input is less than rpm (throw error).
                    #                        Check if user input is equal to rpm (return 1 value)
                    # case 2: if index 1 to n: Check if user input less than rpm (return 2 values)
                    #                          Check if user input equal to rpm (return 1 value)
                    # case 3: if index n: check if user input > rpm (throw error)
                    tas = belowSTP[data]['RPM'][index]['TAS']
                    print("True Airspeed at", user_inputs[0], "degrees,", user_inputs[1], "feet altitude, and ", user_inputs[2], "RPMs is ", tas)
                index += 1
    return


if __name__ == "__main__":
    main()

# data structure:                temp 1                                     temp2
#                       alt1                alt2                    alt1                alt2
#                   rpm1    rpm2        rpm1    rpm2            rpm1    rpm2        rpm1    rpm2
#                   TAS     TAS         TAS     TAS             TAS     TAS         TAS     TAS
#                   %pwr    %pwr        %pwr    %pwr            %pwr    %pwr        %pwr    %pwr
#                   GPH     GPH         GPH     GPH             GPH     GPH         GPH     GPH
